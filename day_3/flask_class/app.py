from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    abc = 'Hello, Ada!!!'
    return render_template('index.html', abc=abc)


@app.route('/ada/<greeting>')
def ada_page(greeting):
    return '{}, Ada'.format(greeting)


if __name__ == '__main__':
    app.run()