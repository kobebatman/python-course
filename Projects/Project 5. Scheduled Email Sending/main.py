import datetime
import schedule
import time
import email_sender
import web_scraper

def get_top_10():
    data = web_scraper.do_web_scraping()
    sorted_data = sorted(data, key=lambda item: item['points'])
    return sorted_data[-10:]

def send_top_10(top_infos):
    email_sender.send_email(top_infos)

def job():
    top_news = get_top_10()
    print(f'[{datetime.datetime.now()}] got top news stories')

    send_top_10(top_news)
    print(f'[{datetime.datetime.now()}] sent email')


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)