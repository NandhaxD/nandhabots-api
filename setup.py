from setuptools import setup, find_packages


with open("README.md", encoding="utf8") as readme:
    long_desc = readme.read()
    


# Setting up
setup(
    name="NandhaAPI",
    version='0.1',
    author="Nandha K",
    author_email="nandhaxd@gmail.com",
    description="My python api tool | NandhaAPI",
    long_description_content_type="text/markdown",
    long_description=long_desc,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/nandhaxd/NandhaAPI",
    download_url="https://github.com/nandhaxd/NandhaAPI/blob/main/README.md",
    install_requires=["requests"],
    keywords=['python', "NandhaAPI","NandhaBots", "tgbotapi", "Tgbots"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    
    project_urls={
        "Tracker": "https://github.com/nandhaxd/NandhaAPI/issues",
        "Community": "https://t.me/nandhasupport",
        "Source": "https://github.com/nandhaxd/NandhaAPI",
    },
    python_requires="~=3.7",
)
