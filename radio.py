
from stations import Stations
from datetime import datetime

import vlc

station_num = 1
station_list = Stations.station_url

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

print("Please Choose Station")
for station in station_list:
    print(f'{station}. {station_list[station_num]["Name"]}')
    station_num += 1

station_choice = int(input('Enter Station Number:'))

p = vlc.MediaPlayer(station_list[station_choice]["URL"])
p.play()
print(station_list[station_choice]["Name"])
input("press enter to quit")
p.stop()