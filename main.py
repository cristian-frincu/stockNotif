import httplib, urllib;
import json;
import sys;
import time;



def sendNotification(title,message,token,user):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
	  urllib.urlencode({
		"token": token,
		"user": user,
		"message": message,
		"title": title,
	  }), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()
	print "Pushover sent sucessfully!"




def getPrice(symbol,exchange):
	prefix = "http://finance.google.com/finance/info?client=ig&q=";
	url = prefix+"%s:%s"%(exchange,symbol)
	u = urllib.urlopen(url)
	content = u.read()    
	obj = json.loads(content[3:])
	return obj[0]
    
    





previousPrice=0; #assuming the price starts at zero for the first time
while(True):
	stockInfo = getPrice("MARKET","TICKER");
	currentPrice = stockInfo['l'];
	changeInPrice = stockInfo['c'];
	if(changeInPrice > 0):
		subject="The price went up by " +changeInPrice;
	elif(changeInPrice == 0):
		subject="The price stayed the same";
	else:
		subject ="The price went down by "+changeInPrice;
		
	message="Current price is "+currentPrice +" and the world keeps spinning";
	print "Price checked!";
	print "Current Price: "+ currentPrice +" change in price of "+ changeInPrice;
	
	if(previousPrice!=currentPrice): #only notify if there has been a change in price
		sendNotification(subject,message,"YOUR Token","YOUR Username"); 
		
	previousPrice = currentPrice;
	time.sleep(600); #checke every 10 minutes
	


    

