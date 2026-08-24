import json
from urllib import error, parse, request

from news_analyzer.config import BASE_URL
from news_analyzer.exception import APIKeyError


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
        return f"NewApi {query} con timeout {timeout}"
    except error.HTTPError as e:
        raise APIKeyError(f"Error en la clave de API: {e.code} - {e.reason}")


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
