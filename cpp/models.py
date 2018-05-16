from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class Series(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series_name = models.CharField(max_length=200)

    def __str__(self):
        return self.series_name


class Model(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name


class Location(models.Model):
    city = models.CharField(max_length=200)


class FuelType(models.Model):
    fuel = models.CharField(max_length=200)


class GearType(models.Model):
    gear = models.CharField(max_length=200)


class CaseType(models.Model):
    case_type = models.CharField(max_length=200)


class OwnerType(models.Model):
    owner_type = models.CharField(max_length=100)


class ExchangeStatus(models.Model):
    owner_type = models.CharField(max_length=100)


class Color(models.Model):
    color = models.CharField(max_length=50)


class RepairStatus(models.Model):
    color = models.CharField(max_length=50)


'''
'Fiyat', 
'Yer', 
'Ilan Tarihi'
'Marka'
'Seri'
'Model'
'Yil'
'Yakit'
'Vites'
'KM'
'Kasa Tipi'
'Motor Gucu'
'Motor Hacmi'
'Renk'
'Garanti' -------> False
'Hasar Durumu'
'Kimden' -------> Sahibinden
'Takas',
'Durumu',
 
 'ABC',
 'ABS',
 'EBP',
 'ASR',
 'ESP / VSA',
 'Airmatic',
 'EDL', 'EBA',
 'EBD', 'TCS',
 'BAS', 'Distronic',
 'Yokuş Kalkış Desteği', 
 'Gece Görüş', 
 'Şeritten Ayrılma İkazı', 
 'Şerit Değiştirme Yardımcısı', 
 'Hava Yastığı (Sürücü)',
 'Hava Yastığı (Yolcu)', 
 'Hava Yastığı (Yan)', 
 'Hava Yastığı (Diz)', 
      'Hava Yastığı (Perde)', 
      'Hava Yastığı (Tavan)', 
      'Kör Nokta Uyarı Sistemi', 
      'Lastik Arıza Göstergesi', 
      'Yorgunluk Tespit Sistemi', 
      'Isofix', 'Alarm', 
      'Merkezi Kilit', 
      'Immobilizer', 
      'Deri Koltuk', 
      'Kumaş Koltuk', 
      'Deri / Kumaş Koltuk', 
      'Elektrikli Ön Camlar', 
      'Elektrikli Arka Camlar', 
      'Klima (Analog)', 
      'Klima (Dijital)', 
      'Otm.Kararan Dikiz Aynası', 
      'Ön Kol Dayama', 
      'Arka Kol Dayama', 
      'Anahtarsız Giriş ve Çalıştırma', 
      '6 İleri Vites', 
      '7 İleri Vites', 
      'Hidrolik Direksiyon', 
      'Fonksiyonel Direksiyon', 
      'Ayarlanabilir Direksiyon', 
      'Deri Direksiyon', 
      'Ahşap Direksiyon', 
      'Isıtmalı Direksiyon', 
      'Koltuklar (Elektrikli)', 
      'Koltuklar (Hafızalı)', 
      'Koltuklar (Katlanır)', 
      'Koltuklar (Ön Isıtmalı)', 
      'Koltuklar (Arka Isıtmalı)',
      'Koltuklar (Soğutmalı)', 
      'Hız Sabitleyici',
      'Adaptive Cruise Control',
      'Soğutmalı Torpido', 
      'Yol Bilgisayarı', 
      'Krom Kaplama', 'Ahşap Kaplama', 
      'Head-up Display', 'Start / Stop',
      'Geri Görüş Kamerası', 'Ön Görüş Kamerası',
      '3. Sıra Koltuk', 'Hardtop', 'Far (LED)', 'Far (Halojen)', 'Far (Xenon)', 'Far (Bi Xenon)', 'Far (Sis)', 'Far (Adaptif)', 'Far Gece Sensörü', 'Far Yıkama', 'Aynalar (Elektrikli)', 'Aynalar (Otom.Katlanır)', 'Aynalar (Isıtmalı)', 'Aynalar (Hafızalı)', 'Park Sensörü (Arka)', 'Park Sensörü (Ön)', 'Alaşımlı Jant', 'Sunroof', 'Panoramik Cam Tavan', 'Yağmur Sensörü', 'Arka Cam Buz Çözücü', 'Panoramik Ön Cam', 'Romörk Çeki Demiri', 'Akıllı Bagaj Kapağı', 'Radyo - Kasetçalar', 'Radyo - CD Çalar', 'Radyo - MP3 Çalar', 'TV-Navigasyon', 'Bluetooth - Telefon', 'USB / AUX', 'AUX', 'iPod Bağlantısı', '6+ Hoparlör', 'CD Değiştirici', 'Arka Eğlence Paketi', 'DVD Değiştirici', '\n']
'''


class CarProperties(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)

    # Car Properties
    year = models.IntegerField(null=False)
    power = models.IntegerField(null=False)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True)
    gear_type = models.ForeignKey(GearType, on_delete=models.SET_NULL, null=True)
    case_type = models.ForeignKey(CaseType, on_delete=models.SET_NULL, null=True)
    owner_type = models.ForeignKey(OwnerType, on_delete=models.SET_NULL, null=True)
    exchange_status = models.ForeignKey(ExchangeStatus, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    repair_status = models.ForeignKey(RepairStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.brand) + "-" + str(self.series)
