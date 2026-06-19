from transformers import pipeline

model = pipeline(
    "sentiment-analysis"
)


def analyze(text):

    result = model(text)

    label = result[0]["label"]

    score = round(
        result[0]["score"]*100,
        2
    )

    return (
        label,
        score
    )