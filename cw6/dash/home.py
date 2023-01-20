from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('winequelity.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

def generate_graf_regression(value):
    return dcc.Graph(id="my-graf",  figure=px.scatter(df, x=value, y="pH",
                 size="quality", color="alcohol", hover_name="target",
                 log_x=True, size_max=60))

def generate_graf_classification(value):
    return dcc.Graph(
        id='example-graph-2',figure=px.bar(df, x=value, y="alcohol", color="target", barmode="group")
    )

app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='Tabelka'),
    generate_table(df),
    dcc.Dropdown(['Regresja', 'Klasyfikacja'], 'Regresja', id='my-dropdown'),
    html.Div(id='myOutOption'),
    dcc.Dropdown(df.columns, 'residual sugar', id='my-value'),
    html.Div(id='myOutGraf'),
    ])

@app.callback(
    [Output('myOutOption', 'children'),
    Output('myOutGraf', 'children')],
    [Input('my-dropdown', 'value') , 
    Input('my-value', 'value')]
)
def update_output(option, selectedValueToGraf):
    if option == "Regresja" :
        return f'Your option: {option}', generate_graf_regression(selectedValueToGraf)
    else :
        return f'Your option: {option}', generate_graf_classification(selectedValueToGraf)

if __name__ == '__main__':
    app.run_server(debug=True)