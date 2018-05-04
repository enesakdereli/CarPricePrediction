import json, sqlite3

db = sqlite3.connect("db.sqlite3")
data = json.load(open('marka_seri_model.json'))
#print(data.keys())
c = db.cursor()
for brand, series_data in data.items():
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

db.commit()
db.close()

#a = "  abc def  gh   "
#print(" ".join(a.split()))