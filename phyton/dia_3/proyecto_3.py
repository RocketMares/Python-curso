
print("Proyecto 3. Analisis de texto")
text = input("Ingresa un texto: ")
letras = input("Ingresa 3 letras de tu eleccion: ")
x,y,z= letras.lower()
conteo = len(text)
con = str(conteo)

text.lower()
conteoX= text.count(x)
conteoY= text.count(y)
conteoZ= text.count(z)


print("El numero de letras que hay en esta cadena de texto es: "+con)
print("Las letras son:"+x+", "+y+", "+z)

print("El contro de la primera letra elegida en el texto es: "+x+"("+str(conteoX) +")")
print("El contro de la segunda letra elegida en el texto es: "+y+"("+str(conteoY) +")")
print("El contro de la tercera letra elegida en el texto es: "+z+"("+str(conteoZ) +")")
texto_altrer =text[::-1]
print("La primera letra del texto es: "+text[0])
print("La ultima letra es: "+texto_altrer[0])
