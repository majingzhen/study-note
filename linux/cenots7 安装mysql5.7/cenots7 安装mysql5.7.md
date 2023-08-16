### cenots7 安装mysql5.7

#### 1. 下载 MySQL Yum Repository 

​	`wget http:``//dev``.mysql.com``/get/mysql57-community-release-el7-8``.noarch.rpm` 

#### 2. 添加 MySQL Yum Repository 

​	` yum localinstall mysql57-community-release-el7-8.noarch.rpm `

#### 3. 通过 Yum 来安装 MySQL 

​	 `yum install mysql-community-server` 

#### 4.修改 root 账户密码

 - 修改 mysql 配置，让 mysqld 启动时不对密码进行验证

   修改 /etc/my.cnf，在 [mysqld] 小节下添加一行：skip-grant-tables=1

 - 重启 mysqld 服务

   ` systemctl restart mysqld `

- 使用 root 用户登录到mysql

  ` mysql -u root  `

-  切换到 mysql 数据库 

  `use mysql;`

- 更新 root 用户密码

  `update user set authentication_string = password('root'), password_expired = 'N', password_last_changed = now() where user = 'root';`

   在之前的版本中，密码字段的字段名是 password，5.7版本改为了 authentication_string 

- 退出 mysql 

- 编辑 /etc/my.cnf 文件，删除 skip-grant-tables=1 的内容

- 重启 mysqld 服务

  ` systemctl restart mysqld `

#### 5.设置 mysql 开机自动启动

​	`shell> systemctl enable mysqld`

​	` shell> systemctl daemon-reload `

#### 6.开启远程登录访问

 - 使用 root 账户登录

   ` mysql -uroot -proot  `

-  切换到 mysql 数据库 

  `use mysql;`

- 开启远程访问权限

  `GRANT  ALL PRIVILEGES  ON *.* TO 'root'@'%';`

- 刷新授权

  ` flush privileges; `



​	







