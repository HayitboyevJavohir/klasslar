# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tugilganman")

# talaba1 = Talaba("Javohir", "Hayitboyev", 2011)
# talaba2 = Talaba("Abbosbek", "Axmedov", 2002)
# talaba3 = Talaba("Olim" "Olimov", 1995)
# talaba4 = Talaba("Husan" "Akbarov", 2004)

# talaba3.tanishtir()
# talaba1.tanishtir()

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil
        
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_fullname()) 

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil
    
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_age(2021))   


# 1-masala

class User:
    def __init__(self,name,username,email):
        self.name = name
        self.uname = username
        self.mail = email
    
    def describe(self):
        print(f"Ism: {self.name}")
        print(f"Username: {self.uname}")
    
    def get_email(self):
          print(f"Email: {self.mail}")



User1 = User("Olim","Olimov","Olimolimov@gmail.com")
User2 = User("Husan","Akbarov","Husanakbarov@gmail.com")
User3 = User("Hasan","Akbarov","Hasanakbarov@gmail.com")


User1.describe()
User1.get_email()

print()

User2.describe()
User2.get_email()

print()

User3.describe()
User3.get_email()

print()
print(User3)