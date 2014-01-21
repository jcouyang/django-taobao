from distutils.core import setup

setup(
    name='django-taobao',
    version='0.2.3',
    author='Jichao Ouyang',
    author_email='oyanglulu@gmail.com',
    packages=['taobao','taobao.templates'],
    url='https://github.com/jcouyang/django-taobao',
    license='MIT',
    keywords='django, taobao, oauth, api',
    description='Taobao SDK for django.',
    long_description=open('README.rst').read(),
)

