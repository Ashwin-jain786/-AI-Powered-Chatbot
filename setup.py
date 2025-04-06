from setuptools import setup, find_packages

setup(
    name="ai_chatbot_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "jinja2",
        "markupsafe==2.0.1",
        "nltk",
        "transformers"
    ],
)
