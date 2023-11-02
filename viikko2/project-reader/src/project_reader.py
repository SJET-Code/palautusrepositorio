from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = tomli.loads(content)
        deserialiasoitu = toml_dict['tool']['poetry']
        dependencies = []
        dev_dep = []
        authors = []
        for key in deserialiasoitu['dependencies']:
            dependencies.append(key)
        for key in deserialiasoitu['group']['dev']['dependencies']:
            dev_dep.append(key)
        for key in deserialiasoitu['authors']:
            authors.append(key)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(deserialiasoitu['name'], deserialiasoitu['description'], dependencies, dev_dep, deserialiasoitu['license'], authors)
