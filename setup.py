from setuptools import setup


setup(
    name="demultiplex",
    description="Demultiplex is a command line utility to demultiplex fastq files.",
    version="1.0",
    scripts=["demultiplex.py"],
    author="Sameesh Kher",
    author_email="khersameesh24@gmail.com",
    maintainer="Sameesh Kher",
    maintainer_email="khersameesh24@gmail.com",
    packages=["src"],
    python_requires=">=3.5",
    install_requires=["coverage"],
)
