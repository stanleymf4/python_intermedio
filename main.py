# main.py - Todo el código en un archivo

"""
Sistemas de analisis de noticias con APIs múltiples
"""

# PEP 8: Configuraciín centralizada - constantes en MAYUSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para string

# PEP 8: Utilidades comunes del proyecto - funciones en snake_case

API_KEY = "baf8c204792f4f32bcbd6bd7985e8ecf"
BASE_URL = "https://newsapi.org/v2/everything"

import json
import urllib.parse
import urllib.request


def clean_text(text):
    # PEP8: 4 espacios por indentación, no tabs
    if not text:
        return ""
    return text.strip().lower()


def validate_api_key(api_key):
    """Valida que la api key tenbga en  formato correcto"""
    return len(api_key) > 10 and api_key.isalnum()


def fetch_news_from_api(api_name, query):
    pass


def process_article_data(raw_date):
    pass


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(*args):
    print(f"Argumentos posicionales: {args}")


""" ejemplo_args("Este", "parametro", "aca") """


def sumar_numeros(*args):
    return sum(args)


def ejemplo_kwargs(**kwargs):
    print(f"kwargs {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("==================================")

def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
        return f"NewApi {query} con timeout {timeout}"
    except urllib.error.HTTPError as e:
        print(f"Error HTTP: {e.code} - {e.reason}")
        return {"articles": []}
    



def fetch_news(api_name, *args, **kwargs):
    """
    Función flexible para conectar con la API
    """
    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {**base_config, **kwargs}

    api_clients = {"newspi": newsapi_client, "guardian": guardian_client}

    client = api_clients.get(api_name)
    return client(*args, **config)


response_date = fetch_news("newspi", api_key=API_KEY, query="Noticias Python")
for article in response_date.get("articles", []):
    title = clean_text(article.get("title"))
    print(f"Título: {title}")
