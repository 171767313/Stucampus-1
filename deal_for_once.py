# -*- coding:utf-8 -*-
# flake*: noqa

import os
import urllib2
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


path1 = './webroot/'

fileList = []
files = os.listdir(path1)

for f in files:
    fileList.append(f)


access_key = 'Zku6ZER5pyqaONQCdGpZ2HhakGoguWsoeIw_Xl96'
secret_key = 'i0JvaLpxriPKgxVGfjaeSalLE-7fYrWcbgaU6fXq'
url = "http://7xrrsw.com1.z0.glb.clouddn.com/"

q = Auth(access_key, secret_key)

bucket_name = 'stucampus-for-jiangxia'

for deal_target in fileList:
    key = deal_target
    token = q.upload_token(bucket_name, key, 60)
    deal_target = deal_target.decode("utf-8")
    localfile = path1 + deal_target
    ret, info = put_file(token, key, localfile)
    os.remove(localfile)
    
    f = open(path1 + deal_target, 'w')
    obj_url = urllib2.Request(url + deal_target)
    content = urllib2.urlopen(obj_url).read()
    f.write(content)
    f.close()
    print deal_target + " has been dealt successfully."

