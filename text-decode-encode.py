#!/usr/bin/env python3

import os
import string
import time
import random
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

def clear_screen():
    """Очистка экрана терминала"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_background(width, height):
    """Отображение фона с белыми точками"""
    for _ in range(height):
        print(''.join(Fore.WHITE + '.' if random.random() > 0.9 else ' ' for _ in range(width)))

def print_colored_text():
    """Отображение большого текста 'TDE' с синим цветом на фоне белых точек"""
    clear_screen()

    # Получаем размер терминала
    width, height = os.get_terminal_size()

    # Отображаем фон с белыми точками
    print_background(width, height)

    # Перемещение курсора обратно к началу для текста
    os.system('tput cup 0 0')  # Для UNIX-подобных систем, может потребоваться другой метод для Windows

    text_art = '''
mmmmmmm mmmm   mmmmmm
   #    #   "m #     
   #    #    # #mmmmm
   #    #    # #     
   #    #mmm"  #mmmmm
    '''

    # Показ текста с эффектом "появления" и синим цветом
    for line in text_art.split('\n'):
        for char in line:
            print(Fore.BLUE + Style.BRIGHT + char, end='', flush=True)
            time.sleep(0.01)  # Задержка для эффекта "появления"
        print()  # Перенос строки
        time.sleep(0.2)  # Задержка между строками

def generate_mixed_alphabet(key):
    """Создание перемешанного алфавита на основе ключа"""
    alphabet = string.ascii_uppercase
    key = ''.join(sorted(set(key.upper()), key=lambda k: key.upper().index(k)))  # Удаление дубликатов и сохранение порядка
    key = key + ''.join(sorted(set(alphabet) - set(key)))  # Добавление оставшихся букв
    return key

def encrypt(text, key):
    """Шифрование текста с использованием перемешанного алфавита, сохранение регистра"""
    alphabet = string.ascii_uppercase
    mixed_alphabet = generate_mixed_alphabet(key)
    translation_table_upper = str.maketrans(alphabet, mixed_alphabet)
    translation_table_lower = str.maketrans(alphabet.lower(), mixed_alphabet.lower())
    
    encrypted_text = text.translate(translation_table_upper)
    encrypted_text = encrypted_text.translate(translation_table_lower)
    
    return encrypted_text

def decrypt(text, key):
    """Расшифрование текста с использованием перемешанного алфавита, сохранение регистра"""
    alphabet = string.ascii_uppercase
    mixed_alphabet = generate_mixed_alphabet(key)
    translation_table_upper = str.maketrans(mixed_alphabet, alphabet)
    translation_table_lower = str.maketrans(mixed_alphabet.lower(), alphabet.lower())
    
    decrypted_text = text.translate(translation_table_upper)
    decrypted_text = decrypted_text.translate(translation_table_lower)
    
    return decrypted_text

def main():
    print_colored_text()  # Показываем текст с эффектами

    while True:
        print(Fore.BLUE + "Choose an action:")
        print("1: Decrypt text")
        print("2: Encrypt text")
        print("0: Exit")
        choice = input("Enter 1, 2, or 0: ")

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice not in ('1', '2'):
            print(Fore.RED + "Invalid choice. Please enter 1, 2, or 0.")
            continue

        key = input(Fore.BLUE + "Enter the key: ")
        text = input(Fore.BLUE + "Enter the text: ")

        if choice == '1':
            print(Fore.GREEN + "Decrypted text:", decrypt(text, key))
        elif choice == '2':
            print(Fore.GREEN + "Encrypted text:", encrypt(text, key))

if __name__ == "__main__":
    main()
