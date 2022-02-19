from crypt import methods
from flask import Flask, request
from collections import Counter

app = Flask(__name__)
#app.config["FILE_UPLOAD"]

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        data = request.data
        return word_counter(str(data)[1:])
    else:
        return "Hello, this is a word counter. Send a line through post method."

def word_counter(data):
    word_list = data.replace(',','').replace('\'','').replace('.','').lower().split()
    return dict(Counter(word_list))


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
