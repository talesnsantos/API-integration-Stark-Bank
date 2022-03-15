
from datetime import date, datetime
import starkbank


now = datetime.now()

day = str(now.strftime("%d"))
month = str(now.strftime("%m"))
year = str(now.strftime("%Y"))



def ListEvents():
    print(f'{year}-{month}-{day}')
    events = starkbank.event.query(
    after = '2022-03-09',
    before = f'{year}-{month}-{day}'
    )   
    return events 
    

