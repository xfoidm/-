#Image.open(os.path.join(self.filename,i))
import random
from PIL import Image
import os
import pickle

import pickle
####获取所有文件路径####
result = []
def py_list(tdir):
    get_dir = os.listdir(tdir)
    
    for i in get_dir:
        sub_dir = os.path.join(tdir,i)
        if(os.path.isdir(sub_dir)):
            py_list(sub_dir)
            
            
            
            
            
        else:
            
            result.append(sub_dir)
#py_list(search_dir)
####获取所有文件路径####


#with open('saved_list.data','rb') as w:
    #pickle.dump(random.sample(result,len(result)),w)
#    result += pickle.load(w)
#print(len(result))

search_dir = 'F://pic2\\pic'
####保存路径变量，第一次要运行###
'''
with open('saved_list_.data','wb') as w:
    
    pickle.dump(random.sample(result,len(result)),w)
    
    #result = pickle.load(w)
'''
####读取变量，以后多次都运行这个部分######
with open('saved_list_.data','rb') as w:
    
    #pickle.dump(random.sample(result,len(result)),w)
    
    result = pickle.load(w)

#######网页生成######
with open('new.html','w',encoding = 'utf8') as w:
    w.write('<!DOCTYPE html> \n')
    w.write('<html> <head> <meta charset="utf-8" /> <title>图片演示</title> </head> <body> ')
    for i in result[200:300]:#选取生成的图片下标
        if('.mp4' in i or '.webm' in i):
            w.write("<p>" + str(i) +"<p>")
            w.write(r"<p> <embed src=" + "\"" + str(i)+ "\"" + " width = \"1300\" height = \"1000\"/> </p> ")

        else:
            w.write("<p>" + str(i) +"<p>")
            w.write("<p> <embed src="+ "\"" + str(i)+ "\"" +  " /> </p> ")


    w.write('</body> </html> ')
#######网页生成######
