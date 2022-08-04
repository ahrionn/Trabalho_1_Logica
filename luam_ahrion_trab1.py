'''
Questão01
Utilizando o Python, crie um arquivo com o “seuNome.py”. Exemplo: IvoneiMarques.py
Neste arquivo, crie o código para o seguinte problema:

Faça um programa que peça para 'n' pessoas (várias pessoas - utilizando while) a sua idade,
o programa deverá verificar se a média de idade da turma
varia nos intervalos de 0 e 25,26 e 60 e maior que 60; e então, diga se a
turma é jovem, adulta ou idosa, conforme a média calculada.
Mostre também a maior idade de cada faixa.

Obs: A digitação da idade encerra ao digitar a palavra fim, ou após digitar 40 Alunos.
    Caso não haja nenhum aluno digitado em uma das faixas mostre a seguinte
    mensagem: 'não houve alunos digitados'

Exemplo:
========
    Após digitar alguns alunos...
Digite a idade do aluno: fim

- A média de idades da Turma é: 17.5
- Portanto, pode-se dizer que a turma é Jovem.
Para essa turma a maior idade digitada para a:
- primeira faixa é 23 anos
- segunda faixa é 33 anos
- terceira faixa não houve alunos digitados.

'''

n = int(input("Informe a quantidade de alunos.(Qtd máxima é 40): "))
if n > 40:
    print("Quantidade de alunos excedida. Reinicie o programa.")
    exit()
i = 0
somaIdades = 0

faixa_jovem = []
faixa_adulta = []
faixa_idosa = []

while i < n:

    try:

        idade = int(input("Digite sua idade: "))

        somaIdades += idade;
        i += 1;
        media = somaIdades/n
        
        if media > 0 and media <= 25:
            turma = 'Jovem'

        elif media > 25 and media <= 60:
            turma = 'Adulta'

        elif media > 60:
            turma = 'Idosa'

        if idade > 0 and idade <= 25:
            faixa_jovem.append(idade)

        elif idade > 25 and idade <= 60:
            faixa_adulta.append(idade)

        elif idade > 60:
            faixa_idosa.append(idade)

    except:
        print("Não houve alunos digitados.")
        
print("A média de idade da turma é: ",media)
print("Portanto, pode-se dizer que a turma é: ",turma)
print("Para esta turma a maior idade digitada para a: ")
if faixa_jovem == []:
    print("Primeira faixa: Não houve alunos digitados.")
else:
    print("Primeira faixa é: ",(max(faixa_jovem)),"anos")
if faixa_adulta == []:
    print("Segunda faixa: Não houve alunos digitados.")
else:
    print("Segunda faixa é: ",(max(faixa_adulta)),"anos")
if faixa_idosa == []:
    print("Terceira faixa: Não houve alunos digitados.")
else:
    print("Terceira faixa é: ",(max(faixa_idosa)),"anos")

input()
