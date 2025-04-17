#entrada de dados
valor = int(input("Informe um valor:"))

#processamento
notas_cem = valor//100
resto = valor%100
notas_cinquenta = resto//50
resto = resto%50
notas_vinte = resto//20
resto = resto%20
notas_dez = resto//10
resto = resto%10
notas_cinco = resto//5
resto = resto%5
notas_dois = resto//2
resto = resto%2
um=resto

#saida de dados
print("Notas de cem = ",notas_cem)
print("Notas de cinquenta = ",notas_cinquenta)
print("Notas de vinte = ",notas_vinte)
print("Notas de dez = ",notas_dez)
print("Notas de cinco = ",notas_cinco)
print("Notas de dois = ",notas_dois)
print("Moedas de um = ",um)