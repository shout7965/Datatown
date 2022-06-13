from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('Sourcing_List_2022.json', encoding='utf-8-sig') as json_file:
        json_data = json.load(json_file)
    return render_template('table.html', title='Sourcing List', json_data=json_data)

if __name__ == '__main__':
    app.run()
