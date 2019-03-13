try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Defrecord Machine Learning',
    'author': 'Jason Walsh',
    'url': 'http://wal.sh/research/2019-machine-learning.html',
    'download_url': 'http://wal.sh/research/2019-machine-learning.html',
    'author_email': 'j@wal.sh',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['defrecord-ml'],
    'scripts': [],
    'name': 'defrecord-ml'
}

setup(**config)
