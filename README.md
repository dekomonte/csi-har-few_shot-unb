# CNN Few-Shot para Aprendizado Flexível em Ambientes Prediais

Este repositório contém os códigos utilizados no meu Trabalho de Conclusão de Curso, cujo objetivo era estimação de atividades em ambientes prediais utilizando técnicas de aprendizado de máquina e Few-Shot Learning, com base em dados CSI (Channel State Information).

## Estrutura do Repositório

- **Aquisições Dados - CSI_UnB**
  - **M1/M2/S:** Códigos main em C para aquisição de dados utilizando ESP32.

- **Limpeza - Clean_CSI**
  - **blank_lines.py** Programa que tira linhas em branco do arquivo CSV adquirido pela aquisição.
  - **cleanCSI_UnB241.ipynb:** Algoritmos responsáveis por corrigir a sequência dos sensores.

<!-- - **showCSI**
  - **showCSI():** Ferramenta para visualizar os resultados do CSI, permitindo a análise visual dos padrões de ocupação e comportamento do ambiente. -->

- **Few_Shot_Learning**
  - **fewShot_UnB_logTests.ipynb:** Implementação do modelo de aprendizado Few-Shot com CNN para estimar a ocupação a partir de poucas amostras, validando o modelo em diferentes ambientes. Resultados e matrizes de confusão do melhor modelo. 
  - **fewShot_UnB.ipynb:** Implementação do modelo de aprendizado Few-Shot com CNN para estimar a ocupação a partir de poucas amostras, validando o modelo em diferentes ambientes. Resulta no melhor modelo e quais parâmetros foram utilizados. 

---
Este projeto faz parte de uma pesquisa voltada para a eficiência energética e automação predial, utilizando aprendizado de máquina para estimar padrões de ocupação com base na variação do sinal CSI.

