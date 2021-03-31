from flask import Flask, render_template, request, jsonify
from bot import user




app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/chat", methods=['GET', 'POST'])
def chat():
    user_query = request.json
    # print(user_query)
    user_query = user_query['name']
    result = user(user_query)
   

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
