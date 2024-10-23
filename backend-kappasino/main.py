from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from typing import List, Dict, Any

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definindo símbolos e pagamentos para combinações vencedoras
symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "🔔", "🍇", "🍀", "7️⃣"]  # Adicionado o símbolo 7️⃣
payouts = {
    "🍒": 10,  # Três cerejas pagam 10x
    "🍋": 5,   # Três limões pagam 5x
    "🍊": 3,   # Três laranjas pagam 3x
    "⭐": 20,   # Três estrelas pagam 20x
    "7️⃣": 50,  # Três setes pagam 50x
}

# RTP desejado (Retorno ao jogador)
RTP = 0.90

def generate_spin_result() -> List[List[str]]:
    """Gera uma matriz 3x3 de símbolos aleatórios."""
    return [[random.choice(symbols) for _ in range(3)] for _ in range(3)]

def calculate_winnings(result: List[List[str]]) -> (int, str):
    """Calcula os ganhos com base nas combinações vencedoras e retorna os ganhos e o símbolo vencedor."""
    winnings = 0
    winning_symbol = None
    
    # Verificar linhas
    for row in result:
        if row[0] == row[1] == row[2]:  # Verifica linhas iguais
            winning_symbol = row[0]
            winnings += payouts.get(winning_symbol, 0)

    # Verificar colunas
    for col in range(3):
        if result[0][col] == result[1][col] == result[2][col]:  # Verifica colunas iguais
            winning_symbol = result[0][col]
            winnings += payouts.get(winning_symbol, 0)

    # Verificar diagonais
    if result[0][0] == result[1][1] == result[2][2]:  # Diagonal principal
        winning_symbol = result[0][0]
        winnings += payouts.get(winning_symbol, 0)
    if result[0][2] == result[1][1] == result[2][0]:  # Diagonal secundária
        winning_symbol = result[0][2]
        winnings += payouts.get(winning_symbol, 0)

    return winnings, winning_symbol

def adjust_winnings(winnings: int) -> int:
    """Ajusta os ganhos com base no RTP e no edge da casa."""
    if winnings > 0:
        house_edge = 1 - RTP
        adjusted_winnings = int(winnings * RTP)

        # Simula a lógica do cassino reter parte dos ganhos
        if random.random() < house_edge:
            winnings = adjusted_winnings
    return winnings

@app.get("/spin")
def spin() -> Dict[str, Any]:
    """Rota para girar a máquina e retornar o resultado."""
    result = generate_spin_result()
    winnings, winning_symbol = calculate_winnings(result)
    winnings = adjust_winnings(winnings)
    
    # Mensagem de vitória
    message = ""
    # Mensagem de vitória
    if winnings > 0 and winning_symbol:
        if winnings <= 10:
            message = f"🍭 Você ganhou! Total de ganhos: {winnings}! Que tal tentar novamente para um prêmio maior? 🍀"
        elif winnings <= 30:
            message = f"🎉 Parabéns! Você ganhou! Total de ganhos: {winnings}! Continue assim, a sorte está ao seu lado! 🌟"
        elif winnings <= 50:
            message = f"✨ Incrível! Você ganhou! Total de ganhos: {winnings}! Está na hora de celebrar essa vitória! 🎈"
        else:  # Ganhos acima de 50
            message = f"💰 Jackpot! Você fez uma grande jogada! Total de ganhos: {winnings}! É hora de festejar! 🎊"

    return {
        "result": result,
        "winnings": winnings,
        "message": message
    }
