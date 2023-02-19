import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="controlnet_hinter",
    version="0.0.1",
    author="takuma104",
    author_email="takuma104@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takuma104/controlnet_hinter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)