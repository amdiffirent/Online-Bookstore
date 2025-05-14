
from setuptools import setup, find_packages

setup(
    name="online_bookstore",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0.0",  # Match your requirements.txt
        "requests>=2.26.0",
    ],
    python_requires=">=3.8",
)
