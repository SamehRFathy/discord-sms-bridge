# listen for messages on a discord server (globally, all channels)
# send to specified phone number if the message wasn't sent from the bot
import discord
import asyncio
from twilio.rest import TwilioRestClient

# discord.py has logging available: see docs. you probs won't need.

twilioNumber = "+16147022179"
phoneNumber  = "+16147022179" # to send messages to (ie, your user)

botName      = 'sms-bot' # IMPORTANT! must be real bot username
#       otherwise you'll get infinite loops of the bot responding to itself

twilioAccountSid = "AC41ad5edf73f8e93ec34b557af4291919"
twilioAuthToken  = "8bdfbe458a0ec9a9bbdb88d84173acd7"

discordBotToken  = "NjcxNTQyMjYwNjUwODY4NzQz.XjDdbg.vMu7_EVv-PvD-jHJPixD0holCow"

###############################################################################
# auth client objects
twilioClient = TwilioRestClient(twilioAccountSid, twilioAuthToken)
discordClient = discord.Client()

@discordClient.event
async def on_ready():
    print('Logged in as ' + discordClient.user.name + " " + discordClient.user.id)
    print('------')

@discordClient.event
async def on_message(message):

    if message.author.name != botName:
        twilioClient.messages.create(
            to    = phoneNumber,
            from_ = twilioNumber,
            body  = "{} - {}".format(message.author.name,message.content),
        )
        print("sent message: {} - {}".format(message.author.name,message.content))

discordClient.run(discordBotToken)
