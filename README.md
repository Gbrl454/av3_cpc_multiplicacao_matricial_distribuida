# Projeto: Multiplicação de Matrizes com Paralelismo e Computação Distribuída

Este projeto implementa e analisa diferentes abordagens de multiplicação de matrizes utilizando **concorrência**, **paralelismo** e **programação distribuída**. O objetivo é demonstrar ganhos de desempenho ao dividir o trabalho entre múltiplos servidores, explorando tanto arquiteturas paralelas quanto distribuídas.

## Objetivos do Projeto

- Implementar um sistema cliente-servidor para multiplicação distribuída de matrizes.
- Aplicar os princípios de concorrência, paralelismo e computação distribuída.
- Utilizar a **Metodologia de Foster** para guiar a decomposição e organização do problema.
- Medir e comparar tempos de execução em diferentes cenários.
- Avaliar o impacto do número de servidores na performance do sistema.

## Conceitos Fundamentais

### Concorrência

Habilidade de lidar com múltiplas tarefas que progridem de forma independente.

### Paralelismo

Execução simultânea de tarefas em múltiplos núcleos ou processadores, reduzindo o tempo total.

### Computação Distribuída

Divisão do processamento entre várias máquinas conectadas em rede, permitindo maior escalabilidade e tolerância a falhas.

### Metodologia de Foster

Abordagem amplamente utilizada para projetar algoritmos paralelos, composta por quatro etapas:
1. **Decomposição**
2. **Comunicação**
3. **Aglomeração**
4. **Mapeamento**

## Testes Realizados

Foram executados testes utilizando matrizes **N × N**, onde:

- **N variou de 10 a 300**, em incrementos de 10;
- **O número de servidores C variou de 2 a 10**, sendo testado dividualmente.

Os testes revelaram:
- A importância de um bom balanceamento de carga.
- O ponto ótimo entre granularidade da decomposição e custo de comunicação.
- O impacto direto do overhead de rede conforme C aumenta.

## Resultados

Os gráficos gerados demonstram:

- Redução significativa no tempo total de execução com o aumento de servidores.
- Efeito de saturação: após certo ponto, adicionar mais servidores não traz ganhos proporcionais.
- Dependência direta entre granularidade da divisão e latência da rede.

## Tecnologias Utilizadas

- Python (ou linguagem utilizada)
- Sockets para comunicação cliente-servidor
- Threads / multiprocessing

## Como Executar

1.  Inicie os servidores:

```python
  python client.py 5000
  python client.py 5001
  python client.py 5002
  ...
  python client.py 5NNN
```

2.  Execute o cliente especificando o número de servidores:

```python
  python client.py
```

3.  Verifique os logs em `/results`.
