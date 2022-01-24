import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
from dash import dash_table
from test import *
import pandas as pd
import psycopg2
from test import *
import numpy as np



connection = psycopg2.connect("postgres://postgres:e26519982@localhost:5432/postgres")

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(external_stylesheets=external_stylesheet)


active_ingredients = common_active_ingredients()
df2 = pd.DataFrame(active_ingredients)
number_of_active_ingredients = df2[0].value_counts().values
names_of_active_ingredients = df2[0].value_counts().index
number_of_active_ingredients = number_of_active_ingredients[0:6]
names_of_active_ingredients = names_of_active_ingredients[0:6]
number_of_active_ingredients = pd.Series(number_of_active_ingredients)
names_of_active_ingredients = pd.Series(names_of_active_ingredients)



life_span = life_span()
df6 = pd.DataFrame(life_span)


weight = weight()
df3 = pd.DataFrame(weight)

breed_group = master_function("SELECT * FROM dogs LIMIT 1000", 6)

names_of_dogs = names_of_dogs()
df4 = pd.DataFrame(names_of_dogs)



received_per_day = master_function("SELECT * FROM results LIMIT 10000", 1)
df5 = pd.DataFrame(received_per_day)
received_per_day_value = df5[0].value_counts().values
received_per_day_index = df5[0].value_counts().index

app.layout = html.Div(
        children=[
            html.H1('Veterinary Business Intelligence App'),
            html.Br(),
            html.H3("Visualizations"),
            html.Div(
                children=[
                    dcc.Graph(
                        figure=dict(
                            data=[
                                dict(
                                    x=names_of_dogs,
                                    y=weight,
                                    name='Weight',
                                    type='bar'
                                ),
                                dict(
                                    x=names_of_dogs,
                                    y=life_span,
                                    name='Life Span',
                                    type='bar'
                                )
                            ],
                            layout=dict(
                                title='Life Span / Weight Correlation per Breed '
                            )
                        ),
                        id='breed'
                    )
                ]
            ),
            html.Div(
                children=[
                    dcc.Graph(
                        figure=dict(
                            data=[
                                dict(
                                    x=names_of_dogs,
                                    y=breed_group,
                                    name='Breed Group',
                                    type='bar'
                                ),
                                dict(
                                    x=names_of_dogs,
                                    y=life_span,
                                    name='Life Span',
                                    type='bar'
                                )
                            ],
                            layout=dict(
                                title='Life Span per Breeding Group '
                            )
                        ),
                        id='breed_group'
                    )
                ]
            ),
            html.Div(
                children=[
                dcc.Graph(
                    figure=dict(
                        data=[dict(
                            x=names_of_active_ingredients.values.tolist(),
                            y=number_of_active_ingredients.tolist(),
                            name='Most Common Active Ingredients',
                            type='bar'
                        )],
                        layout=dict(
                            title='Most Common Active Ingredients'
                        )

                    ),
                    id='common-ingredient'
                )
            ]
        ),
            html.Div(
                children=[
                    dcc.Graph(
                        figure=dict(
                            data=[
                                dict(
                                    x=received_per_day_index,
                                    y=received_per_day_value,
                                    name='Amount of reports per day',
                                    marker=dict(
                                        color='rgb(102, 158, 215)'
                                    ),
                                    type='bar'
                                )
                            ],
                            layout=dict(
                                title='Amount of reports per day',
                                showlegends=True
                            )
                        ),
                        id='amount-of-reports-per-day'
                    )
                ]
            )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
