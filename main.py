'''
Password Checker
-------------------------------------------------------------
'''
import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

print("Требования к паролю: минимум 8 символов, латинские буквы (верхний и нижний регистр), цифры, минимум 1 спецсимвол")


def check_pwd():
    n=0
    while True:
        pwd = input("Введите пароль для проверки: ")
        if len(pwd) < 8:
            print("Пароль слишком короткий!")
        if not (any(char in digits for char in pwd)):
            print("Пароль не может состоять только из букв!")
        if not (any(char in letters for char in pwd)):
            print("Пароль не может состоять только из цифр!")
        if not (any(char in letters[26:] for char in pwd)):
            print("В пароле хотя бы одна буква должна быть в верхнем регистре!")  
        if not (any(char in special_chars for char in pwd)):
            print("В пароле отсутствует спецсимвол!")
            print("-----------------------------------------------")
            n+=1
        else:
            print(f"Пароль соответствует требованиям. Ваш пароль: {pwd}")
            print("-----------------------------------------------")
            break


if __name__ == '__main__':
   check_pwd()
