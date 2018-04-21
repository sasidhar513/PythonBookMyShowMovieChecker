import re
import requests
import mail
import time
import call
movie='avengers'
isLang=True
lang='english'
movieList=[]




def checkFav(hallList):
	fav=""
	if ("Asian GPR".lower() in hallList.lower()):
		fav=fav+"Asian GPR Multiplex: Kukatpally , " 
	if ("Manjeera".lower()  in hallList.lower()):
		fav=fav+" Cinepolis: Manjeera Mall, Kukatpally , "
	if ("Inorbit".lower()  in hallList.lower()):
		fav=fav+" PVR: Inorbit, Cyberabad , "
	if ("GVK One".lower()  in hallList.lower()):
		fav=fav+" INOX: GVK One, Banjara Hills , "
	if ("Forum".lower()  in hallList.lower()):
		fav=fav+" PVR Forum Sujana Mall: Kukatpally, Hyderabad  "
	return fav
#Mail Common variables
toAll= "sasidhardulipudi@gmail.com,sneha.jovi@gmail.com,snehaincredulous@gmail.com,sasidhardulipudi@outlook.com,sasidhardulipudi@rediffmail.com,sasidhardulipudi1@gmail.com"
toMe="sasidhardulipudi@gmail.com"
toLog="sasidhardulipudi1@gmail.com"
sender = "sasidhardulipudi@gmail.com"
mainMessageHTML= '<h1><font color="red"><big>Book ' +movie.upper()+' Tickets : Now Available Hurry up fasttttttttt. <br/>if SNEHA is reading this call SASI immediately</big></font></h1>'




#below are to check lappy charge so I can keep lappy turned on
status =open('/sys/class/power_supply/BAT0/status','r').read().strip()
percent= open('/sys/class/power_supply/BAT0/capacity', 'r').read().strip()
highPercent=99
lowPercent= 20
capacity = int(percent)
					

#below is regex to get all movies that are showing now in Book MY show
pat= re.compile('{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"Filter Impression:category\\\/now showing"},"products":\[{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}\]}}}')


bmsContent = requests.get("https://in.bookmyshow.com/hyderabad/movies").content	

#filtering language specific movies
if isLang:
	movieList =[y[0] for y in [ x for x in pat.findall(bmsContent) if lang.lower() in "".join(x).lower() ]]
else:
	movieList =[y[0] for y in  pat.findall(bmsContent)]

#logging
logMessage=time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())+" -----  Movies currently showing " + ','.join(movieList) + "."
print(logMessage)

#The following will send logmsg to mail every minute so to assure the code is running

startSubject = "Hunting for tickets ***************************"
startMessageHTML= '<h1><font color="red"><big>Application started.<br/><br/>Will notify you, when tickets are released, using mail and phone<br/> Charging in you lappy is '+percent+'%  and your battery status is '+status+' <br/><br/>' +logMessage +' </big></font></h1>'
mail.SendMessage(sender, toLog, startSubject, startMessageHTML, "")



#This "if block"  will send mail to me only if your charge is less than lowPercent and you are you kept lappy = on charge
if capacity<lowPercent and 'Dischar' in status:
	startSubject = "Low Charge **************************** "
	startMessageHTML= '<h1><font color="red"><big>WARNING ********Please charge your lappy ******<br/><br/> Charging in you lappy is '+percent+'% and your battery status is '+status+' <br/><br/>' +logMessage +' </big></font></h1>'	
	mail.SendMessage(sender, toMe, startSubject, startMessageHTML, "")


#This "if block"  will send mail to me only if your charge is more than highPercent and you are didnt keep lappy on charge
if capacity > highPercent and 'Char' in status:
	startSubject = "High Charge **************************** "
	startMessageHTML= '<h1><font color="red"><big>WARNING ********Please unplug your charger ******<br/> <br/>Charging in you lappy is '+percent+'% and your battery status is '+status+' <br/><br/>' +logMessage +' </big></font></h1>'
	mail.SendMessage(sender, toMe, startSubject, startMessageHTML, "")

#this code will run every minute but it should check every sec about movies so looping 60 times to run in one minute
inc = 0
while(inc < 60):
	bmsContent = requests.get("https://in.bookmyshow.com/hyderabad/movies").content
	movieList=[]
	if isLang:
		movieList =[y[0] for y in [ x for x in pat.findall(bmsContent) if lang.lower() in "".join(x).lower() ]]
	else:
		movieList =[y[0] for y in  pat.findall(bmsContent)]
	for i in movieList:
		 if movie in i.lower():				
				while(True):
					#2d urls for the movie
					twodTicketUrl=re.findall('/buytickets/[^"]*?'+movie+'[^"]*?hyderabad[^"]*/', bmsContent)
					#3d urls for the movie
					threedTicketUrl=re.findall('/buytickets/[^"]*?'+movie+'[^"]*?3d[^"]*?hyderabad[^"]*/', bmsContent)
					
					#getting 2d theater list
					msg1=""
					if len(twodTicketUrl) >0:
						listOf2dTheaters= re.findall('data-id=.*\s*data-name=(.*)\s*data-sub',requests.get("https://in.bookmyshow.com"+twodTicketUrl[0]).content)
						msg1= msg1+ '<br/> <br/>Available 2d theaters: <br/><br/>'+" \n ".join(listOf2dTheaters) +'<br/>'
					else:
						msg1= msg1+ '<br/>  2d theaters not available <br/><br/>'
					
					#getting 3d theater list
					if len(threedTicketUrl) >0:
						listOf3dTheaters= re.findall('data-id=.*\s*data-name=(.*)\s*data-sub',requests.get("https://in.bookmyshow.com"+threedTicketUrl[0]).content)
						msg1=msg1+ '<br/>  Available 3d theaters: <br/><br/>'+"  ,  ".join(listOf3dTheaters) +'<br/>'
					else: 
						msg1= msg1+ '<br/>  3d theaters not available <br/><br/>'
					fav=checkFav(msg1)
					favMsg=""
					if fav=="":
						favMsg= "<br/> <br/>  No favorite Halls. Sorry <br/><br/>"
					else:
						favMsg= " <br/> <br/> Your Favourite Halls <br/><br/>" +fav 
						
					mainMessageHTML= '<h1><font color="red"><big>Book ' +movie.upper()+' Tickets : Now Available Hurry up fasttttttttt. <br/>if SNEHA is reading this call SASI immediately'+favMsg+msg1+'</big></font></h1>'
					
					subject = "######################################## NOTICE ####################################"
					mail.SendMessage(sender, toLog, subject, mainMessageHTML, "")
					call.dial_numbers(call.DIAL_NUMBERS)
					time.sleep(60)
	inc=inc+1;
