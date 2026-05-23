# Importamos las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Leemos el archivo CSV con las ventas
ventas = pd.read_csv("datos/ventas.csv")

# Creamos una nueva columna llamada total
# Multiplicamos cantidad por precio
ventas["total"] = ventas["cantidad"] * ventas["precio"]

# Calculamos cuánto se vendió en total
ventas_totales = ventas["total"].sum()

# Mostramos el total de ventas
print("Ventas totales:", ventas_totales)

# Agrupamos por producto y sumamos cantidades
producto_mas_vendido = ventas.groupby("producto")["cantidad"].sum()

# Mostramos cuánto se vendió de cada producto
print("\nCantidad vendida por producto:")
print(producto_mas_vendido)

# Convertimos la fecha a formato fecha
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

# Creamos una columna nueva con el número del mes
ventas["mes"] = ventas["fecha"].dt.month

# Sumamos las ventas según el mes
ventas_por_mes = ventas.groupby("mes")["total"].sum()

# Mostramos las ventas por mes
print("\nVentas por mes:")
print(ventas_por_mes)

# Creamos un gráfico de barras
ventas_por_mes.plot(kind="bar")

# Título del gráfico
plt.title("Ventas por mes")

# Nombre de los ejes
plt.xlabel("Mes")
plt.ylabel("Ventas")

# Ajustamos el diseño
plt.tight_layout()

# Guardamos el gráfico en la carpeta resultados
plt.savefig("resultados/grafico_ventas.png")

# Mostramos el gráfico en pantalla
plt.show()