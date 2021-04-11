# main program
# main.py

import stock_kind as sk
import collect_day.collect_day as cd
import real_time.real_time_price as rt
import naver_crawling.naver_finance_crawling as nfc
import auto.auto_login as at
import multiple_real_time_finding_listmethod as real_time



def start_collect_stock_kind():
    collect_stock_kind = sk.StockKind()
    return collect_stock_kind.start_collect()


def start_collect_day(codes):   # 일자별 데이터 모두 가져오기
    collect_stock_day = cd.DayCollect()
    collect_stock_day.start_get_days_data(codes)


def start_collect_day_update(codes):   # 일자별 데이터 업데이트하기
    collect_stock_day = cd.DayCollect()
    collect_stock_day.start_update_days_data(codes)


def start_real_time_it_service(naver_upjong_name=None): # 실시간 - 정상작동하지 않음
    crawling = nfc.NaverFinanceCrawler()
    for upjong in naver_upjong_name:
        upjong_code = crawling.get_stock_code(upjong)
        start_collect_real_time(upjong_code)


def start_collect_real_time(code=None):     # 실시간 - 정상작동하지 않음
    collect_real_time = rt.RealTimeCollect()
    collect_real_time.start_collect_real_time_data(code)


def start_get_real_time():
    real_time.start()


def start_program():
    auto_login = at.AutoLogin()
    while not auto_login.login():
        pass

    codes = start_collect_stock_kind()
    # start_collect_day_update(codes) # 모든 종목 일별 데이터 갱신
    start_get_real_time()

# IT서비스, 해운사, 조선, 광고, 건설

start_program()


# start_collect_day(codes)  # 모든 종목 일별 데이터 수집(전체)
# start_collect_day_update(codes) # 모든 종목 일별 데이터 갱신
# start_real_time_it_service(('IT서비스', '해운사', '조선', '광고', '건설'))
