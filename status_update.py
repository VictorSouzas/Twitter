import requests

def status_up(oauth, message):
	data = {'status':message}
	twets = requests.post('https://api.twitter.com/1.1/statuses/update.json', auth=oauth, data=data)
	return twets