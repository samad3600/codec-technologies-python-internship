import sqlite3


def init_db():

    conn = sqlite3.connect(
        "chat.db"
    )

    cur = conn.cursor()

    cur.execute(
        """

CREATE TABLE IF NOT EXISTS chats(

id INTEGER PRIMARY KEY,

message TEXT,

reply TEXT

)

"""
    )

    conn.commit()

    conn.close()


def save_chat(
    msg,
    reply
):

    conn = sqlite3.connect(
        "chat.db"
    )

    cur = conn.cursor()

    cur.execute(

        """

INSERT INTO chats(
message,
reply
)

VALUES(

?,
?

)

""",

        (
            msg,
            reply
        )

    )

    conn.commit()

    conn.close()



def get_history():

    conn = sqlite3.connect(
        "chat.db"
    )

    cur = conn.cursor()

    cur.execute(

        """

SELECT
message,
reply

FROM chats

"""

    )

    rows = cur.fetchall()

    conn.close()

    return rows