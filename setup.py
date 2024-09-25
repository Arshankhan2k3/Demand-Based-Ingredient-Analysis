from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    author="Arshan Khan",
    author_email="arshankhan7619@gmail.com",
    packages=find_packages(),
    install_requires=[],
     entry_points={
        'console_scripts': [
            'Burger Buddy = app:main',  
        ],
    },
)
