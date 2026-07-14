from flask import Flask, render_template, request
from research_ai import research_assistant

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    answer=""

    if request.method=="POST":

        text=request.form["research"]

        answer=research_assistant(text)

    return render_template("index.html",answer=answer)

if __name__=="__main__":
    app.run(debug=True)