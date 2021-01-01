from bs4 import BeautifulSoup
import io

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import datetime
from tenacity import retry
from tenacity import *

class FBbot2():
    def __init__(self, url = "https://facebook.com",):

        self.name_link_list=pd.DataFrame(columns=['Name','add','num'])
        print(self.name_link_list)
        x=pd.read_csv('List.csv',dtype=str)[['Name','add','num']]
        print(x)
        self.name_link_list=pd.concat([self.name_link_list,x], ignore_index=True)
        print(self.name_link_list)

        self.sleeptime = 1
        self.url = url

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-notifications")  # disable notifications
        self.options.add_argument("--user-data-dir=C:\\Users\\n2\\AppData\\Local\\Google\\Chrome\\Selenium user data2\\")  # disable notifications
        self.options.add_argument('profile-directory=Profile 1')
        self.options.add_argument("--disable-extensions")

    def open_driver(self,):
        self.driver = webdriver.Chrome(r'C:\Users\n2\devs\cli\chromedriver.exe',
                                        options=self.options,)

    def close_driver(self,):
        self.driver.close()

    def goto_url(self, url):
        self.driver.get(url)

    def get_name_message(self,):
        self.goto_url(self.url)
        time.sleep(self.sleeptime)

        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        mess = soup.find_all('div',{'class':'cxgpxx05 sj5x9vvc'})[3]
        #print(mess)
        #mess2 = mess.find('ul',{'class':'pedkr2u6'})
        mess3 = mess.find_all('a', {'class':'oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi'})
        #for link in mess.find_all('a', {'class':'oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 a8c37x1j mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi'}):
        for link in mess3:

            add=link.get('href').split('/')[3]
            name=link.find('span',{'class':'d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m'}).get_text()
            #print(type(add))
            if len(self.name_link_list[self.name_link_list['add'] == add]) == 0 :

                self.goto_url(self.url+link.get('href'))
                time.sleep(self.sleeptime)

                num = self.sub_num()
                print(num)
                x=pd.DataFrame(columns=['Name','add','num'])
                x=x.append({
                    'Name':name,
                    'add':add,
                    'num':num
                },ignore_index=True)
                x.to_csv('List.csv', mode='a', header=False, index=False)

                self.name_link_list=self.name_link_list.append({
                    'Name':name,
                    'add':add,
                    'num':num
                },ignore_index=True)

                print(name,add,"T")
            print(name,add,"F")
        print(self.name_link_list)

        pass


    @retry(wait=wait_fixed(2))
    def sub_num(self):
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        fd = soup.find('div',{'aria-label':'Messages'})
        num = len(fd.find_all('div'))
        return num

    def send_message(self,add):
        self.goto_url(self.url+'/messages/t/'+add)
        time.sleep(self.sleeptime)
        self.sub_send_message()


    @retry(wait=wait_fixed(1))
    def sub_send_message(self,):
        text_btn = self.driver.find_element_by_xpath("//div[@class='notranslate _5rpu']")
        text_btn.click()
        actions = ActionChains(self.driver).send_keys('สวัสดีปีใหม่ 2021 นะครับ~ ขอให้มีสุขภาพที่แข็งแรง มีความสุขกับหน้าที่การงาน มีเวลาเหลือเฟื้อกับทุกสิ่งที่รัก (≧◡≦)'+Keys.ENTER)
        actions.perform()


    def Happy_New_Year_2021(self):
        for _,row in self.name_link_list[self.name_link_list.apply(lambda x:int(x['num'])>100,axis=1)].iterrows():
            self.send_message(row['add'])
