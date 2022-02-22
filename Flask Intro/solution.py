from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def index():
    multi = request.args
    if "name" in multi:
        return "Hello " + multi["name"]
    else:
        return "Hello World"

@app.route('/hello-json')
def route1():
    return {"text": "Hello World from Dictionary"}

@app.route('/hello-html')
def route2():
    return "<h1>Hello World</h1><p>Subtext</p>"

@app.route('/hello-html-error')
def errorRoute():
    return ("<h1>404</h1><p>Error</p>", 404)

@app.route('/hello/<name>')
def whatevername(name):
   return 'Hello ' + str(name)

@app.route('/hello/<name>/change/<money>')
def change(name, money):
    return 'Hello ' + str(name) + ', your change is ' + str(10 - int(money))

# @app.route('/login',methods = ['POST', 'GET'])

@app.route('/reflect')
def reflect():
    return "Hello " + str(request.data)

@app.route('/reflect/plex')
def reflectJSON():
    dict = request.json
    newDict = {}
    for key, value in dict.items():
        if isinstance(key, str) and isinstance(value, str):
            newDict["plex_" + key] = "plex_" + value
        elif isinstance(key, str):
            newDict["plex_" + key] = value
        elif isinstance(value, str):
           newDict[key] = "plex_" + value
        else:
            newDict[key] = value
    return newDict

@app.route('/reflect/plex/form')
def reflectForm():
    dict = request.form
    newDict = {}
    for key, value in dict.items():
        newDict["plex_" + key] = "plex_" + value
    return newDict

app.run(host='0.0.0.0', port=81, debug=True)