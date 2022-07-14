# 部署到腾讯云函数运行
## 功能

- 功能与[Github运行功能一致](https://github.com/beggerlove/ZDTX/tree/master)

## 注意事项
- 一定要修改脚本内相应的变量，还有学校的登录域名，否则无法运行

## 部署到腾讯云函数

- 1.fork[本仓库](https://github.com/beggerlove/ZDTX)
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@master/img/img3.png)
- 2.切换分支下载压缩包到你本地解压好备用
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/1.png)
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/2.png)
- 3.点击进入[腾讯云控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)
- 4.点击新建
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/3.png)
- 5.从头开始-函数名称随意

> 这里选择 python3.6

![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/4.png)
- 6.改入口函数为 index.main_handler
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/5.png)
- 7.改超时时间(如果出现什么 timeout 什么 3 secords 就改，没有也可以不改)
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/6.png)
- 8.把异步执行和状态追踪打开
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/7.png)
- 9.配置cron语句
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/8.png)
- 10.配置配置文件
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@serverless/img/9.png)
### 鸣谢
@[Qutue](https://github.com/Qutue)
