# coding=UTF-8
import requests
from bs4 import BeautifulSoup

def note():
    HeaderLogin = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }  # 登录头
    url="http://47.94.21.213/mydata"
    web = requests.get(url+"/test1.txt")
    f=open('test1.txt','w')
    f.write(web.text)
    f.close
    wav = requests.get(url+"/result.wav")
    f=open(r'result.wav','ab')
    f.write(wav.content)
    f.close

    return sum
if (__name__=='__main__'):
    print(note())