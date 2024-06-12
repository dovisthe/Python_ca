if __name__ == "__main__":
    import irasas as ir
else:
    from . import irasas as ir


class PajamuIrasas(ir.Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info
        
    def __str__(self):
        return f'Pajamos: {self.suma}, Siuntejas: {self.siuntejas}, Info: {self.papildoma_info}'