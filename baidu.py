import requests, re

a = re.findall(".+?\"one-line.+", requests.get("http://top.baidu.com/", headers={"User-Agent": "Android"}).text)

print("今日热搜(来自：top.baidu.com)")

for i in range(len(a)):

	print("%d. %s" % (i + 1, re.search(r"(?<=>).*?(?=<)", a[i]).group()))
