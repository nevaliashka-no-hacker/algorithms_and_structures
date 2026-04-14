'''
Вход:  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Выход: 6

Визуально:
              █
      █ ░ ░ ░ █ █ ░ █
  █ ░ █ █ ░ █ █ █ █ █ █
───────────────────────
0 1 0 2 1 0 1 3 2 1 2 1

█ - столбец ("земля")
░ - вода
'''

def trap_rain_water(columns):
    if not columns:
        return 0

    n = len(columns)
    stack = []
    matrix = [[] * n] * max(columns)

    for i in range(n - 1, -1, -1):
        for j in range(max(columns)):
            if columns

    #return matrix

    for i in range(n):
        stack.append(columns[i])
        

def main():
    columns = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_rain_water(columns))

if __name__ == "__main__":
    main()
