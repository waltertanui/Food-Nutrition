import csv
import os
import time
import random
import django
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pydjango.settings')
django.setup()
from myApp.models import Foodinfo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class spider(object):
    def __init__(self, start_page):
        self.start_page = start_page
        self.init()  #初始化CSV文件


    def startBrower(self):
        service=Service('./chromedriver.exe')
        # 设置随机请求头
        options = Options()
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
        ]
        options.add_argument(f'user-agent={random.choice(user_agents)}')
        options.add_experimental_option('excludeSwitches',['enable-automation']) #关闭“Chrome 正受到自动测试软件的控制” 的提示
        brower=webdriver.Chrome(service=service,options=options)
        return brower


    def main(self, page_count):  #爬取多少页
        browser = self.startBrower()
        i = 0
        for page in range(self.start_page, self.start_page + page_count):

            spider_url = f'https://nlc.chinanutri.cn/fq/foodinfo/{page}.html'
            print(f"正在爬取页面路径: {spider_url}")
            browser.get(spider_url)
            # 随机化请求间隔
            time.sleep(random.uniform(2, 5))  # 模拟页面加载时间，避免因爬取速度过快而触发网站的反爬机制。

            #食物名称
            Name= browser.find_element(by=By.XPATH, value='//div[@class="food_introduce_top"]/h1').text
            #食物类型
            Type=browser.find_element(by=By.XPATH, value='//div[@class="food_details_navbox"]/h3').text
            #食物成分
            Edible=browser.find_element(by=By.XPATH, value='//td[text()="食部(Edible)"]/following-sibling::td').text
            Water=browser.find_element(by=By.XPATH, value='//td[text()="水分(Water)"]/following-sibling::td').text
            Energy=browser.find_element(by=By.XPATH, value='//td[text()="能量(Energy)"]/following-sibling::td').text
            Protein=browser.find_element(by=By.XPATH, value='//td[text()="蛋白质(Protein)"]/following-sibling::td').text
            Fat=browser.find_element(by=By.XPATH, value='//td[text()="脂肪(Fat)"]/following-sibling::td').text
            Cholesterol=browser.find_element(by=By.XPATH, value='//td[text()="胆固醇(Cholesterol)"]/following-sibling::td').text
            Ash=browser.find_element(by=By.XPATH, value='//td[text()="灰分(Ash)"]/following-sibling::td').text
            CHO=browser.find_element(by=By.XPATH, value='//td[text()="碳水化合物(CHO)"]/following-sibling::td').text
            DietaryFiber=browser.find_element(by=By.XPATH, value='//td[text()="总膳食纤维(Dietary fiber)"]/following-sibling::td').text
            Carotene=browser.find_element(by=By.XPATH, value='//td[text()="胡萝卜素(Carotene)"]/following-sibling::td').text
            Vitamin=browser.find_element(by=By.XPATH, value='//td[text()="维生素A(Vitamin)"]/following-sibling::td').text
            α_TE=browser.find_element(by=By.XPATH, value='//td[text()="α-TE"]/following-sibling::td').text
            Thiamin=browser.find_element(by=By.XPATH, value='//td[text()="硫胺素(Thiamin)"]/following-sibling::td').text
            Riboflavin = browser.find_element(by=By.XPATH,value='//td[text()="核黄素(Riboflavin)"]/following-sibling::td').text
            Niacin = browser.find_element(by=By.XPATH, value='//td[text()="烟酸(Niacin)"]/following-sibling::td').text
            VitaminC = browser.find_element(by=By.XPATH,value='//td[text()="维生素C(Vitamin C)"]/following-sibling::td').text
            Ca = browser.find_element(by=By.XPATH, value='//td[text()="钙(Ca)"]/following-sibling::td').text
            P = browser.find_element(by=By.XPATH, value='//td[text()="磷(P)"]/following-sibling::td').text
            K = browser.find_element(by=By.XPATH, value='//td[text()="钾(K)"]/following-sibling::td').text
            Na = browser.find_element(by=By.XPATH, value='//td[text()="钠(Na)"]/following-sibling::td').text
            Mg = browser.find_element(by=By.XPATH, value='//td[text()="镁(Mg)"]/following-sibling::td').text
            Fe = browser.find_element(by=By.XPATH, value='//td[text()="铁(Fe)"]/following-sibling::td').text
            Zn = browser.find_element(by=By.XPATH, value='//td[text()="锌(Zn)"]/following-sibling::td').text
            Se = browser.find_element(by=By.XPATH, value='//td[text()="硒(Se)"]/following-sibling::td').text
            Cu = browser.find_element(by=By.XPATH, value='//td[text()="铜(Cu)"]/following-sibling::td').text
            Mn = browser.find_element(by=By.XPATH, value='//td[text()="锰(Mn)"]/following-sibling::td').text
            I = browser.find_element(by=By.XPATH, value='//td[text()="碘(I)"]/following-sibling::td').text
            SFA = browser.find_element(by=By.XPATH, value='//td[text()="饱和脂肪酸(SFA)"]/following-sibling::td').text
            MUFA = browser.find_element(by=By.XPATH, value='//td[text()="单不饱和脂肪酸(MUFA)"]/following-sibling::td').text
            PUFA = browser.find_element(by=By.XPATH, value='//td[text()="多不饱和脂肪酸(PUFA)"]/following-sibling::td').text
            TotalFattyAcids = browser.find_element(by=By.XPATH, value='//td[text()="合计(Total)"]/following-sibling::td').text
            i=i+1
            print(f'第{i}条数据爬取完成')

            # 调用保存数据的方法
            self.save_to_csv([Name, Type, Edible, Water, Energy, Protein, Fat, Cholesterol, Ash,
                              CHO, DietaryFiber, Carotene, Vitamin, α_TE, Thiamin, Riboflavin, Niacin, VitaminC,
                              Ca, P, K, Na, Mg, Fe, Zn, Se, Cu, Mn, I, SFA, MUFA, PUFA, TotalFattyAcids])
        browser.quit()

    def clear_csv(self):  # 清洗数据
        df = pd.read_csv('./temp.csv')
        df.drop_duplicates(inplace=True)  # 删除重复行
        # 识别数值列
        numerical_columns = df.select_dtypes(include='number').columns
        rows_to_drop = set()

        for col in numerical_columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            if not outliers.empty:
                print(f"列 {col} 中存在异常值，索引为：{outliers.index.values}")
                rows_to_drop.update(outliers.index)
            else:
                print(f"列 {col} 中未发现异常值。")

        # 删除包含异常值的行
        df = df.drop(rows_to_drop)
        print("总数据量为%d"%df.shape[0])

        return df.values

    def save_to_sql(self): #存储到mysql
       data=self.clear_csv()
       for food in data:
           Foodinfo.objects.create(
               Name=food[0],
               Type=food[1],
               Edible=food[2],
               Water=food[3],
               Energy=food[4],
               Protein=food[5],
               Fat=food[6],
               Cholesterol=food[7],
               Ash=food[8],
               CHO=food[9],
               DietaryFiber=food[10],
               Carotene=food[11],
               Vitamin=food[12],
               α_TE=food[13],
               Thiamin=food[14],
               Riboflavin=food[15],
               Niacin=food[16],
               VitaminC=food[17],
               Ca=food[18],
               P=food[19],
               K=food[20],
               Na=food[21],
               Mg=food[22],
               Fe=food[23],
               Zn=food[24],
               Se=food[25],
               Cu=food[26],
               Mn=food[27],
               I=food[28],
               SFA=food[29],
               MUFA=food[30],
               PUFA=food[31],
               TotalFattyAcids=food[32]
           )



    def save_to_csv(self, data):  # 存储数据
        with open('./temp.csv', 'a', newline='', encoding='utf8') as wf:
            writer = csv.writer(wf)
            writer.writerow(data)


    def init(self):
        if not os.path.exists('/temp.csv'):
            with open('./temp.csv','a',newline='',encoding='utf8')as wf:
                writer=csv.writer(wf)
                writer.writerow([ "Name","Type","Edible", "Water", "Energy", "Protein", "Fat", "Cholesterol", "Ash",
                                 "CHO", "DietaryFiber", "Carotene", "Vitamin","α_TE","Thiamin", "Riboflavin","Niacin", "VitaminC",
                                  "Ca", "P", "K", "Na", "Mg", "Fe", "Zn","Se","Cu","Mn","I","SFA","MUFA","PUFA","TotalFattyAcids"])




if __name__=="__main__":
    spiderObj=spider(259) #从第259页开始爬
   # spiderObj.main(1356)  #1356
    spiderObj.save_to_sql()






