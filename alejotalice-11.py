inversion = float(input("cuanto va a invertir? "))
interes = float(input("Interés anual? "))
años = int(input("años?"))
print("Capital final: " + str(round(inversion * (interes / 100 + 1) ** años, 2)))
