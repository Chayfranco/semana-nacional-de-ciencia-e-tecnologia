from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('backup/index.html')

if __name__ == '__main__':
    app.run(debug=True)

    #deus
    #kkkkkkk