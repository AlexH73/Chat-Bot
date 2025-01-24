import os

def clear_screen():
    """
      Очищает экран в терминале
    """
    os.system('cls' if os.name == 'nt' else 'clear')