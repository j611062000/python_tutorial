import requests
import json
from bs4 import BeautifulSoup as bs

# chcp 65001


class stockPrice():
    def __init__(self, ticker, month, fields = None, title = None, data = None):
        self.ticker = str(ticker)
        self.month = month
        self.url = "http://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=json&date=2018"+self.month+"01&stockNo=" + self.ticker
        html = requests.get(self.url)
        soup = bs(html.content, "lxml")
        python_data = json.loads(soup.get_text())
        
        for key in python_data:
            if key == "fields":
                self.fields = python_data[key]
            elif key == "title":
                self.title = python_data[key]
            elif key == "data":
                self.data = python_data[key]

def printstockprice(dataSet):
    print("{:^15}|{:^15}".format("Date","Closing Price"))
    print("_"*30)
    for data in dataSet:
        print("{:^15}|{:^15}".format(data[0],data[1]))

tsmc2018DataSet = []
for i in range(1,7):
    tsmc2018DataSet.append(stockPrice(2330, "0"+str(i)))
    print("[ {} ]".format(tsmc2018DataSet[i-1].title))
    printstockprice(tsmc2018DataSet[i-1].data)
    print()



