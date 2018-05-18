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
    abc = models.BooleanField(default=False)
    abs = models.BooleanField(default=False)
    ebp = models.BooleanField(default=False)
    asr = models.BooleanField(default=False)
    esp_or_vsa = models.BooleanField(default=False)
    airmatic = models.BooleanField(default=False)
    edl = models.BooleanField(default=False)
    eba = models.BooleanField(default=False)
    ebd = models.BooleanField(default=False)
    tcs = models.BooleanField(default=False)
    bas = models.BooleanField(default=False)
    distronic = models.BooleanField(default=False)
    hill_start_assist = models.BooleanField(default=False)
    night_vision = models.BooleanField(default=False)
    lane_departure_warning = models.BooleanField(default=False)
    lane_change_assist = models.BooleanField(default=False)
    airbag_driver = models.BooleanField(default=False)
    airbag_passenger = models.BooleanField(default=False)
    airbag_side = models.BooleanField(default=False)
    airbag_knee = models.BooleanField(default=False)
    airbag_curtain = models.BooleanField(default=False)
    airbag_roof = models.BooleanField(default=False)
    blind_spot_warning = models.BooleanField(default=False)
    tire_defect_indicator = models.BooleanField(default=False)
    fatigue_detection = models.BooleanField(default=False)
    isofix = models.BooleanField(default=False)
    alarm = models.BooleanField(default=False)
    central_lock = models.BooleanField(default=False)
    immobilizer = models.BooleanField(default=False)
    #Interior equipments
    leather_seat = models.BooleanField(default=False)
    fabric_seat = models.BooleanField(default=False)
    leather_or_fabric_seat = models.BooleanField(default=False)
    electric_windscreen = models.BooleanField(default=False)#?
    electric_rear_window = models.BooleanField(default=False)
    air_conditioning_analogue = models.BooleanField(default=False)
    air_conditioning_digital = models.BooleanField(default=False)
    auto_dimming_rearview_windows = models.BooleanField(default=False)
    front_armrest = models.BooleanField(default=False)
    rear_armrest = models.BooleanField(default=False)
    keyless_entry_and_run = models.BooleanField(default=False)
    six_forward_gear = models.BooleanField(default=False)
    seven_forward_gear = models.BooleanField(default=False)
    hydrolic_steering_wheel = models.BooleanField(default=False)
    functional_steering_wheel = models.BooleanField(default=False)
    adjustable_steering_wheel = models.BooleanField(default=False)
    leather_steering_wheel = models.BooleanField(default=False)
    wooden_steering_wheel = models.BooleanField(default=False)
    heated_steering_wheel = models.BooleanField(default=False)
    power_seat = models.BooleanField(default=False)
    memory_seat = models.BooleanField(default=False)
    folding_seat = models.BooleanField(default=False)
    front_heated_seat = models.BooleanField(default=False)
    rear_heated_seat = models.BooleanField(default=False)
    cooled_seat = models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    adaptive_cruise_control = models.BooleanField(default=False)
    cooled_torpedo = models.BooleanField(default=False)
    trip_computer = models.BooleanField(default=False)
    chrome_plate = models.BooleanField(default=False)
    wooden_plate = models.BooleanField(default=False)
    head_up_display = models.BooleanField(default=False)
    start_stop = models.BooleanField(default=False)
    backup_camera = models.BooleanField(default=False)#?
    front_view_camera = models.BooleanField(default=False)
    third_row_seat = models.BooleanField(default=False)
    #External equipment
    hardtop = models.BooleanField(default=False)
    led_headlight = models.BooleanField(default=False)
    halogen_headlight = models.BooleanField(default=False)
    xenon_headlight = models.BooleanField(default=False)
    bi_xenon_headlight = models.BooleanField(default=False)
    fog_headlight = models.BooleanField(default=False)
    adaptive_headlight = models.BooleanField(default=False)
    night_sensor_headlight = models.BooleanField(default=False)
    washing_headlight = models.BooleanField(default=False)
    electric_mirror = models.BooleanField(default=False)
    automatic_folding_mirror = models.BooleanField(default=False)
    heated_mirror = models.BooleanField(default=False)
    memory_mirror = models.BooleanField(default=False)
    rear_parking_sensor = models.BooleanField(default=False)
    front_parking_sensor = models.BooleanField(default=False)
    allow_wheel = models.BooleanField(default=False)
    sunroof = models.BooleanField(default=False)
    panoramic_sunroof = models.BooleanField(default=False)
    rain_sensor = models.BooleanField(default=False)
    rear_window_defroster = models.BooleanField(default=False)
    panoramic_windscreen = models.BooleanField(default=False)
    trailer_tow_bar = models.BooleanField(default=False)
    smart_luggage_cover = models.BooleanField(default=False)
    #Multimedia
    radio_tape_recorder = models.BooleanField(default=False)
    radio_cd_player = models.BooleanField(default=False)
    radio_mp3_player = models.BooleanField(default=False)
    tv_or_navigation = models.BooleanField(default=False)
    bluetooth_or_phone = models.BooleanField(default=False)
    usb_or_aux = models.BooleanField(default=False)
    #aux?
    ipod_connection = models.BooleanField(default=False)
    six_plus_speaker = models.BooleanField(default=False)
    cd_changer = models.BooleanField(default=False)
    rear_entertainment_package = models.BooleanField(default=False)
    dvd_changer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.brand) + "-" + str(self.series)
