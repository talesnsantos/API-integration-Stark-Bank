
from random import randint
from utils.Invoice_Functions import *
from flask import Flask, redirect, url_for
from utils.transfer import *
from utils.Events import *
from utils.auth import auth

# from time import sleep
# from datetime import datetime

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Iniciado com Sucesso' 


@app.route('/invoice/launch')
def invoice_launch():

    # while True:
    #     if self.hour == datetime.now().hour:
    #         if self.minute == datetime.now().minute:
    #             break
    for Invoice_send in range(randint(8,13)):
        createInvoices()

    return redirect(url_for('log'))

        # return
        # sleep(10800)

@app.route('/log')
def log():
    eventLog = ''
    events = ListEvents()

    for event in events:
    #  |  ## Attributes event.log:
    #  |  - id [string]: unique id returned when the log is created. ex: "5656565656565656"
    #  |  - invoice [Invoice]: Invoice entity to which the log refers to.
    #  |  - errors [list of strings]: list of errors linked to this Invoice event
    #  |  - type [string]: type of the Invoice event which triggered the log creation. ex: "registered" or "paid"
    #  |  - created [datetime.datetime]: creation datetime for the log. ex: datetime.datetime(2020, 3, 10, 10, 30, 0, 0)

        if event.subscription == "transfer":
            eventLog = eventLog + str(event.log.transfer)
            eventLog = eventLog + '<br><br>'

        elif event.subscription == "boleto":
            eventLog = eventLog + str(event.log.boleto)
            eventLog = eventLog + '<br><br>'

        elif event.subscription == "boleto-payment":
            eventLog = eventLog + str(event.log.payment)
            eventLog = eventLog + '<br><br>'

        elif event.subscription == "utility-payment":
            eventLog = eventLog + str(event.log.payment)
            eventLog = eventLog + '<br><br>'

        elif event.subscription == "invoice":
            eventLog = eventLog + str(event.log.invoice)
            eventLog = eventLog + '<br><br>'

    return f"{eventLog}"

@app.route('/transfer/launch/')
def transfer_launch():

    Transfers()
    return 

if __name__ == "__main__":
    auth()
    app.run(debug = True)