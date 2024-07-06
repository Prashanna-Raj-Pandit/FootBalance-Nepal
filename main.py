import os
import requests
from flask import Flask, render_template, send_from_directory, redirect, request, url_for
from flask import request
import json

import email_sender

app = Flask(__name__)

SHEETY_API =os.environ.get('SHEETY_API')
SHEETY_ENDPOINT = F"https://api.sheety.co/{SHEETY_API}/footBalanceAppointment/sheet1"

SHEETY_USERNAME=os.environ.get('SHEETY_USERNAME')
SHEETY_PASSWORD=os.environ.get('SHEETY_PASSWORD')

shetty_header = {
    "Content-Type": "application/json",
    "Authorization": "Basic Zm9vdGJhbGFuY2VuZXBhbDoyUHAoJiQja1U1MEdoSGpz",
    "username": SHEETY_USERNAME,
    "password": SHEETY_PASSWORD
}

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
        return send_from_directory('static', path='files/Product_Sheet_Dynamic_Profile_292.pdf')


@app.route('/appointment', methods=['POST'])
def appointment_form():
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['number']
    appointment_date_n_time = request.form['date']
    client_problem = request.form['discuss']
    app_date, app_time = appointment_date_n_time.split('T')
    email_sender.send_appointment_email(email, name, app_date, app_time, client_problem, phone_number)
    update_google_sheet(name, email, phone_number, app_date, app_time, client_problem)
    return redirect(url_for('home'))


def update_google_sheet(name, email, phone_number, app_date, app_time, client_problem):
    body = {
        "sheet1": {
            "date": app_date,
            "time": app_time,
            "name": name,
            "phonenumber": phone_number,
            "email": email,
            "problem": client_problem
        }
    }
    response = requests.post(SHEETY_ENDPOINT, json=body, headers=shetty_header)
    # print(response.text)


@app.route('/faqs')
def faqs():
    with open('static/files/faqs.json', 'r') as file:
        data = json.load(file)  # Parse JSON string to dictionary
        return render_template("faqs.html", q_n_a=data)


if __name__ == "__main__":
    app.run(debug=True)
