from flask import render_template, Flask, request
from smtplib import *


app = Flask(__name__)


@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello():
    return render_template('hello.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/send-email/', methods=["POST"])
def send_email():
    server = SMTP('smtp.gmail.com', 587)
    try:
        sender_email = request.form[('mail')]
        receiver_email = "izzyevermore123@gmail.com"        #Created a dummy account
        password = "callmedorg420"
        message = request.form[('comment')]
        server.starttls()

        server.login(receiver_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("the message has been successfully sent")

    except Exception as err:
        print("Something went wrong..", err)
    finally:
        server.close()

    return "The message has been sent succesfully"
