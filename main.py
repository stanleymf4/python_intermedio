# main.py - Todo el código en un archivo

"""
Sistemas de analisis de noticias con APIs múltiples
"""

# PEP 8: Configuraciín centralizada - constantes en MAYUSCULAS con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para string

# PEP 8: Utilidades comunes del proyecto - funciones en snake_case


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


def newsapi_client(api_key, query, timeout=30, retries=3):
    return f"NewApi {query} con timeout {timeout}"


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(*args):
    print(f"Argumentos posicionales: {args}")


ejemplo_args("Este", "parametro", "aca")


def sumar_numeros(*args):
    return sum(args)


print(sumar_numeros(1, 2, 3, 4, 5))
