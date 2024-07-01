from flask import Flask, render_template, send_from_directory
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/insole/<int:insole_id>')
def insoles(insole_id):
    if insole_id == 1:
        return send_from_directory('static', path='files/FB_ProductSheets_custom-impact.pdf')
    elif insole_id == 2:
        return send_from_directory('static', path='files/Product_Sheet_Max.pdf')
    elif insole_id == 3:
        return send_from_directory('static', path='files/FB_ProductSheet_Medical_Black-EN_rev1.pdf')
    elif insole_id == 4:
        return send_from_directory('static', path='files/FB_ProductSheet_34insoles_2.pdf')
    elif insole_id == 5:
        return send_from_directory('static', path='files/FB_ProductSheet_Medical_Green.pdf')
    elif insole_id == 6:
        return send_from_directory('static', path='files/FB_ProductSheet_Medical_Kids_7.pdf')
    elif insole_id == 7:
        return send_from_directory('static',path='files/Product_Sheet_Dynamic_Profile_292.pdf')


if __name__ == "__main__":
    app.run(debug=True)
