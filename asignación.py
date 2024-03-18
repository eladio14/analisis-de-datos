import pandas as pd
import matplotlib.pyplot as plt
# Asignación: realizar 3 análisis con los datos proporcionados usando pandas, generando gráfica en base los datos analizados y estadísticas.
# Análisis realizados.
# Gráfico 1: Se realizó un histograma para visualizar la distribución del peso.
# Gráfico 2: Se creó otro histograma para visualizar la distribución de la longitud del pie.
# Gráfico 3: Se generó un gráfico de dispersión para mostrar la distribución del peso por año.
# Estadísticas Descriptivas: Se calcularon y mostraron las estadísticas descriptivas de las columnas numéricas del DataFrame.

# Cargar el archivo CSV
surveys = pd.read_csv("surveys.csv")

# Mostrar las primeras filas del DataFrame para verificar la carga correcta
print("Primeras filas del DataFrame:")
print(surveys.head())

# Convertir las fechas en una columna "year", manejando errores (porque hay un valor fuera de rango para el día en alguna de las filas.)
surveys["year"] = pd.to_datetime(
    surveys[["year", "month", "day"]], errors="coerce"
).dt.year

# Estadísticas descriptivas
statistics = surveys.describe()

# Gráfico 1: Distribución de peso
plt.figure(figsize=(10, 6))
plt.hist(surveys["weight"].dropna(), bins=20, color="skyblue", edgecolor="black")
plt.title("Distribución de Peso")
plt.xlabel("Peso")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# Gráfico 2: Distribución de longitud del pie
plt.figure(figsize=(10, 6))
plt.hist(
    surveys["hindfoot_length"].dropna(), bins=20, color="lightgreen", edgecolor="black"
)
plt.title("Distribución de Longitud del Pie")
plt.xlabel("Longitud del Pie")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# Gráfico 3: Distribución de peso por año
plt.figure(figsize=(10, 6))
plt.scatter(surveys["year"], surveys["weight"], alpha=0.5)
plt.title("Distribución de Peso por Año")
plt.xlabel("Año")
plt.ylabel("Peso")
plt.grid(True)
plt.show()

# Imprimir estadísticas
print("Estadísticas:")
print(statistics)
