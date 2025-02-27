# Pesquisa de Estimação de Ocupação em Ambientes Prediais

Este repositório contém os códigos desenvolvidos para a pesquisa de estimação de ocupação em ambientes prediais utilizando técnicas de aprendizado de máquina e Few-Shot Learning, com base em dados CSI (Channel State Information).

## Estrutura do Repositório

- **AquisicoesDados/**
  - **M1/M2/S:** Códigos para aquisição de dados utilizando ESP32. Os scripts realizam a coleta das informações de estado do canal (CSI) nos modos Master (M1/M2) e Slave (S).

- **cleanCSI/**
  - **cleanCSI():** Algoritmos responsáveis por corrigir a sequência dos sensores, tratando erros e inconsistências nos dados coletados para melhorar a qualidade do treinamento.

- **showCSI/**
  - **showCSI():** Ferramenta para visualizar os resultados do CSI, permitindo a análise visual dos padrões de ocupação e comportamento do ambiente.

- **FewShot/**
  - **FewShot():** Implementação do modelo de aprendizado Few-Shot com CNN para estimar a ocupação a partir de poucas amostras, validando o modelo em diferentes ambientes.

## Como Executar os Códigos

1. **Aquisição de Dados:**
   - Configure o ESP32 com os códigos de M1/M2/S.
   - Envie os dados coletados para o ambiente de processamento.

2. **Correção dos Dados:**
   - Use a função `cleanCSI()` para organizar e limpar os dados brutos.

3. **Visualização:**
   - Execute `showCSI()` para analisar os dados graficamente.

4. **Treinamento e Validação:**
   - Rode a função `FewShot()` para treinar e validar o modelo com as amostras coletadas.

## Requisitos

- Python 3.x
- Bibliotecas: NumPy, Matplotlib, TensorFlow/PyTorch
- Ambiente ESP32 configurado

---
Este projeto faz parte de uma pesquisa voltada para a eficiência energética e automação predial, utilizando aprendizado de máquina para estimar padrões de ocupação com base na variação do sinal CSI.

