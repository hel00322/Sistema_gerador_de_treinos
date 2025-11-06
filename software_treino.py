from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Pessoa(ABC):
    __nome : str 
    __dataNascimento : str
    __cpf : int
    peso : float
    altura : float

    def __init__(self, nome, data, cpf, peso, altura):
        self.__nome = nome 
        self.__dataNascimento = datetime.strptime(data, "%d/%m/%Y")
        self.__cpf = cpf 
        self.peso = peso 
        self.altura = altura

    def calcular_Idade(self):
        data_atual = datetime.now()
        idade = data_atual.year - self.__dataNascimento.year
    # Ajuste se ainda não fez aniversário no ano atual
        if data_atual.month < self.__dataNascimento.month or (data_atual.month == self.__dataNascimento.month and data_atual.day < self.__dataNascimento.day):
            idade -= 1
        return idade

    def __str__(self):
        idade = self.calcular_Idade()
        txt = f"Nome: {self.__nome}\n"
        txt += f"Idade: {idade} anos\n"
        txt += f"Peso: {self.peso}kg\n"
        txt += f"Altura: {self.altura}m\n"
        return txt

class Aluno(Pessoa):
    matricula: int 
    objetivo: str
    treinos: List[str]

    # Variáveis de classe para controle das matrículas
    _matriculas_existentes = set()
    _proxima_matricula = 1000  

    def __init__(self, nome, data, cpf, peso, altura):
        super().__init__(nome, data, cpf, peso, altura)
        self.matricula = self._gerar_matricula_unica()
        self.objetivo = self.definir_objetivo()
        self.treino = Treino("Treino Personalizado", "Iniciante", self.objetivo)

    @classmethod
    def _gerar_matricula_unica(cls):
        """Gera número de matrícula único automaticamente."""
        while cls._proxima_matricula in cls._matriculas_existentes:
            cls._proxima_matricula += 1
        nova_matricula = cls._proxima_matricula
        cls._matriculas_existentes.add(nova_matricula)
        cls._proxima_matricula += 1
        return nova_matricula

    def definir_objetivo(self):
        objetivos_possiveis = ["Emagrecimento", "Hipertrofia", "Resistência", "Condicionamento"]

        while True:
            print("\nEscolha o objetivo do aluno:")
            for i, obj in enumerate(objetivos_possiveis, 1):
                print(f"{i} - {obj}")
            try:
                escolha = int(input("Digite o número correspondente: "))
                if 1 <= escolha <= len(objetivos_possiveis):
                    return objetivos_possiveis[escolha - 1]
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Digite apenas números válidos.")

    def __str__(self):
        txt = super().__str__()
        txt += f"Matrícula: {self.matricula}\n"
        txt += f"Objetivo: {self.objetivo}\n"
        return txt

class Exercicio:
    __nome : str 
    __grupoMuscular : str
    __series : int 
    __repeticoes : int 

    def __init__(self, nomeExercicio, grupoMuscular, series, repeticoes):
        self.__nome = nomeExercicio
        self.__grupoMuscular = grupoMuscular
        self.__series = series 
        self.__repeticoes = repeticoes

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_grupo_muscular(self):
        return self.__grupo_muscular

    def set_grupo_muscular(self, grupo: str):
        self.__grupo_muscular = grupo

    def get_series(self):
        return self.__series

    def set_series(self, series: int):
        if series <= 0:
            raise ValueError("O número de séries deve ser positivo.")
        self.__series = series

    def get_repeticoes(self):
        return self.__repeticoes

    def set_repeticoes(self, repeticoes: int):
        if repeticoes <= 0:
            raise ValueError("O número de repetições deve ser positivo.")
        self.__repeticoes = repeticoes
        
    def detalhar_Exercicio(self):
        return (f"{self.__nome} | Grupo: {self.__grupoMuscular} | "
            f"Séries: {self.__series} | Repetições: {self.__repeticoes}")
class Treino:
    __nomeTreino : str
    __nivel : str 
    __objetivo : str 
    __exercicios : List

    def __init__(self, nomeTreino, nivel, objetivo):
        self.__nomeTreino = nomeTreino
        self.__nivel = nivel
        self.__objetivo = objetivo.lower()
        self.__exercicios: List[Exercicio] = []

        # Gera automaticamente os exercícios ao criar o treino
        self.__gerar_exercicios_por_objetivo()

    def __gerar_exercicios_por_objetivo(self):
        """Cria exercícios automaticamente conforme o objetivo do aluno"""
        if self.__objetivo == "emagrecimento":
            self.__exercicios = [
                Exercicio("Corrida na esteira", "Cardio", 1, 30),
                Exercicio("Agachamento livre", "Pernas",4, 15),
                Exercicio("Prancha", "Abdômen", 3, 45)
            ]

        elif self.__objetivo == "hipertrofia":
            self.__exercicios = [
                Exercicio("Supino reto", "Peito", 4, 8),
                Exercicio("Leg press", "Pernas", 4, 10),
                Exercicio("Remada curvada", "Costas", 4, 8)
            ]

        elif self.__objetivo == "condicionamento":
            self.__exercicios = [
                Exercicio("Corrida leve", "Cardio", 1, 20),
                Exercicio("Flexão de braço", "Peito",3, 15),
                Exercicio("Abdominais", "Core", 3, 20)
            ]

        else:
            self.__exercicios = [
                Exercicio("Caminhada leve", "Cardio",1, 20),
                Exercicio("Polichinelos", "Corpo inteiro", 3, 20)
            ]

    def exibir_treino_completo(self):
        print(f"\nTreino: {self.__nomeTreino} ({self.__nivel}) - Objetivo: {self.__objetivo.capitalize()}")
        for ex in self.__exercicios:
            print(" -", ex.detalhar_Exercicio())


        
if __name__ == "__main__":
    aluno1 = Aluno("Heloisa", "22/03/2006", 12345678900, 68, 1.63)
    print(aluno1)
    aluno1.treino.exibir_treino_completo()
    aluno2 = Aluno("Bianca", "24/09/2003", 49057643863, 66, 1.63)
    print(aluno2)
    aluno2.treino.exibir_treino_completo()





