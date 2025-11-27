import csv
import random
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
    
        if data_atual.month < self.__dataNascimento.month or (data_atual.month == self.__dataNascimento.month and data_atual.day < self.__dataNascimento.day):
            idade -= 1
        return idade
    
    def get_peso(self):
        return self.peso 

    def __str__(self):
        idade = self.calcular_Idade()
        txt = f"Nome: {self.__nome}\n"
        txt += f"Idade: {idade} anos\n"
        txt += f"Peso: {self.peso}kg\n"
        txt += f"Altura: {self.altura}m\n"
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
        self.__exercicios = []
        todos_exercicios_compativeis = []
        
        try:
            with open('exercicios.csv', mode='r', encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo)
                
                for linha in leitor:
                    if linha['Objetivo'].strip().lower() == self.__objetivo:
                        novo_exercicio = Exercicio(
                            linha['Nome do Exercício'],
                            linha['Grupo Muscular'],
                            linha['Séries'],
                            linha['Repetições']
                        )
                        todos_exercicios_compativeis.append(novo_exercicio)

            if not todos_exercicios_compativeis:
                print(f"\nAviso: Nenhum exercício encontrado no CSV para o objetivo '{self.__objetivo}'.")
            elif len(todos_exercicios_compativeis) > 5:
                self.__exercicios = random.sample(todos_exercicios_compativeis, 5)
            else:
                self.__exercicios = todos_exercicios_compativeis

        except Exception as e:
            print(f"\nErro ao ler o arquivo de exercícios: {e}")

    def exibir_treino_completo(self):
        print(f"\nTreino: {self.__nomeTreino} ({self.__nivel}) - Objetivo: {self.__objetivo.capitalize()}")
        if not self.__exercicios:
            print(" - Nenhum exercício cadastrado.")
        for ex in self.__exercicios:
            print(f" - {ex.get_nome()} ({ex.get_grupo_muscular()}) - {ex.get_series()}x{ex.get_repeticoes()}")


class Aluno(Pessoa):
    matricula: int 
    objetivo: str
    treino: Treino 
    ultimo_imc: float

    _matriculas_existentes = set()
    _proxima_matricula = 1000  

    def __init__(self, nome, data, cpf, peso, altura, objetivo_escolhido):
        super().__init__(nome, data, cpf, peso, altura)
        self.matricula = self._gerar_matricula_unica()
        self.objetivo = objetivo_escolhido
        self.treino = Treino("Treino Personalizado", "Iniciante", self.objetivo)
        self.ultimo_imc = None

    @classmethod
    def _gerar_matricula_unica(cls):
        while cls._proxima_matricula in cls._matriculas_existentes:
            cls._proxima_matricula += 1
        nova_matricula = cls._proxima_matricula
        cls._matriculas_existentes.add(nova_matricula)
        cls._proxima_matricula += 1
        return nova_matricula

    def __str__(self):
        txt = super().__str__()
        txt += f"Matrícula: {self.matricula}\n"
        if self.ultimo_imc:
            txt += f"Último IMC: {self.ultimo_imc:.2f}\n"
        return txt

class AvaliacaoFisica:
    
    def __init__(self, pessoa: Aluno, data_atual, imc_anterior=None):
        self.pessoa = pessoa 
        self.data_atual = data_atual
        self.imc_anterior = imc_anterior 

    def calcular_IMC(self):
        peso_pessoa = self.pessoa.get_peso()  
        altura_pessoa = self.pessoa.altura  
        
        if altura_pessoa > 0:
            imc = peso_pessoa / (altura_pessoa ** 2)
            return imc
        else:
            return "Altura inválida!"
    
    def classificar_IMC(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"

    def evolucao(self):
        imc_atual = self.calcular_IMC()  

        if type(imc_atual) == str:
            return imc_atual 
 
        if self.imc_anterior is None:
            classificacao_imc = self.classificar_IMC(imc_atual)
            return f"Primeira avaliação! Seu IMC atual é {imc_atual:.2f} ({classificacao_imc}). Vamos acompanhar sua evolução!"

        if imc_atual < self.imc_anterior:
            evolucao = "melhorou"
        elif imc_atual > self.imc_anterior:
            evolucao = "piorou"
        else:
            evolucao = "não teve alteração"

        objetivo = self.pessoa.objetivo.lower()
        classificacao_imc = self.classificar_IMC(imc_atual)

        if objetivo == "emagrecimento":
            if evolucao == "melhorou":
                return f"Parabéns! IMC baixou de {self.imc_anterior:.2f} para {imc_atual:.2f} ({classificacao_imc})."
            elif evolucao == "piorou":
                return f"Atenção. IMC subiu de {self.imc_anterior:.2f} para {imc_atual:.2f} ({classificacao_imc})."
            else:
                return f"Estável em {imc_atual:.2f} ({classificacao_imc})."

        elif objetivo == "hipertrofia":
            if evolucao == "melhorou": 
                return f"IMC diminuiu para {imc_atual:.2f}. Cuidado com perda de massa."
            elif evolucao == "piorou":
                return f"IMC subiu para {imc_atual:.2f} ({classificacao_imc}). Ótimo se for músculo!"
            else:
                return f"Estável em {imc_atual:.2f}. Foco no treino!"

        else:
            return f"IMC atual: {imc_atual:.2f} ({classificacao_imc})."