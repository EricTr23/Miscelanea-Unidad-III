import pandas as pd
import numpy as np


df = pd.read_csv('datos.csv')
print("--- Primeras filas del conjunto de datos ---")
print(df.head())


h_valor = df['x'].iloc[1] - df['x'].iloc[0]
df['h'] = h_valor


df['derivada_adelante'] = np.nan
df['derivada_atras'] = np.nan
df['derivada_central'] = np.nan

n = len(df)


for i in range(n):

    if i < n - 1:
        df.loc[i, 'derivada_adelante'] = (df.loc[i+1, 'f(x)'] - df.loc[i, 'f(x)']) / h_valor
        

    if i > 0:
        df.loc[i, 'derivada_atras'] = (df.loc[i, 'f(x)'] - df.loc[i-1, 'f(x)']) / h_valor
        

    if 0 < i < n - 1:
        df.loc[i, 'derivada_central'] = (df.loc[i+1, 'f(x)'] - df.loc[i-1, 'f(x)']) / (2 * h_valor)

print("\n--- DataFrame con Derivadas Calculadas ---")
print(df)



x_arr = df['x'].to_numpy()
y_arr = df['f(x)'].to_numpy()

# --- Método del Trapecio ---
def integrar_trapecio(x, y, h):
    suma_intermedia = sum(y[1:-1])
    return (h / 2) * (y[0] + 2 * suma_intermedia + y[-1])

# --- Método de Simpson 1/3 Compuesto ---

def integrar_simpson13(x, y, h):
    y_s = y[:11]
    suma_impares = sum(y_s[1:-1:2])
    suma_pares = sum(y_s[2:-1:2])
    return (h / 3) * (y_s[0] + 4 * suma_impares + 2 * suma_pares + y_s[-1])

# --- Método de Simpson 3/8 Compuesto ---

def integrar_simpson38(x, y, h):
    y_s = y[:10]
    integral = y_s[0] + y_s[-1]
    for i in range(1, len(y_s) - 1):
        if i % 3 == 0:
            integral += 2 * y_s[i]
        else:
            integral += 3 * y_s[i]
    return integral * (3 * h / 8)


I_trapecio = integrar_trapecio(x_arr, y_arr, h_valor)
I_simpson13 = integrar_simpson13(x_arr, y_arr, h_valor)
I_simpson38 = integrar_simpson38(x_arr, y_arr, h_valor)

print("\n--- Resultados de las Integrales ---")
print(f"Aproximación por Trapecio (Todo el intervalo): {I_trapecio:.5f}")
print(f"Aproximación por Simpson 1/3 (Puntos 0 al 10): {I_simpson13:.5f}")
print(f"Aproximación por Simpson 3/8 (Puntos 0 al 9):  {I_simpson38:.5f}")


df.to_csv('resultados_totales.csv', index=False)
print("\n¡Archivo 'resultados_totales.csv' generado con éxito!")