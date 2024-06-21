import math

# Definisikan set data minuman
drinks = [
    #coffee
    {'name': 'Americano', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'pahit'},
    {'name': 'Espresso', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'pahit'},
    {'name': 'V60', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'pahit'},
    {'name': 'Latte', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'manis'},
    {'name': 'Affogato', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'manis'},
    {'name': 'Caramel Machiato', 'suhu': 'ice', 'based': 'coffee', 'rasa': 'manis'},
    {'name': 'Americano', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'pahit'},
    {'name': 'Espresso', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'pahit'},
    {'name': 'V60', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'pahit'},
    {'name': 'Latte', 'suhu': 'hot', 'based': 'coffee', 'rasa': 'manis'},
    #milk
    {'name': 'Fresh Milk', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Hot Fresh Milk', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Matcha Latte', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Matcha Latte', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Red Velvet Latte', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Red Velvet Latte', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Kakao Latte', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Kakao Latte', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Taro Latte', 'suhu': 'ice', 'based': 'milk', 'rasa': 'manis'},
    {'name': 'Taro Latte', 'suhu': 'hot', 'based': 'milk', 'rasa': 'manis'},
    #mojito
    {'name': 'Lychee Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    {'name': 'Lime Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    {'name': 'Strawberry Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    {'name': 'Blackberry Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    #tea
    {'name': 'Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Hot Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Lemon Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Lemon Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Lychee Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Lychee Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'manis'},


]

# Input preferensi pengguna
user_preferences = {
    'suhu': input("Pilih suhu (ice/hot): ").strip().lower(),
    'based': input("Pilih bahan dasar (coffee/milk/tea/mojito): ").strip().lower(),
    'rasa': input("Pilih rasa (manis/pahit/kecut): ").strip().lower()
}

# Fungsi untuk menghitung entropi
def entropy(data, attribute, value):
    subset = [d for d in data if d[attribute] == value]
    total = len(subset)
    if total == 0:
        return 0
    
    rasa_counts = {}
    for item in subset:
        rasa = item['rasa']
        if rasa in rasa_counts:
            rasa_counts[rasa] += 1
        else:
            rasa_counts[rasa] = 1
            
    ent = 0
    for rasa in rasa_counts:
        prob = rasa_counts[rasa] / total
        ent -= prob * math.log2(prob)
    
    return ent

# Fungsi untuk menghitung entropi atribut
def calculate_entropy(data):
    entropies = {}
    for attribute in ['suhu', 'based', 'rasa']:
        values = set([d[attribute] for d in data])
        attribute_entropy = 0
        for value in values:
            subset = [d for d in data if d[attribute] == value]
            prob = len(subset) / len(data)
            attribute_entropy += prob * entropy(data, attribute, value)
        entropies[attribute] = attribute_entropy
    return entropies

# Fungsi untuk merekomendasikan minuman
def recommend_drinks(data, preferences):
    filtered_drinks = data
    for attribute, value in preferences.items():
        filtered_drinks = [drink for drink in filtered_drinks if drink[attribute] == value]
    
    if not filtered_drinks:
        return "Tidak ada minuman yang cocok dengan preferensi Anda."
    
    recommendations = [drink['name'] for drink in filtered_drinks]
    return recommendations

# Hitung entropi
entropies = calculate_entropy(drinks)

# Rekomendasi minuman
recommendations = recommend_drinks(drinks, user_preferences)

print("Rekomendasi Minuman untuk Anda:", recommendations)
