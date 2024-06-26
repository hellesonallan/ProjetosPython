import random
import string

# Função de pergunta
def pergunta(prompt):
    resposta = input(prompt).strip().upper()
    while resposta not in ["S", "N", "SIM", "NAO", "NÃO"]:
        resposta = input(prompt).strip().upper()
    return resposta

# Função de geração de senha
def gerar_senha():
    # Definir variáveis
    tamanho = int(input("Quantos caracteres?: "))
    opcoes = []

    # Perguntar ao usuário sobre as opções
    if pergunta("Incluir letras? (S/N): ") in ["S", "SIM"]:
        opcoes.extend(string.ascii_letters)
    if pergunta("Incluir números? (S/N): ") in ["S", "SIM"]:
        opcoes.extend(string.digits)
    if pergunta("Incluir símbolos e letras especiais? (S/N): ") in ["S", "SIM"]:
        opcoes.extend(string.punctuation)
    if pergunta("Incluir espaços em branco? (S/N): ") in ["S", "SIM"]:
        opcoes.extend(string.whitespace)

    # Gerar a senha
    senha = str().join(random.choices(opcoes, k=tamanho))
    return senha

print("Senha Gerada: " + gerar_senha())
input("Press enter to exit...")
