# Gorm 逻辑删除字段类型修改

本文记录了在 grom 使用中自定义逻辑删除字段。

## 1.介绍

gorm 在使用时提供了，硬删除和软删除两种方式。

硬删除：即将数据物理删除。

软删除：在表中加入 delete_at 字段，默认类型为 time 类型，在进行删除操作时会将Delete 语句 变更为 update 语句，修改 delete_at 字段的值为当前时间。在进行查询时，gorm 会自动忽略 delete_at 字段不为空的数据，实现软删除（逻辑删除）的效果。



有时候我们在实际开发过程中，逻辑删除字段并不固定，在 gorm 中默认是 time 类型的 delete_at 字段，所以就需要进行修改。

## 2.定义结构体

```go
// GvaModel 基础模型
type GvaModel struct {
	Id         string     `json:"id" gorm:"id"` // 主键ID
	CreateBy   string     `json:"createBy" gorm:"create_by"`
	UpdateBy   string     `json:"updateBy" gorm:"update_by"`
	CreateTime *time.Time `json:"createTime" gorm:"create_time"` // 创建时间
	UpdateTime *time.Time `json:"updateTime" gorm:"update_time"` // 更新时间
	IsDel      int        `gorm:"index" json:"-"`                // 逻辑删除字段
}
```

这里创建了一个公用的基础模型，包含了一些公用属性，当然也包含我们的软删除字段。

这里 我将字段名定义为 is_del 类型是 tinyint(1)

## 3.设置软删除字段

在初始化数据库链接对象时，我们可以设置软删除字段。

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


