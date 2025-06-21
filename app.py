from flask import Flask, jsonify, render_template
import openpyxl

app = Flask(__name__)
DATA_FILE = "data.xlsm"  # Pastikan file ini sesuai dengan file Excel kamu

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/data")
def ambil_data():
    wb = openpyxl.load_workbook(DATA_FILE, data_only=True)
    ws = wb.active
    data = []

    for row in ws.iter_rows(min_row=2, values_only=True):
        waktu = row[0]
        jumlah = row[1] or 0
        plastik = row[2] or 0
        kaleng = row[3] or 0

        # Hanya tambahkan data jika ada isinya
        if not (jumlah == 0 and plastik == 0 and kaleng == 0):
            harga = (plastik * 30) + (kaleng * 50)
            data.append({
                "waktu": str(waktu),
                "jumlah": jumlah,
                "botol_plastik": plastik,
                "botol_kaleng": kaleng,
                "harga": harga
            })

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
