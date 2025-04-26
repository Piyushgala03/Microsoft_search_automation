from bs4 import BeautifulSoup
import requests
import pyautogui as pg
import random
import time

url='https://timesofindia.indiatimes.com/india'
pg.hotkey('win','1')
pg.hotkey('ctrl','t')
try:
    response=requests.get(url)  
    soup=BeautifulSoup(response.text,'html.parser')
    list1=soup.find_all('a')
    list2=[]
    for i in list1:
        if len(i.getText())<=60:
            if i.getText()!=' ' or i.getText()!='\n' or i.getText()!='\n\n':
                list2.append(i.getText().strip('\n'))
    random.shuffle(list2)
    for i in range(0,35):
        pg.typewrite('bing.com')
        pg.press('enter')
        time.sleep(6)
        pg.typewrite(list2[i])
        pg.press('enter')
        time.sleep(1)
        pg.hotkey('ctrl','t')
    time.sleep(2)
    pg.typewrite('https://rewards.bing.com/status/pointsbreakdown')
    pg.press('enter')
except Exception as e:
    print(f'Getting Error - {e}')
