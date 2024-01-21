
import fibonacci
#First class AI
# user ='shree'
# password = 1234

# i_user = input('Entrt user name: ')
# i_password = int(input('Enter user password: '))

# if user != i_user and password == i_password:
#     print('name not matched')
# elif user == i_user and password != i_password:
#     print('password not matched')
# elif user == i_user and password == password:
#     print('success')
# else:
#     print('invalid')

# ..............................





#self practice

#Range
# for i in range(3):
#     print(i)
# .....


# #array
# a = [2, 3, 4, 5, 6]
# print(a[3])
# print(a[:3])



# for i in range(5):
#     print(i)



#break and continue statement
# for n in range (2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#             print(n, 'is a prime number.')





# for n in range(2, 10):
#     if n % 2 == 0:
#         print('the number', n, 'even number')
#         continue
#     else:
#         print('the number', n, 'odd number')


#pass statement



# class Student:
#class banauna khojya aayena
#     def __init__(self):
#         self.name = ''
#         self.roll = 0
#         self.add()

#     def add(self):
#         self.name = input('Enter your name: ')
#         self.roll = int(input('Enter your roll no:'))
#         print(self.name)
#         print(self.roll)
        
# #match statement
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"


# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"






#Functions

#Fibonacci series
# a = 0
# b = 1
# n = 20

# while a < n:
#     print (a, end = ', ')
#     a = b
#     b = a + b



#finding fibonacci series using functions
# def fib(n):
  
#     a = 0
#     b = 1

#     while a < n:
#         print(a, end= ', ')
#         a = b
#         b = a + b
#     print()class TodoList:
    def __init__(self):
        self.todos = []

    def show_todos(self):
        if not self.todos:
            print("Todos not found")
        else:
            print("Todo list:")
        for index, task in enumerate(self.todos, start=1):
            print(f"{index}. {task}")

    def add_todo(self):
        add_task = input("Enter the todo task:")
        self.todos.append(add_task)
        print(f"Task {add_task} added successfully")

    def remove_todo(self):
        self.show_todos()
        if not self.todos:
            return
        try:
            index = int(input("Enter the number of index you want to delete:"))
            if 1 <= index <= len(self.todos):
                removed_task = self.todos.pop(index - 1)
                print(f"Task {removed_task} removed from todo list")
            else:
                print("Invalid task number")

        except ValueError:
            print("Invalid input. Please input a number")

    def main_menu(self):
        while True:
            print("To-do list menu")
            print("1. Show todo task")
            print("2. Add todo task")
            print("3. Remove todo task")
            print("4. Quit")

            choice = input("Enter your choice:")

            if choice == '1':
                self.show_todos()
            elif choice == '2':
                self.add_todo()
            elif choice == '3':
                self.remove_todo()
            elif choice == '4':
                print("Exiting terminal,")
                break
            else:
                print("Invalid input")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.main_menu()
