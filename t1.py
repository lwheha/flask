from flask import Flask, render_template

app = Flask(__name__)


@app.route("/user/list")
def user_list():
    return render_template("biaodan.html")


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
