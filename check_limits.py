def isTemperatureInRange(temperature):
  if (temperature < 0 or temperature > 45):
    print('Temperature is out of range!')
    return False
  else:
    return True
  
def issocInRange(soc):
  if (soc < 20 or soc > 80):
    print('soc is out of range!')
    return False
  else:
    return True
  
def ischarge_rateInRange(charge_rate):
  if charge_rate > 0.8:
    print('charge_rate is out of range!')
    return False
  else:
    return True
  

def battery_is_ok(temperature, soc, charge_rate):
  return isTemperatureInRange(temperature) and issocInRange(soc) and ischarge_rateInRange(charge_rate)


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
