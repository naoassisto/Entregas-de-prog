from setuptools import setup, find_packages

setup(
    name='Pacote_Ingestao_de_Dados',
    version='0.1',
    packages=find_packages(),  # Automatically find your modules
    install_requires=[
        'requests',
        'boto3',
        'pytest',
        'moto'
    ],
)
