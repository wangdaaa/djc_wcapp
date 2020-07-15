import hashlib

from djc_wcapp.settings import IMAGE_TYPE_LIST

m=hashlib.md5()
import time
def create_new_name(name):
    """
    生成uuid.png格式的id
    name="你好.png"
    return
    """
    new_name=None
    name_list=name.split('.')
    print(name_list,"name_list")
    if len(name_list)==2 and name_list[1] in IMAGE_TYPE_LIST:
        name=name_list[0]
        m.update((str(time.time())+name).encode('utf8'))
        print(m.hexdigest(),'sssss')
        new_name=m.hexdigest()+"."+ name_list[1]
    return new_name
a=create_new_name("你好")
# b=create_new_name("aaa")

print(a)
# print(b)
