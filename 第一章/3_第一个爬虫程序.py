from urllib.request import urlopen
url = "https://www.baidu.com"
response = urlopen(url)
with open("mybaidu.html", mode="w") as f:
    f.write(response.read().decode("utf-8"))
print("Done!")
