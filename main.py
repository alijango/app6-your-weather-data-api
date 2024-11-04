from flask import Flask, render_template
import pandas as pd

app = Flask('Weather')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20,
                     parse_dates=['    DATE'])
    return {'station': station,
            'date': date,
            'temperature': temperature}


app.run(debug=True)
