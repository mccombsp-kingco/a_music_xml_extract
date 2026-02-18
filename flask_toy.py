from flask import Flask, render_template, request
import demo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/details", methods=['POST'])
def details():
    songdetails = demo.long_print(int(request.form['songid']))
    return render_template('results.html', output_text=songdetails)

@app.route("/results", methods=['POST'])
def results():
    queryresult = demo.concat_results(demo.find_keys(request.form['option'],request.form['searchfor']))
    return render_template('results.html', output_text=queryresult)

if __name__ == "__main__":
    app.run(debug=True)
