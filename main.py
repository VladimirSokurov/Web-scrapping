import requests
import bs4

URL_MAIN = 'https://habr.com'
URL = "https://habr.com/ru/all/"
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'твиттер', 'хабр']
HEADERS = {'Accept': '*/*', 'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36',
           'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}

response = requests.get(URL, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all(class_="tm-articles-list__item")

capitalized_list = [word.capitalize() for word in KEYWORDS]
for i in capitalized_list:
    if i not in KEYWORDS:
        KEYWORDS.append(i)

for id, article in enumerate(articles):
    article_date = article.find(class_='tm-article-snippet__datetime-published').text
    article_title = article.find(class_='tm-article-snippet__title-link').text
    article_link = article.find(class_='tm-article-snippet__title-link').attrs['href']
    article_description = article.find(class_='tm-article-body tm-article-snippet__lead').text
    for keyword in KEYWORDS:
        if keyword in article_description:
            print(f'Дата: {article_date}; заголовок: "{article_title}"; ссылка: {URL_MAIN}{article_link}')
            break
