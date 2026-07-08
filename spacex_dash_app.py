# SpaceX Launch Records Dashboard - Plotly Dash
# IBM Applied Data Science Capstone
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the launch data
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)

# Dropdown options: All Sites + each unique launch site
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
    [{'label': s, 'value': s} for s in spacex_df['Launch Site'].unique()]

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Launch Site drop-down input
    dcc.Dropdown(id='site-dropdown',
                 options=site_options,
                 value='ALL',
                 placeholder='Select a Launch Site here',
                 searchable=True),
    html.Br(),

    # TASK 2: Pie chart of successful launches
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Payload range slider
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                    value=[min_payload, max_payload]),

    # TASK 4: Scatter chart of payload vs. outcome
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2: callback for the pie chart
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df[spacex_df['class'] == 1], names='Launch Site',
                     title='Total Successful Launches by Site')
    else:
        df = spacex_df[spacex_df['Launch Site'] == entered_site]
        counts = df['class'].value_counts().rename({1: 'Success', 0: 'Failure'})
        fig = px.pie(names=counts.index, values=counts.values,
                     title=f'Total Success vs. Failure for site {entered_site}')
    return fig


# TASK 4: callback for the scatter chart
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) &
                   (spacex_df['Payload Mass (kg)'] <= high)]
    if entered_site != 'ALL':
        df = df[df['Launch Site'] == entered_site]
    fig = px.scatter(df, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category',
                     title='Payload vs. Launch Outcome')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
