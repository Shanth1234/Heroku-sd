""""import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)""""

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)
server = app.server

df = pd.read_csv('https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/matches.csv')

fig = px.bar(df, x="winner", y="win_by_runs",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60,)

app.layout = html.Div([
    dcc.Graph(
        id='Best winning teams based on the win by runs',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)

