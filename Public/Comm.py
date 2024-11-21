"""
常用的一些单个方法 单个函数 写在这里
多个方法 写在类里
"""

import zipfile,os


#代码打包压缩包
"""
要压缩的文件路径为：file_path ./Repot/report.zip
压缩好放置的路径为：zip_path ./Repot/

"""
def zip_dir(file_path,zip_path):
    #找到路径 下的所有文件
    file_list = os.listdir(file_path)
    #开始压缩./Repot/report文件夹
    zf = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for file in file_list:
        #把文件添加到压缩包里
        zf.write(os.path.join(file_path,file))

    
    


    
