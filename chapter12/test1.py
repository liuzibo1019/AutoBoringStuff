import requests

res = requests.get("http://172.23.160.212/Videos/Friends/Friends.S10E01.chs&eng.ass")
playfile = open('test.ass', 'wb')
for chunk in res.iter_content():
    playfile.write(chunk)
playfile.close()