import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv("/Users/rosiedempsey/Desktop/MusicProject/finely_tuned/DataExports/SongsSummary.csv")
df['song_title'] = df['song']+", "+df['artist']
top_artist = df[['username','artist','artist_rank', 'total_artist_plays']].drop_duplicates()
top_artist = top_artist[top_artist['artist_rank']<=10].sort_values(by=['total_artist_plays','username'], ascending=False)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children="Rosie and Carl's top artists",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Carl: Listens to artists much more obsessively than Rosie. App is work in progress!', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Bar(
                    x=top_artist[top_artist['username'] == i]['artist'],
                    y=top_artist[top_artist['username'] == i]['total_artist_plays'],
                    # text=df[df['username'] == i]['total_plays']
                    name=i
                ) for i in top_artist['username'].unique()
            ],
            'layout': go.Layout(
                xaxis={ 'title': 'Artist'},
                yaxis={'title': 'Total Plays'},
                margin={'l': 40, 'b': 100, 't': 10, 'r': 50},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)