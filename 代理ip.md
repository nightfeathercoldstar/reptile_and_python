import requests

proxies={

    "https":"https://101.37.22.207:3128"

}

resp=requests.get("https://www.baidu.com",proxies=proxies,verify=False)

resp.encoding="utf-8"

print(resp.text)