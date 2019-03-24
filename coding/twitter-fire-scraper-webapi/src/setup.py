import setuptools

with open("../README.md", 'r') as f:
    long_description = f.read()

with open("VERSION", 'r') as f:
    version = f.read()

setuptools.setup(
    name="twitter-fire-scraper-webapi",
    version=version,

    author="Henry Post",
    author_email="HenryFBP@gmail.com",

    description="A web API interfact to the twitter-fire-scraper package.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/raaraa/IPRO497-Analytics-Team/tree/master/coding/twitter-fire-scraper-webapi",

    package_data = {
        'twitter-fire-scraper': [
            'data/*.yml',
            'templates/*.html'
        ]
    },

    packages=setuptools.find_packages(),
    install_requires=[
        "twitter-fire-scraper",
        "flask"
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
