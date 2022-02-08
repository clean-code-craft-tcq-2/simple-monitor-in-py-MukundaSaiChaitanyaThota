def PrintLowerthanRange(parameter,value):
  print(parameter ,'with the reading',value,'is below the range!')
  
def PrintHigherthanRange(parameter,value):
  print(parameter ,'with the reading',value,'is above the range!')
  
def isTemperatureInRange(temperature):
  if temperature < 0 :
    PrintLowerthanRange("Temperature",temperature)
    return False
  elif temperature > 45 :
    PrintHigherthanRange("Temperature",temperature)
    return False
  else:
    return True
  
def issocInRange(soc):
  if soc < 20 :
    PrintLowerthanRange("soc",soc)
    return False
  elif soc > 80 :
    PrintHigherthanRange("soc",soc)
    return False
  else:
    return True
  
def ischarge_rateInRange(charge_rate):
  if charge_rate > 0.8:
    PrintHigherthanRange("charge_rate",charge_rate)
    return False
  else:
    return True
  

def battery_is_ok(temperature, soc, charge_rate):
  Checktemperature=isTemperatureInRange(temperature)
  Checksoc=issocInRange(soc)
  Checkcharge_rate=ischarge_rateInRange(charge_rate)
    
  return Checktemperature and Checksoc and Checkcharge_rate


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
