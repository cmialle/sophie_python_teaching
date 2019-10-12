import os
import bs4

print(os.getcwd())
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")
print(type(exampleSoup))

elem1 = exampleSoup.select('p span')
elem2 = exampleSoup.select('span')

is_same = (elem1 == elem2)
print(is_same)
print(len(elem2))
# print(elem[0].getText())
