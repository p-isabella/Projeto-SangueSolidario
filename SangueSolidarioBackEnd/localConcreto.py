from localAbstrato import LocalAbstrato
import copy

class LocalAbstrato():
    def __init__(self):
        pass

    def copia_base(self,local):
        local = LocalAbstrato()
        self = copy.deepcopy(local)
        return self
    