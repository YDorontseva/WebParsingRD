from bs4 import BeautifulSoup
import requests
import lxml
import json
import re
def parse_bbc():
    url = 'https://www.bbc.com/sport'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')

    data = []

    links = soup.find_all('a', class_='ssrcss-zmz0hi-PromoLink', href = True)

    news_links = [f"https://www.bbc.com{link['href']}" if link['href'].startswith('/') else link['href']
                  for link in links
                  if not link.find('span', class_='ssrcss-agwl82-LiveContainer')][:5]

    for link in news_links:
        response = requests.get(link)
        content = response.content
        soup = BeautifulSoup(content, 'lxml')
        related_topics = soup.find_all('a', class_='ssrcss-1ef12hb-StyledLink')
        related_topics = [topic.get_text() for topic in related_topics]

        data.append({
        'link': link,
        'related_topics': related_topics
        })

    with open('homework_6.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    parse_bbc()