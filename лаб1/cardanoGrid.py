import random

def createGrid(size: int):
    if size % 2 != 0:
        size += 1
    
    grid = [['■' for _ in range(size)] for _ in range(size)]
    
    holes_per_quarter = (size * size) // 16
    quarter_size = size // 2
    
    positions = []
    attempts = 0
    
    while len(positions) < holes_per_quarter and attempts < 1000:
        i = random.randint(0, quarter_size - 1)
        j = random.randint(0, quarter_size - 1)
        
        if (i, j) not in positions:
            positions.append((i, j))
        
        attempts += 1
    
    for i, j in positions:
        grid[i][j] = '◯'
        grid[j][size-1-i] = '◯'
        grid[size-1-i][size-1-j] = '◯'
        grid[size-1-j][i] = '◯'
    
    return grid

def saveGrid2File(grid):
    size = len(grid)
    
    result = f"Решетка Кардано {size}×{size}\n"

    with open("./results/cardanoGrid/result.txt", 'w', encoding='utf-8') as file:
        file.write(f"Решетка Кардано {size}×{size}\n")
        file.write("+" + "-" * (size * 2) + "+\n")
        result += "+" + "-" * (size * 2) + "+\n"

        for row in grid:
            file.write("| " + " ".join(row) + " |\n")
            result += "| " + " ".join(row) + " |\n"
        
        file.write("+" + "-" * (size * 2) + "+\n")
        result += "+" + "-" * (size * 2) + "+\n"

        hole_count = sum(row.count('◯') for row in grid)

        file.write(f"\nОтверстий: {hole_count} из {size*size}\n")
        result += f"\nОтверстий: {hole_count} из {size*size}\n"

    return result


def showWork(gridSize):
    print(saveGrid2File(createGrid(gridSize)))