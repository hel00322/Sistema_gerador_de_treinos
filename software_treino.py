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

    def __init__(self, nome, data, cpf, peso, altura, objetivo_escolhido):
        super().__init__(nome, data, cpf, peso, altura)
        self.matricula = self._gerar_matricula_unica()
        self.objetivo = objetivo_escolhido
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


    def __str__(self):
        txt = super().__str__()
        txt += f"Matrícula: {self.matricula}\n"
        return txt

class Exercicio:
    def __init__(self, nomeExercicio, grupoMuscular, series, repeticoes):
        self.__nome = nomeExercicio
        self.__grupoMuscular = grupoMuscular
        self.__series = series
        self.__repeticoes = repeticoes

    
    def get_nome(self):
        return self.__nome

    def get_grupo_muscular(self):
        return self.__grupoMuscular

    def get_series(self):
        return self.__series

    def get_repeticoes(self):
        return self.__repeticoes

    def detalhar_exercicio(self):
        return f"{self.__nome} ({self.__grupoMuscular}) - {self.__series}x{self.__repeticoes}"

class Treino:

    def __init__(self, nomeTreino, nivel, objetivo):
        self.__nomeTreino = nomeTreino
        self.__nivel = nivel
        self.__objetivo = objetivo.lower()
        self.__exercicios: List[Exercicio] = []
        self.__gerar_exercicios_por_objetivo()

    def __gerar_exercicios_por_objetivo(self):
        if self.__objetivo == "emagrecimento":
            self.__exercicios = [
                Exercicio("Corrida na esteira", "Cardio", 1, 30),
                Exercicio("Agachamento livre", "Pernas", 4, 15),
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
                Exercicio("Flexão de braço", "Peito", 3, 15),
                Exercicio("Abdominais", "Core", 3, 20)
            ]
        else:
            self.__exercicios = [
                Exercicio("Caminhada leve", "Cardio", 1, 20),
                Exercicio("Polichinelos", "Corpo inteiro", 3, 20)
            ]

    def exibir_treino_completo(self):
        print(f"\nTreino: {self.__nomeTreino} ({self.__nivel}) - Objetivo: {self.__objetivo.capitalize()}")
        for ex in self.__exercicios:
            print(f" - {ex.get_nome()} ({ex.get_grupo_muscular()}) - {ex.get_series()}x{ex.get_repeticoes()}")


    



