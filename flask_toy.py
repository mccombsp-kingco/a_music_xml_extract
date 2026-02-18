from flask import Flask, render_template, request
import demo

app = Flask(__name__)

menu = """
    1) Search by Artist
    2) Search by Song Title
    3) Search by Album Title
    4) All details for song key
    """

test = demo.concat_results(demo.find_keys("1","Giants"))

@app.route("/")
def index():
    return render_template('index.html', menu_text=menu, output_text=test)

@app.route("/results", methods=['POST'])
def results():
    test = demo.concat_results(demo.find_keys(request.form['option'],request.form['searchfor']))
    return render_template('results.html', menu_text=menu, output_text=test)

if __name__ == "__main__":
    app.run(debug=True)
