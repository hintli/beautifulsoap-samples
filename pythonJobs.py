import requests
from bs4 import BeautifulSoup
url = "https://www.python.org/jobs"
r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
#kaç page var ul pagination classı içinde kaç li varsa o kadar sayfa vardır.
# -2 next ve prev
pages = len(soup.find_all("ul",attrs={"class":"pagination"})[0].find_all("li")) - 2
totalJobs = 0
#pageNumbera göre dönücez
for pageNumber in range(1,pages + 1):#10 dahil olmuyor
    #misal 1. sayfa kaynağını alıyoz
    pageRequest = requests.get("https://www.python.org/jobs/?page=" + str(pageNumber))
    pageSource = BeautifulSoup(pageRequest.content,"lxml")
    #her bir kutu-bir iş div.row>ol>li(isim,maaş,şirket...)
    jobs = pageSource.find("div",attrs={"class":"row"}).ol.find_all("li")
    # Tüm işleri çektik, döngü ile ilan detaylarını alalım.
    for job in jobs:
        name = job.h2.find("a").text
        location = job.find("span",attrs={"class":"listing-location"}).text
        #brden sonraki etiket
        company = job.find("span",attrs={"class":"listing-company-name"}).br.next.strip()
        publish_time = job.find("time").text
        totalJobs += 1
        print(name,company,location,publish_time,sep="\n")#sep her bir değişkeni basarken arasına \n "alt satıra geç"
        print("-"*60)

print("Total {} jobs found.".format(totalJobs))

#misal her bir ürünün içine girip içindende bir şeyler çekmek istersek
#a etiketini al ve request yapıp istediklerini yap