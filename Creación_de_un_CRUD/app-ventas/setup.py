from importlib.metadata import entry_points
from setuptools import setup

setup(
    name = 'pv',
    version = '0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
    ], # punto de entrada de nuestra app
    entry_points=''' 
        [console_scripts]
        pv=pv:cli
    ''',
)