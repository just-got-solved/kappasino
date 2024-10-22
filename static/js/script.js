document.getElementById('spin-btn').addEventListener('click', function() {
    const reels = document.querySelectorAll('.reel-inner');
    const symbolHeight = 120;  // Altura de cada símbolo
    const totalSymbols = reels[0].children.length;

    reels.forEach((reel, index) => {
        // Inicia a rotação contínua
        let position = 0;
        const spinTime = 2000;  // Tempo para rotação completa em milissegundos
        let endTime = Date.now() + spinTime;  // Tempo de fim para a rotação

        // Função de animação
        function spin() {
            let currentTime = Date.now();
            if (currentTime >= endTime) {
                // Finaliza a rotação
                let finalPosition = Math.floor(Math.random() * totalSymbols) * symbolHeight;
                reel.style.transition = 'transform 1s ease-out';
                reel.style.transform = `translateY(${-finalPosition}px)`;
                return;
            }
            // Continua a rotação
            position += (symbolHeight / 10);  // Incrementa a posição para a animação
            if (position >= (symbolHeight * totalSymbols)) {
                position = 0;  // Reseta a posição após uma volta completa
            }
            reel.style.transform = `translateY(${-position}px)`;
            requestAnimationFrame(spin);
        }

        // Começa a rotação imediatamente
        requestAnimationFrame(spin);

        // Parar a rotação após o tempo definido
        setTimeout(() => {
            let finalPosition = Math.floor(Math.random() * totalSymbols) * symbolHeight;
            reel.style.transition = 'transform 1s ease-out';
            reel.style.transform = `translateY(${-finalPosition}px)`;
        }, spinTime + index * 500);  // Garante que as colunas parem em sequência
    });
});
