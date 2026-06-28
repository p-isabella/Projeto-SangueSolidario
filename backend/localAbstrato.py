class LocalAbstrato:
    def __init__(self,doador,cep,estado,municipio,bairro,rua,numero):
        self._involucro = doador
        self._cep = cep
        self._estado = estado
        self._municipio = municipio
        self._bairro = bairro
        self._rua = rua
        self._numero = numero

    def puxa_involucro(self):
        return self._involucro

    def puxa_cep(self):
        return self._cep

    def puxa_estado(self):
        return self._estado
    
    def puxa_municipio(self):
        return self._municipio
    
    def puxa_bairro(self):
        return self._bairro

    def puxa_rua(self):
        return self._rua
    
    def puxa_numero(self):
        return self._numero
    
