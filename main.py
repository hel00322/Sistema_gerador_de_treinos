from software_treino import *
from datetime import datetime

def menu():
    print("\n============================")
    print("SISTEMA GERADOR DE TREINOS")
    print("============|💪|============")
    print("1) Cadastrar aluno")
    print("2) Listar alunos cadastrados")
    print("3) Consultar treino de um aluno")
    print("4) Exibir treinos de todos os alunos")
    print("5) Atualizar Peso (para IMC)")
    print("6) Realizar Avaliação Física (IMC)")
    print("7) Remover aluno")
    print("0) Sair")

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
            print("\n=== CADASTRAR NOVO ALUNO ===")
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
                continue

            alunos.append(aluno)
            print(f"\nAluno(a) {nome} cadastrado com sucesso!")
            print("Treino gerado automaticamente:")
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
                print(f"{i}. {a._Pessoa__nome}")
            try:
                escolha = int(input("\nEscolha o aluno: ").strip()) - 1
                if 0 <= escolha < len(alunos):
                    alunos[escolha].treino.exibir_treino_completo()
                else:
                    print("Aluno inválido.")
            except ValueError:
                print("Entrada inválida.")

        elif opc == "4":
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                continue
            print("\n=== CONSULTAR TODOS OS TREINOS ===")
            for a in alunos:
                print(f"\nAluno: {a._Pessoa__nome}")
                a.treino.exibir_treino_completo()

        elif opc == "5": 
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                continue
            print("\n=== ATUALIZAR DADOS ===")
            for i, a in enumerate(alunos, start=1):
                print(f"{i}. {a._Pessoa__nome} (Peso atual: {a.peso}kg)")
            try:
                escolha = int(input("\nEscolha o aluno: ").strip()) - 1
                if 0 <= escolha < len(alunos):
                    novo_peso = ler_float("Novo peso (kg): ")
                    alunos[escolha].peso = novo_peso
                    print("Peso atualizado!")
                else:
                    print("Inválido.")
            except ValueError:
                print("Erro.")

        elif opc == "6":
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                continue
            
            print("\n=== AVALIAÇÃO FÍSICA ===")
            for i, a in enumerate(alunos, start=1):
                print(f"{i}. {a._Pessoa__nome}")
                
            try:
                escolha = int(input("\nEscolha o aluno para avaliar: ").strip()) - 1
                if 0 <= escolha < len(alunos):
                    aluno_selecionado = alunos[escolha]
                    
                    avaliacao = AvaliacaoFisica(
                        aluno_selecionado, 
                        datetime.now(), 
                        imc_anterior=aluno_selecionado.ultimo_imc
                    )
                    
                    print("\n" + "="*30)
                    print(avaliacao.evolucao())
                    print("="*30)
                    
                    imc_atual = avaliacao.calcular_IMC()
                    if isinstance(imc_atual, float):
                        aluno_selecionado.ultimo_imc = imc_atual
                        
                else:
                    print("Aluno inválido.")
            except ValueError:
                print("Entrada inválida.")

        
        elif opc == "7":
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                continue
            print("\n=== REMOVER ALUNO ===")
            for i, a in enumerate(alunos, start=1):
                print(f"{i}. {a._Pessoa__nome}")
            try:
                escolha = int(input("\nEscolha o aluno a remover: ").strip()) - 1
                if 0 <= escolha < len(alunos):
                    removido = alunos.pop(escolha)
                    print(f"Aluno {removido._Pessoa__nome} removido.")
                else:
                    print("Aluno inválido.")
            except ValueError:
                print("Entrada inválida.")

        elif opc == "0":
            print("\nSaindo...")
            break

        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main()