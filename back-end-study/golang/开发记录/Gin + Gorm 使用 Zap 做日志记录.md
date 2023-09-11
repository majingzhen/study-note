# Gin + Gorm使用 Zap 做日志记录

本文介绍了在 gin + grom 的web项目中如何使用 zap 做日志记录，并输出到文件。

## 1.导入所需要的包

```
github.com/gin-gonic/gin

go.uber.org/zap

gorm.io/driver/mysql

gorm.io/gorm

gopkg.in/natefinch/lumberjack.v2 用于切割日志文件

github.com/spf13/viper 读取配置文件
```

## 2.创建全局变量

```go
var (
	GormDao     *gorm.DB
	Viper       *viper.Viper
	Logger      *zap.Logger
)
```

## 3.初始化日志配置

```go
// InitLogger 初始化日志
func InitLogger() {
	logPath := Viper.GetString("logger.file_path")
	if logPath == "" {
		logPath = "./log/manager.log" // 如果未配置日志路径，则默认在项目根目录下创建log目录
	}
	// 设置日志文件的位置、文件名、最大大小、最大备份数量和压缩
	hook := lumberjack.Logger{
		Filename:   logPath, // 日志路径
		MaxSize:    128,     // MB
		MaxBackups: 30,
		MaxAge:     7, // days
		Compress:   true,
	}
	// 配置日志级别
	atomicLevel := zap.NewAtomicLevel()
	logLevel := Viper.GetInt32("logger.level")
	atomicLevel.SetLevel(zapcore.Level(logLevel))
	// 创建编码器
	// 设置日志格式
	encoderConfig := zapcore.EncoderConfig{
		TimeKey:        "time",
		LevelKey:       "level",
		NameKey:        "logger",
		CallerKey:      "caller",
		MessageKey:     "msg",
		StacktraceKey:  "stacktrace",
		LineEnding:     zapcore.DefaultLineEnding,
		EncodeLevel:    zapcore.LowercaseLevelEncoder,
		EncodeTime:     zapcore.ISO8601TimeEncoder,
		EncodeDuration: zapcore.SecondsDurationEncoder,
		EncodeCaller:   zapcore.ShortCallerEncoder,
	}
	// 创建core
	writer := zapcore.NewCore(
		zapcore.NewConsoleEncoder(encoderConfig),
		zapcore.NewMultiWriteSyncer(zapcore.AddSync(os.Stdout), zapcore.AddSync(&hook)),
		atomicLevel,
	).With([]zap.Field{})
	// 初始化logger
	Logger = zap.New(writer)
}
```

## 4.创建gin的logger中间件

```go

func GinLogger() gin.HandlerFunc {
	return func(c *gin.Context) {
		start := time.Now()
		// 处理请求
		c.Next()
		// 计算请求处理时间
		latency := time.Since(start)
		// 获取相关信息
		statusCode := c.Writer.Status()
		clientIP := c.ClientIP()
		method := c.Request.Method
		path := c.Request.URL.Path

		if method == "OPTIONS" { // 跨域请求会先发送一个OPTIONS请求，这里不做处理
			return
		}
		// 将日志输出到Zap
		global.Logger.Info("Gin request",
			zap.Int("status", statusCode),
			zap.String("method", method),
			zap.String("path", path),
			zap.String("ip", clientIP),
			zap.Duration("latency", latency),
		)
	}
}
```

## 5.使用中间件

```go
// InitRouter 初始化路由
func (routers *Routers) InitRouter() *gin.Engine {
	r := gin.New()
	r.Use(middleware.GinLogger())
	r.Use(gin.Recovery())

	// 跨域处理
	// 使用Cors中间件处理跨域请求
	r.Use(middleware.Cors())

	r.GET("/", func(ctx *gin.Context) {
		ctx.String(200, "hello")
	})

	return r
}


```

## 6.实现Gorm自定义日志记录器 *--重点*

```go

type GormLogger struct {
	ZapLogger     *zap.Logger
	SlowThreshold time.Duration
}

func NewGormLogger() GormLogger {
	return GormLogger{
		ZapLogger:     Logger,
		SlowThreshold: 200 * time.Millisecond,
	}
}

// LogMode 实现 gormlogger.Interface 的 LogMode 方法
func (l GormLogger) LogMode(level gormlogger.LogLevel) gormlogger.Interface {
	return GormLogger{
		ZapLogger:     l.ZapLogger,
		SlowThreshold: l.SlowThreshold,
	}
}

// Info 实现 gormlogger.Interface 的 Info 方法
func (l GormLogger) Info(ctx context.Context, str string, args ...interface{}) {
	l.logger().Sugar().Debugf(str, args...)
}

// Warn 实现 gormlogger.Interface 的 Warn 方法
func (l GormLogger) Warn(ctx context.Context, str string, args ...interface{}) {
	l.logger().Sugar().Warnf(str, args...)
}

// Error 实现 gormlogger.Interface 的 Error 方法
func (l GormLogger) Error(ctx context.Context, str string, args ...interface{}) {
	l.logger().Sugar().Errorf(str, args...)
}

// Trace 实现 gormlogger.Interface 的 Trace 方法
func (l GormLogger) Trace(ctx context.Context, begin time.Time, fc func() (string, int64), err error) {

	// 获取运行时间
	elapsed := time.Since(begin)
	// 获取 SQL 请求和返回条数
	sql, rows := fc()

	// 通用字段
	logFields := []zap.Field{
		zap.String("sql", sql),
		zap.String("time", utils.MicrosecondsStr(elapsed)),
		zap.Int64("rows", rows),
	}

	// Gorm 错误
	if err != nil {
		// 记录未找到的错误使用 warning 等级
		if errors.Is(err, gorm.ErrRecordNotFound) {
			l.logger().Warn("Database ErrRecordNotFound", logFields...)
		} else {
			// 其他错误使用 error 等级
			logFields = append(logFields, zap.Error(err))
			l.logger().Error("Database Error", logFields...)
		}
	}

	// 慢查询日志
	if l.SlowThreshold != 0 && elapsed > l.SlowThreshold {
		l.logger().Warn("Database Slow Log", logFields...)
	}

	// 记录所有 SQL 请求
	l.logger().Debug("Database Query", logFields...)
}

// logger 内用的辅助方法，确保 Zap 内置信息 Caller 的准确性（如 paginator/paginator.go:148）
func (l GormLogger) logger() *zap.Logger {

	// 跳过 gorm 内置的调用
	var (
		gormPackage    = filepath.Join("gorm.io", "gorm")
		zapgormPackage = filepath.Join("moul.io", "zapgorm2")
	)

	// 减去一次封装，以及一次在 logger 初始化里添加 zap.AddCallerSkip(1)
	clone := l.ZapLogger.WithOptions(zap.AddCallerSkip(-2))

	for i := 2; i < 15; i++ {
		_, file, _, ok := runtime.Caller(i)
		switch {
		case !ok:
		case strings.HasSuffix(file, "_test.go"):
		case strings.Contains(file, gormPackage):
		case strings.Contains(file, zapgormPackage):
		default:
			// 返回一个附带跳过行号的新的 zap logger
			return clone.WithOptions(zap.AddCallerSkip(i))
		}
	}
	return l.ZapLogger
}
```

## 7.初始化数据库时使用zap进行日志输出

```go
// InitDataSource 初始化数据库
func InitDataSource() {
	dsn := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?parseTime=True&loc=Local",
		Viper.GetString("datasource.username"),
		Viper.GetString("datasource.password"),
		Viper.GetString("datasource.host"),
		Viper.GetString("datasource.port"),
		Viper.GetString("datasource.db_name"))
	gcf := &gorm.Config{
		NamingStrategy: schema.NamingStrategy{
			TablePrefix:   Viper.GetString("datasource.table_prefix"), // 控制表前缀
			SingularTable: true,
		},
		Logger: logger.Default, // 控制是否sql输出，默认是不输出
	}
	if Viper.GetBool("datasource.log_mode") {
		gcf.Logger = NewGormLogger() // 使用zap进行日志输出
	}

	if tmp, err := gorm.Open(mysql.Open(dsn), gcf); err != nil {
		Logger.Error("MySQL启动异常", zap.Error(err))
		panic(err)
	} else {
		// 设置delete_at字段类型
		tmp.Set("gorm:softDelete", "is_del")
		GormDao = tmp
	}
}
```
