import nox
from shlex import split
from os.path import realpath

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "venv"

@nox.session
def start(session):
    for i in ["requirements.txt"]:
        session.run("pip", "install", "-U", "-r", i, silent=True)
    session.run(*"myst start".split(), *session.posargs)

@nox.session
def test(session):
    for i in ["requirements.txt"]:
        session.run("pip", "install", "-U", "-r", i, silent=True)
    session.run("python", "src/blogpost.py") 
