# -*- coding:utf-8 -*-

from lib.webrequest import webrequest

class from_baidu(webrequest):

    def __init__(self,domain):
        nowline = 0
        maxline = 0
        while maxline*10>=nowline and nowline < 200:
            url = "https://www.baidu.com/s?wd=site%3A"+domain+"&pn="+str(nowline)+"&tn=78040160_14_pg&ie=utf-8&ch=8"
            resptxt = self._simple_getrequest(url)
            pattern = '((?:(?:[a-z0-9]*?\.)*?)'+domain+')'
            domainresult = self._get_refindall(pattern,resptxt)
            for baidu_subdomain in domainresult:
                if self._ifdomain(domain,baidu_subdomain):
                    self._subdomain.add(baidu_subdomain)

            if maxline*10 == nowline:
                pattern = r'<span class=\"pc\">(.*?)</span>'
                numresult = self._get_refindall(pattern,resptxt)
                if numresult:
                    maxline = int(numresult[-1])
            nowline += 10
        self._set_headers({'Connection':'close'})
        self._simple_getrequest(url)
