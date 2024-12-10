print("Задание", 1)
with open('learning_python.txt') as file:
    cont = file.read()
print(cont)

print("Задание", 2)
with open('learning_python.txt') as file:
    cont = file.readlines()
for message in cont:
    new_message = message.replace('python', 'C++')
print(new_message)

