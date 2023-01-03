import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="faker_mobile_bank_clickstream",
    version="0.0.1",
    description="Mobile Banking Clickstream Faker Provider for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manganganath/faker-mobile-bank-clickstream",
    project_urls={
        "Issues Tracker": "https://github.com/manganganath/faker-mobile-bank-clickstream/issues",
    },
    install_requires=['Faker'],
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=["faker_mobile_bank_clickstream"],
    python_requires=">=3.6",
    license='Apache License, Version 2.0',
)
