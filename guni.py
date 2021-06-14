
bind = "127.0.0.1:8000"  # 绑定的ip与端口
workers = 3  # 核心数

backlog = 512
errorlog = "/www/log/gunicorn_error.log"  # 发生错误时log的路径
accesslog = "/www/log/gunicorn_access.log"  # 正常时的log路径
# loglevel = 'debug'   #日志等级
proc_name = "dj"  # 进程名

