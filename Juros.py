# Projeto de calcular o juros simples

# Apresentação

print('\n\t\t\t -- Calculo de Juros Simples --\n ')

# Entrada

# Capital ou Valor
capital = float(input('Informe Capital: '))

# Taxa do Juros
taxa = float(input('Informe Taxa: '))

# Prazo ou Tempo
prazo = int(input('Informe Prazo: '))

# Processamento

juros = capital * taxa * prazo / 100

# Saída

print(f' {capital} * {taxa} * {prazo} / {100} = {juros}')
