def readKeys(filename: str):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        key1 = list(map(int, lines[0].strip().split()))
        key2 = list(map(int, lines[1].strip().split()))

        return key1, key2

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return None, None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None, None


def validateKeys(key1: list, key2: list):
    if len(key1) != 18:
        print("Ошибка: ключ первой перестановки должен содержать 18 чисел")
        return False

    if len(key2) != 7:
        print("Ошибка: ключ второй перестановки должен содержать 7 чисел")
        return False

    if sorted(key1) != list(range(1, 19)):
        print("Ошибка: ключ первой перестановки должен быть перестановкой чисел от 1 до 18")
        return False

    if sorted(key2) != list(range(1, 8)):
        print("Ошибка: ключ второй перестановки должен быть перестановкой чисел от 1 до 7")
        return False

    return True


def addPadding2Text(text: str, block_size: int):
    padding_length = block_size - (len(text) % block_size)
    if padding_length == block_size:
        return text
    return text + ' ' * padding_length


def removePadding(text: str):
    return text.rstrip()


def encryptText(text: str, key: list):
    n = len(key)
    text = addPadding2Text(text, n)
    encrypted = []

    for i in range(0, len(text), n):
        block = text[i:i + n]
        permuted_block = [''] * n
        for j in range(n):
            permuted_block[int(key[j]) - 1] = block[j]
        encrypted.append(''.join(permuted_block))

    return str(''.join(encrypted))


def decryptText(text: str, key: list):
    n = len(key)
    decrypted = []

    for i in range(0, len(text), n):
        block = text[i:i+n]
        original_block = [''] * n
        for j in range(n):
            original_block[j] = block[key[j]-1]
        decrypted.append(''.join(original_block))

    result = ''.join(decrypted)
    return removePadding(result)


def complex_encrypt(text, key1, key2):
    intermediate = encryptText(text, key1)
    encrypted = encryptText(intermediate, key2)
    return encrypted


def complex_decrypt(text, key1, key2):
    intermediate = decryptText(text, key2)
    decrypted = decryptText(intermediate, key1)
    return decrypted


def showWork(text4encrypt: str) -> None:
    key1, key2 = readKeys("./keys.txt")

    enc = complex_encrypt(text4encrypt, key1, key2)

    with open("./results/block_permutation/encrypted.txt", "w", encoding="utf-8") as file:
        file.write(enc)

    with open("./results/block_permutation/decrypted.txt", "w", encoding="utf-8") as file:
        file.write(complex_decrypt(enc, key1, key2))
