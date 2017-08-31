
from flask import Flask, request
from pymessenger import Bot
from util2 import fetch_reply

app = Flask(__name__)


FB_ACCESS_TOKEN = "EAABv9S28mmgBAOvMvElFQo2TURGWYMADIMvxkCC9VGrWMs8Pa8BuJbvZBN24h5KjpHBsruoD2x84b1vmqEBbjNKIZAzt04FnPXF6xIuviHIfiYZARjLYVVGZBRRfzNeWKa2TKiWUWbsZCk5f1SzGEruLVmsy1eGB8758plVTDhj0BSE6K2Izg"
bot = Bot(FB_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	print(request.data)

	data = request.get_json()

	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):

					if messaging_event['message'].get('text'):

						query = messaging_event['message']['text']
						reply = fetch_reply(query, sender_id)

						bot.send_text_message(sender_id, reply['data'])

	return "ok", 200

if __name__ == "__main__":
	app.run(port=8000, use_reloader = True)