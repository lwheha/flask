from flask import Flask
import time

app = Flask(__name__)


@app.route("/time")
def atime():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(current_time)
    return current_time


if __name__ == "__main__":
    app.run()
