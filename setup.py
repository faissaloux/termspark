from setuptools import setup, find_packages

setup(
    name='termspark',
    version='0.0.6',
    author='Faissal Wahabali',
    author_email='fwahabali@gmail.com',
    description='Takes control of terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='terminal, cmd, design',
    python_requires='>=3.7',
    url='https://github.com/faissaloux/termspark',
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.5',
    ],
    extras_require={
        'dev': [
            'pytest==7.1.2',
            'pytest-cov==3.0.0',
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)