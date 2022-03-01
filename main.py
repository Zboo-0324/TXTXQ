import os
import shutil

firstdir = 'D:/Desktop/ex/'  # 文件原路径
tardir = 'D:/Desktop/'  # 文件目标路径路径
pathdir = os.listdir(firstdir)  # 获取所在路径下的所有文件

path = []
for path1 in pathdir:
    path.append(firstdir + path1)

for file in path:
    cut1 = file.split('.')
    if cut1[-1] == 'txt':
        cut2 = file.split('/')
        shutil.move(file, tardir + '/' + cut2[-1])
