def PrintoutofRange(parameter,value):
  print(parameter ,'with the reading',value,'is out of the range!')
  
  
def isTemperatureInRange(temperature):
  if temperature < 0 :
    PrintoutofRange("Temperature",temperature)
    return False
  elif temperature > 45 :
    PrintoutofRange("Temperature",temperature)
    return False
  else:
    return True
  
def issocInRange(soc):
  if soc < 20 :
    PrintoutofRange("soc",soc)
    return False
  elif soc > 80 :
    PrintoutofRange("soc",soc)
    return False
  else:
    return True
  
def ischarge_rateInRange(charge_rate):
  if charge_rate > 0.8:
    PrintoutofRange("charge_rate",charge_rate)
    return False
  else:
    return True
 
def convertTocelsius(temperature):
  if('f' in temperature.lower() ):
    return((int(temperature.lower().split('f')[0])-32.0)*(5.0/9.0))
  elif('k' in temperature.lower()):
    return(int(temperature.lower().split('k')[0])-273.0)
  elif('c' in temperature.lower()):
    return(int(temperature.lower().split('c')[0]))

def battery_is_ok(temperature, soc, charge_rate):
  Checktemperature=isTemperatureInRange(temperature)
  Checksoc=issocInRange(soc)
  Checkcharge_rate=ischarge_rateInRange(charge_rate)
  
  
  return Checktemperature and Checksoc and Checkcharge_rate


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
