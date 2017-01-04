from setuptools import setup

setup(
    name='kews',
    packages=['kews'],
    include_package_data=True,
    install_requires=[
        'flask',
        'mecab-python3',
    ],
)
