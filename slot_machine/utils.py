import random

import random

SYMBOLS = ['🍒', '🔔', '🍋', '💎', '🍉', '⭐', '7️⃣', '🎰']

def generate_reels():
    reels = []
    
    # Gerar três bobinas independentes
    for _ in range(3):
        # Criar uma bobina com uma sequência de símbolos que se repete
        reel = random.sample(SYMBOLS, len(SYMBOLS)) * 3  # Simulando várias voltas
        reels.append(reel)
    
    return reels


def check_winner(reels):
    """
    Check for winning combinations in rows, columns, and diagonals.
    Returns True if there's a winning combination, False otherwise.
    """
    # Check rows
    for row in range(3):
        if reels[0][row] == reels[1][row] == reels[2][row]:
            return True

    # Check columns
    for col in reels:
        if col[0] == col[1] == col[2]:
            return True

    # Check diagonals
    if (reels[0][0] == reels[1][1] == reels[2][2]) or (reels[0][2] == reels[1][1] == reels[2][0]):
        return True

    return False
