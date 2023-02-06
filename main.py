# applikasi kalkulator sederhana

from src.perhitungan import hitung 
import os
import numpy as np
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
        print("-> *")
        print("-> /")
        print("-> %")
        opr = input("Masukan opr : ")
        h = hitung(a,b,opr)
        if h.opr == "+" :
            print("hasil adalah : {}".format(h.tambah()) )
        elif h.opr == "-" :
            print("hasil adalah : {}".format(h.kurang()) )
        elif h.opr == "*":
            print("hasil adalah : {}".format(h.kali()) )
        elif h.opr == "/":
            print("hasil adalah : {}".format(h.bagi()) )
        elif h.opr == "%":
            print("hasil adalah : {}".format(h.modulus()) )
    except:
        print("data ada yang salah")
# selesai
