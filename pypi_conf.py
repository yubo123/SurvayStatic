import os

ini="""[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
"""
pippath=os.environ["USERPROFILE"]+"\\pip\\"
print(pippath)
if not os.path.exists(pippath):
    os.mkdir(pippath)

with open(pippath+"pip.ini","w+") as f:
    f.write(ini)