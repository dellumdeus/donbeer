import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="donbeer",
    version="1.0.5",
    author="dellumdeus",
    author_email="alion.develop@gmail.com",
    description="The user is able to click on a beer until a donut appears.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pygame'],
    url="https://github.com/dellumdeus/donbeer",
    packages=setuptools.find_packages(),
    package_dir={'donbeer': 'donbeer'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # include_package_data=True,
    package_data={
        "donbeer": ["assets/images/*.png"],
    },
    data_files=[('assets/images', ['./donbeer/assets/images/beer2.png'])]
)
