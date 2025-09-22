from cardanoGrid import createGrid

def rotate_grid(grid, angle):
    size = len(grid)
    
    if angle == 0:
        return grid
    elif angle == 90:
        return [[grid[size-1-j][i] for j in range(size)] for i in range(size)]
    elif angle == 180:
        return [[grid[size-1-i][size-1-j] for j in range(size)] for i in range(size)]
    elif angle == 270:
        return [[grid[j][size-1-i] for j in range(size)] for i in range(size)]

def encrypt(grid, text):
    size = len(grid)
    
    text = text.replace(' ', '').upper()
    
    total_cells = size * size
    while len(text) < total_cells:
        text += 'X'
    
    encrypted_matrix = [[' ' for _ in range(size)] for _ in range(size)]
    
    text_index = 0
    
    for angle in [0, 90, 180, 270]:
        rotated_grid = rotate_grid(grid, angle)
        
        for i in range(size):
            for j in range(size):
                if rotated_grid[i][j] == '◯' and text_index < len(text):
                    encrypted_matrix[i][j] = text[text_index]
                    text_index += 1
    
    encrypted_text = ''
    for row in encrypted_matrix:
        encrypted_text += ''.join(row)
    
    return encrypted_text

def decrypt(grid, encrypted_text):
    size = len(grid)
    
    if len(encrypted_text) != size * size:
        raise ValueError(f"Длина зашифрованного текста должна быть {size * size}")
    
    encrypted_matrix = []
    for i in range(0, len(encrypted_text), size):
        row = list(encrypted_text[i:i + size])
        encrypted_matrix.append(row)
    
    decrypted_text = ''
    
    for angle in [0, 90, 180, 270]:
        rotated_grid = rotate_grid(grid, angle)
        
        for i in range(size):
            for j in range(size):
                if rotated_grid[i][j] == '◯':
                    decrypted_text += encrypted_matrix[i][j]
    
    decrypted_text = decrypted_text.rstrip('X')
    
    return decrypted_text

def showWork(text4encode: str, gridSize=8):
    grid = createGrid(gridSize)
    encrypted_text = encrypt(grid, text4encode)

    with open("./results/cardanoGrid/encrypted.txt", 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

    with open("./results/cardanoGrid/decrypted.txt", 'w', encoding='utf-8') as file:
        file.write(decrypt(grid, encrypted_text))