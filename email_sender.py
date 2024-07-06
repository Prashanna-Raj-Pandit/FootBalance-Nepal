import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
from jinja2 import Template
import os

FOOT_BALANCE_EMAIL = "footbalance.nepal@gmail.com"
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def send_appointment_email(receiver_email, name, appointment_date, appointment_time, patient_problem, phone_number):
    # Load the HTML template
    with open('templates/appointment_confirmation.html', 'r') as file:
        template_content = file.read()

    # Define your email parameters
    sender_email = FOOT_BALANCE_EMAIL
    sender_name = "FootBalance Nepal"
    subject = "Appointment Confirmation"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = FOOT_BALANCE_EMAIL
    smtp_password = EMAIL_PASSWORD

    # Define the context for the template
    context = {
        "name": name,
        "appointment_date": appointment_date,
        "appointment_time": appointment_time
    }

    # Render the HTML template with the context
    template = Template(template_content)
    html_content = template.render(context)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Attach the logo image
    with open('static/images/fb_nepal_logo.png', 'rb') as img:
        logo = MIMEImage(img.read())
        logo.add_header('Content-ID', '<logo>')
        logo.add_header('Content-Disposition', 'inline', filename='logo FB_Nepal.png')
        msg.attach(logo)

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.sendmail(sender_email, "novelwellness.nepal@gmail.com",
                            msg=f"Subject:New Appoint\n\nAppointment On: {appointment_date} at {appointment_time}\n\nPatient Problem:{patient_problem}\n\nPatient Details:\nName:{name}\nPhone Number:{phone_number}\nEmail:{receiver_email}")
            # print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
