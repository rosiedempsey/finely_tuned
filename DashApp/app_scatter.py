import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("/Users/rosiedempsey/Desktop/MusicProject/finely_tuned/DataExports/SongsSummary.csv")
df['song_title'] = df['song']+", "+df['artist']


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['username'] == i]['song_rank'],
                    y=df[df['username'] == i]['artist_rank'],
                    text=df[df['username'] == i]['song_title'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.username.unique()
            ],
            'layout': go.Layout(
                xaxis={ 'title': 'Song ranking'},
                yaxis={'title': 'Artist Ranking'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)