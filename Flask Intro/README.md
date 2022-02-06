# Flask Intro Project

## Setup
- You created this repo and set up two remotes last time. Pull from the starter remote to make sure 
your repo is in sync. Run `git pull starter main`
- Download [Postman](https://www.postman.com/downloads/). The web version is also fine.

## Installation and Virtual Environment
You will need to add a virtual environment for this project where you will install your dependencies.
This basically makes it so that the libraries needed for this project will remain in your local folder, and not crowd storage in your "global" python installation.

- In your Flask Group folder, run `python -m venv env`
- Run `source env/bin/activate` to start your virtual environment
- Run `pip install flask` to install flask

Note that you will have to enter your virtual environment each time you work to have access to Flask

## What is Postman, what is a browser?
- A browser runs a GET HTTP request to the server corresponding to the domain you enter
- It also runs many other requests depending on the html response of the server, to render components, etc.
- Postman provides a flexible interface to make customized requests with a variety of payloads with all kinds of HTTP methods

## Basic GET Request
- Enter "google.com" in your browser. Now enter "google.com" in Postman with the GET method. What do you notice?
- Now let us create a server of our own!

### Hello World
- Tutorial taken in large part from [Python Basics](https://pythonbasics.org/flask-tutorial-hello-world/)
- Great! Now that everything is installed you can create your first Flask App
- Create a file called `solution.py` and put the following code in it:

- Use the line below to import Flask in Python.
```python3
from flask import Flask
```

- Create app, that hosts the application
```python3
app = Flask(__name__)
```

- Then you need a route that calls a Python function. A route maps what you type in the browser (the url) to a Python function. The app.route decorator does this.
```python3
@app.route('/hello')
    def index():
```

- The function should return something to the web browser,
```python3
return 'Hello World'
```

- Almost done, the server needs to be started. This starts the web app at port 81.
```python3
app.run(host='0.0.0.0', port=81)
```

- Code summary:
```python3
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=81)
```

- Now run this code. While it is running, your server is on
- If you want to update the server's source code, you must quit the server application (ctrl+c) and restart it

- While the code is running, enter `http://localhost:81/hello` in your browser. What does it show?
- You can also try this out in postman as before

## Responses
- What you returned in your route method is treated as Flask as the HTTP response
- HTTP responses can take various forms: plain text (like we did before), JSON, HTML (which https://google.com/ responds with), and even files like PDFs, and images (which we won't go over today)
- Make your server code have two other routes:
    - /hello-json, which returns a dictionary: {"text": "Hello World from Dictionary"}
    - /hello-html, which returns "&lt;h1>Hello World&lt;/h1>&lt;p>Subtext&lt;/p>"
- Test these out from your browser/postman
- HTTP responses also have status codes. These tell your browser/application about if the request was successful or not. If you return a tuple in a route function, the second element is treated as the status code
- Make your server code have the /hello-html-error route, which returns the same as /hello-html but with a 404 status code. Look at how your browser renders this!

## Requests
- There is a lot of ways to send information to a server in an HTTP Request

### Path Variables
- Paths can contain variables. These can be passed in as variables to the route function.

- Add this code to your server:
```python3
@app.route('/hello/<name>')
def whatevername(name):
   return 'Hello ' + str(name)
```
- Now try out the `/hello/Adam` route on the browser/postman
- Once you understand how this works, implement a route such that:
    - `/hello/Adam/change/10` would respond with the text "Hello Adam, your change is 0"
    - `/hello/Dev/change/9` would respond with "Hello Dev, your change is 1" (Change for a $10 total).

### Queries
- Go to `youtube.com/watch`. It redirects you back to youtube.com. This is because it doesn't have its usual ?v=[video_id] in front of it. This is the query, a set of keys and values, such as: {"v": "[video_id]"}
- Every HTTP request can have such a query. You can access this using the `request.args` [MultiDict](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Request.args) in a route function
- Change the `/hello` route such that it works the same as before with no query, but with a "name" query, it works the same as the `/hello/<name>` route
    - So `/hello` -> "Hello World"
    - `/hello?key=value` -> "Hello World"
    - `/hello?name=Shamith` -> "Hello Shamith"

### Methods
- "GET" is just one method of HTTP Requests. It is used primarily to "get" information, and should not change anything about internal storage ideally
- GET requests do not have any "Request Payloads" but other methods can send data along with a Request
- To specify methods of your route function, add the methods argument to @app.route
- `@app.route('/login',methods = ['POST', 'GET'])` runs the following function for the `/login` route for both POST and GET requests

### Plain Text payload
- You need Postman for this, since it is a customized post request
- You can access a raw payload* using `request.data`
- Make a route at `/reflect` that takes a text payload and responds with the text "Hello " + whatever the payload was
- To add a payload, go to postman's "body" section, and choose "raw" and "Text" and enter your payload there

### JSON payload
- You will use this a lot in the future!
- Try running the same `/reflect` method but pass in a JSON payload (choose JSON) in Postman instead of Text
- You will see there's not that much difference in these payloads. You can parse `request.data` into JSON and use it for whatever you want. Flask already does this for you, if you use `request.json` you get a dictionary from properly a properly formatted JSON payload
- Make a route at `/reflect/plex` that takes a JSON payload and returns a JSON payload with each key and each key and string value being prepended with "plex_"
    - Payload: {"name":"X","age":12} -> {"plex_name":"plex_X","plex_age":12}

### Form Submission and POST
- Make an HTML file, put this in it:
```html
<html>
   <body>
      <form action = "http://localhost:81/login" method = "PUT">
         <p>Enter Name:</p>
         <p><input type = "text" name = "username" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>   
   </body>
</html>

```
- This is a form, that has our server's `/login` route as its submission URL using the method PUT. PUT works the same as POST (but has different conventions for use, which we ignore for now)
- When you click submit on this form, it sends a request to `/login` with a payload with keys and values corresponding to the form's inputs
- Even though this is a key-value payload, it is formatted very differently from our JSON example from earlier. However Flask makes it simple and puts it as a dictionary in the `request.form` if the request has this format ("formdata")
- You can send this kind of payload in Postman using the "x-www-form-urlencoded" option
- Now implement the same thing you did in `/reflect/plex` in a new route `/reflect/plex/form` except here treat all values as string

## Finishing Up
- Congragulations! We now have a strong understanding of basic Flask and HTTP servers
- Make sure to push your code to your own repository by committing first and then running `git push origin main`
- We will run tests on your methods in this exercise to make sure they work, and give you feedback in the next Curriculum meeting!
