def Game():
    angka_rahasia = 9
    batas = 3
    penghitung = 0

    while penghitung < batas:
        user = int(input("Masukkan Angka > "))
    
        if user == angka_rahasia:
            print ("Selamat, Angka Rahasia yang Anda Masukkan Benar!")
            break
        else:
            print ("Salah!")
            penghitung += 1

    else:
        print("Angka Rahasia yang Anda Masukkan Salah, Angka Rahasia nya adalah 9")