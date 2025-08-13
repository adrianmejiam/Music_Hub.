import os

# Configuración general y constantes
QOBUZ_TOKEN = os.environ.get('QOBUZ_TOKEN', "3Uw0hztyRKeZgbLSlvnKZ3zZIDg4U-K6QRPk02P6bGmrQSs48CWgCkxvMPa00CmIegDGjpfM5vyhstklcqufPg")

# Token de Genius API - usar variable de entorno o fallback
GENIUS_TOKEN = os.environ.get('GENIUS_TOKEN', "bOb0AM7TteQJ9J2t1JjQtHfSw2qlhp_U5oyFRenLmshiQw0jgrowXLyurdbda6Rt")

# Flask settings
FLASK_DEBUG = os.environ.get('FLASK_ENV') == 'development'
PORT = int(os.environ.get('PORT', 5000))

__all__ = ["QOBUZ_TOKEN", "GENIUS_TOKEN", "FLASK_DEBUG", "PORT"]
