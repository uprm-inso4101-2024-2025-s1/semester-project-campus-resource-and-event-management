from flask import Flask, make_response

app = Flask(__name__)

class reqCounter():
    def __init__(self):
        self.count = 0
    
    def getCount(self):
        self.count += 1
        return self.count
    
reqCount = reqCounter()

@app.route("/api/")
def hello_world():
    resp = make_response(f"This is the server request # {reqCount.getCount()}", 200)

    # Setting CORS request headers
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run(port=3415)
