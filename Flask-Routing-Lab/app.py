from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

@app.route('/')
def homeHtml():
    return render_template("home.html")
@app.route('/cart')
def car():
    return render_template("cart.html")
@app.route('/product')
def function():
    return render_template("product.html")

if __name__ == "__main__":
    app.run(debug=True)
