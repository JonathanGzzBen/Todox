from setuptools import setup, find_packages

setup(
    name='Todox',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Tabulate'
    ],
    entry_points= {
        "console_scripts": [
            "todox = todox.todox:main"
        ]
    },
)