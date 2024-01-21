import random
import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_character = string.punctuation
selection_list = letters + digits + special_character

password_length = 10

password = ''
for i in range(password_length):
    password +=''.join(secrets.choice(selection_list))
print(password)