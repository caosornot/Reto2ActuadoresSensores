from flask import Flask, render_template

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('template.html')

@app.route("/historico")
def historico():
    return render_template('historico.html')

@app.route("/analisis")
def analisis():
    return render_template('analisis.html')

@app.route("/implementacion")
def implementacion():
    return render_template('implementacion.html')

if __name__ == "__main__":
    app.run(debug=True)
