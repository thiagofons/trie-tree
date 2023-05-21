from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoints
@app.route()
def transferValue(source, target, value):
    return

@app.route()
def generateReport():
    return


# Run API
app.run(port=5000, host='localhost', debug=True)