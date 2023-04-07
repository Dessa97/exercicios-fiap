# 2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das
# lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
# (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o
# escolhido.

opcao1 = int(input("Informe a quantidade de votos para segunda-feira: "))
opcao2 = int(input("Informe a quantidade de votos para terça-feira: "))
opcao3 = int(input("Informe a quantidade de votos para quarta-feira: "))
opcao4 = int(input("Informe a quantidade de votos para quinta-feira: "))
opcao5 = int(input("Informe a quantidade de votos para sexta-feira: "))


segunda = opcao1
terca = opcao2
quarta = opcao3
quinta = opcao4
sexta = opcao5

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda-feira foi escolhida!")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça-feira foi escolhida!")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta-feira foi escolhida!")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Quinta-feira foi escolhida!")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("Sexta-feira foi escolhida!")
else:
    print("Houve empate!")
