from flask import Flask as Fk
import sys

application = Fk(__name__)
args_list = sys.argv
if len(args_list) < 2:
    print(__file__, "is supposed to be run with a config class specified", 
        "as a command line argument", file=sys.stderr)
    sys.exit(1)

application.config.from_object(args_list[1])

@application.route("/")
def process_root():
    return "<h2>An unbelievable guitar tabs application root page stub</h2>"

if __name__ == "__main__":
    print("Running with a following bunch of settings: ", 
        application.config, sep='\n')
    application.run(port=8088)
