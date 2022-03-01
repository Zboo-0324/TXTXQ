import os
import shutil

firstdir = 'D:/Desktop/ex/'  # 要复制文件所在路径
tardir = 'D:/Desktop/'  # 想要复制到的路径
pathdir = os.listdir(firstdir)  # 获取所在路径下的所有文件

path = []
for path1 in pathdir:
    path.append(firstdir + path1)

for file in path:
    cut1 = file.split('.')
    if cut1[-1] == 'txt':
        cut2 = file.split('/')
        shutil.move(file, tardir + '/' + cut2[-1])
