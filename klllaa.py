class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        
    def describe_user(self):
      print(f"Имя: {self.first_name}")
      print(f"Фамилия: {self.last_name}")
      print(f"Дата рождения: {self.age}")
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
    
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()
    
    def show_privileges(self):
        print(f'Администратор может: ')
        for privilege in self.privileges:
            print(f'{privilege}')
            
class Privileges():
    
    def __init__(self,):
        self.privileges = ['Разрешено добавлять сообщения', 'разрещено удалять пользователя', 'разрешено банить пользователей']
        
    def show_privileges(self):
        print(f'У вас есть следующие возможности: ')
        for privilege in self.privileges:
            print(f'{privilege}')

prev = Privileges()
prev.show_privileges()