# frida-hook
This is the frida hook exercise project.

### 官网
```
https://frida.re
```
### 源代码
```
https://github.com/frida/frida/releases
```

## 环境安装步骤 
step 1: 下载手机端服务
```
https://github.com/frida/frida/releases
找到包含server相对应的设备及架构
eg: frida-server-16.0.7-android-arm64.xz
```
step 2: 解压包并将包导入设备目录，修改执行权限
```
# 解压并修改名称： frida-server-16.0.7-android-arm64.xz > frida-server  
adb push frida-server /data/local/tmp
# 设置可执行权限
adb shell 
su
cd /data/local/tmp
chmod -x frida-server
```
setp 3: 将手机服务端口映射到本地端口
```
adb forward tcp:27042 tcp:27042
```

### frida 常用命令
```shell
frida-ls-devices  # 查看设备信息
frida-ps -Uai     # 查看设备进程


```




