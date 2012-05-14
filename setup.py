from distutils.core import setup

setup(
    name='django-taobao',
    version='0.1.0',
    author='Jichao Ouyang',
    author_email='oyanglulu@gmail.com',
    packages=['taobao','taobao.templates','taobao.taobaoapi2'],
    url='https://github.com/geogeo/django-taobao',
    license='LICENSE.txt',
    description='Taobao saler tools for django.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.3.1",
        "django-social-auth",
    ],
)

