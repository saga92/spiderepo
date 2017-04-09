#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
def getList():
	url="http://wenshu.court.gov.cn/List/ListContent?MmEwMD=15NhbPCRuF_OfGY38NcupF3nOqSowZ.UZAD45cfq7YLUvBDnjSdxwO8V4iYLWarbIhjZ2RqaRchwzb6m3fQlD7OVd1TI8lCLH7yj.ybT4p2JoRGohz_b9wRiqmedb11n9FnCyoECPB4H.RPk_Fnb1pvgNEVEQsV7WnL4mULcH1bpuGOLEtzBAHlnVqBeYM_ySzfzWDgktCk0wHhTcfSlUdQwtpoFJcm2HnPtDGNafFp4tiWpCIhdgwm_rz1eQnvo5yWFLvdbp4aDt6XQl36EYjoYSDQSJNcw_Wuq1ivXYkHivXK_gNdWeNePKlE1cYHfmeASBqYISRqY3rVP4U2Ehj.KZ_WblFYIvdw1FKr1FdYOInAl46mNx.V5I9l765WtTk5"
	headers={'Referer':'http://wenshu.court.gov.cn/list/list/?sorttype=1&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E5%8C%97%E4%BA%AC%E7%9F%A5%E8%AF%86%E4%BA%A7%E6%9D%83%E6%B3%95%E9%99%A2',\
        	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",\
        	'X-Requested-With':'XMLHttpRequest'}
	payload={"Param": "%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2%3A%E5%8C%97%E4%BA%AC%E7%9F%A5%E8%AF%86%E4%BA%A7%E6%9D%83%E6%B3%95%E9%99%A2",\
			'Index':'1', 'Page':'20', 'Order':'%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7', 'Direction':'asc'}
	cookies={'FSSBBIl1UgzbN7N80S':'OTKybKsX6URUtiai7uuP18iIY6hD18WhDqoLt9t4EFXLiKF.EniquFvuXlVNLko5',\
 		'ASP.NET_SessionId':'oo0pu1jxyna3nur4fjiizg44','_gscu_2116842793':'91700068gl8i3s79', '_gscs_2116842793':'917000681tb4v379|pv:6', '_gscbrs_2116842793':'1',\
  		'Hm_lvt_3f1a54c5a86d62407544d433f6418ef5':'1491700069', 'Hm_lpvt_3f1a54c5a86d62407544d433f6418ef5':'1491702785',\
  		'FSSBBIl1UgzbN7N80T':'1O8KpdrlloJ5KePmN0TXboBBVwDFjfQthJSbxIKwMEItAnSBw7EVj5NxWsPT4zC4LKwf1l6zXIZqF4q3BZ.RSSVhMw8zhZoSsWXL18sNz_cnO39MbNcaqPrk9rPrleLgBGgYIBtlQrNu8eJs5WvME504t1qR_SsZSw176cLDWtBQhRLuD.z3BUy6nV2G60HurY.m9.Yq3FvmyxIfEVkiuf1FmZwGEW951Qt2BXIdrx9JeIsyrRAD.D0ue0M2G2iA1sUM_cGfllLyhowZpTaDcwekxSfGTG3eRvuZDPDU0o7SCWZeGQ479z_lBdeZ90eNlca'}
	r=requests.post(url, headers=headers, data=payload, cookies=cookies)
	print r.content

def getDoc():
	url="http://wenshu.court.gov.cn/CreateContentJS/CreateListDocZip.aspx?action=1"
	headers={'Referer':'http://wenshu.court.gov.cn/list/list/?sorttype=1&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E5%8C%97%E4%BA%AC%E7%9F%A5%E8%AF%86%E4%BA%A7%E6%9D%83%E6%B3%95%E9%99%A2',\
        	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
	payload={"docIds":"6b89a06f-8b6c-4818-937a-da9e8d050a60%7C%E8%A5%BF%E5%AE%89%E8%A5%BF%E7%94%B5%E6%8D%B7%E9%80%9A%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E9%80%9A%E4%BF%A1%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E4%B8%8E%E8%8B%B9%E6%9E%9C%E7%94%B5%E5%AD%90%E4%BA%A7%E5%93%81%E5%95%86%E8%B4%B8%EF%BC%88%E5%8C%97%E4%BA%AC%EF%BC%89%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E3%80%81%E8%8B%B9%E6%9E%9C%E7%94%B5%E8%84%91%E8%B4%B8%E6%98%93%EF%BC%88%E4%B8%8A%E6%B5%B7%EF%BC%89%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E7%AD%89%E7%AE%A1%E8%BE%96%E8%A3%81%E5%AE%9A%E4%B9%A6%7C2016-09-26"}
	cookies={'FSSBBIl1UgzbN7N80S':'OTKybKsX6URUtiai7uuP18iIY6hD18WhDqoLt9t4EFXLiKF.EniquFvuXlVNLko5',\
 		'ASP.NET_SessionId':'oo0pu1jxyna3nur4fjiizg44','_gscu_2116842793':'91700068gl8i3s79', '_gscs_2116842793':'917000681tb4v379|pv:6', '_gscbrs_2116842793':'1',\
  		'Hm_lvt_3f1a54c5a86d62407544d433f6418ef5':'1491700069', 'Hm_lpvt_3f1a54c5a86d62407544d433f6418ef5':'1491702785',\
  		'FSSBBIl1UgzbN7N80T':'1O8KpdrlloJ5KePmN0TXboBBVwDFjfQthJSbxIKwMEItAnSBw7EVj5NxWsPT4zC4LKwf1l6zXIZqF4q3BZ.RSSVhMw8zhZoSsWXL18sNz_cnO39MbNcaqPrk9rPrleLgBGgYIBtlQrNu8eJs5WvME504t1qR_SsZSw176cLDWtBQhRLuD.z3BUy6nV2G60HurY.m9.Yq3FvmyxIfEVkiuf1FmZwGEW951Qt2BXIdrx9JeIsyrRAD.D0ue0M2G2iA1sUM_cGfllLyhowZpTaDcwekxSfGTG3eRvuZDPDU0o7SCWZeGQ479z_lBdeZ90eNlca'}
	r=requests.post(url, headers=headers, data=payload, cookies=cookies)
	print r.content

if __name__ == '__main__':
	getList();