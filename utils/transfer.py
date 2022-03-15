from encodings import utf_8
from turtle import clear
import starkbank
# import sys
# sys.path.append("./Events.py")
from datetime import datetime, timedelta
import Events as events
from auth import auth




def Transfers(amount):
    
    # print(type(str(amount)
    transfers = starkbank.transfer.create([
        starkbank.Transfer(
            amount= amount,
            bank_code="20018183",  # TED
            branch_code="0001",
            account_number="6341320293482496",
            tax_id="20.018.183/0001-80",
            name="Stark Bank S.A.",
            tags=["Stark", "Challenge"]
        )
        ])
        
def transfering():
    transfered = ""
    # try:
    f = open("utils/paid.txt", "r+",encoding='utf_8')
    for event in events.ListEvents():
            if event.log.type == 'paid':

                if str(event.log.invoice.id) in f.readlines():
                    print("segundo ")
                else:
                    #Transfers(event.log.invoice.amount)
                    print("terceiro if")
                    transfered = transfered + str(event.log)
                    f.write(str(event.log.invoice.id))
                    f.write("\n\r")
    f.close()
    return 'x'
    # except:
        # return {'error': 'erro ao transferir'}

# import os
# print(os.getcwd())
auth()
x = transfering()
print(x)


