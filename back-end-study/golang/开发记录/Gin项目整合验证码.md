# Gin项目整合验证码

本文介绍如何在gin项目中整合验证码功能，进行登录验证操作。

## 1.安装依赖库

这里使用的是base64Captcha

```shell
go get -u "github.com/mojocn/base64Captcha"
```

## 2.生成验证码

base64Captcha可以生成多种类型的验证码，返回一个base64格式的数据和一个string格式的id（验证时需要一起提交）

创建一个 captcha 的路由，用于验证码生成

```go
// store 验证码
var store = base64Captcha.DefaultMemStore

// CaptchaImage 验证码
func (api *SystemApi) CaptchaImage(c *gin.Context) {
    //字符,公式,验证码配置
    //定义一个driver
    var driver base64Captcha.Driver
    //创建一个字符串类型的验证码驱动DriverString, DriverChinese :中文驱动
    driverString := base64Captcha.DriverString{
        Height:          40,    //高度
        Width:           100,   //宽度
        NoiseCount:      0,     //干扰数
        ShowLineOptions: 2 | 4, //展示个数
        Length:          4,     //长度
        // Source:          "1234567890qwertyuiplkjhgfdsazxcvbnm", //验证码随机字符串来源
        Source: "1234567890", //验证码随机字符串来源
        BgColor: &color.RGBA{ // 背景颜色
            R: 3,
            G: 102,
            B: 214,
            A: 125,
        },
        Fonts: []string{"wqy-microhei.ttc"}, // 字体
    }
    driver = driverString.ConvertFonts()
    captcha := base64Captcha.NewCaptcha(driver, store)
    id, b64s, err := captcha.Generate()
    if err != nil {
        // 处理生成验证码时的错误
        response.FailWithMessage("登录失败", c)
    }
    response.OkWithData(&view.Captcha{
        Key: id,
        Img: b64s,
    }, c)
```

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "img": "data:image/png;base64,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",
        "key": "nuVO3GrYAHsZ7ZRbCDNn"
    }
}
```

## 3.使用验证码

在前端页面使用img标签进行展示就可以了

## 4.校验验证码

登录提交时携带验证码及id一起提交

```json
{"username":"admin","password":"123456","code":"4268","uuid":"nuVO3GrYAHsZ7ZRbCDNn"}
```

后台接收参数后，进行验证码校验

```go
// VerifyCaptcha 校验验证码
func VerifyCaptcha(id string, VerifyValue string) bool {
    // 参数说明: id 验证码id, verifyValue 验证码的值, true: 验证成功后是否删除原来的验证码
    if store.Verify(id, VerifyValue, true) {
        return true
    } else {
        return false
    }
}
```

```go
// Login 登录
// @Summary 登录系统
// @Router /sysOauth2/login [post]
func (api *SystemApi) Login(c *gin.Context) {
    var loginUserView view.LoginUserView
    _ = c.ShouldBindJSON(&loginUserView)
    // 校验验证码
    captcha := VerifyCaptcha(loginUserView.VerifyUuid, loginUserView.VerifyCode)
    if !captcha {
        response.FailWithMessage("验证码错误", c)
        return
    }
    // 取加密密码
    hashedPassword := utils.EncryptionPassword(loginUserView.Password, byUserName.Salt)
    if hashedPassword != byUserName.Password {
        global.Logger.Error("登录失败")
        response.FailWithMessage("登录失败", c)
        return
    } else {
        token, err := framework.GenerateToken(userView.Id, userView.UserName)
        if err != nil {
            response.FailWithMessage("登录失败", c)
            return
        }
        response.OkWithData(token, c)
    }
}
```

## 5.总结

这里使用 base64Captcha 生成了验证码，配置很多可以自行查看文档

```go
driverString := base64Captcha.DriverString{
        Height:          40,    //高度
        Width:           100,   //宽度
        NoiseCount:      0,     //干扰数
        ShowLineOptions: 2 | 4, //展示个数
        Length:          4,     //长度
        // Source:          "1234567890qwertyuiplkjhgfdsazxcvbnm", //验证码随机字符串来源
        Source: "1234567890", //验证码随机字符串来源
        BgColor: &color.RGBA{ // 背景颜色
            R: 3,
            G: 102,
            B: 214,
            A: 125,
        },
        Fonts: []string{"wqy-microhei.ttc"}, // 字体
    }
```

在登录页面使用 img 标签进行验证码的展示，在进行登录时，携带验证码及验证码id进行提交，使用 base64Captcha.DefaultMemStore.Verify 函数进行校验。

还有其他的验证码生成方式，大家可以自行研究。
