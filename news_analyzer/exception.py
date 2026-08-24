class NewsSystemError(Exception):
    """Error en el sistema de noticias"""


class APIKeyError(NewsSystemError):
    """Error en la clave de API"""
