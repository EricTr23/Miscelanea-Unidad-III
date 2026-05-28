import numpy as np

# =========================================================================
# CLASE PADRE: ENCAPSULA LOS VECTORES DE DATOS
# =========================================================================
class AnalisisNumerico:
    def __init__(self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        # Distancia h basada en los primeros puntos equidistantes
        self.h = self.x[1] - self.x[0] if len(self.x) > 1 else 0.0

# =========================================================================
# 1.1 CLASE HIJA: DERIVACIÓN NUMÉRICA POO
# =========================================================================
class Derivador(AnalisisNumerico):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def procesar_derivadas(self):
        n = len(self.x)
        derivadas_calculadas = np.zeros(n)
        
        for i in range(n):
            if i == 0:
               
                derivadas_calculadas[i] = (self.y[i+1] - self.y[i]) / self.h
            elif i == n - 1:
               
                derivadas_calculadas[i] = (self.y[i] - self.y[i-1]) / self.h
            else:
               
                derivadas_calculadas[i] = (self.y[i+1] - self.y[i-1]) / (2 * self.h)
                
        return derivadas_calculadas

# =========================================================================
# 1.2 CLASE HIJA: INTEGRACIÓN NUMÉRICA POO
# =========================================================================
class Integrador(AnalisisNumerico):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def ejecutar_trapecio(self):
        # Fórmula del Trapecio Compuesto
        suma_interior = sum(self.y[1:-1])
        return (self.h / 2) * (self.y[0] + 2 * suma_interior + self.y[-1])
        
    def ejecutar_simpson_13(self):
        
        if len(self.y) % 2 == 0:
            return "No aplica: Requiere número impar de puntos."
        suma_impares = sum(self.y[1:-1:2])
        suma_pares = sum(self.y[2:-1:2])
        return (self.h / 3) * (self.y[0] + 4 * suma_impares + 2 * suma_pares + self.y[-1])
        
    def ejecutar_simpson_38(self):
        
        puntos_validos = self.y[:4] 
        resultado = puntos_validos[0] + puntos_validos[-1] + 3 * puntos_validos[1] + 3 * puntos_validos[2]
        return resultado * (3 * self.h / 8)

# =========================================================================
# EVALUACIÓN DE LAS TABLAS DE LA MISCELÁNEA
# =========================================================================
if __name__ == "__main__":
    # Conjunto de datos extraído del PDF institucional (Págs. 1 y 2)
    puntos_x = [0.4, 0.5, 0.6, 0.7, 0.8]
    puntos_y = [1.45, 2.57, 3.71, 4.88, 6.12]
    
    print("=========================================================")
    print("  RESULTADOS: DERIVACIÓN NUMÉRICA POO ")
    print("=========================================================")
    objeto_derivador = Derivador(puntos_x, puntos_y)
    resultados_dy = objeto_derivador.procesar_derivadas()
    
    for i in range(len(puntos_x)):
        print(f"x = {puntos_x[i]} | f(x) = {puntos_y[i]} | f'(x) aprox = {resultados_dy[i]:.4f}")
        
    print("\n=========================================================")
    print("  RESULTADOS: INTEGRACIÓN NUMÉRICA POO ")
    print("=========================================================")
    objeto_integrador = Integrador(puntos_x, puntos_y)
    
    print(f"Aproximación por Trapecio: {objeto_integrador.ejecutar_trapecio():.4f}")
    print(f"Aproximación por Simpson 1/3: {objeto_integrador.ejecutar_simpson_13():.4f}")
    print(f"Aproximación por Simpson 3/8 (Primeros 3 int.): {objeto_integrador.ejecutar_simpson_38():.4f}")
    print("=========================================================")