import setuptools

with open("README.md", "r", encoding="utf-8") as f:
  long_description = f.read()

_version_ = "0.0.0"

REPO_NAME = "Document-Summarizer"
AUTHOR_USER_NAME = "Abhi-08-28"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "abhishekgarje2@gmail.com"




setuptools.setup(
  name = REPO_NAME,
  version = _version_,
  author = AUTHOR_USER_NAME,
  author_email = AUTHOR_EMAIL,
  description = "Document Summarizer using BART",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/Abhi-08-28/Document-Summarizer",
  packages = setuptools.find_packages(),
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)