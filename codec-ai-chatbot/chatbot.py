from transformers import pipeline

chat = pipeline(
    "text-generation",
    model="distilgpt2"
)


def get_response(msg):

    prompt = f"""
User: {msg}

Assistant:
"""

    result = chat(

        prompt,

        max_new_tokens=50,

        do_sample=True,

        temperature=0.7,

        repetition_penalty=1.8,

        pad_token_id=50256
    )

    generated = result[0][
        "generated_text"
    ]

    response = generated.split(
        "Assistant:"
    )[-1]

    response = response.strip()


    lines = response.split("\n")

    response = lines[0]


    if len(response) < 5:

        response = (
            "Can you ask in another way?"
        )

    return response