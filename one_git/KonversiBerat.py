def KonversiBerat():
  weight = int(input("Masukkan Berat > "))
  types = input("Kg(K) atau Lbs(L) > ")

  if types.upper() == "K":
    print(weight * 2.2046, "pounds")

  elif types.upper() == "L":
    print(weight * 0.454, "kilos")