from fastapi import FastAPI
import pyjokes
import sentry_sdk


sentry_sdk.init(
    dsn="https://89a3b9d8f93047f9adf6053336156111@o4505387008720896.ingest.sentry.io/4505387018420224",
    traces_sample_rate=1.0,
)

app = FastAPI(title='Joke`s generator')


def joke_generator():
    joke_get = pyjokes.get_joke(language="en", category="neutral")
    return joke_get


@app.get('/{user_input}')
def joke_print(user_input: str):
    joke = joke_generator()
    return {"joke": joke, "user_input": user_input}
