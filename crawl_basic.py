from bs4 import BeautifulSoup
import requests
import re


def get_basic():
    html = requests.get('https://dacon.io', headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(html.text, 'html.parser')

    titles = html.select("span.text-subtitle-1")

    for i in range(0, len(titles)):
        titles[i] = titles[i].text
        titles[i] = re.sub('\s|\t|\r|\n|\.|//|\{|\}|', '', titles[i])

    types = html.select("span.text-caption")

    for i in range(0, len(types)):
        types[i] = types[i].text
        types[i] = re.sub('\s|\t|\r|\n|\.|//|\{|\}|', '', types[i])

    progress = html.select("div.v-progress-linear.mt-5")

    for i in range(0, len(progress)):
        progress[i] = progress[i].attrs['aria-valuenow']

    persons = html.select("div.d-flex.flex-row.justify-space-between.text-caption.grey--text")

    for i in range(0, len(persons)):
        persons[i] = persons[i].text.split('명')[0]
        persons[i] = re.sub('\s|\t|\r|\n|\.|//|\{|\}|', '', persons[i])

    left = html.select("div.d-flex.flex-row.justify-space-between.text-caption.grey--text")

    for i in range(0, len(left)):
        left[i] = left[i].text.split('명')[1]
        left[i] = re.sub('\s|\t|\r|\n|\.|//|\{|\}|', '', left[i])
        if int(persons[i].replace(',', '')) > 0:
            left[i] = '종료 ' + left[i]
        else:
            left[i] = '시작 ' + left[i]

    return {'title': titles, 'type': types, "progress": progress, "person" : persons, "left": left}
