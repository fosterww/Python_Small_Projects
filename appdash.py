import dash_core_components as dcc
import dash_html_components as html
import dash

app = dash.Dash()
colors = {
    'background': '#87D653',
    'text': '#ff0033'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),
    html.Div(children='''Dash Framework: A web application framework for Python.'''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Delphi'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Python'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)


