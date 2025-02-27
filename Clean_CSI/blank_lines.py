import pandas as pd
import os

def remover_linhas_em_branco(caminho_arquivo):
    # Carrega o arquivo CSV
    df = pd.read_csv(caminho_arquivo)

    # Procura a palavra "CSI_DATA" e remove a linha anterior a ela
    linhas_removidas = 0
    for index, row in df.iterrows():
        if 'CSI_DATA' in row.values:
            indice_remover = index - 1
            if indice_remover >= 0:
                df = df.drop(indice_remover)
                linhas_removidas +=1

    # Obtém o nome do arquivo original e seu diretório
    nome_arquivo = os.path.basename(caminho_arquivo)
    diretorio = os.path.dirname(caminho_arquivo)

    # Salva o arquivo com o novo nome
    nome_original, extensao = os.path.splitext(nome_arquivo)
    novo_nome_arquivo = f"c{nome_original}{extensao}"
    novo_caminho_arquivo = os.path.join(diretorio, novo_nome_arquivo)
    df.to_csv(novo_caminho_arquivo, index=False)

    print(f"As linhas em branco antes de 'CSI_DATA' foram removidas. O novo arquivo foi salvo como {novo_caminho_arquivo}.")
    print(f"Número de linhas removidas: {linhas_removidas}")

# Substitua 'caminho_para_arquivo.csv' pelo caminho do seu arquivo CSV


remover_linhas_em_branco('06022025//Eu_rot1_06022025.csv')
remover_linhas_em_branco('06022025//Eu_rot2_06022025.csv')
remover_linhas_em_branco('06022025//Eu_rot3_06022025.csv')
remover_linhas_em_branco('06022025//Eu_rot4_06022025.csv')
remover_linhas_em_branco('06022025//Eu_rot5_06022025.csv')
remover_linhas_em_branco('06022025//Eu_rot6_06022025.csv')
# remover_linhas_em_branco('06022025//Eu_rot7_06022025.csv')
# remover_linhas_em_branco('06022025//Eu_rot8_06022025.csv')
# remover_linhas_em_branco('06022025//Eu_rot9_06022025.csv')
# remover_linhas_em_branco('06022025//Eu_rot10_06022025.csv')
