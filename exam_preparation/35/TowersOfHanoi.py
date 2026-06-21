'''Ханойская башня'''
'''Перекладываем башенку с A на B'''

def recursive(n, start, final, temp):
    if n == 1:
        print(f"Перекладываем с {start} на {final}")
        return
        
    recursive(n - 1, start, temp, final)    
    print(f"Перекладываем с {start} на {final}")
    recursive(n - 1, temp, final, start)
    
recursive(3, "A", "C", "B")    