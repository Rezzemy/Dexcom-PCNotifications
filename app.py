from plyer import notification #pip install plyer
import time
from datetime import datetime
from pydexcom import Dexcom #pip install pydexcom
dexcom = Dexcom("Username", "Password") # https://pypi.org/project/pydexcom/ # has explanation on what username/password, and the prerequisite to this functioning properly
oldbg = datetime.now() #placeholder? looks better than None

while True:
    #print(oldbg, datetime.now())
    bg = dexcom.get_current_glucose_reading()
    if bg != None and bg.time != oldbg:
        oldbg = bg.time
        notification.notify( 
        title='WinDexcom',
        message=f'{bg.time}\nGlucose is {bg.mg_dl}\nYou are {bg.trend_description}',
        app_icon=None,
        timeout=10,
        )
        time.sleep(60)
