class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print("Horas registradas...")
    
    def mostrar_tarefas(self):
        print("Fez muita coisa...")
    
class EmpresaA(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, EmpresaA")
    
    def busca_cursos_do_mes(self, mes=None):
        print(f"Mostrando cursos - {mes}" if mes else "Mostrando cursos desse mês")

class EmpresaB(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, EmpresaB")
    
    def busca_perguntas_sem_resposta(self):
        print("Mostrando perguntas não resondidas do fórum")

#Classe Mixin
class Hipster:
    def __str__(self):
        return f"Hipster, {self.nome}"

class Junior(EmpresaB):
    pass

class Pleno(EmpresaB, EmpresaA):
    pass

class Senior(EmpresaA,EmpresaB, Hipster):
    pass


#jose = Junior()
#jose.busca_perguntas_sem_resposta()

#A Linha a baixo não funcionaria pois jose não pertence a classe Pleno
#jose.busca_cursos_do_mes

#luan = Pleno()
#Já Luan como é Pleno, possui ambas as funções

luan = Senior("Luan")
print(luan)

