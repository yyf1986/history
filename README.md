vim /etc/profile

 ```
export PROMPT_COMMAND='\
cmd=$(history 1 | { read x y; echo $y; })
user=$(who ami i|awk "{print \$1}")
tty=$(who ami i|awk "{print \$2}")
rq=$(who ami i|awk "{print \$3\" \"\$4}")
ip=$(who ami i|awk "{print \$5}"|sed -e "s/(/ /" -e "s/)/ /")
pwd=`pwd`
curl -X POST "http://10.11.20.127:8089/v1/cmd/" -H  "accept: application/json" -H  "content-type: application/json" -d "{  \"Cmd\": \"$cmd\",  \"Ip\": \"$ip\",  \"Pwd\": \"$pwd\",  \"Rq\": \"$rq\",  \"Tty\": \"$tty\",  \"Username\": \"$user\"}"
'
```

source /etc/profile

启动web收集服务
