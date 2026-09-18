# choose a mode of transfer based on the distance
#  (eg: <3km: Walk, 3-15 km: Bike, >15km : Car).

distance = 5

if distance < 3:
    transport = 'Walk'
elif distance <= 15 :
    transport = "Bike"
else:
    transport = "Car"  

print("AI recommended you the transport of: ", transport )         