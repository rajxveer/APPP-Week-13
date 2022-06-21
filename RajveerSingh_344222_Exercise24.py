import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
#import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'] 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("C:\\Users\\User\\Downloads\\USA_Housing.csv")
address = df['Address'].unique()

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Price by Address', style = {'textAlign':'center', 'marginTop':30, 'marginBottom':30}),
        dcc.Dropdown( id = 'dropdown',
        options = [{'label': i, 'value': i} for i in address],
        value='Address'),
        dcc.Graph(id = 'bar_plot')
    ])
    
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])

def graph_update(dropdown_value):
    print(dropdown_value)
    dff = df[df['Address'] == dropdown_value]
    fig = go.Figure([go.Scatter(x = dff['Address'], y = dff['Price'],
                                line = dict(color = 'firebrick', width = 4))])
    
    fig.update_layout(title = 'House Price by Address',
                      xaxis_title = 'Address',
                      yaxis_title = 'Prices')
    return fig  

if __name__ == '__main__':
    app.run_server(debug=False)
