from twilio.rest import TwilioRestClient


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = "+91##########"

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+91##########"]#,"+91##########"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL =  "https://demo.twilio.com/docs/voice.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient("ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)

    
    
    
    import operator
import functools 
import numpy as np
import tensorflow

def dotProduct(X,theta):
	product=X*theta
	return np.array([functools.reduce(operator.add,lis) for lis in product])

def rootMeanSqareError(predictedY, actualY)
	predictedY-actualY


X=np.array([[[2,3,3,6],[1,2,4,5],[1,3,5,7]],[[1,7,3,2],[2,7,3,4],[1,0,4,2]]])
output=([[13,54,46,7],[1,3,5,63]])






inputsampleCount=1
outputSampleCount=1
foodsCount=3 # no of food items(features) you are giving to find out the optimal
inNutrientCount=4
outNutrientCount=4 #how many nutrients you gonna find out

#testInputShape=inputsampleCount X foodsCount X inNutrientCount
#testOutputShape= outputSampleCount X outNutrientCount
theta= np.array([[i]*inNutrientCount for i in np.random.rand(foodsCount)])










