from conta import Conta

conta = Conta(123, "Lucas", 100.0, 1000.0)

conta.extrato()
conta.deposita(100)
conta.extrato()
conta.saca(1000)
conta.extrato()
print(conta.get_titular())
