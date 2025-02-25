"""
Programa hello
Descrição: imprima na tela a frase "hello, world!".
Autor: Augusto Jacques
Data: 25/02/2025
Versão: 0.0.4
Nesta versão:
1. O usuário poderá entrar com seu nome para ser cumprimentado pelo programa.
2. Utilizamos f-strings para escrever um código mais limpo.
"""

# Alocação de memória

nome = ""
frase = ""

# Entrada de dados

nome = str(input("\nQual o seu nome?"))

# Processamento de dados

frase = f"Hello, {nome}!"

# Saída de dados

print(frase)