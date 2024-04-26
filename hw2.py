"""
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, 
додає всі його символи до двосторонньої черги (deque з модуля collections в Python), 
а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. 
Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
а також бути нечутливою до регістру та пробілів.
"""
from collections import deque

def check_palindrom(text, ):
    """Check text palindrom using deque module"""
    d = deque()
    for char in text.lower().replace(' ',''):
        d.append(char)
    is_palindrom = True
    while is_palindrom and d:
        right = d.pop()
        left = d.popleft() if d else right
        if right != left:
            is_palindrom = False
    return is_palindrom


PALINDROM_1 = 'level'
PALINDROM_2  = 'We panic in a pew'
NOT_PALINDROM = 'notplindromon'

print(f"Word: '{PALINDROM_1}' is palindrom {check_palindrom(PALINDROM_1)}")
print(f"Word: '{PALINDROM_2}' is palindrom {check_palindrom(PALINDROM_2)}")
print(f"Word: '{NOT_PALINDROM}' is palindrom {check_palindrom(NOT_PALINDROM)}")
