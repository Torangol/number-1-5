from flask import Flask, request

app = Flask(__name__)


@app.route('/sum2/', methods=['POST'])
def sum2():
    print(request.json)
    a = request.json['data']
    return {'sum': sum(a)}

app.run(host='0.0.0.0', port=5000)