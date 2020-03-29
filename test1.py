import requests
link = 'http://' + 'freevids.ga/download/Kg1_zcXfqfE/ti-sn-ca-trn-i-quang-nh-th-no-_3gp-mp4-flv-avi-mp3-webm.html'
res1 = requests.get(link)
#res2 = requests.get('http://24h.com.vn')
print(res1.status_code, res1.reason)
#print(res1.content.decode('utf-8'))
a = res1.content
print(res1.status_code)
print(type(int(res1.status_code)))
if res1.status_code == 200:
    print('access')
else:
    print('dont')
#print(res1.content)
#print(res2.content)

