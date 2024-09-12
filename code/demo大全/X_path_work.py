#拿到页面源代码
#提取和解析数据
import requests
from lxml import etree

url="https://www.zbj.com/fw/website/"
headers={
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'cookie':
'_uq=1f512f496d4e4df78c3b94683540beb9; uniqid=d014x0eqiykbtm; _suq=b7d05f90-4490-416c-8568-09a5b6f2a673; oldvid=; vid=4a69f8bee7dc0aabe14cdf966d511443; Hm_lvt_a360b5a82a7c884376730fbdb8f73be2=1726038124; HMACCOUNT=D751E37C8FBDE92F; unionJsonOcpc=eyJvdXRyZWZlcmVyIjoiaHR0cHM6Ly9jbi5iaW5nLmNvbS8iLCJwbWNvZGUiOiIifQ==; nsid=s%3APIV86XYyiN2T3E_ccWdPfjXaGCej9CkD.T9S%2FrVo5BslSdJZZOjm5ZfEWyGAxHpfscuTs1P0rlc8; local_city_path=wuhan; local_city_name=%E6%AD%A6%E6%B1%89; local_city_id=3627; Hm_lpvt_a360b5a82a7c884376730fbdb8f73be2=1726038158; vidSended=1; s_s_c=xhA3dh7QsA2lgP8ro4tGRySwnIERGWjvArJ%2B78u21sCm5UiCPP2dQwBXxgDc%2F3pF6FaUuF1flUOHHDURcJsYIS%2BaIbBuqVEvAOKEn0lPjTk%3D'


}
resp=requests.get(url,headers=headers)
print(resp.text)
html=etree.HTML(resp.text)
divs=html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[6]')
for div in divs:
    x=div.xpath('./div/div/@data-linkid/text()')
    print(x)
