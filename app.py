from flask import Flask

#creating flask object
app = Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def helloWorld():
     return "Pragya's home page"

@app.route("/ContactPage")
def ContactP():
    return "Plz contact 917890..."



if( __name__ == "__main__"):
     app.run(debug = True , port = 8000)