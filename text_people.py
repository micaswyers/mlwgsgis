import csv
import time

from twilio.rest import Client

import credentials as creds
import util


CLIENT = Client(creds.ACCOUNT_SID, creds.AUTH_TOKEN)

def text_nondonors(contact_list=None, grad_year=2004):
    try:
        names_numbers_list = util.get_names_numbers(contact_list, grad_year)
    except Exception, e:
        print e
        return
    for first_name, number in names_numbers_list:
        body = u"\U0001F409  \U0001F409  \U0001F409  \U0001F409  \U0001F409\nHi, %s!\nIt's Mica, texting you from the cloud.\nToday is the last day to donate, and the class of 2004 still needs 30 more donors!\nYOU can donate using this link: https://goo.gl/B1ErxD\nThank youuuuu! \u2764\uFE0F\n\U0001F4B8  \U0001F4B8  \U0001F4B8  \U0001F4B8  \U0001F4B8 """ % (first_name, )

        """
        CLIENT.messages.create(
            body=body,
            from_=creds.TWILIO_NUMBER,
            to=number,
        )
        """
        print "Sending to: %s" % (number,)
        print body
        print "******"
        time.sleep(2) # Sleep for 2 seconds to avoid over-messaging
    print "Finished texting!"

if __name__ == "__main__":
    text_nondonors('2004nondonors.csv')
