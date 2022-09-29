import random

from time import *

check=True

while(check):

    temp=random.randint(0,50)

    humidity=random.randint(10,60)

    if temp>45 or humidity>50:

        print("Temperature=",temp,'°C',"Humidity=",humidity)

        print("ALARM ON")

        check=False

    else:

        print("Temperature=",temp,'°C',"Humidity=",humidity)

    sleep(0.5)
