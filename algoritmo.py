# Algoritmo em Python: Cadastro de 20 alunos
# Recebe nome, nota e idade de 20 alunos e apresenta quem é maior de idade na tela.

# Quantidade total de alunos (altere para 3 ou 5 se quiser testar mais rápido)
TOTAL_ALUNOS = 20

alunos = []

print("=== ENTRADA DE DADOS DOS ALUNOS ===")
for i in range(1, TOTAL_ALUNOS + 1):
    print(f"\nAluno {i} de {TOTAL_ALUNOS}:")
    nome = input("Digite o nome: ")
    nota = float(input("Digite a nota: "))
    idade = int(input("Digite a idade: "))
    
    # Armazena os dados do aluno em um dicionário
    alunos.append({
        "nome": nome,
        "nota": nota,
        "idade": idade
    })

# --- MOSTRANDO OS RESULTADOS NA TELA ---
print("\n" + "=" * 45)
print("             RESULTADOS NA TELA")
print("=" * 45)

# 1. Alunos maiores de idade (idade igual ou superior a 18 anos)
print("\n>>> ALUNOS MAIORES DE IDADE (>= 18 ANOS):")
tem_maior_de_idade = False

for aluno in alunos:
    if aluno["idade"] >= 18:
        print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']:.1f} | Idade: {aluno['idade']} anos")
        tem_maior_de_idade = True

if not tem_maior_de_idade:
    print("Nenhum aluno é maior de idade.")

# 2. Aluno com a MAIOR idade da turma (o mais velho)
aluno_mais_velho = alunos[0]
for aluno in alunos:
    if aluno["idade"] > aluno_mais_velho["idade"]:
        aluno_mais_velho = aluno

print("\n>>> ALUNO COM A MAIOR IDADE (MAIS VELHO DA TURMA):")
print(f"Nome: {aluno_mais_velho['nome']} | Nota: {aluno_mais_velho['nota']:.1f} | Idade: {aluno_mais_velho['idade']} anos")

# 3. Lista completa de todos os alunos cadastrados
print("\n>>> LISTAGEM COMPLETA DE TODOS OS ALUNOS:")
for i, aluno in enumerate(alunos, start=1):
    situacao = "Maior de idade" if aluno["idade"] >= 18 else "Menor de idade"
    print(f"{i:02d}. {aluno['nome']} - Nota: {aluno['nota']:.1f} - Idade: {aluno['idade']} ({situacao})")
