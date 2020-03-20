peso = input("Cuál es tu peso? ")
altura = input("Cuanto mides ")
bmi = round(float(peso)/float(altura)**2,2)


print("Tu índice de masa corporal es " + str(bmi))
