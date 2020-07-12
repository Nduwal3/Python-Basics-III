from setuptools import setup

setup(
    name = 'academy-cli',
    version = '0.1.0',
    package = ['academy'],
    entry_points = {
        'console_scripts':[
            'academy = academy.__main__:main'
        ]
    }
)