from selenium import webdriver
import time

class InvestingCrawler:
    def __init__(self):
        self.base_url = 'https://kr.investing.com/'

        self.login_id = '아이디'
        self.login_pw = '비밀번호'

        self.dollar_index_url = 'currencies/us-dollar-index-historical-data'

        self.gold_url = 'commodities/gold-historical-data'
        self.wti_url = 'commodities/crude-oil-historical-data'

        self.nasdaq_url = 'indices/nasdaq-composite-historical-data'
        self.dowjones_url = 'indices/us-spx-500-historical-data'
        self.uro_stocks_url = 'indices/eu-stoxx50-historical-data'
        self.nikkei_url = 'indices/japan-ni225-historical-data'

        self.hangseng_url = 'indices/hang-sen-40-historical-data'

        self.usa_2years_url = 'rates-bonds/us-2-yr-t-note-historical-data'
        self.usa_5years_url = 'rates-bonds/us-5-yr-t-note-historical-data'
        self.usa_10years_url = 'rates-bonds/us-10-yr-t-note-historical-data'
        self.usa_30years_url = 'rates-bonds/us-30-yr-t-bond-historical-data'

        self.download_list = [self.dollar_index_url, self.gold_url, self.wti_url, self.nasdaq_url, self.dowjones_url,
                              self.uro_stocks_url, self.nikkei_url, self.hangseng_url, self.usa_2years_url,
                              self.usa_5years_url, self.usa_10years_url, self.usa_30years_url]

        self.download_xpath = '''//*[@id="column-content"]/div[4]/div/a'''
        self.date_select_xpath = '''//*[@id="widgetFieldDateRange"]'''
        self.start_date_xpath = '''element_select_date'''
        self.date_choice_id = 'datePickerIconWrap'
        self.apply_btn_xpath = '''//*[@id="applyBtn"]'''

    def login(self, driver):
        login_btn = driver.find_element_by_xpath('''//*[@id="userAccount"]/div/a[1]''')
        if login_btn is None:
            login_btn = driver.find_element_by_xpath('''//*[@id="PromoteSignUpPopUp"]/div[2]/div/a''')
        login_btn.click()
        input_id = driver.find_element_by_id('loginFormUser_email')
        input_id.send_keys('dakso0124@gmail.com')

        input_pw = driver.find_element_by_id('loginForm_password')
        input_pw.send_keys('adsa1212')

        btn_login = driver.find_element_by_xpath('''//*[@id="signup"]/a''')
        btn_login.click()


    def start_crawling(self, start_date, end_date):
        driver = webdriver.Chrome('../driver/chromedriver.exe')
        driver.get(self.base_url)

        self.login(driver)
        driver.implicitly_wait(20)

        for download in self.download_list:
            driver.get(self.base_url + download)
            element_select_date = driver.find_element_by_xpath(self.date_select_xpath)
            element_select_date.click()

            element_start_date = driver.find_element_by_xpath('''//*[@id="startDate"]''')
            element_start_date.clear()
            element_start_date.send_keys(start_date)

            element_end_date = driver.find_element_by_xpath('''//*[@id="endDate"]''')
            element_end_date.clear()
            element_end_date.send_keys(end_date)

            element_apply = driver.find_element_by_xpath(self.apply_btn_xpath)
            element_apply.click()

            time.sleep(5)

            btn_download = driver.find_element_by_xpath(self.download_xpath)
            btn_download.click()

            driver.implicitly_wait(5)
        driver.close()

InvestingCrawler().start_crawling('2011/04/01', '2020/12/31')