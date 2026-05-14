from banco.conta import ContaBancaria
import pytest

def test_criar_conta_com_saldo_inicial():
    conta = ContaBancaria(saldo_inicial=100)
    assert conta.saldo == 100

def test_depositar_valor_positivo():
    """Deve aumentar o saldo quando depositar valor positivo"""
    conta = ContaBancaria(saldo_inicial=100)
    conta.depositar(50)
    assert conta.saldo == 150

def test_depositar_valor_negativo_deve_lancar_excecao():
    """Deve lançar exceção ao tentar depositar valor negativo"""
    conta = ContaBancaria(saldo_inicial=100)
    with pytest.raises(ValueError):
        conta.depositar(-50)

def test_depositar_zero_deve_lancar_excecao():
    """Deve lançar exceção ao tentar depositar zero"""
    conta = ContaBancaria(saldo_inicial=100)
    with pytest.raises(ValueError):
        conta.depositar(0)