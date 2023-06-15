from flask import Flask, jsonify, request

app = Flask(__name__)


# Endpoints
@app.route("/transaction", methods=["POST"])
def transferValue():
    app.logger.info(request.data)
    return jsonify("")


@app.route("/report", methods=["POST"])
def generateReport():
    data = request.data.json()
    app.logger.debug("teste")
    if(data):
        return data

# Run API
app.run(port=5000, host="localhost", debug=True)
