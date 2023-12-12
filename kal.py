x=input("Zadejte proměnou x: ")
y=input("Zadejte proměnou y: ")

x = int(x)
y = int(y)

print("Zde mate možnoszi")
print(" pro sčitani zadejte +")
print(" pro odečitani zadejte -")
print(" pro děleni zadejte /")
print(" pro nasobeni zadejte *")
print(" pro mocněni zadejte **, x=mocněni a y=mocnitel")
print(" pro odmocněni zadejte /*, x= odmocněnec a y=odmocnitel")

znamenko = input("zadejte vaši volbu operatoru: ")
  
if znamenko == "+":
  print(x+y)
elif znamenko == "-":
  print(x-y)
elif znamenko == "/":
  if y == 0:
    print("nelze dělit nulou")
  else:
    print(x/y)
elif znamenko == "*":
  print(x*y)
elif znamenko == "**":
  print(x**y)
elif znamenko == "/*":
  if y<0:
   print(x**(1/y))


     