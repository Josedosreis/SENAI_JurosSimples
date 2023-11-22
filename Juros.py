# Projeto de calcular o juros simples

# Apresentação

print('\n\t\t\t -- Calculo de Juros Simples --\n ')

# Entrada

# Capital ou Valor
Capital = int(input('Informe Capital: '))

# Taxa do Juros
Taxa = int(input('Informe Taxa: '))

# Prazo ou Tempo
Prazo = int(input('Informe Prazo: '))

#Porcentagem
Porcentagem = int(input('Informe Porcentagem: '))

# Processamento

Juros = Capital * Taxa * Prazo / Porcentagem

# Saída

print(f' {Capital} * {Taxa} * {Prazo} / {Porcentagem} = {Juros}')