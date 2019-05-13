#No1
print('no 1')
import re

f = open('Indonesia.txt', 'r')
p = r'me[\w\.-]+'
string = re.findall(p, f.read())
print (string)

#No2
print ('no 2')
import re
f = open('Indonesia.txt', 'r')
p = r'di[\w\.-]+'
string = re.findall(p, f.read())
print (string)

#No3
print ('no 3')
f = open ('Indonesia.txt', 'r')
r = r'di\s[\w\.-]+'
string3 = re.findall(r, f.read())
print (string3)

#No4
import re

wiki = open('KEI.html', 'r')

teks = wiki.read()
wiki.close()


cari = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', teks)

listbaru = []

for i in cari:
    a = (i[0],float(i[4]))
    listbaru.append(a)

print(listbaru)
