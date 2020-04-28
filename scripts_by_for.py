import requests
import urllib3
from requests_toolbelt import MultipartEncoder
import os


N = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 禁用安全紧急警告
myPicList = os.listdir("./pic")

for i in range(len(myPicList)):
    url = "https://mfgtest.deckers.com/storage-service/aws/storagenode.mvc?" \
          "sbId=40289f1f69d9253d0169d942591c0001&" \
          "sdId=028770d1133c45ab8260c08ef19c129d&" \
          "parentId=ff8080816b0cbcac016b0cf148ab0002&" \
          "isFolder=N"
    cookies = {"token_UAT_AWS": "75e14dc7-3557-4243-9e76-07d54f5fc219"}
    m = MultipartEncoder(fields={'doc': (myPicList[i], open('./pic/' + myPicList[i], 'rb'), 'image/jpeg')})
    headers = {'Content-Type': m.content_type}  # Content-Type = Multipart Form data
    r = requests.post(url=url, headers=headers, cookies=cookies, verify=False, data=m)  # 不进行SSL认证
    print("第 %d 次请求：\n %s" % (i+1, r.text))
