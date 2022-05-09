import os

parentdir = "E:/Medios Cine/"

subdir = os.listdir(parentdir)

for i in subdir:
    if (os.path.isdir(os.path.join(parentdir,i))):
        pickedfold = os.path.join(os.path.join(parentdir,i),"Picked")
        os.mkdir(os.path.join(pickedfold,"Done"))