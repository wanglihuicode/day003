#提取图片存入文件
import  requests
URLS = []
url = 'http://www.image-net.org'
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wind=n02127808'
response = requests.get(url)
HTML = res.text
#print(HTML)
URLS = html.SPLIT('\n')
for url in URLS
    name = url.split('/')[-1]
    #print(name)
    response = requests.get(url)
    content = response.content
    with open(name,'wb') as f:
        f.write(content)
#寻找http,https
impoer requests
url = 'http://www.baidu.com/s?'
def baidu(wds):
    count = 1
    for wd in wds:
        res = requests.get(url,params={'wd':wd})
        path = 'res%d.txt'%count
        with open(path,'w',encoding='utf8') as f:
            f.write(res.text)
            count +=1
if__name__=="__main__":
 wds = ('美女','丑女','Joker')
 baidu(wds)
 str_ =open('res1.txt',"rb").read()
 results = res1.findall('http://www.baidu.com/s?',s)
 with open('urls.txt','wb').write("\r\n",joint(results))
     print(wb)