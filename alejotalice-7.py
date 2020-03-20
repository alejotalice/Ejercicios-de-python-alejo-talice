horas = float(input("Introduce tus horas de trabajo "))
costo = float(input("Introduce lo que cobras por hora "))
paga = round(horas * costo, 3)


print("Tu sueldo es " + str(paga))
