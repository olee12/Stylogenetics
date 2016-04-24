import requests;
from bs4 import BeautifulSoup;



fw = open(r'মাহিরাহি.doc', 'w',encoding='utf8');
fw.close();
def blog_spider():
    page = 1;
    cnt = 1;
    source_code = open('mahi_rahi.html','r',encoding='utf8').read();
    plain_text = source_code;
    soup = BeautifulSoup(plain_text,'lxml');

    for link in soup.findAll('h2', {"class": "post-title"}):
        href = link.get('href');
        title = link.string;
        tolink = BeautifulSoup(str(link), 'lxml');
        ll = tolink.findAll('a');
        print(tolink.find('a').string);

        post_link = validate(ll[0].get('href'));
        find_content(post_link, link, cnt);
        cnt += 1;
    #get_single_item_data(href);
    #return ;

def validate(ulr):
    if ulr[0]=='h':
        return ulr;
    else :
        return "http://www.somewhereinblog.net"+ulr;

def find_content(url,title,cnt):
    print(url)
    #return ;
    source_code = requests.get(url);
    plain_text = source_code.text;
    soup = BeautifulSoup(plain_text, 'lxml');
    fw = open(r'মাহিরাহি.doc', 'a', encoding='utf8');
    fw.write(BeautifulSoup(str(title),'lxml').get_text());
    fw.write("\n");
    for link in soup.findAll('div',{"class":"blog-content"}):
        text =  BeautifulSoup(str(link),'lxml').get_text();
        print(text);
        lines = str(text).split("\\n")
        fw.write(str(text));
        break;
    fw.write("\n");
    fw.write("\n");
    fw.write("\n");
    fw.write("\n");
    fw.write("\n");
    fw.close();




blog_spider();
