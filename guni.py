import multiprocessing
bind = "127.0.0.1:8000"  # 绑定的ip与端口
workers = multiprocessing.cpu_count() * 2 + 1  # 核心数
worker_class = 'gevent'

timeout=60
backlog = 512
errorlog = "/www/log/gunicorn.error"  # 发生错误时log的路径
accesslog = "/www/log/gunicorn.log"  # 正常时的log路径
# loglevel = 'debug'   #日志等级
proc_name = "dj"  # 进程名

