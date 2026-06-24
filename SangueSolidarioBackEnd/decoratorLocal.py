from localConcreto import LocalConcreto

class decoratorLocal:
    def __init__(self,doador):
        self._doador = doador

    def adicionaLocal(self):
        oLocal = LocalConcreto()
        oLocal._involucro = self._doador
        return oLocal
