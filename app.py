from flask import Flask, render_template, jsonify
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)

ALGORITMA_DATA = {
    "fuzzy": {
        "judul": "Algoritma Fuzzy Logic",
        "pengertian": "Logika Fuzzy memperluas logika klasik dengan derajat kebenaran antara 0 dan 1, sehingga cocok untuk memodelkan ketidakpastian atau data samar.",
        "kelebihan": ["Mampu menangani ketidakpastian dan ambiguitas data.", "Mudah diinterpretasikan dengan aturan IF-THEN.", "Tidak butuh model matematis yang rumit."],
        "kekurangan": ["Akurasi bergantung pada pakar untuk rule base.", "Membutuhkan banyak validasi dan verifikasi."]
    },
    "jst": {
        "judul": "Jaringan Syaraf Tiruan (JST)",
        "pengertian": "JST adalah model komputasi yang terinspirasi dari struktur dan fungsi jaringan saraf biologis di otak manusia. JST belajar dari data untuk mengenali pola.",
        "kelebihan": ["Kemampuan belajar dan beradaptasi.", "Mampu memproses data secara paralel.", "Memiliki toleransi kesalahan."],
        "kekurangan": ["Bersifat Black Box (Sulit diinterpretasi).", "Membutuhkan data pelatihan besar.", "Membutuhkan sumber daya komputasi tinggi."]
    },
    "genetika": {
        "judul": "Algoritma Genetika",
        "pengertian": "Algoritma pencarian adaptif yang meniru proses seleksi alam dan evolusi biologis untuk mencari solusi optimal melalui operator seleksi, crossover, dan mutasi.",
        "kelebihan": ["Mampu menangani masalah optimasi yang kompleks.", "Cocok untuk masalah multi-kriteria.", "Sangat robust."],
        "kekurangan": ["Bersifat stokastik (tidak ada jaminan optimal).", "Membutuhkan banyak iterasi (waktu konvergen lama).", "Sensitif terhadap pemilihan parameter."]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/materi/<algoritma_name>')
def get_materi(algoritma_name):
    data = ALGORITMA_DATA.get(algoritma_name.lower())
    if data:
        return jsonify(data)
    return jsonify({"error": "Algoritma tidak ditemukan"}), 404

if __name__ == '__main__':
    # host='0.0.0.0' agar bisa diakses via IP
    app.run(debug=True, host='0.0.0.0')
