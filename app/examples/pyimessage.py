from py_imessage import imessage
from time import sleep

phone = "+66818726755"

if not imessage.check_compatibility(phone):
    print("Not an iPhone.")
else:
    print("Yes, he use iPhone.")

# guid = imessage.send(phone, "Hello World!")
#
# # Let the recipient read the message
# sleep(5)
# resp = imessage.status(guid)
#
# print(f'Message was read at {resp.get("date_read")}')