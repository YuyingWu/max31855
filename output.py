#!/usr/bin/python
from max31855 import MAX31855, MAX31855Error

units = "c"
thermocouples = []
thermocouples.append(MAX31855(24, 25, 18, units)) # ET
thermocouples.append(MAX31855(22, 5, 27, units)) # BT

data = []

for thermocouple in thermocouples:
    data.append(thermocouple.get())

print("{},{}".format(data[0], data[1]))

for thermocouple in thermocouples:
        thermocouple.cleanup()
