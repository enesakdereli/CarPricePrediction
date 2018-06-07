import json, sqlite3

db = sqlite3.connect("db.sqlite3")
data = json.load(open('marka_seri_model.json'))
#print(data.keys())
c = db.cursor()
"""for brand, series_data in data.items():
    brand = " ".join(brand.split())
    c.execute("INSERT INTO cpp_brand VALUES (NULL, ?)", [brand])
    c.execute("SELECT * FROM cpp_brand WHERE brand_name= '%s'" % " ".join(brand.split()))
    brand_id = c.fetchone()[0]
    for serie, models in series_data.items():
        c.execute("INSERT INTO cpp_series VALUES (NULL, ?, ?)", (" ".join(serie.split()), brand_id))
        c.execute("SELECT * FROM cpp_series WHERE series_name = '%s'" % " ".join(serie.split()))
        serie_id = c.fetchone()[0]
        for model in models:
            c.execute("INSERT INTO cpp_model VALUES (NULL, ?, ?)", (" ".join(model.split()), serie_id))
"""




#a = "  abc def  gh   "
#print(" ".join(a.split()))

data2 = json.load(open('other_features.json'))
#print(data2["Yer "])
"""locations = data2["Yer "][1:]
#print(locations)
for location in locations:
    c.execute("INSERT INTO cpp_location VALUES (NULL, ?)", [location])
"""

data3 = json.load(open('marka_seri_model_motorGucu.json'))
print(data3)
"""for brand,series in data3.items():
    for serie, models in series.items():
        for model, powers in models.items():
            for power in powers:
                print(power)"""

"""for brand, series_data in data3.items():
    brand = " ".join(brand.split())
    #print(brand)
    c.execute("INSERT INTO cpp_brand VALUES (NULL, ?)", [brand])
    c.execute("SELECT id FROM cpp_brand WHERE brand_name= '%s'" % " ".join(brand.split()))
    brand_id = c.fetchone()[0]
    #print(brand_id)
    for serie, models in series_data.items():
        #print(serie)
        c.execute("INSERT INTO cpp_series VALUES (NULL, ?, ?)", (" ".join(serie.split()), brand_id))
        c.execute("SELECT * FROM cpp_series WHERE series_name = '%s'" % " ".join(serie.split()))
        serie_id = c.fetchone()[0]
        for model, powers in models.items():
            #print(model)
            #print(model)
            c.execute("INSERT INTO cpp_model VALUES (NULL, ?, ?)", (" ".join(model.split()), serie_id))
            c.execute("SELECT * FROM cpp_model WHERE  model_name = '%s'" % " ".join(model.split()))
            model_id = c.fetchone()[0]
            for power in powers:
                c.execute("INSERT INTO cpp_power VALUES  (NULL, ?, ?)", (" ".join(power.split()), model_id))
"""
"""
c.execute("DELETE FROM cpp_power")
c.execute("DELETE FROM cpp_model")
c.execute("DELETE FROM cpp_series")
c.execute("DELETE FROM cpp_brand")
"""
#c.execute("DELETE FROM cpp_carproperty")

db.commit()
db.close()
