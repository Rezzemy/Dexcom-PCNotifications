from plyer import notification #pip install plyer
import time
from datetime import datetime
from pydexcom import Dexcom #pip install pydexcom
dexcom = Dexcom("Username", "Password") # https://pypi.org/project/pydexcom/ # has explanation on what username/password, and the prerequisite to this functioning properly
oldbg = datetime.now() #placeholder? looks better than None
oldbgval = 1

while True:
    #print(oldbg, datetime.now())
    bg = dexcom.get_current_glucose_reading()
    if bg != None and bg.time != oldbg:
        oldbg = bg.time
        valdiff = bg.mg_dl / oldbgval
        oldbgval = bg.mg_dl
        if valdiff >= 1.1 or valdiff <= 0.9: #condition to only make notification if difference in glucose has changed by 10 or more percent
            notification.notify( 
            title='WinDexcom',
            message=f'{bg.time}\nGlucose is {bg.mg_dl}mg/dL\nYou are {bg.trend_description}\nDifference is {valdiff}',
            app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds)
            )
            time.sleep(60)
