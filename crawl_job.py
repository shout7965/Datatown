import requests
from bs4 import BeautifulSoup
import re

def get_job_list(category):

    # category : 빅데이타 161, 인공지능 162
    htmls = []
    page_to = 2
    for page in range(0, page_to):
        url = "https://www.peoplenjob.com/jobs?type=work&work_code_id=" + str(category) + "&page=" + str(page+1)
        raw = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        htmls.append(BeautifulSoup(raw.text, "html.parser"))

    date_tags = []
    for i in range(0, page_to):
        for j in range(0, len(htmls[i].select('.date'))):
            date_tags.append(htmls[i].select('.date')[j])

    dates = []
    for i in range(0, len(date_tags)):
        dates.append(re.sub('\W', '-', date_tags[i].text))

    title_tags = []
    for i in range(0, page_to):
        for j in range(0, len(htmls[i].select('.job-title'))):
            title_tags.append(htmls[i].select('.job-title')[j])

    titles = []
    for i in range(0, len(title_tags)):
        titles.append(re.sub('\n', '', title_tags[i].select('a')[0].text))

    hrefs = []
    for i in range(0, len(title_tags)):
        hrefs.append(title_tags[i].select('a')[0]['href'])

    job_list = zip(dates, titles, hrefs)

    job_dict_list = []
    for job in job_list:
        job_dict = {
            "date": job[0],
            "title": job[1],
            "href": job[2]
        }

        job_dict_list.append(job_dict)

    return job_dict_list

def get_job_count(category):

    # category : 빅데이타 161, 인공지능 162
    htmls = []
    page_to = 5
    for page in range(0,page_to):
        url = "https://www.peoplenjob.com/jobs?type=work&work_code_id=" + str(category) + "&page=" + str(page+1)
        raw = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        htmls.append(BeautifulSoup(raw.text, "html.parser"))

    date_tags = []
    for i in range(0, page_to):
        for j in range(0, len(htmls[i].select('.date'))):
            date_tags.append(htmls[i].select('.date')[j])

    dates = []
    for i in range(0, len(date_tags)):
        dates.append(re.sub('\W', '-', date_tags[i].text))

    job_count = {}
    for date in dates:
        try:
            job_count[date] += 1
        except:
            job_count[date] = 1

    return job_count
