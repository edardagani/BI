import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
from dash import dash_table
from norm_old import *
import pandas as pd
import psycopg2
from norm_old import *



connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(external_stylesheets=external_stylesheet)


breed = common_breeds()


# print(breed)

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
# print(names_of_active_ingredients)
# print(number_of_active_ingredients)

common_reactions = common_reactions()
df3 = pd.DataFrame(common_reactions)
common_reactions = df3[0].value_counts().values
common_reactions_names = df3[0].value_counts().index
common_reactions = common_reactions[0:6]
common_reactions_names = common_reactions_names[0:6]

duration = duration()
df4 = pd.DataFrame(duration)
duration = df4[0][0:50]
print(duration)


age = age()
df5 = pd.DataFrame(age)
age = df5[0][0:50]

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
                            data=[
                                dict(
                                    x=names_of_breeds.values.tolist(),
                                    y=number_of_breeds.tolist(),
                                    name='Most common Breed',
                                    type='bar'
                                ),
                                dict(
                                    x=names_of_active_ingredients.values.tolist(),
                                    y=number_of_active_ingredients.tolist(),
                                    name='Most Active Ingredients',
                                    type='bar'
                                )
                            ],
                            layout=dict(
                                title='Most Common Active Ingredients / Breeds'
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
        ),
            html.Div(
                children=[
                    dcc.Graph(
                        figure=dict(
                            data=[
                                dict(
                                x="Number of Days",
                                y=duration.tolist(),
                                name='Duration',
                                type='line'
                            )],
                            layout=dict(
                                title='Duration'
                            )

                        ),
                        id='duration-days'
                    )
                ]
            ),
            html.Div(
                children=[
                dcc.Graph(
                    figure=dict(
                        data=[
                            dict(
                                x=names_of_breeds.values.tolist(),
                                y=common_reactions.tolist(),
                                name='Most Common Reactions',
                                marker=dict(
                                    color='rgb(177, 35, 5)'
                                ),
                                type='bar'
                            ),
                            dict(
                                x=common_reactions_names.values.tolist(),
                                y=number_of_breeds.tolist(),
                                name='Most Common Breeds',
                                marker=dict(
                                    color='rgb(26, 118, 255)'
                                ),
                                type='bar'
                            ),
                        ],
                        layout=dict(
                            title='God help us',
                            showlegends=True
                        )
                    ),
                    id='Common-reactions-breeds'
                )
            ]
        ),
            html.Div(
                children=[
                    dcc.Graph(
                        figure=dict(
                            data=[
                                dict(
                                    x="Number of Days",
                                    y=age.tolist(),
                                    name='Age in Years',
                                    marker=dict(
                                        color='rgb(177, 35, 5)'
                                    ),
                                    # type='bar'
                                ),
                                dict(
                                    x="Number of Days",
                                    y=duration.tolist(),
                                    name='Duration In Days',
                                    marker=dict(
                                        color='rgb(26, 118, 255)'
                                    ),
                                    # type='bar'
                                ),
                            ],
                            layout=dict(
                                title='Age / Duration',
                                showlegends=True
                            )
                        ),
                        id='Age-Duration-id'
                    )
                ]
            )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
