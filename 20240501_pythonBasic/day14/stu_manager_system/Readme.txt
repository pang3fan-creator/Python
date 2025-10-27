某高校有一个学生管系统，可以添加、显示、删除、修改学生信息 姓名 年龄 性别
添加方法
显示方法
删除 --> 名字
修改 --> 啥都能改

1. 创建模块bll,存储 xxxController 业务逻辑层 business logic layer
2. 创建模块usl,存储 xxxView 用户显示层 user show layer
3. 创建模块dtl,存储 xxxModel 数据传输层 data transfer layer
4. 创建模块main，调用xxxView的代码，启动程序
