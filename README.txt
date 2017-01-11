vim /etc/profile

####
export HISTTIMEFORMAT="%Y-%m-%d_%H:%M:%S "
#export PROMPT_COMMAND='{ msg=$(history 1 | { read x y; echo $y; });echo $(date +"%Y-%m-%d %H:%M:%S") [$(whoami)@$SSH_USER `pwd` ]" $msg" >> /var/log/history_log; }'
export PROMPT_COMMAND='\
msg=$(history 1 | { read x y; echo $y; })
user=[`who am i`:`pwd`]
curl -X POST -d "$user $msg" http://10.21.38.77:8000/log
'
####

source /etc/profile
