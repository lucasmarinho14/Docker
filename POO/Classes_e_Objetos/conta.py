class Conta:

    #Metodo Construtor
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Métodos
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
    
    def deposita(self, valor):
        print("depositando {} na conta de {}".format(valor, self.__titular))
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #Getters e Setters
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite
    
    def get_numero(self):
        return self.__numero
    
    def set_limite(self, limite):
        self.__limite = limite

    #Método Estático
    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}


  
    

    
