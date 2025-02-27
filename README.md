# Pesquisa de Estimação de Ocupação em Ambientes Prediais

Este repositório contém os códigos desenvolvidos para a pesquisa de estimação de ocupação em ambientes prediais utilizando técnicas de aprendizado de máquina e Few-Shot Learning, com base em dados CSI (Channel State Information).

## Estrutura do Repositório

- **Aquisições Dados**
  - **M1/M2/S:** Códigos para aquisição de dados utilizando ESP32.

- **cleanCSI**
  - **cleanCSI():** Algoritmos responsáveis por corrigir a sequência dos sensores, tratando erros e inconsistências nos dados coletados para melhorar a qualidade do treinamento.

- **showCSI**
  - **showCSI():** Ferramenta para visualizar os resultados do CSI, permitindo a análise visual dos padrões de ocupação e comportamento do ambiente.

- **Few-Shot Learning**
  - **FewShot():** Implementação do modelo de aprendizado Few-Shot com CNN para estimar a ocupação a partir de poucas amostras, validando o modelo em diferentes ambientes.

---
Este projeto faz parte de uma pesquisa voltada para a eficiência energética e automação predial, utilizando aprendizado de máquina para estimar padrões de ocupação com base na variação do sinal CSI.

