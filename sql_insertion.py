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
locations = data2["Yer "][1:]
#print(locations)
"""for location in locations:
    c.execute("INSERT INTO cpp_location VALUES (NULL, ?)", [location])
"""
db.commit()
db.close()
"""
for i,j in data2.items():
    print(i)
    if " ".join(i.split()) == "Yer":
        for k in j:
            print(k)
    if " ".join(i.split()) == "Yakit":
        for k in j:
            print(k)
    if " ".join(i.split()) == "Yakit":
        for k in j:
            print(k)
    if " ".join(i.split()) == "Yakit":
        for k in j:
            print(k)
    if " ".join(i.split()) == "Kasa Tipi":
        for k in j:
            print(k)
    if " ".join(i.split()) == "Motor Gucu":
        for k in j:
            print(k)
    if " ".join(i.split()) == "Motor Hacmi":
        for k in j:
            print(k)
"""
