
# número digitado pelo usuário

user_numero = int(input("Digite um número:"))

# primeiros valores da sequência para uso dentro do loop

fibo_init = [0,1]

# Escolhendo um valor  inicial para prox_num

prox_num = 0

# loop que calcula a soma dos dois últimos valores da lista e coloa os numeros da sequencia na lista

while  (prox_num <= user_numero):

    prox_num = fibo_init[-1] + fibo_init[-2]

    fibo_init.append(prox_num)

# Função para verificar se o numero digitado pelo usuario está na sequência (poderia ter feito outra iteração mas in fica mais enxuto)

def verifica_user_numero(user_numero):
    if user_numero in fibo_init:
        print('O número digitado pertence à sequência de Fibonacci')
    else:
        print('O número digitado não pertence à sequência de Fibonacci')

# Aplicação da função

verifica_user_numero(user_numero)

