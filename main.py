class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tugilganman")

talaba1 = Talaba("Javohir", "Hayitboyev", 2011)
talaba2 = Talaba("Abbosbek", "Axmedov", 2002)
talaba3 = Talaba("Olim" "Olimov", 1995)
talaba4 = Talaba("Husan" "Akbarov", 2004)

talaba3.tanishtir()
talaba1.tanishtir()