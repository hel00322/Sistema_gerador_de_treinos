from software_treino import *

def menu():
    print("\n============================")
    print("SISTEMA GERADOR DE TREINOS")
    print("============|💪|============")
    print("1) Cadastrar aluno")
    print("2) Listar alunos cadastrados")
    print("3) Consultar treino de um aluno")
    print("4) Exibir treinos de todos os alunos")
    print("5) Remover aluno")
    print("6) Sair")

def escolher_objetivo():
    objetivos = ["Emagrecimento", "Hipertrofia", "Resistência", "Condicionamento"]
    print("\nEscolha o objetivo do aluno:")
    for i, obj in enumerate(objetivos, 1):
        print(f"{i}) {obj}")
    while True:
        escolha = input("Número do objetivo: ").strip()
        try:
            idx = int(escolha)
            if 1 <= idx <= len(objetivos):
                return objetivos[idx - 1]
            else:
                print("Escolha um número entre 1 e", len(objetivos))
        except ValueError:
            print("\nDigite apenas números válidos.")

def ler_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("\nInforme um número válido.")

def main():
    alunos: list[Aluno] = []

    while True:
        menu()
        opc = input("\nSelecione uma opção: ").strip()

        if opc == "1":
            print("\n=== Cadastro de Novo Aluno ===")
            nome = input("Nome: ").strip()
            data = input("Data de nascimento (dd/mm/yyyy): ").strip()
            cpf = input("CPF: ").strip()
            peso = ler_float("Peso (kg): ")
            altura = ler_float("Altura (m): ")
            objetivo = escolher_objetivo()

            try:
                aluno = Aluno(nome, data, cpf, peso, altura, objetivo)
            except Exception as e:
                print("Erro ao criar aluno:", e)
                print("Verifique os dados e tente novamente.")
                continue

            alunos.append(aluno)
            print(f"\nAluno(a) {nome} cadastrado(a) com sucesso!")
            print(f"Matrícula gerada: {aluno.matricula}")
            print(f"Objetivo: {aluno.objetivo}")
            print("\nTreino gerado automaticamente:")
            aluno.treino.exibir_treino_completo()

        elif opc == "2":
            if not alunos:
                print("\nNenhum aluno cadastrado.")
            else:
                print("\n=== ALUNOS CADASTRADOS ===")
                for i, a in enumerate(alunos, start=1):
                    print(f"[{i}]")
                    print(a)

        elif opc == "3":
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                continue

            print("\n=== CONSULTAR TREINO ===")
            for i, a in enumerate(alunos, start=1):
                print(f"{i}. {a._Pessoa__nome} (Matrícula: {a.matricula})")

            try:
                escolha = int(input("\nEscolha o número do aluno: ").strip()) - 1
            except ValueError:
                print("\nDigite um número válido.")
                continue

            if 0 <= escolha < len(alunos):
                aluno = alunos[escolha]
                print(f"\nTreino de {aluno._Pessoa__nome}:")
                aluno.treino.exibir_treino_completo()
            else:
                print("\nAluno inválido.")

        elif opc == "4":
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                continue
            print("\n=== TREINOS DE TODOS OS ALUNOS ===")
            for a in alunos:
                print(f"\nAluno: {a._Pessoa__nome} (Matrícula: {a.matricula})")
                a.treino.exibir_treino_completo()

        elif opc == "5":
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                continue
            print("\n=== REMOVER ALUNO ===")
            for i, a in enumerate(alunos, start=1):
                print(f"{i}. {a._Pessoa__nome} (Matrícula: {a.matricula})")
            try:
                escolha = int(input("\nEscolha o número do aluno a remover: ").strip()) - 1
                if 0 <= escolha < len(alunos):
                    removido = alunos.pop(escolha)
                    print(f"\nAluno {removido._Pessoa__nome} removido.")
                else:
                    print("\nAluno inválido.")
            except ValueError:
                print("\nDigite um número válido.")

        elif opc == "6":
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
