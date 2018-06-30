import requests
import json
from linked_list import node
from bs4 import BeautifulSoup as bs

# chcp 65001
date = "20180629"
url = "http://www.twse.com.tw/exchangeReport/MI_5MINS?response=json&date=" + date
html = requests.get(url)
json_data = bs(html.content, "lxml").get_text()
python_data = json.loads(json_data)

def printFormat(key, python_data):
    for element in python_data[key]:
        print("{:^10}".format(element),end = "")
    print()

printFormat("fields", python_data)


root = node(date,True)
for data in python_data["data"]:
    for element in data:
        root.addNode(node(element))

root.traversalPrint()
