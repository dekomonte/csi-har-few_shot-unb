# csi-har-unb
Códigos Trabalho de Graduação

Códigos do professor Adolfo com algumas pequenas alterações pra rodar os programas na minha máquina (Linux-Ubuntu).

#### Instruções
1. Abrir primeiro terminal -> Ir para o diretório CSI261M1 -> No terminal: source start
2. Abrir segundo terminal -> Ir para o diretório CSI261M2 -> No terminal: source start 
3. Abrir terceito terminal -> Ir para o diretório CSI261S -> No terminal: source start (sensores)

#### Lembretes
* Editor de texto no terminal = pico
* /dev/ttyUSB* -> Descobrir em qual USB o módulo está conectado
* ESP-IDF 4.4.3 e Python 3.9.12

* -----------#-----------#-----------#-----------#-----------#-----------#-----------#-----------#-----------#-----------#
## Atualizações
Mudamos para o Windows.
ESP-IDF 5.0
Diretório do Boyang Li

#### Intruções (Atualizadas)
1. Abrir atalho de terminal "ESP-IDF 5.0 CMD" ou "ESP-IDF 5.0 POWERSHELL" presentes na Área de Trabalho
2. Ir para o diretório csi261M1
   -> idf.py build
   -> idf.py -p [PORT] flash monitor (só monitor se os módulos já estiverem gravados)
3. Ir para o diretório csi261M2
   -> idf.py build
   -> idf.py -p [PORT] flash monitor (só monitor se os módulos já estiverem gravados)
4. Ir para o diretório csi261S
   -> idf.py build
   -> idf.py -p [PORT] flash monitor (só monitor se os módulos já estiverem gravados)
