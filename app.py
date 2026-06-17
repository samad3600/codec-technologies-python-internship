from flask import Flask
from flask import render_template
from flask import request

from chatbot import get_response

from database import (
init_db,
save_chat,
get_history
)

app = Flask(__name__)

init_db()


@app.route("/")
def home():

    history = get_history()

    return render_template(

        "index.html",

        history=history
    )


@app.route("/chat")
def chat():

    msg = request.args.get(
        "msg"
    )

    reply = get_response(
        msg
    )

    save_chat(
        msg,
        reply
    )

    return reply


if __name__ == "__main__":

    app.run(
        debug=True
    )from flask import Flask
from flask import render_template
from flask import request

from chatbot import get_response

from database import (
init_db,
save_chat,
get_history
)

app = Flask(__name__)

init_db()


@app.route("/")
def home():

    history = get_history()

    return render_template(

        "index.html",

        history=history
    )


@app.route("/chat")
def chat():

    msg = request.args.get(
        "msg"
    )

    reply = get_response(
        msg
    )

    save_chat(
        msg,
        reply
    )

    return reply


if __name__ == "__main__":

    app.run(
        debug=True
    )