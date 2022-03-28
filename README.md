# 指点天下
## 功能
1. 每日健康打卡自动打卡
2. 晚上定位签到(经纬度要精确到10位)
3. 推送方式支持PushPlus(使用其它推送方式自己更改即可)
4. 支持[Github Actions](https://github.com/beggerlove/ZDTX) & [腾讯云函数](https://github.com/beggerlove/ZDTX/tree/serverless)

## 注意事项
- 这里所需要的抓包工具(证书安装视频也包括)还有低版本的的指点天下我打包放在[百度云盘](https://pan.baidu.com/s/1ZhgkBPuQL_TplsMtFLWs1A) 提取码是:q8v9
- 利用Github运行的时候时间不精确，如果学校有晚签推荐使用[腾讯云函数](https://github.com/beggerlove/ZDTX/tree/serverless/)

> 本项目Fork自[@Qutue](https://github.com/Qutue)

## 部署到Github运行
- 1.首先保证你有一个[Github账号](https://github.com/)

- 2.fork[本仓库](https://github.com/beggerlove/ZDTX)到你的Github
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@master/img/img3.png)
- 3.打开settings，找到secrets
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@master/img/img2.png)
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@master/img/img1.png)

- 4.新建secret如下
| secret_iD   | value                   |
| ----------- | ----------------------- |
| PHONE       | 登录手机号|
| PASSWORD    | 登录密码|
| ADDRESS     | 打卡定位地址|
| LAT         | 纬度|
| LNG         | 经度|
| DISTRICT    | 地区:如xx省-xx市-xx区|
| DEVICETOKEN | 你抓包得到的devicetoken|
| PUSHPLUS       | PushPlus推送的token|

- 5.DEVICETOKEN[获取方法](https://mp.weixin.qq.com/s/9ww2373nxj3JyV4o1VAvAw)。

- 6.经纬度可以进入各大地图官网查询自己的经纬度

- 7.PushPlus使用参见[官网](http://www.pushplus.plus/)。

- 8.开启 Actions 并触发每日自动执行
Github Actions 默认处于关闭状态，大家请手动开启 Actions ，执行一次工作流，验证是否可以正常工作。
![Fork](https://cdn.jsdelivr.net/gh/beggerlove/ZDTX@master/img/img4.png)

- 7.如果需要修改每日任务执行的时间，请修改 `.github/workflows/clockIn_new.yml`，在第 8 行左右位置找到下如下配置。

```yml
  schedule:
    - cron: '10 21 * * *'
    # cron表达式，Actions时区是国际时间，国际时间21点的时候，国内时间是5点。
    # 示例： 每天早上8点10分执行 '13 21 * * *'
```

## 致谢
@[Qutue](https://github.com/Qutue)

@[sauciest9](https://github.com/sauciest9)


