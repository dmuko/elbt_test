from flask import Flask
import bcrypt

app = Flask(__name__)

@app.route("/")
def hello():
    hashed = bcrypt.hashpw("saapas", bcrypt.gensalt())
    return "Hello brave new world! hash: %s <- hash should be there" % hashed


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
