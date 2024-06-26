from setuptools import setup

setup(
    name='open_metal_detector',
    version='2024.01.29',
    packages=['omsdetector'],
    install_requires=["pandas>=1.3.5",
                      "matplotlib>=2.1.2",
                      "numpy>=1.21.6",
                      "pymatgen>=2023.2.28"],
    url='',
    license='MIT',
    author='Emmanuel Haldoupis',
    author_email='emmhald@gmail.com',
    description='A tool to detect open metal sites in collections of MOFs.',
    python_requires='>=3.9'
)
