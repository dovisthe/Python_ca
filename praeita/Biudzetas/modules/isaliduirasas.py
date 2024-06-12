if __name__ == "__main__":
    import irasas as ir
else:
    from . import irasas as ir


class IslaiduIrasas(ir.Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        
    def __str__(self):
        return f'Islaidos: {self.suma}, Atsiskaitymo budas: {self.atsiskaitymo_budas}, Preke/Paslauga: {self.isigyta_preke_paslauga}'