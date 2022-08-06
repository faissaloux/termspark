from setuptools import setup

setup(
    name='termspark',
    version='0.0.4',
    author='Faissal Wahabali',
    author_email='fwahabali@gmail.com',
    description='Takes control of terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='terminal, cmd, design',
    python_requires='>=3.7',
    url='https://github.com/faissaloux/termspark',
    py_modules=["termspark"],
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)