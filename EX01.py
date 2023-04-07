# 1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em
# parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com
# máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma
# porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano. Sua tarefa é criar um algoritmo que
# receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o
# cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

# Basic 30%
# Silver 20%
# Gold 10%
# Platinum 5%

tipo_assinatura = input("Digite a assinatura escolhida: BASIC, SILVER, GOLD ou PLATINUM ")
faturamento = float(input("Digite o faturamento anual do canal "))

if tipo_assinatura.upper() == "BASIC":
    bonus = faturamento * 0.3
elif tipo_assinatura.upper() == "SILVER":
    bonus = faturamento * 0.2
elif tipo_assinatura.upper() == "GOLD":
    bonus = faturamento * 0.1
elif tipo_assinatura.upper() == "PLATINUM":
    bonus = faturamento * 0.05
else:
    print("Tipo de assinatura inexistente!")

print("Você deve pagar R$ {:.2f} de bônus".format(bonus))