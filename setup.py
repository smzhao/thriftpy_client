from setuptools import setup, find_packages
setup(
    name = 'thriftpy_client',
    version = '0.1',
    keywords='thriftpy_client',
    description = 'a library for thriftpy client',
    license = 'MIT License',
    url = 'https://github.com/smzhao/thriftpy_client',
    author = 'zhaowenpeng',
    author_email = 'binpocn@163.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['thriftpy'],
)
