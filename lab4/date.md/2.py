yest = datetime.now() - timedelta(1) 
today = datetime.now() 
tom = datetime.now() + timedelta(1) 
print("Yesterday:", yest.strftime('%d-%m-%Y')) 
print("Today:", today.strftime('%d-%m-%Y')) 
print("Tomorrow:", tom.strftime('%d-%m-%Y')) 
 
