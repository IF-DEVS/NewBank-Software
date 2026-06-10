class CalculadoraJuros:
    """
    Calculadora de Juros Simples e Compostos
    Implementação seguindo TDD (GREEN phase)
    """
    
    def __init__(self, taxa: float = 0.0):
        """Inicializa a calculadora com uma taxa"""
        self._taxa = taxa
    
    def get_taxa(self) -> float:
        """Retorna a taxa atual"""
        return self._taxa
    
    def set_taxa(self, nova_taxa: float) -> None:
        """Define nova taxa com validações"""
        if nova_taxa < 0:
            raise ValueError("Taxa não pode ser negativa")
        if nova_taxa > 1.0:
            raise ValueError("Taxa não pode ser maior que 100%")
        self._taxa = nova_taxa
    
    def calcular_juros_simples(self, capital: float, tempo: int) -> float:
        """Juros Simples: J = C * i * t"""
        if capital < 0:
            raise ValueError("Capital não pode ser negativo")
        if tempo < 0:
            raise ValueError("Tempo não pode ser negativo")
        return capital * self._taxa * tempo
    
    def calcular_juros_compostos(self, capital: float, tempo: int) -> float:
        """Juros Compostos: M = C * (1+i)^t, Juros = M - C"""
        if capital < 0:
            raise ValueError("Capital não pode ser negativo")
        if tempo < 0:
            raise ValueError("Tempo não pode ser negativo")
        if capital == 0 or tempo == 0:
            return 0.0
        montante = capital * (1 + self._taxa) ** tempo
        return montante - capital