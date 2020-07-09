# -*- coding:utf-8 -*-

import requests,re

class webrequest:
    _subdomain = set()
    __headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
                 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                 'Connection':'keep-alive'}
    def __init__(self,domainlist):
        pass

    def _simple_getrequest(self,url,info={}):
        resp = requests.get(url=url,headers=self.__headers,timeout=3)
        resp.encoding = 'utf-8'
        return resp.text

    def _get_refindall(self,patternmatch,resptxt):
        pattern = re.compile(patternmatch)
        domainresult = pattern.findall(resptxt)
        return domainresult

    def get_subdomain(self):
        return self._subdomain

    def _set_headers(self,header):
        self.__headers.update(header)

    def _ifdomain(self,domain,line):
        patten=r''+domain+'$'
        return self._get_refindall(patten, line)
