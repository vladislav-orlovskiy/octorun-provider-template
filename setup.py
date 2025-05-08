from setuptools import find_packages, setup

# Get version from file VERSION
with open("VERSION") as version_file:
    version = version_file.read().strip()

setup(
    name="octorun-provider",
    version=version,
    author="Uladzislau Orlovskiy",
    author_email="painanguishagony@gmail.com",
    description="python based provider for octorun controller",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
