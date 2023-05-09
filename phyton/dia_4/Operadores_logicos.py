

# mi_bool = 4 < 5 and 5 > 6
# mi_bool = 4 < 5 or 5 > 6

# text = "esta frase es breve"

# mi_bool = 'breve' in text and ('frase' in text)
# mi_bool = 'breve' in text and ('python' in text)
# mi_bool = 'breve' in text or ('python' in text)

# mi_bool = not ('a' == 'a')


# print(mi_bool)

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not ((palabra1 in frase) and (palabra2 in frase) )

print(mi_bool)