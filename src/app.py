# Import required libraries
import os
from random import randint

import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import pandas as pd

# Import data
#data_path = os.path.join("../data", "export_dataframe.csv")
data = pd.read_csv("export_dataframe.csv")

# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)


# Put your Dash code here
app.layout = html.Div(
    children=[
        html.H1(children="STF1 Data Analysis", className="header-title"),
        html.P(
            children="Analyze the behavior of STF1 sensor reading while orbiting around earth"
            " There are Temperature,Gyro and Magnetometer readings available ", className="header-description",
        ),
            dcc.Dropdown(
            id='demo-dropdown',
            options=[
                {'label': 'Temprature X axis', 'value': 'TEMP_0'},
                {'label': 'Temprature Y axis', 'value': 'TEMP_1'},
                {'label': 'Magnetometer X axis', 'value': 'MAG_0'},
                {'label': 'Magnetometer Y axis', 'value': 'MAG_1'},
                {'label': 'Magnetometer Z axis', 'value': 'MAG_2'},
                {'label': 'Gyrometer X axis', 'value': 'GYRO_0'},
                {'label': 'Gyrometer Y axis', 'value': 'GYRO_1'},
                {'label': 'Gyrometer Z axis', 'value': 'GYRO_2'},
            ],
            value='TEMP_0'
        ),
        html.Div(
            id='dd-output-container',
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["CCSDS_SECONDS"],
                        "y": data["MAG_0"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Magnetic field analysis"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["CCSDS_SECONDS"],
                        "y": data["GYRO_0"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Gyrometer Data Analysis"},
            },
        ),
    ]
)


# Add  callback
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    return [
        'You have selected "{}"'.format(value),
        dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": data["CCSDS_SECONDS"],
                                "y": data[value],
                                "type": "lines",
                            },
                        ],
                        "layout": {"title": value, },
                    },
                ),
]
# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True,  port=8050)
