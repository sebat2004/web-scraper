from bs4 import BeautifulSoup

with open("sssindex.html") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find_all("p")

for food in tag:
    food = food.string
    print(food)