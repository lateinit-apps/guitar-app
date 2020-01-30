from flask import Flask as Fk

application = Fk(__name__)

@application.route("/")
def process_root():
    return "A test string"

if __name__ == "__main__":
    application.run()