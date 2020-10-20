import requests
import random
import os
pts=input('Print path to save waifu\n')
i=int(input('Print nums of waifu\n'))
url='https://www.thiswaifudoesnotexist.net/example-'
ext='.jpg'
os.chdir(pts)
for i in range(0,i):
    exnum=random.randint(1,99999)
    exnumstr=str(exnum)
    flink=url+exnumstr+ext
    file=exnumstr+'.jpg'
    r = requests.get(flink)
    with open(file, "wb") as code:
        code.write(r.content)
    print('Downloading {}... Completed!'.format(file))
print('Programm by Alexsandr Uskov\nGithub:https://github.com/PaintedCat/TWDNE-scrapper')

