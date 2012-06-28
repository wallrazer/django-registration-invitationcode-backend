#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "django-registration-invitationcode-backend",
    description = "Invitation code backend for Django-Registration",
    author = "Grzegorz Bialy, Steve Ivy",
    author_email = "grzegorz@elcodo.pl, steve@wallrazer.com",
    url = "https://github.com/elcodo/django-registration-invitationcode-backend",
    version = "0.0.1",
    packages = find_packages(),
    zip_safe = False,
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)