import requests
import datetime
import time


# https://api.stackexchange.com/2.3/questions?page=1&pagesize=100&fromdate=1684108800&todate=1684281600&order=desc&sort=activity&tagged=python&site=stackoverflow

def news_stackoverflow_last_days(days,tag):
    '''
    :param days: Принимает целое число, используется для просмотра новостей за заданное количество дней
    :return: Возвращает статьи в формате JSON
    '''
    current_date = datetime.datetime.today()
    past_date = current_date - datetime.timedelta(days=days)
    unixtime_today = int(time.mktime(current_date.timetuple()))
    unixtime_past = int(time.mktime(past_date.timetuple()))
    page = 1
    code = 200
    news_list = []

    while code == 200:
        url = 'https://api.stackexchange.com/2.3/questions'
        # url = f'https://api.stackexchange.com/2.3/questions?page={page}&pagesize=100&fromdate={unixtime_past}&todate={unixtime_today}&order=desc&sort=activity&tagged=Python&site=stackoverflow'
        params = {
            "page": page,
            "pagesize": 100,
            "fromdate": unixtime_past,
            "todate": unixtime_today,
            "order": "desc",
            "sort": "activity",
            "tagged": tag,
            "site": "stackoverflow",
        }
        res = requests.get(url, params)
        if len(res.json()['items']) == 0:
            break
        code = res.status_code
        responce = res.json()
        news_list.extend(responce['items'])
        page += 1

    return news_list


fresh_news = news_stackoverflow_last_days(2, 'python')

for items in fresh_news: # Более красивый вывод, иначе выводит в одну строку
    print(items)


