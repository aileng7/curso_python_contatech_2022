capital = float(input("¿Cantidad a invertir? "))
percentage = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
profit = round(capital * (percentage / 100 + 1) ** years, 2)
print(f"Capital final: {profit}")
