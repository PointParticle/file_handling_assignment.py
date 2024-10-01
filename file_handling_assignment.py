with open('my_file.txt', 'w') as file:
    file.write('name = input("What is your name: ")\n')
    file.write('age = input("How old are you: ")\n')
    file.write('gender = input("What is your gender: ")\n')
    file.write('print(name, "I want you to know that you are", age, "years old this year.")\n')
