from klllaa import *

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