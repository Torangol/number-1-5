from flask import Flask, request

app = Flask(__name__)

@app.route('/sum3/', methods=['POST'])
def hello_world():
    a = request.json.values()
    b = sum(a)
    c = {'sum': b}
    return c

app.run(host='0.0.0.0', port = 5000)