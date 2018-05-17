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
    abc = models.BooleanField(null=True)
    abs = models.BooleanField(null=True)
    ebp = models.BooleanField(null=True)
    asr = models.BooleanField(null=True)
    esp_or_vsa = models.BooleanField(null=True)
    airmatic = models.BooleanField(null=True)
    edl = models.BooleanField(null=True)
    eba = models.BooleanField(null=True)
    ebd = models.BooleanField(null=True)
    tcs = models.BooleanField(null=True)
    bas = models.BooleanField(null=True)
    distronic = models.BooleanField(null=True)
    hill_start_assist = models.BooleanField(null=True)
    night_vision = models.BooleanField(null=True)
    lane_departure_warning = models.BooleanField(null=True)
    lane_change_assist = models.BooleanField(null=True)
    airbag_driver = models.BooleanField(null=True)
    airbag_passenger = models.BooleanField(null=True)
    airbag_side = models.BooleanField(null=True)
    airbag_knee = models.BooleanField(null=True)
    airbag_curtain = models.BooleanField(null=True)
    airbag_roof = models.BooleanField(null=True)
    blind_spot_warning = models.BooleanField(null=True)
    tire_defect_indicator = models.BooleanField(null=True)
    fatigue_detection = models.BooleanField(null=True)
    isofix = models.BooleanField(null=True)
    alarm = models.BooleanField(null=True)
    central_lock = models.BooleanField(null=True)
    immobilizer = models.BooleanField(null=True)
    #Interior equipments
    leather_seat = models.BooleanField(null=True)
    fabric_seat = models.BooleanField(null=True)
    leather_or_fabric_seat = models.BooleanField(null=True)
    electric_windscreen = models.BooleanField(null=True)
    electric_rear_window = models.BooleanField(null=True)
    air_conditioning_analogue = models.BooleanField(null=True)
    air_conditioning_digital = models.BooleanField(null=True)
    auto_dimming_rearview_windows = models.BooleanField(null=True)
    front_armrest = models.BooleanField(null=True)
    rear_armrest = models.BooleanField(null=True)
    keyless_entry_and_run = models.BooleanField(null=True)
    six_forward_gear = models.BooleanField(null=True)
    seven_forward_gear = models.BooleanField(null=True)
    hydrolic_steering_wheel = models.BooleanField(null=True)
    functional_steering_wheel = models.BooleanField(null=True)
    adjustable_steering_wheel = models.BooleanField(null=True)
    leather_steering_wheel = models.BooleanField(null=True)
    wooden_steering_wheel = models.BooleanField(null=True)
    heated_steering_wheel = models.BooleanField(null=True)
    power_seat = models.BooleanField(null=True)
    memory_seat = models.BooleanField(null=True)
    folding_seat = models.BooleanField(null=True)
    front_heated_seat = models.BooleanField(null=True)
    rear_heated_seat = models.BooleanField(null=True)
    cooled_seat = models.BooleanField(null=True)
    cruise_control = models.BooleanField(null=True)
    adaptive_cruise_control = models.BooleanField(null=True)
    cooled_torpedo = models.BooleanField(null=True)
    trip_computer = models.BooleanField(null=True)
    chrome_plate = models.BooleanField(null=True)
    wooden_plate = models.BooleanField(null=True)
    head_up_display = models.BooleanField(null=True)
    start_stop = models.BooleanField(null=True)
    backup_camera = models.BooleanField(null=True)
    front_view_camera = models.BooleanField(null=True)
    third_row_seat = models.BooleanField(null=True)
    #External equipment
    hardtop = models.BooleanField(null=True)
    led_headlight = models.BooleanField(null=True)
    halogen_headlight = models.BooleanField(null=True)
    xenon_headlight = models.BooleanField(null=True)
    bi_xenon_headlight = models.BooleanField(null=True)
    fog_headlight = models.BooleanField(null=True)
    adaptive_headlight = models.BooleanField(null=True)
    night_sensor_headlight = models.BooleanField(null=True)
    washing_headlight = models.BooleanField(null=True)
    electric_mirror = models.BooleanField(null=True)
    automatic_folding_mirror = models.BooleanField(null=True)
    heated_mirror = models.BooleanField(null=True)
    memory_mirror = models.BooleanField(null=True)
    rear_parking_sensor = models.BooleanField(null=True)
    front_parking_sensor = models.BooleanField(null=True)
    allow_wheel = models.BooleanField(null=True)
    sunroof = models.BooleanField(null=True)
    panoramic_sunroof = models.BooleanField(null=True)
    rain_sensor = models.BooleanField(null=True)
    rear_window_defroster = models.BooleanField(null=True)
    panoramic_windscreen = models.BooleanField(null=True)
    trailer_tow_bar = models.BooleanField(null=True)
    smart_luggage_cover = models.BooleanField(null=True)
    #Multimedia
    radio_tape_recorder = models.BooleanField(null=True)
    radio_cd_player = models.BooleanField(null=True)
    radio_mp3_player = models.BooleanField(null=True)
    tv_or_navigation = models.BooleanField(null=True)
    bluetooth_or_phone = models.BooleanField(null=True)
    usb_or_aux = models.BooleanField(null=True)
    ipod_connection = models.BooleanField(null=True)
    six_plus_speaker = models.BooleanField(null=True)
    cd_changer = models.BooleanField(null=True)
    rear_entertainment_package = models.BooleanField(null=True)
    dvd_changer = models.BooleanField(null=True)

    def __str__(self):
        return str(self.brand) + "-" + str(self.series)
