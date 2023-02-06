# applikasi kalkulator sederhana

from src.perhitungan import hitung 
import os
os.system('cls')

if __name__ == "__main__":
    print("Applikasi kalkulator CLI")
    print("")
    try:
        a = int(input("Masukan Nilai a : "))
        b = int(input("Masukan Nilai b : "))
        print("pilih opr ")
        print("-> +")
        print("-> -")
        opr = input("Masukan opr : ")
        h = hitung(a,b,opr)
        if h.opr == "+" :
            print("hasil adalah : {}".format(h.tambah()) )
    except:
        print("data ada yang salah")
