from pathlib import WindowsPath


file_inpath = file_inpath.encode('utf-8')
print(file_inpath)                         #result: 3D\cam\21、碱制备单元\
print(type(file_inpath))                   #result: <type 'str'>
folder_names = WindowsPath(file_inpath)
print(type(folder_names))                  #result: <class 'pathlib.WindowsPath'>
print(folder_names.parts)                  #result: ('3D', 'cam', '21\xe3\x80\x81\xe7\xa2\xb1')




#coding:utf-8


#SyntaxError: encoding declaration in Unicode string (<input>, line 0)