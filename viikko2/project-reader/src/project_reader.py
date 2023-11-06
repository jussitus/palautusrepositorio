from urllib import request
from project import Project
from tomlkit import parse


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content = parse(content)
        tool_poetry = content["tool"]["poetry"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            tool_poetry["name"],
            tool_poetry["description"],
            tool_poetry["authors"],
            tool_poetry["license"],
            list(tool_poetry["dependencies"].keys()),
            list(tool_poetry["group"]["dev"]["dependencies"].keys()),
        )
