import urllib
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
	print ''
	acct = raw_input('Your twitter accound')
	if (len(acct) < 1 ) : break
	url = twurl.augment(TWITTER_URL, {
		'screen_name' : acct,
		'count' : '5'
	})
	print 'Recuperando' + url
	connection = urllib.urlopen(url)
	data = connection.read()
	headers = connection.info().dict
	print 'Restante', headers['x-rate-limit-remaining']
	js = json.loads(data)
	print json.dumps(js, indend=4)
