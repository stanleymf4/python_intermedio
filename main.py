# main.py - Todo el código en un archivo

"""
Sistemas de analisis de noticias con APIs múltiples
"""

from news_analyzer.config import API_KEY
from news_analyzer.exception import APIKeyError
from news_analyzer.news_api_client import fetch_news
from news_analyzer.utils import (
    get_articles_by_source,
    get_reading_time,
    get_unique_sources,
)

response_data = None
try:
    response_data = fetch_news("newspi", api_key=API_KEY, query="Noticias Python")
except APIKeyError as e:
    print(f"No se pudo obtener las noticias: {e}")

if response_data:
    sources_set = get_unique_sources(response_data["articles"])
    for index, source in enumerate(sources_set, start=1):
        print(f"No. {index} -- {source}")

    articles = list(map(get_reading_time, response_data["articles"]))
    for article in articles:
        print(f"{article['title']} -- Tiempo de lectura_ {article['reading_time']}")

    for article in response_data.get("articles", []):
        print(article["title"])

    github_articles = get_articles_by_source(response_data["articles"], "TechNews")
    print(github_articles)
