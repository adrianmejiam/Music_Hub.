import os

# Configuración general y constantes
QOBUZ_TOKEN = os.environ.get('QOBUZ_TOKEN', "-6MoVR8hli5CDAhNuEaMmAC1MYyYV9OTpi3uU4Nv39BMYNsGlCAcDQAJsKVyKqDvyc8IOGR2YxM4_4hfHNsy9w")

# Token de Genius API - usar variable de entorno o fallback
GENIUS_TOKEN = os.environ.get('GENIUS_TOKEN', "bOb0AM7TteQJ9J2t1JjQtHfSw2qlhp_U5oyFRenLmshiQw0jgrowXLyurdbda6Rt")

# Flask settings
FLASK_DEBUG = os.environ.get('FLASK_ENV') == 'development'
PORT = int(os.environ.get('PORT', 5000))

__all__ = ["QOBUZ_TOKEN", "GENIUS_TOKEN", "FLASK_DEBUG", "PORT"]
