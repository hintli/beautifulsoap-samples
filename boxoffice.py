import requests
from bs4 import BeautifulSoup

#site adresi
url = "https://boxofficeturkiye.com/hafta/?yil=2018&hafta=7"
#server istek attığımızda user-agent,refear,tarayıcı bilgisii felan yoksa hata verebiliyor
#sasyfa incele-network-ilki-request headers: user-agent copy-paste yap
headers_param = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
#servera istek attık sayfa kaynağını aldık
r = requests.get(url,headers = headers_param)
#bsye verdik-güzelleşti
soup = BeautifulSoup(r.content,"lxml")


# class değeri ustcizgi olan table altındaki 2. tr nin altındaki td nin altındaki 3. table ın altındaki tr yi çektik.
filmTablosu = soup.find("table",attrs={"class":"ustcizgi"}).select("tr:nth-of-type(2) > td > table:nth-of-type(3) > tr")

for i in range(1,21):
    #a etiketli classı şu olanın titlenın çek//yoksa link olarak gelir
    filmAdi = filmTablosu[i].find("a",attrs={"class":"film"}).get("title")
    #copy celector-td url kısmına yapıştır kaçıncı td
    toplamSeyirci = filmTablosu[i].select("td:nth-of-type(10) > font")[0].text
    hasilat = filmTablosu[i].select("td:nth-of-type(9) > font")[0].text
    print("Film Adı: {} \nHasılat: {} \nToplam Seyirci: {}".format(filmAdi,hasilat,toplamSeyirci))
    print("-"*30)

#boxofficedeki filmlerin adı,hasılat,seyirci listele
#python3 etkileşimlii kabuğa geç