# -*- coding: utf-8 -*-
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

    #Car Properties
    year = models.IntegerField(null=False)
    power = models.IntegerField(null=False)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True)
    gear_type = models.ForeignKey(GearType, on_delete=models.SET_NULL, null=True)
    case_type = models.ForeignKey(CaseType, on_delete=models.SET_NULL, null=True)
    owner_type = models.ForeignKey(OwnerType, on_delete=models.SET_NULL, null=True)
    exchange_status = models.ForeignKey(ExchangeStatus, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    repair_status = models.ForeignKey(RepairStatus, on_delete=models.SET_NULL, null=True)
    #Detail inputs
    #Security
    abc = models.IntegerField(null=False,default=2)
    abs = models.IntegerField(null=False,default=2)
    ebp = models.IntegerField(null=False,default=2)
    asr = models.IntegerField(null=False,default=2)
    esp_or_vsa = models.IntegerField(null=False,default=2)
    airmatic = models.IntegerField(null=False,default=2)
    edl = models.IntegerField(null=False,default=2)
    eba = models.IntegerField(null=False,default=2)
    ebd = models.IntegerField(null=False,default=2)
    tcs = models.IntegerField(null=False,default=2)
    bas = models.IntegerField(null=False,default=2)
    distronic = models.IntegerField(null=False,default=2)
    hill_start_assist = models.IntegerField(null=False,default=2)
    night_vision = models.IntegerField(null=False,default=2)
    lane_departure_warning = models.IntegerField(null=False,default=2)
    lane_change_assist = models.IntegerField(null=False,default=2)
    airbag_driver = models.IntegerField(null=False,default=2)
    airbag_passenger = models.IntegerField(null=False,default=2)
    airbag_side = models.IntegerField(null=False,default=2)
    airbag_knee = models.IntegerField(null=False,default=2)
    airbag_curtain = models.IntegerField(null=False,default=2)
    airbag_roof = models.IntegerField(null=False,default=2)
    blind_spot_warning = models.IntegerField(null=False,default=2)
    tire_defect_indicator = models.IntegerField(null=False,default=2)
    fatigue_detection = models.IntegerField(null=False,default=2)
    isofix = models.IntegerField(null=False,default=2)
    alarm = models.IntegerField(null=False,default=2)
    central_lock = models.IntegerField(null=False,default=2)
    immobilizer = models.IntegerField(null=False,default=2)
    #Interior equipments
    leather_seat = models.IntegerField(null=False,default=2)
    fabric_seat = models.IntegerField(null=False,default=2)
    leather_or_fabric_seat = models.IntegerField(null=False,default=2)
    electric_windscreen = models.IntegerField(null=False,default=2)#?
    electric_rear_window = models.IntegerField(null=False,default=2)
    air_conditioning_analogue = models.IntegerField(null=False,default=2)
    air_conditioning_digital = models.IntegerField(null=False,default=2)
    auto_dimming_rearview_windows = models.IntegerField(null=False,default=2)
    front_armrest = models.IntegerField(null=False,default=2)
    rear_armrest = models.IntegerField(null=False,default=2)
    keyless_entry_and_run = models.IntegerField(null=False,default=2)
    six_forward_gear = models.IntegerField(null=False,default=2)
    seven_forward_gear = models.IntegerField(null=False,default=2)
    hydrolic_steering_wheel = models.IntegerField(null=False,default=2)
    functional_steering_wheel = models.IntegerField(null=False,default=2)
    adjustable_steering_wheel = models.IntegerField(null=False,default=2)
    leather_steering_wheel = models.IntegerField(null=False,default=2)
    wooden_steering_wheel = models.IntegerField(null=False,default=2)
    heated_steering_wheel = models.IntegerField(null=False,default=2)
    power_seat = models.IntegerField(null=False,default=2)
    memory_seat = models.IntegerField(null=False,default=2)
    folding_seat = models.IntegerField(null=False,default=2)
    front_heated_seat = models.IntegerField(null=False,default=2)
    rear_heated_seat = models.IntegerField(null=False,default=2)
    cooled_seat = models.IntegerField(null=False,default=2)
    cruise_control = models.IntegerField(null=False,default=2)
    adaptive_cruise_control = models.IntegerField(null=False,default=2)
    cooled_torpedo = models.IntegerField(null=False,default=2)
    trip_computer = models.IntegerField(null=False,default=2)
    chrome_plate = models.IntegerField(null=False,default=2)
    wooden_plate = models.IntegerField(null=False,default=2)
    head_up_display = models.IntegerField(null=False,default=2)
    start_stop = models.IntegerField(null=False,default=2)
    backup_camera = models.IntegerField(null=False,default=2)#?
    front_view_camera = models.IntegerField(null=False,default=2)
    third_row_seat = models.IntegerField(null=False,default=2)
    #External equipment
    hardtop = models.IntegerField(null=False,default=2)
    led_headlight = models.IntegerField(null=False,default=2)
    halogen_headlight = models.IntegerField(null=False,default=2)
    xenon_headlight = models.IntegerField(null=False,default=2)
    bi_xenon_headlight = models.IntegerField(null=False,default=2)
    fog_headlight = models.IntegerField(null=False,default=2)
    adaptive_headlight = models.IntegerField(null=False,default=2)
    night_sensor_headlight = models.IntegerField(null=False,default=2)
    washing_headlight = models.IntegerField(null=False,default=2)
    electric_mirror = models.IntegerField(null=False,default=2)
    automatic_folding_mirror = models.IntegerField(null=False,default=2)
    heated_mirror = models.IntegerField(null=False,default=2)
    memory_mirror = models.IntegerField(null=False,default=2)
    rear_parking_sensor = models.IntegerField(null=False,default=2)
    front_parking_sensor = models.IntegerField(null=False,default=2)
    allow_wheel = models.IntegerField(null=False,default=2)
    sunroof = models.IntegerField(null=False,default=2)
    panoramic_sunroof = models.IntegerField(null=False,default=2)
    rain_sensor = models.IntegerField(null=False,default=2)
    rear_window_defroster = models.IntegerField(null=False,default=2)
    panoramic_windscreen = models.IntegerField(null=False,default=2)
    trailer_tow_bar = models.IntegerField(null=False,default=2)
    smart_luggage_cover = models.IntegerField(null=False,default=2)
    #Multimedia
    radio_tape_recorder = models.IntegerField(null=False,default=2)
    radio_cd_player = models.IntegerField(null=False,default=2)
    radio_mp3_player = models.IntegerField(null=False,default=2)
    tv_or_navigation = models.IntegerField(null=False,default=2)
    bluetooth_or_phone = models.IntegerField(null=False,default=2)
    usb_or_aux = models.IntegerField(null=False,default=2)
    #aux?
    ipod_connection = models.IntegerField(null=False,default=2)
    six_plus_speaker = models.IntegerField(null=False,default=2)
    cd_changer = models.IntegerField(null=False,default=2)
    rear_entertainment_package = models.IntegerField(null=False,default=2)
    dvd_changer = models.IntegerField(null=False,default=2)

    def __str__(self):
        return str(self.brand) + "-" + str(self.series)
