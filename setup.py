from setuptools import setup, find_packages

setup(
    name='table-data-process-lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'xgboost',
        'sklearn',
        'imblearn'
    ],
    description='Library for table data processing',
    author='Pavel Malyshev',
    author_email='p.malyshev@razumai.pro',
    url='https://github.com/PavelMalyshev01/table-data-process-lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
