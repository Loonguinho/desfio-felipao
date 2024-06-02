# Instruções para entrega
# # 1️⃣ Desafio Classificador de nível de Herói

# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões

# ## Objetivo

# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# Se XP for menor do que 1.000 = Ferro
# Se XP for entre 1.001 e 2.000 = Bronze
# Se XP for entre 2.001 e 5.000 = Prata
# Se XP for entre 5.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000= Imortal
# Se XP for maior ou igual a 10.001 = Radiante

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói de nome **{nome}** está no nível de **{nivel}**"

hero_name = input("Qual o nome do seu herói?\n")
hero_xp = int(input("Quanto xp o herói tem?\n"))
hero_level = ""

if hero_xp < 1000:
    hero_level = "Ferro"
elif hero_xp > 1001 and hero_xp < 2000:
    hero_level = "Bronze"
elif hero_xp > 2001 and hero_xp < 5000:
    hero_level = "Prata"
elif hero_xp > 5001 and hero_xp < 7000:
    hero_level = "Ouro"
elif hero_xp > 7001 and hero_xp < 8000:
    hero_level = "Platina"
elif hero_xp > 8001 and hero_xp < 9000:
    hero_level = "Ascendente"
elif hero_xp > 9001 and hero_xp < 10000:
    hero_level = "Imortal"
elif hero_xp > 10000:
    hero_level = "Radiante"


print(f'O Herói {hero_name} está no nível de {hero_level}')