from urllib import request;

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=3&e=14&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv";

def download_csv_file(csv_url):
    response = request.urlopen(csv_url);
    csv = response.read();
    print(csv);
    csv_string = str(csv);
    lines = csv_string.split("\\n")
    print(lines);

    fw = open(r'csvfile.csv','w');
    for line in lines :
        fw.write(line);
        fw.write("\n");
    fw.close();

download_csv_file(goog_url);
print('hello olee');