# -*- coding:utf-8 -*-

## 依赖库
import argparse,threading,os
from lib.from_baidu import from_baidu
from lib.from_google import from_google
#读取域名文件
def txtmerge(path):
    txtlist = []
    try:
        with open(path, 'rb') as filename:
            for oneline in filename.readlines():
                oneline = oneline.decode('utf-8').strip()
                txtlist.append(oneline)
            return set(txtlist)
    except:
        print('open file false')
        return False

def threaduse(linelist):
    threads = []
    for line in linelist:
        t = threading.Thread(target=get_webdomain, args=(line,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def get_webdomain(line):
    domainvalues = from_baidu(line)
    domainlist1 = domainvalues.get_subdomain()
    domainvalues = from_google(line)
    domainlist2 = domainvalues.get_subdomain()
    domainlist = domainlist1 | domainlist2
    txtwrite(domainlist,line)

def txtwrite(linelist,path):
    filepath = os.getcwd()+'/output/'+path+'.txt'
    with open(filepath, 'w') as file:
        for line in linelist:
            file.write(line+'\n')

if __name__ == "__main__":
    #读取命令行参数
    parser = argparse.ArgumentParser(description="Web - based subdomain collection tool")
    parser.add_argument("-u", help="Enter the domain name")
    parser.add_argument("-f", help="Enter file name")
    args = parser.parse_args()
    #生成域名列表
    domainlist = []
    if(args.f):
        filename = args.f
        domainlist = txtmerge(filename)
        threaduse(domainlist)
    elif(args.u):
        domainlist.append(args.u)
        threaduse(domainlist)
    else:
        print ('请输入参数')