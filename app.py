import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

testimonials = [
    {"name": "Andi", "message": "Desain interiornya sangat memuaskan!"},
    {"name": "Budi", "message": "Pekerjaan sangat profesional, hasil luar biasa!"},
    {"name": "Citra", "message": "Sangat puas dengan layanan Digitech."}
]

# Fungsi untuk menyimpan data ke file CSV
def save_to_csv(data):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

@app.route('/')
def index():
    return render_template('index.html', testimonials=testimonials)

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        # Simpan data ke file CSV
        save_to_csv([name, email, phone])
        
        return redirect(url_for('index'))  # Setelah daftar, kembali ke halaman utama

    return render_template('join.html')  # Menampilkan halaman Join Us

if __name__ == '__main__':
    app.run(debug=True)
