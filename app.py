from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-2024'

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Услуги
@app.route('/services')
def services():
    services_list = [
        {'name': 'Диагностика', 'price': '500-1000₽', 'time': '30 мин', 'icon': '🔧'},
        {'name': 'Замена экрана', 'price': '2000-5000₽', 'time': '1-2 часа', 'icon': '📱'},
        {'name': 'Замена аккумулятора', 'price': '1500-3000₽', 'time': '1 час', 'icon': '🔋'},
        {'name': 'Чистка от пыли', 'price': '1000-2000₽', 'time': '1 час', 'icon': '💨'},
        {'name': 'Переустановка ПО', 'price': '800-1500₽', 'time': '1 час', 'icon': '💻'},
        {'name': 'Восстановление данных', 'price': '1500-4000₽', 'time': '2-3 часа', 'icon': '💾'},
    ]
    return render_template('services.html', services=services_list)

# О нас
@app.route('/about')
def about():
    team = [
        {'name': 'Алексей Иванов', 'role': 'Главный инженер', 'experience': '10 лет'},
        {'name': 'Дмитрий Петров', 'role': 'Специалист по ремонту', 'experience': '7 лет'},
        {'name': 'Елена Смирнова', 'role': 'Менеджер', 'experience': '5 лет'},
    ]
    return render_template('about.html', team=team)

# Контакты
@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash('Спасибо! Мы свяжемся с вами', 'success')
        return redirect(url_for('contacts'))
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)