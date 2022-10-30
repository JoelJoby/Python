from xml.dom.minidom import Element


population = {"New York":17.8, "Spain":13.3, "Dhaka":13.0, "Mumbai":12.5}

print(population.get('london'))

print(population.get('Lendon','there\'s no such place '))

print(population.get('Spain'))

ele = {"hydrogen":{"number": 1,
                    "weight": 1.0079,
                    "symbol": "H"},
        "Helium":{"number": 2,
                    "Weight": 4.002,
                    "symbol": "He"}
    }

print(ele["Helium"])
print(ele["hydrogen"]["weight"])


# To add a new key

oxygen = {"number":8,"weight":15.999,"symbol":"O"}
ele["oxy"] = oxygen

print('elements', ele)


