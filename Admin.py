class User:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
class Privileges:
    def __init__(self):
        self.privileges = [
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей"
        ]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, username, first_name, last_name):
        super().__init__(username, first_name, last_name)
        self.privileges = Privileges()

admin = Admin("admin_user", "Dimon", "Novgorodov")
admin.privileges.show_privileges()