import requests, bs4

res = requests.get("http://172.23.160.212/")

soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select("#author")
print(elems[0].getText())
