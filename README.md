#### 首先按照profile.md在需要收集的服务器上进行配置
#### 下载cmdlog至本地
#### 启动
`nohup ./cmdlog > /dev/null 2>&1 &`
#### 说明
- 默认端口8089
- 通过-port指定端口号
- 通过-esip指定es的ip
- 通过-esport指定es的端口
- 指定了es后，会在es里面创建一个cmdlog的index，被收集的服务器IP作为type
- 不指定es或者es连不上，会在当前目录生成一个cmd.log的文件存放命令记录
- 访问http://serverip，显示hello world说明服务启动成功
