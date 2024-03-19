# Análisis de Datos - Encuestas
## Descripción:

Este código utiliza la biblioteca Pandas para realizar un análisis de datos sobre un conjunto de datos de encuestas. Se generan tres gráficos y se calculan estadísticas descriptivas para las columnas numéricas del DataFrame.

## Librerías:

Pandas
Matplotlib
## Instalación:
Instalar virtualenv -> pip install virtualenv
Crear entorno -> python -m venv venv 
Seleccionar entorno virtual
Instalar dependencias-> pip install -r requirements.txt
Correr programa asignación.py

## Archivos:

surveys.csv: archivo CSV con los datos de las encuestas
## Análisis:

1 Distribución del peso:

Se crea un histograma para visualizar la distribución del peso.
Se observa una distribución unimodal con un ligero sesgo a la derecha.
2 Distribución de la longitud del pie:

Se crea un histograma para visualizar la distribución de la longitud del pie.
Se observa una distribución normal con la mayoría de los valores en el rango medio.
3 Distribución del peso por año:

Se crea un gráfico de dispersión para mostrar la distribución del peso por año.
No se observa una tendencia clara entre el peso y el año.
## Estadísticas:

Se calculan las estadísticas descriptivas de las columnas numéricas del DataFrame:
Media
Mediana
Desviación estándar
Mínimo
Máximo
Rango
Percentiles 25%, 50% y 75%
Resultados:

Los resultados del análisis se presentan en forma de gráficos y tablas. Los gráficos permiten visualizar la distribución de las variables y las estadísticas descriptivas proporcionan información numérica sobre las mismas.

## Limitaciones:

El conjunto de datos puede no ser representativo de la población general.
Hay un valor fuera de rango para el día en alguna de las filas.
### Próximos pasos:

Se puede realizar un análisis más profundo de los datos, como:
Análisis de la relación entre las variables.
Identificación de grupos o patrones en los datos.
Predicción de variables futuras.


