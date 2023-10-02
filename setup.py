from setuptools import setup, find_packages

setup(
    name="seclook",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "requests",
        "configparser",
    ],
    entry_points={
        "console_scripts": [
            "seclook=seclook.cli:main",
        ],
    },
    description="Simple security lookups via CLI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ackatz/seclook",
)
