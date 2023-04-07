# 3 - Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa
# razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você
# criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos
# que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par
# (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final,
# qual delas teve a maior nota.
# Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas,
# deve ser exibida uma mensagem no seguinte padrão:
# VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
# POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

soma_impar = 0.0
soma_par = 0.0

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES")

for impar in range(1, 51, 2):
    nota_impar = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(impar)))
    soma_impar = soma_impar + nota_impar

media_impar = soma_impar / 25

print("OS ALUNOS ÍMPARES TEM MÉDIA {:.1f}".format(media_impar))


print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")

for par in range(2, 51, 2):
    nota_par = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(par)))
    soma_par = soma_par + nota_par

media_par = soma_par / 25

print("OS ALUNOS PARES TEM MÉDIA {:.1f}".format(media_par))


if media_par > media_impar:
    print("OS ALUNOS PARES TEM A MAIOR NOTA!")
elif media_impar > media_par:
    print("OS ALUNOS ÍMPARES TEM A MAIOR NOTA!")
else:
    print("HOUVE EMPATE!")