# flask_web/app.py

from flask import Flask, render_template, request
app = Flask(__name__)

import urllib2, json

@app.route('/')
def hello_world():
	albums = get_albums()
	return render_template('index.html', albums = albums)


def get_albums():
	url = urllib2.urlopen('https://itunes.apple.com/search?term=knife+party&entity=album&limit=6')
	res = json.loads(url.read())
	albums = res['results']
	return albums


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




