class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """Adiciona valor ao saldo da conta
        
        Args:
            valor: Valor a depositar (deve ser positivo)
            
        Raises:
            ValueError: Se o valor for negativo ou zero
        """
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.saldo += valor