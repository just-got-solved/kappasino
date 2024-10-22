from django.shortcuts import render
from .utils import generate_reels, check_winner

def slot_machine_view(request):
    if request.method == 'POST':
        # Obter o valor da aposta
        bet = int(request.POST.get('bet', 10))  # Valor padrão de 10 créditos
        
        # Gerar as bobinas
        reels = generate_reels()
        
        # Verificar se houve vitória
        is_winner = check_winner(reels)
        
        # Calcular os ganhos ou perdas
        if is_winner:
            winnings = bet * 2  # Dobrar o valor da aposta como recompensa
        else:
            winnings = 0
        
        return render(request, 'slot_machine/slot.html', {
            'reels': reels,
            'is_winner': is_winner,
            'bet': bet,
            'winnings': winnings
        })
    
    # Exibir a página inicial com a slot vazia na primeira carga
    return render(request, 'slot_machine/slot.html', {'reels': None})
