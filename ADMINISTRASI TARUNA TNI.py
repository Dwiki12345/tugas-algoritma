nama = (input('masukan nama:'))
umur = int(input('masukan umur:'))
berat_badan = int(input('masukan berat badan:'))
tinggi_badan = int(input('masukan tinggi badan:'))
nilai_ujian = bool(input('masukan nilai ujian:'))

hasil = "SELAMAT ANDA LOLOS ADMINISTRASI TARUNA TNI" if (umur >=17 
         and berat_badan >=60
           and tinggi_badan >= 160
             and nilai_ujian >=70) else "MOHON MAAF ANDA TIDAK LOLOS ADMINISTRASI TARUNA TNI"
print(hasil)