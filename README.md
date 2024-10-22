# Projeto: Previsão de Fechamento da B3 com Cadeia de Markov

## Sobre o Projeto
Este projeto utiliza a técnica de Cadeia de Markov para prever o fechamento diário da B3 (Ibovespa), categorizando as variações percentuais diárias em estados e calculando as probabilidades de transição entre eles. O modelo se baseia na variação percentual do fechamento de um dia para prever o estado de fechamento do dia seguinte.

O objetivo principal é demonstrar a aplicação de modelos probabilísticos em séries temporais financeiras, com foco na simplicidade e eficácia da técnica de Markov.

## Funcionalidades Principais
1. **Baixar Dados Históricos**: O projeto utiliza a biblioteca `yfinance` para baixar os dados históricos da B3.
2. **Categorização de Estados**: A variação percentual do fechamento diário é classificada em quatro estados, com base na magnitude da variação.
3. **Criação da Matriz de Transição**: A partir dos dados categorizados, é criada uma matriz de transição de Markov para calcular as probabilidades de mudança entre estados.
4. **Previsão de Próximo Estado**: Com base no estado atual da bolsa, o modelo retorna as probabilidades de fechamento no dia seguinte.
