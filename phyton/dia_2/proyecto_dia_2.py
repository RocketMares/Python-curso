

nombre = input("¿Cual es tu nombre? ")

valor_mensual = input("¿Cual es tu ingreso de este mes? ")

comision = round(float(valor_mensual) * 0.13,2)

print(f"{nombre} tú comisión de este mes es del 13% de tus ganancias del mes por lo tanto comisionas: ${comision} pesos MXM")