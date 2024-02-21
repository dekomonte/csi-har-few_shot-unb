Primeira aplicação no WIN10 - hello_world

* Abrir atalho de terminal (já configurado com ambiente)
* Conectar o ESP e descobrir em qual porta ele está
* Ir até o diretório do projeto
* Instruções no terminal:<br>
```idf.py set-target esp32 fullclean```<br>
```idf.py menuconfig```<br>
```idf.py build```<br>
```idf.py -p PORT flash```<br>
```idf.py -p PORT monitor```<br>
