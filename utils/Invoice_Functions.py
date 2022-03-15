from datetime import datetime, timedelta
from random import randint
import starkbank






def createInvoices( name = "Stark Bank S.A", tax_id = "20.018.183/0001-80",  tags=["scheduled"], amount=1):
    invoices = starkbank.invoice.create([
    starkbank.Invoice(
        amount=amount,  
        name=name,
        tax_id=tax_id, 
        due=datetime.utcnow() + timedelta(hours=1),
        expiration=timedelta(hours=3).total_seconds(),
        #fine=5,  # 5%
        #interest=2.5,  # 2.5% per month
        tags= tags
    )
        ])


def GetInvoicesPerDate(after, before):

    """
    after: a tuple with year, month and day separated by commas ex: (2020, 1, 1)

    before: a tuple with year, month and day separated by commas ex: (2020, 1, 1)
    """

    invoices = starkbank.invoice.query(
        after=after,
        before=before
    )

    for invoice in invoices:
        print(invoice)


def GetInvoicesPDF(Id):
    pdf = starkbank.invoice.pdf(Id)

    with open("invoice.pdf", "wb") as file:
        file.write(pdf)




def GetInvoicesQRCode(Id):

    qrcode = starkbank.invoice.qrcode(Id, size= 15)

    with open("qrcode.png", "wb") as file:
        file.write(qrcode)

    
def CancelInvoice(Id):
    invoice = starkbank.invoice.update(Id, status="canceled")
    print(invoice)


# def Log():
#     logs = starkbank.
#     logs = starkbank.invoice.log.query(limit=1)
#     return logs
#     # for log in logs:
#     #     print(log)

def last_Log():
    logs = starkbank.invoice.log.query(limit=1)
    # return logs
    for log in logs:
        return log


def GetInvoiceInformation(id):
    paymentInformation = starkbank.invoice.payment(id)

    return paymentInformation






if __name__=='__main__':
    # for i in range(randint(8,13)):

    #     createInvoices()

    # getInvoicesPerDate(datetime(2020, 1, 1), datetime(2022, 3, 9))

    # GetInvoicesQRCode()
    # auth()
    # print(last_Log()) 
    # print(Log()['id'])
    # createInvoices()
    # print(GetInvoicesPDF(last_Log()))

    # pass

    # auth().project.allowed_ips
    # x = getLastAmount()
    # print(type(x))
    pass