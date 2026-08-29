#!/bin/bash

echo "🤖 Robô de backup iniciado! Pressione CTRL+C neste terminal para parar."

while true
do
    # 1. Verifica se existem alterações para commitar
    if [[ -n $(git status -s) ]]; then
        echo "📦 Alterações encontradas! Fazendo backup às $(TZ="America/Sao_Paulo" date '+%H:%M:%S')..."
        
        # 2. Adiciona todos os arquivos novos e modificados
        git add .
        
        # 3. Cria o commit com a data e hora atual
        git commit -m "Backup automático: $(TZ="America/Sao_Paulo" date '+%Y-%m-%d %H:%M:%S')"
        
        # 4. Envia para o GitHub (detecta automaticamente a sua branch atual)
        git push origin $(git branch --show-current)
        
        echo "✅ Backup concluído com sucesso!"
    else
        echo "💤 Nenhuma alteração detectada às $(TZ="America/Sao_Paulo" date '+%H:%M:%S'). Aguardando próximo ciclo..."
    fi

    # 5. Espera 900 segundos (15 minutos) antes de rodar de novo
    sleep 900
done