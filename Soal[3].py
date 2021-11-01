ujian_teori = input("Berapa Nilai Ujian Teori Anda ? ")
ujian_praktek = input("Berapa Nilai Ujian Praktek Anda ? ")
if int(ujian_teori) >= 70 and int(ujian_praktek) >=70:
    print("Selamat, anda lulus!")
elif int(ujian_teori)>=70 and int(ujian_praktek)<70:
    print("Anda harus mengulang ujian praktek")
elif int(ujian_teori)<70 and int(ujian_praktek)>=70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")
