# -*- coding:utf-8 -*-

from lib.webrequest import webrequest
from time import sleep
from urllib.parse import urlparse

class from_google(webrequest):
    def __init__(self, domain):
        nowline = 0
        maxline = 0
        while maxline * 10 >= nowline and nowline < 200:
            url = "https://www.google.com/search?q=site%3A"+domain+"&start="+str(nowline)+"&sxsrf=ALeKk003AHt4-VZXAPUIPDi-2s7PSX5TDA%3A1592813455885&ei=j2fwXr_LNc3_wAP-gIw4"
            resptxt = self._simple_getrequest(url)
            pattern = '((?:(?:[a-z0-9]*?\.)*?)'+domain+')'
            domainresult = self._get_refindall(pattern, resptxt)
            for google_subdomain in domainresult:
                if self._ifdomain(domain,google_subdomain):
                    self._subdomain.add(google_subdomain)
            print(domainresult)
            if maxline * 10 == nowline:
                pattern = r'20px\"></span>(.*?)<'
                numresult = self._get_refindall(pattern, resptxt)
                if numresult:
                    maxline = int(numresult[-1])
            nowline += 10
            sleep(5)

        self._set_headers({'Connection': 'close'})
        self._simple_getrequest(url)

    def __getdomain(self,url):
        res = urlparse(url)
        return res.netloc