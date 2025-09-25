from collections import Counter
from operator import itemgetter

def encrypt(text, key):
    russian_letters_up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    russian_letters_low = russian_letters_up.lower()
    n = len(russian_letters_up)
    key = key % n
    
    encrypted_text = []
    
    for char in text:
        if char in russian_letters_up:
            old_index = russian_letters_up.index(char)
            new_index = (old_index + key) % n
            encrypted_text.append(russian_letters_up[new_index])
        elif char in russian_letters_low:
            old_index = russian_letters_low.index(char)
            new_index = (old_index + key) % n
            encrypted_text.append(russian_letters_low[new_index])
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decrypt(text, key):
    russian_letters_up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    russian_letters_low = russian_letters_up.lower()
    n = len(russian_letters_up)
    key = key % n  

    decrypted_text = []
    
    for char in text:
        if char in russian_letters_up:
            old_index = russian_letters_up.index(char)
            new_index = (old_index - key) % n
            decrypted_text.append(russian_letters_up[new_index])
        elif char in russian_letters_low:
            old_index = russian_letters_low.index(char)
            new_index = (old_index - key) % n
            decrypted_text.append(russian_letters_low[new_index])
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

def bruteForce(encrypted_text):
    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    
    n = len(letters)
    results = []
    for key in range(n):
        decrypted = decrypt(encrypted_text, key)
        results.append({
            'key': key,
            'text': decrypted,
        })
    
    return results

def showWork(text4encrypt: str, key: int):

    PATH = "./results/caesarBrut/"

    with open(PATH + "origin.txt", "w", encoding="utf-8") as file:
        file.write(text4encrypt)

    enc = encrypt(text4encrypt, key)

    with open(PATH + "encrypted.txt", 'w', encoding='utf-8') as file:
        file.write(enc)

    with open(PATH + "decrypted.txt", 'w', encoding='utf-8') as file:
        file.write(decrypt(enc, key))

    print("Результаты перебора\n" + "=" * 25)
    for br in sorted(bruteForce(enc), key=itemgetter('key')):
        print(f"Ключ: {br['key']} \nРасшифрованный текст: {br['text'][:101]}\n\n" + "=" * 25)