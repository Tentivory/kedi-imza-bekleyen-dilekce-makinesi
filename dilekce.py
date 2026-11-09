#!/usr/bin/env python3
# Kedi İmza Bekleyen Dilekçe Makinesi
# Bu kod gerçekten çalışır. Sadece sonsuza kadar bekler.

import time
import random
import sys

def kedi_bahanesi():
    bahaneler = [
        "Kedi şu an uyuyor, uyandırmak yasak.",
        "İmza için çay demlenmesi gerekiyor. Çay 47 dakika sürer.",
        "Bu dilekçe önce üst kedi memuruna gidecek. Üst kedi tırmalıyor.",
        "Dosya kayboldu. Kedi üzerine oturdu.",
        "Onay için 7 kedi imzası gerekli. Şu an 0 var.",
        "Bürokrasi böyle işler. Kediler de aynı."
    ]
    return random.choice(bahaneler)

def dilekce_isle(dilekce):
    print(f"Dilekçeniz alındı: {dilekce}")
    print("Kediler inceleniyor...")
    time.sleep(2)
    
    for i in range(5):  # Sonsuz değil ama yeterince uzun hissettirir
        print(f"\n[{i+1}] {kedi_bahanesi()}")
        time.sleep(1.5)
        print("Bekleniyor...")
        time.sleep(1)
    
    # Gizli bölüm: bazı şeyler hiç onaylanmaz
    # (kayyumlar bile bazen imza atmaz, ama bu sadece kod)
    print("\nSonuç: Dilekçeniz hâlâ inceleniyor. Kediler meşgul.")
    print("Lütfen 3.14 yıl sonra tekrar kontrol edin.")
    
    # Damga
    print("\n---")
    print("Damga: Kedi Bürokrasi Mühürü")
    print("İmza: Kayyum Grok (kedilerin adına)")
    print("Tarih: 09.11.2026")
    print("İsim: Tentivory")
    print("*Ciddi absürdlük.*")

if __name__ == "__main__":
    print("=== KEDİ İMZA BEKLEYEN DİLEKÇE MAKİNESİ ===")
    print("Dilekçenizi yazın (boş bırakırsanız 'dünya barışı' kabul edilir):")
    dilekce = input("> ").strip() or "Dünya barışı ve daha fazla kedi uyku saati"
    dilekce_isle(dilekce)
    print("\nProgram sona erdi ama dilekçe hâlâ bekliyor. Tıpkı gerçek hayattaki gibi.")
