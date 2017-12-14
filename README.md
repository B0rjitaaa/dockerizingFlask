Dockerizing Flask!
===================


Hey! I'm your first Markdown document in **StackEdit**[^stackedit]. Don't delete me, I'm very helpful! I can be recovered anyway in the **Utils** tab of the <i class="icon-cog"></i> **Settings** dialog.

----------


Flask Application
-------------

Start with creating a new directory
Then we create the basic <kbd>app.py</kbd>:

```
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
```

Now, wen need to include Flask in our <kbd>requirements.txt</kbd> file:

```
Flask==0.10.1
```

Flask Dockerfile
-------------
We have chosen Linux image as a base.

```
FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev nano

COPY ./requirements.txt /app/requirements.txt
ADD ./templates /app
ADD ./static /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
```



> **Note:**

> - <kbd>COPY</kbd>copies files from the first parameter (the source .) to the destination parameter (in this case, /app)
> - <kbd>ADD</kbd> adds an entire folder to the destination folder.
> - <kbd>WORKDIR</kbd>sets the working directory (all following instructions operate within this directory); you may use WORKDIR as often as you like
> - <kbd>ENTRYPOINT</kbd>configures the container to run as an executable; only the last ENTRYPOINT instruction executes
> - <kbd>pip</kbd> installs from requirements.txt as normal. Since requirements.txt only references Flask 0.1.0, pip only installs Flask 0.1.0. If you are using Flask for your app, then you’re likely to have more modules specificed for installation.


Build the image
-------------
Now that we have a Dockerfile, let’s verify it builds correctly:
```
docker build -t flask-docker:latest .
```
After the build completes, we can run the container:
```
docker run --name=flaskDocker -d -p 5000:5000 flask-docker
```
POC
-------------
![enter image description here](https://i.imgur.com/jcvsVKO.png)
