import datetime
import os
import string
import random


mahasiswa_template = {

      "nama":"nama",
      "nim": "00000000",
      "sks_lulus":0,
      "lahir":datetime.datetime(1111,11,1)
}

data_mahasiswa = {}

while True:
      os.system("cls")

      print(f"{'SELMATA DATANG':^20}")
      print(f"{'DATA MAHASISWA TI':^20}")
      print("-"*20)

      mahasiswa = dict.fromkeys(mahasiswa_template.keys())
      mahasiswa["nama"] = input("Masukan Nama : ")
      mahasiswa["nim"] = input("Masukan NIM :")
      mahasiswa["sks_lulus"] = input("Masukan Jumlah SKS : ")
      TAHUN_LAHIR = int(input("Masukan tahun lahir (YYYY) : "))
      BULAN_LAHIR = int(input("Masukan Bulan Lahir (1-12) : "))
      TANGGAL_LAHIR = int(input("Masukan Tanggal Lahir(1-31) : "))
      mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

      KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
      data_mahasiswa.update({KEY:mahasiswa})

      print(f"{'KEY':<6} {'Nama':<17} {'Nim':<8} {'SKS':<10}  {'Tanggal Lahir':<10}")
      print("-"*60)


      for mahasiswa in data_mahasiswa:
                  KEY = mahasiswa
                  NAMA = data_mahasiswa[KEY]["nama"]
                  NIM = data_mahasiswa[KEY]["nim"]
                  SKS = data_mahasiswa[KEY]["sks_lulus"]
                  LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
                  print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:<10}  {LAHIR:^10}")

      print("\n")
      is_Done = input("Apakah sudah selesai (y/n)? ")
      if is_Done == "n":
                   break

print("\nAkhir dari Program, Terima kasih")