sample_articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles):
    """Extrae solo los titulos usuando un for"""
    titles = []
    for article in articles:
        if len(article["title"]) > 20:  # PEP8: Espacios alrededor de operadores
            titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae solo los titulos usando un comprehension"""
    return [
        article["title"] for article in articles if len(article["title"]) > 20
    ]  # PEP8: Espacios alrededor de operadores


def extact_article_summary(articles):
    """Extrae el recumen de un article"""
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 10
    }


def extract_source(articles):
    """Extraer las fuentes de cada articulo"""
    return {article["source"]["name"] for article in articles}


def categorize_traditional(articles):
    """Categorizar articulos"""
    sources = extract_source(articles)
    result = {}
    for source in sources:
        if source not in result:
            result[source] = []
        for article in articles:
            if source == article.get("source").get("name"):
                result[source].append(article)
    return result


def categorize(articles):
    """Categorizar articulos con comprehesion"""
    sources = extract_source(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize_traditional(sample_articles))
print("******************************************")
print(categorize(sample_articles))
