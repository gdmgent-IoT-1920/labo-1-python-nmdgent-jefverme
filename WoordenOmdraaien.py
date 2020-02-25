zin = input("geef een zin op: ")

zinOut = zin.split(" ")

zinOut.reverse()

print("De zin omgedraaid: ")
for x in range(len(zinOut)):
  print(zinOut[x], end = ' ')