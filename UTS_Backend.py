# Faturrohman
#1120101898

print("==============================")
print("==== GoKet ====")
print("==============================")
tiketbeli = []
while True:
    pilihan = input('==============================\n====       GoKet     ====\n====       1.Pesawat      ====\n====       2.Kereta Api      ====\n====       3.Kapal        ====\n==============================\n Input Pilihan [1-3]:\n')
    if pilihan == "1":
        print("==============================")
        print("Anda Memilih : Pesawat")
        print("Pilih tiket :")
        pesawat = ["Garuda Indonesia", "Sriwijaya Air Ways", "Lion Air", "Citilink"]
        while True:
            for a in range(0, len(pesawat)):
                print(f'{a + 1}.{pesawat[a]}')
            daftar_pesawat = int(input('Input tiket [1-4]:\n'))
            if daftar_pesawat == 1:
                tiketbeli.append(pesawat[0])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_pesawat == 2:
                tiketbeli.append(pesawat[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_pesawat == 3:
                tiketbeli.append(pesawat[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_pesawat == 4:
                tiketbeli.append(pesawat[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            else:
                print("==============================")
                print("Silahkan pilih dengan benar\n")
                continue
    elif pilihan == "2":
        print("==============================")
        print("Anda Memilih : Kereta Api")
        print("Pilih tiket :")
        kereta = ["Pandanwangi", "Mutiara Timur Siang", "Tawang Alun", "Probowangi"]
        while True:
            for a in range(0, len(kereta)):
                print(f'{a + 1}.{kereta[a]}')
            daftar_kereta = int(input('Input tiket [1-4]:\n'))
            if daftar_kereta == 1:
                tiketbeli.append(kereta[0])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_kereta == 2:
                tiketbeli.append(kereta[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_kereta == 3:
                tiketbeli.append(kereta[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_kereta == 4:
                tiketbeli.append(kereta[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            else:
                print("==============================")
                print("Silahkan pilih dengan benar\n")
                continue
    elif pilihan == "3":
        print("==============================")
        print("Anda Memilih : Kapal")
        print("Pilih tiket :")
        kapal = ["PRATHITA IV", "MUTIS", "GILIMANUK I", "PUTRI SRITANJUNG I "]
        while True :
            for a in range(0, len(kapal)):
                print(f'{a + 1}.{kapal[a]}')
            daftar_kapal = int(input('Input tiket [1-4]:\n'))
            if daftar_kapal == 1:
                tiketbeli.append(kapal[0])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_kapal == 2:
                tiketbeli.append(kapal[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_kapal == 3:
                tiketbeli.append(kapal[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            elif daftar_kapal == 4:
                tiketbeli.append(kapal[1])
                print('=== tiket yang dibeli ===')
                for b in range(0,len(tiketbeli)):
                    print(f'{b + 1}.{tiketbeli[b]} 1x')
                break
            else:
                print("==============================")
                print("Silahkan input dengan benar\n")
                continue
    validasi_tiket = input('Apakah Anda ingin beli tiket lainnya? Y/n\n')
    if validasi_tiket == "Y" or validasi_tiket == "y":
        print("==============================")
        continue
    else:
        print("Tiket akan segera diproses mohon tunggu.....")
        break

