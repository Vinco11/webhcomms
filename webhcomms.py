import requests
# place your webhook url below #
webhook_url = "webhook url goes here"

while True:
    say = input("input:")
    postage = {
		"content": say,
	}
    requests.post(webhook_url,postage)
