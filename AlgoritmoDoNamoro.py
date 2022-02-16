#AlgoritmoDoNamoro by Suellen KT
nome = input ('Qual seu nome?')
print('Olá, ', nome, '.')

print ('Eu sou a voz da razão e por isso, vou dizer a você, se você já pode namorar.')
idade: int
idade=int(input ('Qual sua idade?'))

if idade <=14:
  namoro = "Não pode namorar."
elif idade>=15 and idade<18:
  namoro = "Pode namorar, mas com supervisão."
elif idade>=18 and idade<30:
  namoro = 'Pode namorar, mas não casar! Porque você é da mamãe. :)'
elif idade>=30:
  namoro = "Pode namorar e casar."

print (namoro)
