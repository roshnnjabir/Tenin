from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/product')
def product():
    return render_template('product.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)