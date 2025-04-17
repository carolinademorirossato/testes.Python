#Entrada de dados
idade = int(input("Digite a sua idade:"))

#Processamento e saída de dados
if(idade>=16):
    print("Você já pode votar.")
else:
    print("Você ainda deve aguardar",16-idade,"ano(s) para votar.")
if(idade>=18):
    print("Você já pode conduzir veículos e motos.")
else:
    print("Você ainda precisa aguardar",18-idade,"ano(s)para dirigir.")