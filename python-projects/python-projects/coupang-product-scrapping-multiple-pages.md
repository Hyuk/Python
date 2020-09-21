# Coupang Product Scrapping Multiple Pages

* Product Title & Price & Rating & Rating Count Scraping including 5 pages
```python
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36"}

for i in range(1, 6):
  url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")

  items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
  for item in items:

    # Exclude the Ads products
    ad_badge = soup.find("span", {"class":"ad-badge-text"})
    if ad_badge:
      continue

    name = item.find("div", attrs={"class":"name"}).get_text()

    # exclude apple product
    if "Apple" in name:
      continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    # exclude no rating
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
      rate = rate.get_text()
    else:
      continue

    # exclude no review
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
      rate_cnt = rate_cnt.get_text()[1:-1]
    else:
      continue

    link = item.find("a", attrs={"class":"search-product-link"})

    # rate > 4.5 && rate_cnt > 100
    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
      print(f"Product Title: {name}")
      print(f"Price: {price}")
      print(f"Rating: {rate}")
      print(f"Review: {rate_cnt}")
      print("link: {}".format("https://www.coupang.com" + link))
      print("-"*100)
```