import json

print("""
Listeyi Görmek --> Listeyi Göster
Görev Eklemek --> Görev ekle
Görev Silmek --> Görev sil
Tamamlanan Görevler --> Tamamlandı
Görevi Geri Almak --> Geri al
Görev Düzenleme --> Görev düzenle      
Görev İstatistikleri --> İstatistik      
Programı Kapatmak --> kapat      
""")

def yukle():
    try:
        with open("todo_list.json", "r", encoding= "utf-8") as dosya:
            veri = json.load(dosya)
            return veri
    except:
        return []

def kaydet(tasks):
    with open("todo_list.json", "w", encoding= "utf-8") as dosya:
        json.dump(tasks, dosya, indent=4, ensure_ascii=False)

def Listeyi_yazdir(tasks):
    if not tasks:
        print("Liste Boş")
    else:
        print("Güncel Görevler")
        for i, task in enumerate(tasks, start=1):
            if task["done"]:
                durum = "[x]"
            else:
                durum = "[ ]"

            print(f"{i} - {durum} - {task['task']}")

def durumu_degistir(yeni_durum):
   if not tasks:
      print("Liste Boş")
      return[]
   try:
     Listeyi_yazdir(tasks)
     girdi = int(input("Sayı gir: "))
     ind = girdi - 1
     if tasks[ind]["done"] == yeni_durum:
            print("Görev Zaten Tamamlanmış.")
     tasks[ind]["done"] = yeni_durum
     kaydet(tasks)
     Listeyi_yazdir(tasks)
   except IndexError:
       print("Geçersiz Görev Numarası.")
   except ValueError:
       print("Geçersiz Değer.")

tasks = yukle()
Listeyi_yazdir(tasks)

while True:
    user_input = str(input("Sen: ")).strip()
    if user_input == "kapat":
        break
    
    elif user_input == "Görev ekle":
        task = str(input("Görev giriniz: ")).strip()
        tasks.append({
            "task": task,
            "done": False
        })
        kaydet(tasks)
        Listeyi_yazdir(tasks)

    elif user_input == "Listeyi Göster":
        Listeyi_yazdir(tasks)

    elif user_input == "Görev sil":
        if not tasks:
            print("Silinecek Görev Yok.")
            continue
        Listeyi_yazdir(tasks)
        try:
            index = int(input("Silinecek Görev Numarasını Giriniz: "))
            tasks.pop(index - 1)
            kaydet(tasks)
            Listeyi_yazdir(tasks)
        except IndexError:
         print("Geçersiz görev numarası.")
        except ValueError:
         print("Geçersiz değer")
    
    elif user_input == "İstatistik":
        tamamlanan = 0
        toplam = len(tasks)
        if not tasks:
            print("Liste boş.")
            continue
        for task in (tasks):
            if task["done"] == True:
                tamamlanan += 1
        bekleyen = toplam - tamamlanan
        oran = tamamlanan / toplam * 100
        print(f"Toplam Görev: {toplam}")
        print(f"Tamamlanan Görev: {tamamlanan}")
        print(f"Bekleyen Görev: {bekleyen}")
        print(f"Görev Oranı: %{int(oran)}")

    elif user_input == "Görev düzenle":
        if not tasks:
            print("Liste boş.")
            continue
        Listeyi_yazdir(tasks)
        try:
         yazı = int(input("Düzenlenecek Görevin Numarasını Seçin: "))
         Listeyi_yazdir(tasks)
         ini = yazı - 1
         yeni_gorev = str(input("Yeni Görev: "))
         tasks[ini]["task"] = yeni_gorev
         kaydet(tasks)
         Listeyi_yazdir(tasks)
        except ValueError:
            print("Geçersiz Değer.")           
        except IndexError:
         print("Geçersiz Görev Numarası.")
    
    elif user_input == "Tamamlandı":
        durumu_degistir(True)
        
    elif user_input == "Geri al":
        durumu_degistir(False)        