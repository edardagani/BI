import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
from dash import dash_table

import pandas as pd
import psycopg2
from norm import *



connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(external_stylesheets=external_stylesheet)


breed = common_breeds()


print(breed)

df = pd.DataFrame(breed)


number_of_breeds = df[0].value_counts().values
names_of_breeds = df[0].value_counts().index
number_of_breeds = number_of_breeds[0:6]
names_of_breeds = names_of_breeds[0:6]


active_ingredients = common_active_ingredients()
df2 = pd.DataFrame(active_ingredients)
number_of_active_ingredients = df2[0].value_counts().values
names_of_active_ingredients = df2[0].value_counts().index
number_of_active_ingredients = number_of_active_ingredients[0:6]
names_of_active_ingredients = names_of_active_ingredients[0:6]
print(names_of_active_ingredients)
print(number_of_active_ingredients)

# test = df.head().to_dict('list')
# print("ST2 Reqeust : {}".format(test))

app.layout = html.Div(
    children=[
    html.H1('BI APP PLEZ WORK'),
    html.Br(),
    html.H3("My Visualizations"),
    html.Div(
        children=[
            dcc.Graph(
                figure=dict(
                    data=[dict(
                        x=names_of_breeds.values.tolist(),
                        y=number_of_breeds.tolist(),
                        name='Most common Breed',
                        type='bar'
                    )],
                    layout=dict(
                        title='Most Common Breeds'
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
                        data=[dict(
                            x=names_of_active_ingredients.values.tolist(),
                            y=number_of_active_ingredients.tolist(),
                            name='Most common Active Ingredients',
                            type='bar'
                        )],
                        layout=dict(
                            title='Most common Active Ingredients'
                        )

                    ),
                    id='common-ingredient'
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
