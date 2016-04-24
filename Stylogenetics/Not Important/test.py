import requests;
from bs4 import BeautifulSoup;



fw = open(r'datafile.doc', 'w',encoding='utf8');
fw.close();
def blog_spider(max_page):
    page = 1;
    cnt = 1;
    while page <= max_page :
        url = "http://www.somewhereinblog.net/blog/sumon98316";
        source_code = requests.get(url);
        plain_text = source_code.text;
        soup = BeautifulSoup(plain_text,'lxml');

        for link in soup.findAll('h2',{"class":"post-title "}) :
            href = link.get('href');
            title = link.string;
            print(title);

            #print(href);
            #print(link);
            tolink = BeautifulSoup(str(link),'lxml');
            ll = tolink.findAll('a');
            print(tolink.find('a').string);
            print(ll[0].get('href'));
            find_content(ll[0].get('href'),link,cnt);
            cnt+=1;
            #get_single_item_data(href);
            #return ;
        page+=1;

def find_content(url,title,cnt):
    source_code = requests.get(url);
    plain_text = source_code.text;
    soup = BeautifulSoup(plain_text, 'lxml');
    fw = open(r'datafile.doc', 'a', encoding='utf8');
    fw.write(BeautifulSoup(str(title),'lxml').get_text());
    fw.write("\n");
    for link in soup.findAll('div',{"class":"blog-content"}):
        text =  BeautifulSoup(str(link),'lxml').get_text();
        print(text);
        lines = str(text).split("\\n")
        fw.write(str(text));
        break;
    fw.write("\n\n\n");
    fw.close();




blog_spider(1);
