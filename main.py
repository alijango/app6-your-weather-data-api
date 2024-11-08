from flask import Flask, render_template
import pandas as pd

# Data App
app = Flask('Weather')

station = pd.read_csv('data_small/stations.txt', skiprows=17)
station = station[['STAID', 'STANAME                                 ']]


@app.route('/')
def home():
    return render_template('home.html', data=station.to_html())


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    station_id = pd.read_csv('data_small/stations.txt', skiprows=17)
    name_st = station_id.loc[int(station) - 1, 'STANAME                                 ']
    return {'station': station,
            'station_name': name_st,
            'date': date,
            'temperature': temperature}


@app.route('/api/v1/<station>/')
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    result = df.to_dict(orient='records')
    return result


@app.route('/api/v1/yearly/<station>/<year>')
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return result


app.run(debug=True)
