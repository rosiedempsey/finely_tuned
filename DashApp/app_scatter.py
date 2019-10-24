import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("/Users/rosiedempsey/Desktop/MusicProject/finely_tuned/DataExports/SongsSummary.csv")
df['song_title'] = df['song']+", "+df['artist']
df['max_song_rank'] = df.groupby('username')['song_rank'].transform(np.max)
df['song_rank_percent'] = df['song_rank']/df['max_song_rank']
df['max_artist_rank'] = df.groupby('username')['artist_rank'].transform(np.max)
df['song_rank_percent'] = df['song_rank']/df['max_song_rank']
df['artist_rank_percent'] = df['artist_rank']/df['max_artist_rank']
fav_df = df[df['percent_of_artist_play']<0.2]

app.layout = html.Div([
    dcc.Graph(
        id='rank',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['username'] == i]['song_rank_percent'],
                    y=df[df['username'] == i]['artist_rank_percent'],
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
            )}),
    dcc.Graph(
        id='plays',
        figure={
            'data': [
                go.Scatter(
                    x=fav_df[fav_df['username'] == i]['total_plays'],
                    y=fav_df[fav_df['username'] == i]['percent_of_artist_play'],
                    text=fav_df[fav_df['username'] == i]['song_title'],
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
                xaxis={'type':'log', 'title': 'total_plays'},
                yaxis={'title': 'percent_of_artist_play'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            ),
        }
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)