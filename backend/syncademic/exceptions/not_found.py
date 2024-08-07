class ObjectNotFound(Exception):
    """ Excepción genérica para objeto no encontrado de cualquier tipo de Modelo
        Creado por Alejandra Colcha
    """
    def __init__(self, model_name, detail="No existe el objeto solicitado."):
        self.model_name = model_name
        self.detail = detail
        super().__init__(self.detail)
