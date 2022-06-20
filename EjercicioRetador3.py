cementoKg = 40
yesoKg = 30
capacidadMaximaKg = 3254
cantCemento = int(input ("Número de costales de cemento (kg): "))
cantYeso = int(input ("Número de costales de yeso (kg): "))
totalCementoKg = cantCemento*cementoKg
totalYesoKg = cantYeso*yesoKg
pesoTotalKg = totalCementoKg + totalYesoKg
print ("El peso total en kg es: ", pesoTotalKg, " kg")
SiNo = pesoTotalKg>=(capacidadMaximaKg/2) and pesoTotalKg<=capacidadMaximaKg
print ("¿Se puede realizar el envío?: ", SiNo)