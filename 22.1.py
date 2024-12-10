print("Задание", 22.1)
class Restaraunt():
 def __init__(self, restaraunt_name, cuisine_type):
    self.restaraunt_name = restaraunt_name
    self.cuisine_type = cuisine_type

 def describe_restaraunt(self):
     print(f"Ресторан:{self.restaraunt_name}")
     print(f"Тип кухни:{self.cuisine_type}")

 def open_restaraunt(self):
     print(f"{self.restaraunt_name} ОТКРЫТ")
rst = Restaraunt("У АШОТА", "ГРУЗИНСКАЯ")
rst.describe_restaraunt()
rst.open_restaraunt()

class IceCreamStand(Restaraunt):
   def __init__(self, restaraunt_name, cuisine_type):
    super().__init__(restaraunt_name, cuisine_type)
    self.flavors = ['канопляное', 'с анашой', 'гашишное']

   def flavors_type(self):
    print(f"в продаже есть следующие виды мороженого")
    for ice_cream in self.flavors:
       print(f"{ice_cream}")

rst = IceCreamStand("У ПАШОТА", "Наркоманская")
rst.describe_restaraunt()
rst.open_restaraunt()
rst.flavors_type()

print("Задание", 22.2)
class User():
   def __init__(self, first_name, last_name, data, country):
      self.first_name = first_name
      self.last_name = last_name
      self.data = data
      self.country = country
    
   def describe_user(self):
      print(f"Имя: {self.first_name}")
      print(f"Фамилия: {self.last_name}")
      print(f"Дата рождения: {self.data}")
      print(f"Страна: {self.country}")
   
   def greet_user(self):
      print(f"{self.first_name} {self.last_name} ДОБРО ПОЖАЛОВАТЬ В БОЙЦОВСКИЙ КЛУБ")
rst1 = User("Денис", "Шариков", "21.03.2001", "Россия")
rst1.describe_user()
rst1.greet_user()
rst2 = User("Иван", "Филинов", "19.05.2008", "Россия")
rst2.describe_user()
rst2.greet_user()

class Admin(User):
   def __init__(self, first_name, last_name, data, country):
      super().__init__(first_name, last_name, data, country)
      self.privileges = ['Разрешено добавлять сообщения', 'разрещено удалять пользователя', 'разрешено банить пользователей']
      
   def show_privileges(self):
      print(f"У вас есть следующие возможности:")
      for priv in self.privileges:
         print(f" {priv}")

rst1 = Admin("Админ", "Админов", "21.08.1999", "Россия")
rst1.greet_user()
rst1.describe_user()
rst1.show_privileges()

print("Задание", 22.3)
class User():
   def __init__(self, first_name, last_name, data, country):
      self.first_name = first_name
      self.last_name = last_name
      self.data = data
      self.country = country
    
   def describe_user(self):
      print(f"Имя: {self.first_name}")
      print(f"Фамилия: {self.last_name}")
      print(f"Дата рождения: {self.data}")
      print(f"Страна: {self.country}")
   
   def greet_user(self):
      print(f"{self.first_name} {self.last_name} ДОБРО ПОЖАЛОВАТЬ В БОЙЦОВСКИЙ КЛУБ")
rst1 = User("Денис", "Шариков", "21.03.2001", "Россия")
rst1.describe_user()
rst1.greet_user()
rst2 = User("Иван", "Филинов", "19.05.2008", "Россия")
rst2.describe_user()
rst2.greet_user()



rst1 = Admin("Админ", "Админов", "21.08.1999", "Россия")
rst1.greet_user()
rst1.describe_user()
rst1.show_privileges()

class Privilegies(Admin):
   def __init__(self, first_name, last_name, data, country):
      super().__init__(first_name, last_name, data, country)
      self.privileges = ['Разрешено добавлять сообщения', 'разрещено удалять пользователя', 'разрешено банить пользователей']
      
   def show_privileges(self):
      return super().show_privileges()

user = Privilegies("Александр", "Миняйло", "20.07.2006", "Россия")
user1 = Privilegies("Светлана", "Крупина", "20.09.2003", "Россия")
user.show_privileges()

class Admin(User, Privilegies):
   def __init__(self, first_name, last_name, data, country):
      super().__init__(first_name, last_name, data, country)
      self.privileges = Privilegies
      
   def show_privileges(self):
      print(f"У вас есть следующие возможности:")
      for privelegii in self.privileges:
         print(f" {privelegii}")