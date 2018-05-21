#!/usr/bin/env python

from setuptools import setup
from subprocess import call


def convert_readme():
    try:
        call(["pandoc", "-f", "markdown_github", "-t",  "rst", "-o",  "README.txt", "README.markdown"])
    except OSError:
        pass
    return open('README.txt').read()

setup(
    name='django-genericadmin',
<<<<<<< HEAD
    version='0.6.4',
    description="Adds support for generic relations within Django's admin interface.",
    author='Weston Nielson, Jan Schrewe',
    author_email='wnielson@gmail.com, jschrewe@googlemail.com',
    url='https://github.com/jschrewe/django-genericadmin',
    packages=['genericadmin'],
    # package_data={'genericadmin': ['static/genericadmin/js/genericadmin.js']},
=======
    version='0.7.0',
    description="Adds support for generic relations within Django's admin interface.",
    author='Weston Nielson, Jan Schrewe, Arthur Hanson',
    author_email='wnielson@gmail.com, jschrewe@googlemail.com, worldnomad@gmail.com',
    url='https://github.com/arthanson/django-genericadmin',
    packages = ['genericadmin'],
#    package_data={'genericadmin': ['static/genericadmin/js/genericadmin.js']},
>>>>>>> b4916ea9421a484e893543bd1cbc6edc1c27fa66
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    long_description=convert_readme(),
    include_package_data=True,
    zip_safe=False,
)
