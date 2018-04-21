from twilio.rest import TwilioRestClient


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = "+919908438890"

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+919908438890"]#,"+917286825692"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL =  "https://demo.twilio.com/docs/voice.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = TwilioRestClient("AC24e0b252e340834653b0f59f26b90f81", "2d0bfd3f0750f95a92e9589f5cf55bfd")


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
