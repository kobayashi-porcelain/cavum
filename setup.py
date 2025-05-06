from setuptools import setup, find_packages

setup(
    name="cavum",
    version="0.1.0",
    description="Linux memory forensics framework for embedded and industrial systems",
    author="Kobayashi Porcelain",
    author_email="sinsinackrst@gmail.com",
    url="https://github.com/kobayashi-porcelain/cavum",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.3.5",
        "construct>=2.10.67",
    ],
    entry_points={
        "console_scripts": [
            "cavum = cavum.cli.main:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Security",
    ],
    python_requires='>=3.7',
)

