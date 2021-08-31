from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



#my token : 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

# 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