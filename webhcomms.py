import requests

webhook_url = input("webhook url:")

while True:
    say = input("send:")
    postage = {
"content": say,
}
    requests.post(webhook_url,postage)

    #webhcommsLIVE by damien poptart and mrgenie151#
