# Essa s erá apenas uma introdução ao Try e ao Except

# o try tenta executar o código
# o except ocorre quando ocorreu um erro dentro do bloco do try
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número.')