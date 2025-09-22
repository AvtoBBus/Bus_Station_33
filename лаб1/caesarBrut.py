from collections import Counter

def encrypt(text, key):
    russian_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    n = len(russian_letters)
    key = key % n  # Нормализуем ключ
    
    encrypted_text = []
    
    for char in text:
        if char in russian_letters:
            old_index = russian_letters.index(char)
            new_index = (old_index + key) % n
            encrypted_text.append(russian_letters[new_index])
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

def decrypt(text, key):
    russian_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    n = len(russian_letters)
    key = key % n  # Нормализуем ключ
    
    decrypted_text = []
    
    for char in text:
        if char in russian_letters:
            old_index = russian_letters.index(char)
            new_index = (old_index - key) % n
            decrypted_text.append(russian_letters[new_index])
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

def bruteForce(encrypted_text):
    letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    common_letters = ['О', 'Е', 'А', 'И', 'Н', 'Т', 'С', 'Р', 'В', 'Л']
    
    n = len(letters)
    results = []
    for key in range(n):
        decrypted = decrypt(encrypted_text, key)
        
        score = 0
        letter_count = Counter(decrypted)
        total_letters = sum(letter_count.values())
        
        if total_letters > 0:
            for common_letter in common_letters[:5]:
                if common_letter in letter_count:
                    frequency = letter_count[common_letter] / total_letters
                    score += frequency
        
        results.append({
            'key': key,
            'text': decrypted,
            'score': score
        })
    
    results.sort(key=lambda x: x['score'], reverse=True)
    
    return results

def frequencyAnalysis(text,):
    expected_freq = {
        'О': 0.1097, 'Е': 0.0845, 'А': 0.0801, 'И': 0.0735, 'Н': 0.0670,
        'Т': 0.0626, 'С': 0.0547, 'Р': 0.0473, 'В': 0.0454, 'Л': 0.0440
    }
    
    letter_count = Counter(text)
    total_letters = sum(letter_count.values())
    
    if total_letters == 0:
        return 0
    
    score = 0
    for letter, expected_frequency in expected_freq.items():
        if letter in letter_count:
            actual_frequency = letter_count[letter] / total_letters
            score += min(actual_frequency, expected_frequency)
    
    return score


def showWork(text4encrypt: str, key: int):
    enc = encrypt(text4encrypt, key)

    with open("./results/caesarBrut/encrypted.txt", 'w', encoding='utf-8') as file:
        file.write(enc)

    with open("./results/caesarBrut/decrypted.txt", 'w', encoding='utf-8') as file:
        file.write(decrypt(enc, key))