"""
Programa hello
Descrição: imprima na tela a frase "hello, world!".
Autor: Augusto Jacques
Data: 25/02/2025
Versão: 0.0.3
Nesta versão, o usuário poderá entrar com seu nome para ser cumprimentado pelo programa.
"""

# Alocação de memória

nome = ""
frase = ""

# Entrada de dados

nome = str(input("\nQual o seu nome?"))

# Processamento de dados

frase = "Hello, " + nome + "!"

# Saída de dados

print(frase)