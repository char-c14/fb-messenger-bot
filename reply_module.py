import json

def reply_handler_nlp(message_nlp, message_text):

	if message_text == "Extra Help":
		reply = "Contact Charsi for further details "
	elif message_nlp == {}:
		reply = "I'm Sorray"
	elif (message_nlp.keys())[0] == "greetings":
		reply = "Hello There!"
	else:
		reply = "LoL"
	
	return reply

def reply_handler_payload(payload):
	reply = []
	if payload == "help":
		reply.append("No Help. Contact a coordie whose lukkha :P \nJK check this out")
		reply.append(1)
		reply.append([])
		data = json.dumps({
	        "content_type":"text",
	        "title":"Extra Help",
	        "payload":"help"
	      },
	      {
	        "content_type":"text",
	        "title":"Something Else",
	        "payload":"else"
      	})
		reply[2].append(data)
	else:
		return 0 

	return reply