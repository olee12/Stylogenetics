import requests;
from bs4 import BeautifulSoup;
from builtins import print


def ebay_spider(max_page):
    page = 1;
    while page <= max_page :
        url = "http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_nkw=macbook&_pgn="+ str(page) + "&_skc=50&rt=nc";
        print(url)
        source_code = requests.get(url);
        plain_text = source_code.text;
        soup = BeautifulSoup(plain_text,'lxml');

        for link in soup.findAll('a',{'class':'vip'}) :
            href = link.get('href');
            title = link.string;
            print(title);
            print(href);
            get_single_item_data(href);
        page+=1;


def get_single_item_data(item_url):
    source_code = requests.get(item_url);
    plain_text = source_code.text;
    soup = BeautifulSoup(plain_text, 'lxml');

    for link in soup.findAll('span', {'class': 'notranslate',"itemprop":"price"}):
        price = link.string;
        print("price :",price);

ebay_spider(3);
