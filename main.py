from software_treino import *

def menu():
    print("\nMENU SISTEMA GERADOR DE TREINOS")
    print("==============|💪|==============")
    print("1) Cadastrar aluno")
    print("2) Alunos cadastrados")
    print("3) Consultar treino")
    print("4) Criar treino")
    print("5) Sair")

def main():
    alunos = []

    while True:
        menu()
        opcao = input("\nSelecione uma opção: ")

        if opcao == "1":
            print("\nCadastrar novo auno:")
            nome = input("Nome: ")
            data = input("Data de nascimento (dd/mm/aa): ")
            cpf = input("CPF: ")
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))

            aluno = Aluno(nome, data, cpf, peso, altura)
            alunos.append(aluno)

            print(f"\nAluno(a) {nome} cadastrado(a) com sucesso!")

        elif opcao == "2":
            if not alunos:
                print("\n Nenhum aluno cadastrado")
            else:
                print("\n==== Alunos Cadastrados ===")
                for i, aluno in enumerate(alunos):
                    print(f"\n[{i + 1}]")
                    print(aluno)

        elif opcao == "3":
            if not alunos:
                print("\nNenhum aluno cadastrado, cadastre um aluno para consultar os treinos")
                continue

            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno._Pessoa__nome}")
            escolha = int(input("Escolha o número do aluno: ")) - 1

            if 0 <= escolha < len(alunos):
                print(f"\nTreinos de {alunos[escolha]._Pessoa__nome}:")
                alunos[escolha].visualizar_Treino()
            else:
                print("Aluno inválido!")

        elif opcao == "4":
            if not alunos:
                print("\nNenhum aluno cadastrado, cadastre um aluno para criar o treino")
                continue

            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno._Pessoa__nome}")
            escolha = int(input("Escolha o número do aluno: ")) - 1

            if 0 <= escolha < len(alunos):
                treino = input("Digite o nome do treino para adicionar: ")
                alunos[escolha].treinos.append(treino)
                print(f"Treino '{treino}' adicionado para {alunos[escolha]._Pessoa__nome}")
            else:
                print("Aluno inválido!")

        elif opcao == "5":
            print("\nSaindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
