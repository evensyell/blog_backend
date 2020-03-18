import os, time, random,hashlib,datetime
from django.conf import settings
 
# 计算文件的md5
def GetMd5(file):
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    return md5.hexdigest()
 
#文件重命名及写入
def Save_and_Rename(file):
    times=time.strftime('%Y%m%d%H%M%S')
    ran=random.randint(0,1000)
    ext = os.path.splitext(file.name)[1]
    newfile="{}{}{}".format(times,ran,ext)
    path=os.path.join('filesome/img/',newfile).replace('\\','/')
    read=open(path, 'wb+')
    for chunk in file.chunks():
        read.write(chunk)
    read.close()
    return  path
 