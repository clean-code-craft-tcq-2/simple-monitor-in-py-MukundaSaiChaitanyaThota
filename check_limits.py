def isTemperatureInRange(value):
  if (value < 0 or value > 45):
    print('Temperature is out of range!')
    return False
  else:
    return True
  
def issocInRange(value):
  if (value < 20 or value > 80):
    print('soc is out of range!')
    return False
  else:
    return True
  
def ischarge_rateInRange(value):
  if value > 0.8:
    print('charge_rate is out of range!')
    return False
  else:
    return True
  

def battery_is_ok(temperature, soc, charge_rate):
  return isTemperatureInRange(temperature) and issocInRange(soc) and ischarge_rateInRange(charge_rate)


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
