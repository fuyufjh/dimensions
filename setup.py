from distutils.core import setup


with open('README.txt') as f:
    readme = f.read()

setup(
    name='dimensions',
    version='0.0.2',
    author='Phil Adams',
    author_email='phil@philadams.net',
    url='https://github.com/philadams/dimensions',
    license='LICENSE.txt',
    description='Python lib to read width and height of image files',
    long_description=readme,
    packages=['dimensions'],
    scripts=['bin/dimensions'],
)
