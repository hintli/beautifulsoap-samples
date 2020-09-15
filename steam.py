#kaynak kodunu almak için
import requests
#kaynak kodunu parse etmek için
from bs4 import BeautifulSoup

#web sitesine bağlan(sayfa kaynağını al)
#
r = requests.get("https://goo.gl/pXM4u1",allow_redirects=True,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"})
#kaynak kodunu bsye aktar,lxml kütüphanesi ile parçalıycaz
soup = BeautifulSoup(r.content,"lxml")

#classı tab_row olan tüm divleri seç //oyun adını,resmini felan tutuyo
#find deseydik ilk divi getirirdi
games = soup.find_all("div",attrs={"class":"tab_row"})
#kaç div var
print("{} games listed.".format(len(games)))

print("#"*20)

for game in games:
    try:
        #format(1.alan,2.alan,3.alam)
        print("Game: [{}] -> Discount: [{}] -> Price: [{}] -> Url: [{}]".format(
        game.h4.text,#oyunun adını aldık
        #indirim(div class olduğu için game.div yazamıyoz)
        #classı şu olanı bana getir
        #kodlardan arındırmak için string  //.strip boşluk kaldırma
        game.find("div",attrs={"class":"tab_discount discount_pct"}).string.strip(),
        #fiyat
        game.find("span",attrs={"class":"price"}).string.strip(),
        #
        game.find("div",attrs={"class":"tab_overlay"}).a.get("href")
        ))
    except Exception as e:
        pass

#belirli bir kaynağın içindeki verileri alırız
#steam kaynak kodunu al beatifulsoapa aktar ve oyunun adını fiyatını almaya çalış
#kurulum pip3 install beatifulsoup4
#sudo apt-get install python3-pip
