from setuptools import setup, find_packages

setup(
    name="seclook",
    version="0.1.0",
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
)
