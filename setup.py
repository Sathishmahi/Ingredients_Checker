import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

print(long_description)
__version__ = "0.0.0"

REPO_NAME = "Ingredients_Checker"
AUTHOR_USER_NAME = "Sathishmahi"
SRC_REPO = "Ingredients_Checker"
AUTHOR_EMAIL = "sathishmahi433@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="this is a ingredients checker app",
    # long_description=long_description,
    # long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
