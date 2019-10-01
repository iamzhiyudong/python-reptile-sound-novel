import requests
import re       #导入所需模块
import os
import time

#定义全局变量 文件名的  编号   (初始值为 1 )
global file_name_num
file_name_num = 1


#下载文件的方法
def download_file(url,folderpath,num,file_name):     #参数中 folderpath 为要保存的文件夹的路径    num 为文件编号
    #文件夹不存在则创建文件夹
    folder = os.path.exists(folderpath)
    if not folder:
        os.makedirs(folderpath)

    print('---正在下载第' + str(num) + '集>>>>>', folderpath+'/'+file_name+'-'+str(num)+'.mp3')

    #读取远程MP3资源
    res = requests.get(url)
    res.raise_for_status()

    #设置保存的文件名
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #修改文件名的地方
    filename = os.path.basename(file_name+'-'+str(num)+'.mp3')
    file_path = os.path.join(folderpath, filename)


    #保存到本地
    mp3_file = open(file_path, 'wb')
    for chunk in res.iter_content(100000):
        mp3_file.write(chunk)
    mp3_file.close()
    print('  ***第'+str(num)+'集下载成功')

    #修改文件编号  加 1
    global file_name_num
    file_name_num+=1


#获取下载链接的方法
def getinfo(url0):
    #请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    #请求网页数据
    req = requests.get(url=url0, headers=headers)
    req.encoding = 'utf-8'
    html = req.text

    #查找下载链接
    res = re.findall(r"http://(.*).m4a", html)

    #拼合链接
    res = 'http://' + res[0] + '.m4a'
    return res

def onclick(file_name,store_path,wangzhi,begin0,end0):
    #网页路径

    begin = int(begin0)
    end = int(end0)

    global file_name_num
    file_name_num = begin
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #修改要下载的小说的网址  以及下载的集数
    wangzhi_1 = wangzhi
    strinfo = re.compile('-(\d|\d\d|\d\d\d|\d\d\d\d).shtml')
    wangzhi_2 = strinfo.sub('-{}.shtml', wangzhi_1)

    urls = [wangzhi_2.format(str(i)) for i in range(begin, end+1)]
    #'https://www.qktsw.net/ting-book-play-3483-1-{}.shtml'
    #https://www.qktsw.net/

    print("############开始下载############")
    for url in urls:
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #设置要保存到的路路径
        folderpath = store_path
    #通过函数返回下载链接
        url_download = getinfo(url)
    #开始下载

        download_file(url_download, folderpath, file_name_num, file_name)

        time.sleep(1)

    print("############全部下载完成############")

