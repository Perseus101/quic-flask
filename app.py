from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route("/test", methods=['POST'])
def test():
    body = request.data.decode("utf-8")
    print(body)
    return body



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
