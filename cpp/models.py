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
    abc = models.IntegerField(null=False)
    abs = models.IntegerField(null=False)
    ebp = models.IntegerField(null=False)
    asr = models.IntegerField(null=False)
    esp_or_vsa = models.IntegerField(null=False)
    airmatic = models.IntegerField(null=False)
    edl = models.IntegerField(null=False)
    eba = models.IntegerField(null=False)
    ebd = models.IntegerField(null=False)
    tcs = models.IntegerField(null=False)
    bas = models.IntegerField(null=False)
    distronic = models.IntegerField(null=False)
    hill_start_assist = models.IntegerField(null=False)
    night_vision = models.IntegerField(null=False)
    lane_departure_warning = models.IntegerField(null=False)
    lane_change_assist = models.IntegerField(null=False)
    airbag_driver = models.IntegerField(null=False)
    airbag_passenger = models.IntegerField(null=False)
    airbag_side = models.IntegerField(null=False)
    airbag_knee = models.IntegerField(null=False)
    airbag_curtain = models.IntegerField(null=False)
    airbag_roof = models.IntegerField(null=False)
    blind_spot_warning = models.IntegerField(null=False)
    tire_defect_indicator = models.IntegerField(null=False)
    fatigue_detection = models.IntegerField(null=False)
    isofix = models.IntegerField(null=False)
    alarm = models.IntegerField(null=False)
    central_lock = models.IntegerField(null=False)
    immobilizer = models.IntegerField(null=False)
    #Interior equipments
    leather_seat = models.IntegerField(null=False)
    fabric_seat = models.IntegerField(null=False)
    leather_or_fabric_seat = models.IntegerField(null=False)
    electric_windscreen = models.IntegerField(null=False)#?
    electric_rear_window = models.IntegerField(null=False)
    air_conditioning_analogue = models.IntegerField(null=False)
    air_conditioning_digital = models.IntegerField(null=False)
    auto_dimming_rearview_windows = models.IntegerField(null=False)
    front_armrest = models.IntegerField(null=False)
    rear_armrest = models.IntegerField(null=False)
    keyless_entry_and_run = models.IntegerField(null=False)
    six_forward_gear = models.IntegerField(null=False)
    seven_forward_gear = models.IntegerField(null=False)
    hydrolic_steering_wheel = models.IntegerField(null=False)
    functional_steering_wheel = models.IntegerField(null=False)
    adjustable_steering_wheel = models.IntegerField(null=False)
    leather_steering_wheel = models.IntegerField(null=False)
    wooden_steering_wheel = models.IntegerField(null=False)
    heated_steering_wheel = models.IntegerField(null=False)
    power_seat = models.IntegerField(null=False)
    memory_seat = models.IntegerField(null=False)
    folding_seat = models.IntegerField(null=False)
    front_heated_seat = models.IntegerField(null=False)
    rear_heated_seat = models.IntegerField(null=False)
    cooled_seat = models.IntegerField(null=False)
    cruise_control = models.IntegerField(null=False)
    adaptive_cruise_control = models.IntegerField(null=False)
    cooled_torpedo = models.IntegerField(null=False)
    trip_computer = models.IntegerField(null=False)
    chrome_plate = models.IntegerField(null=False)
    wooden_plate = models.IntegerField(null=False)
    head_up_display = models.IntegerField(null=False)
    start_stop = models.IntegerField(null=False)
    backup_camera = models.IntegerField(null=False)#?
    front_view_camera = models.IntegerField(null=False)
    third_row_seat = models.IntegerField(null=False)
    #External equipment
    hardtop = models.IntegerField(null=False)
    led_headlight = models.IntegerField(null=False)
    halogen_headlight = models.IntegerField(null=False)
    xenon_headlight = models.IntegerField(null=False)
    bi_xenon_headlight = models.IntegerField(null=False)
    fog_headlight = models.IntegerField(null=False)
    adaptive_headlight = models.IntegerField(null=False)
    night_sensor_headlight = models.IntegerField(null=False)
    washing_headlight = models.IntegerField(null=False)
    electric_mirror = models.IntegerField(null=False)
    automatic_folding_mirror = models.IntegerField(null=False)
    heated_mirror = models.IntegerField(null=False)
    memory_mirror = models.IntegerField(null=False)
    rear_parking_sensor = models.IntegerField(null=False)
    front_parking_sensor = models.IntegerField(null=False)
    allow_wheel = models.IntegerField(null=False)
    sunroof = models.IntegerField(null=False)
    panoramic_sunroof = models.IntegerField(null=False)
    rain_sensor = models.IntegerField(null=False)
    rear_window_defroster = models.IntegerField(null=False)
    panoramic_windscreen = models.IntegerField(null=False)
    trailer_tow_bar = models.IntegerField(null=False)
    smart_luggage_cover = models.IntegerField(null=False)
    #Multimedia
    radio_tape_recorder = models.IntegerField(null=False)
    radio_cd_player = models.IntegerField(null=False)
    radio_mp3_player = models.IntegerField(null=False)
    tv_or_navigation = models.IntegerField(null=False)
    bluetooth_or_phone = models.IntegerField(null=False)
    usb_or_aux = models.IntegerField(null=False)
    #aux?
    ipod_connection = models.IntegerField(null=False)
    six_plus_speaker = models.IntegerField(null=False)
    cd_changer = models.IntegerField(null=False)
    rear_entertainment_package = models.IntegerField(null=False)
    dvd_changer = models.IntegerField(null=False)

    def __str__(self):
        return str(self.brand) + "-" + str(self.series)
