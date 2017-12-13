import json

def reply_handler_nlp(message_nlp, message_text):

	if message_nlp == {}:
		reply = "I'm Sorray"
	elif (message_nlp.keys())[0] == "greetings":
		reply = "Hello There!"
	else:
		reply = "LoL"
	
	return reply

def reply_handler_payload(payload):
	pass
	if payload == "help":
		reply = "No Help. Contact a coordie whose lukkha :P"
	else:
		return 0 

	return reply