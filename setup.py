from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="jr-trapezoid",
    version="0.0.1",
    author="Jørgen Riseth",
    email="jnriseth@gmail.com",
    description="Python package for 1D numerical integration by trapezoid method.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorgenriseth/jr-trapezoid",
    include_package_data=True,
    packages=find_packages(exclude=[]),
    install_requires=["numpy"],
)
