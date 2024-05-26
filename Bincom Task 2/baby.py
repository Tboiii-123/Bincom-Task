

#Extracting a Baby name from and html file
import re

with open('baby2008.html','r') as Handler:
    BabyName = Handler.read()
    search=re.findall(r'<td>([a-zA-z]+)</td>',BabyName)
    for i in search:
        print(i)

