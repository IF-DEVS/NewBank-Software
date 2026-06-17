class CalculadoraJuros:
    """
    Calculadora de Juros Simples e Compostos
    Versão refatorada seguindo TDD
    
    Regras de negócio:
    - Taxa deve estar entre 0% e 100% (0.0 a 1.0)
    - Capital não pode ser negativo
    - Tempo não pode ser negativo
    """
    
    # Constantes para validação
    TAXA_MINIMA = 0.0
    TAXA_MAXIMA = 1.0
    
    def __init__(self, taxa: float = 0.0):
        """Inicializa a calculadora com uma taxa válida"""
        self._validar_taxa(taxa)
        self._taxa = taxa
    
    # ==================== MÉTODOS PÚBLICOS ====================
    
    def get_taxa(self) -> float:
        """Retorna a taxa de juros atual"""
        return self._taxa
    
    def set_taxa(self, nova_taxa: float) -> None:
        """Define uma nova taxa de juros com validação"""
        self._validar_taxa(nova_taxa)
        self._taxa = nova_taxa
    
    def calcular_juros_simples(self, capital: float, tempo: int) -> float:
        """
        Calcula juros simples: J = C * i * t
        
        Args:
            capital: Valor principal
            tempo: Período de tempo
            
        Returns:
            Valor dos juros calculados
        """
        self._validar_capital_tempo(capital, tempo)
        return self._calcular_juros_simples(capital, tempo)
    
    def calcular_juros_compostos(self, capital: float, tempo: int) -> float:
        """
        Calcula juros compostos: M = C * (1 + i)^t, Juros = M - C
        
        Args:
            capital: Valor principal
            tempo: Período de tempo
            
        Returns:
            Valor dos juros calculados
        """
        self._validar_capital_tempo(capital, tempo)
        return self._calcular_juros_compostos(capital, tempo)
    
    # ==================== MÉTODOS PRIVADOS ====================
    
    def _validar_taxa(self, taxa: float) -> None:
        """Valida se a taxa está dentro dos limites permitidos"""
        if taxa < self.TAXA_MINIMA:
            raise ValueError(f"Taxa não pode ser negativa. Informado: {taxa}")
        if taxa > self.TAXA_MAXIMA:
            raise ValueError(f"Taxa não pode ser maior que 100%. Informado: {taxa}")
    
    def _validar_capital_tempo(self, capital: float, tempo: int) -> None:
        """Valida se capital e tempo são válidos"""
        if capital < 0:
            raise ValueError(f"Capital não pode ser negativo. Informado: {capital}")
        if tempo < 0:
            raise ValueError(f"Tempo não pode ser negativo. Informado: {tempo}")
    
    def _calcular_juros_simples(self, capital: float, tempo: int) -> float:
        """Cálculo interno de juros simples"""
        return capital * self._taxa * tempo
    
    def _calcular_juros_compostos(self, capital: float, tempo: int) -> float:
        """Cálculo interno de juros compostos"""
        if capital == 0 or tempo == 0:
            return 0.0
        montante = capital * (1 + self._taxa) ** tempo
        return montante - capital