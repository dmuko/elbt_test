from flask import Flask
import bcrypt

app = Flask(__name__)

@app.route("/")
def hello():
    hashed = bcrypt.hashpw("saapas", bcrypt.gensalt())
    print hashed 
    return "Hello brave new world! %s" % hashed


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
