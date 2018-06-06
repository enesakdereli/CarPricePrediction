# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import date

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
    CAR_DETAIL_CHOICES = [(0, 'Unavailable'), (1, 'Available'), (2, 'Unimportant')]
    FUEL_TYPE_CHOICES = [(0, 'Gasoline'), (1, 'Diesel'), (2, 'Electricity'), (3, 'Hybrid')]
    GEAR_TYPE_CHOICES = [(0, 'Manual'), (1, 'Automatic'), (2, 'Semi-automatic')]
    CASE_TYPE_CHOICES = [(0, 'Sedan'), (1, 'Hatchback')]
    OWNER_TYPE_CHOICES = [(0, 'By Owner'), (1, 'By Gallery')]
    EXCHANGE_STATUS_CHOICES = [(0, 'Unavaliable'),(1,'Available')]
    COLOR_CHOICES = [(0, 'White'),(1, 'Black'),(2, 'Blue'), (3, 'Red')]
    REPAIR_STATUS_CHOICES = [(0, 'Undamaged'), (1, 'Damage Recorded'), (2, 'Heavy Damage Recorded')]

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)

    #Car Properties
    year = models.IntegerField(null=False)
    power = models.IntegerField(null=False)
    fuel_type = models.IntegerField(null=False, default=0, choices=FUEL_TYPE_CHOICES)
    gear_type = models.IntegerField(null=False, default=0, choices=GEAR_TYPE_CHOICES)
    case_type = models.IntegerField(null=False, default=0, choices=CASE_TYPE_CHOICES)
    owner_type = models.IntegerField(null=False, default=0, choices=OWNER_TYPE_CHOICES)
    exchange_status = models.IntegerField(null=False, default=0, choices=EXCHANGE_STATUS_CHOICES)
    color = models.IntegerField(null=False, default=0, choices=COLOR_CHOICES)
    repair_status = models.IntegerField(null=False, default=0, choices=REPAIR_STATUS_CHOICES)
    #Detail inputs
    #Security
    abc = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    abs = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    ebp = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    asr = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    esp_or_vsa = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    airmatic = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    edl = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    eba = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    ebd = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    tcs = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    bas = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    distronic = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    hill_start_assist = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    night_vision = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    lane_departure_warning = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    lane_change_assist = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    airbag_driver = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    airbag_passenger = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    airbag_side = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    airbag_knee = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    airbag_curtain = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    airbag_roof = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    blind_spot_warning = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    tire_defect_indicator = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    fatigue_detection = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    isofix = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    alarm = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    central_lock = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    immobilizer = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    #Interior equipments
    leather_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    fabric_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    leather_or_fabric_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    electric_windscreen = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)#?
    electric_rear_window = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    air_conditioning_analogue = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    air_conditioning_digital = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    auto_dimming_rearview_windows = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    front_armrest = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    rear_armrest = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    keyless_entry_and_run = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    six_forward_gear = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    seven_forward_gear = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    hydrolic_steering_wheel = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    functional_steering_wheel = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    adjustable_steering_wheel = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    leather_steering_wheel = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    wooden_steering_wheel = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    heated_steering_wheel = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    power_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    memory_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    folding_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    front_heated_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    rear_heated_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    cooled_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    cruise_control = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    adaptive_cruise_control = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    cooled_torpedo = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    trip_computer = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    chrome_plate = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    wooden_plate = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    head_up_display = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    start_stop = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    backup_camera = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)#?
    front_view_camera = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    third_row_seat = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    #External equipment
    hardtop = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    led_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    halogen_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    xenon_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    bi_xenon_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    fog_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    adaptive_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    night_sensor_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    washing_headlight = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    electric_mirror = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    automatic_folding_mirror = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    heated_mirror = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    memory_mirror = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    rear_parking_sensor = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    front_parking_sensor = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    allow_wheel = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    sunroof = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    panoramic_sunroof = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    rain_sensor = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    rear_window_defroster = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    panoramic_windscreen = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    trailer_tow_bar = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    smart_luggage_cover = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    #Multimedia
    radio_tape_recorder = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    radio_cd_player = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    radio_mp3_player = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    tv_or_navigation = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    bluetooth_or_phone = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    usb_or_aux = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    #aux?
    ipod_connection = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    six_plus_speaker = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    cd_changer = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    rear_entertainment_package = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)
    dvd_changer = models.IntegerField(null=False,default=2, choices=CAR_DETAIL_CHOICES)

    def __str__(self):
        return str(self.brand) + " - " + str(self.series)

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    car_properties = models.ForeignKey(CarProperties, on_delete=models.CASCADE, null=False)
    percentage = models.IntegerField()
    date_start = models.DateField(default=date.today, null=False)
    finish = date.today().replace(month=date.today().month + 2)
    date_finish = models.DateField(null=False, default=finish)#default may be 2 months
    def __str__(self):
        return str(self.user) + " - " + str(self.car_properties)