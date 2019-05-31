from setuptools import setup

setup(
    name = 'es_app',
    version = '0.1.0',
    packages = ['es_app'],
    install_requires=[ 'plumbum', ],
    entry_points = {
        'console_scripts': [
            'es_app = es_app.__main__:MyApp',
        ]
    })