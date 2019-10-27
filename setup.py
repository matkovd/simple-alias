from setuptools import setup

setup(
    name='create_alias',
    version='0.1',
    py_modules=['create_alias'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        create_alias=create_alias:create_alias
    ''',
)
