from local import Local

class decoratorLocal:
    def __init__(self,doador):
        self._doador = doador

    def adicionaLocal(self):
        oLocal = Local()
        oLocal._involucro = self._doador
        return oLocal