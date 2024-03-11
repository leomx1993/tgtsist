# Usuário digita string

string = (input("Digite uma string:"))

# i calcula o número de itens da string -1 porque no python o length da um numero  e o for começa do 0

i = len(string) - 1 

# Iniciando string invertida com uma string vazia

string_invertida = ''

# Loop decresente que soma cada caractere de trás pra frente dado que i inicialmente era o comprimento da string -1 e foi descendo

for caractere in range(len(string)):

    caractere = string[i]
    string_invertida = string_invertida + caractere
    i = i - 1 

# print da string

print('string invertida:', string_invertida)



    
    