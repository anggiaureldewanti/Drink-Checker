from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Definisikan set data minuman
drinks = [
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
    {'name': 'Lychee Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    {'name': 'Lime Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    {'name': 'Strawberry Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    {'name': 'Blackberry Mojito', 'suhu': 'ice', 'based': 'mojito', 'rasa': 'kecut'},
    {'name': 'Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Hot Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Lemon Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'kecut'},
    {'name': 'Lemon Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'kecut'},
    {'name': 'Lychee Tea', 'suhu': 'ice', 'based': 'tea', 'rasa': 'manis'},
    {'name': 'Lychee Tea', 'suhu': 'hot', 'based': 'tea', 'rasa': 'manis'},
]

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/suhu')
def suhu():
    return render_template('suhu.html')

@app.route('/select_suhu', methods=['POST'])
def select_suhu():
    session['suhu'] = request.form['suhu']
    return redirect(url_for('based'))

@app.route('/based')
def based():
    return render_template('based.html')

@app.route('/select_based', methods=['POST'])
def select_based():
    session['based'] = request.form['based']
    return redirect(url_for('rasa'))

@app.route('/rasa')
def rasa():
    return render_template('rasa.html')

@app.route('/select_rasa', methods=['POST'])
def select_rasa():
    session['rasa'] = request.form['rasa']
    user_preferences = {
        'suhu': session.get('suhu'),
        'based': session.get('based'),
        'rasa': session.get('rasa')
    }
    recommendations = recommend_drinks(drinks, user_preferences)
    return render_template('result.html', recommendations=recommendations)

def recommend_drinks(data, preferences):
    filtered_drinks = data
    for attribute, value in preferences.items():
        filtered_drinks = [drink for drink in filtered_drinks if drink[attribute] == value]
    
    if not filtered_drinks:
        return ["Tidak ada minuman yang cocok dengan preferensi Anda."]
    
    recommendations = [drink['name'] for drink in filtered_drinks]
    return recommendations

if __name__ == '__main__':
    app.run(debug=True)
