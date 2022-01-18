import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
from dash import dash_table
from norm_old import *
import pandas as pd
import psycopg2
from norm_old import *
import numpy as np



connection = psycopg2.connect("postgres://postgres:banana_2@localhost:5432/postgres")

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(external_stylesheets=external_stylesheet)


breed = common_breeds()


# print(breed)

df = pd.DataFrame(breed)


number_of_breeds = df[0].value_counts().values
names_of_breeds = df[0].value_counts().index
names_of_breeds = pd.Series(names_of_breeds)
number_of_breeds = pd.Series(number_of_breeds)
number_of_breeds = number_of_breeds[0:6]
names_of_breeds = names_of_breeds[0:6]


active_ingredients = common_active_ingredients()
df2 = pd.DataFrame(active_ingredients)
number_of_active_ingredients = df2[0].value_counts().values
names_of_active_ingredients = df2[0].value_counts().index
number_of_active_ingredients = number_of_active_ingredients[0:6]
names_of_active_ingredients = names_of_active_ingredients[0:6]
number_of_active_ingredients = pd.Series(number_of_active_ingredients)
names_of_active_ingredients = pd.Series(names_of_active_ingredients)
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


life_span = life_span()
df6 = pd.DataFrame(life_span)


weight = weight()
df7 = pd.DataFrame(weight)

breed_group = master_function("SELECT * FROM dogs LIMIT 1000", 5)

names_of_dogs = names_of_dogs()
df8 = pd.DataFrame(names_of_dogs)


veddra_term_name = veddra_term_name()
df9 = pd.DataFrame(veddra_term_name)


previous_exposure_to_drug = previous_exposure_to_drug()
df10 = pd.DataFrame(previous_exposure_to_drug)
previous_exposure_to_drug = df10[0].value_counts().values


unique_id_number_test = unique_id_number_test()
df11 = pd.DataFrame(unique_id_number_test)

duration_value = master_function("SELECT * FROM temp_table LIMIT 10000", 3)
# df12 = pd.DataFrame(duration_value)
duration_value = np.mean(duration_value)
print(duration_value)

false_duration_value = master_function("SELECT * FROM temp_table2 LIMIT 10000", 3)
df14 = pd.DataFrame(false_duration_value)
false_duration_value = np.mean(false_duration_value)

false_previous_exposure_to_drug = master_function("SELECT * FROM temp_table2 LIMIT 10000", 2)
df15 = pd.DataFrame(false_previous_exposure_to_drug)
# test = df.head().to_dict('list')
# print("ST2 Reqeust : {}".format(test))

false_most_common_breeds = master_function("SELECT * FROM temp_table3 LIMIT 10000",2 )
df16 = pd.DataFrame(false_most_common_breeds)
# false_most_common_breeds_value = df16[0].value_counts().values
# false_most_common_breeds_index = df16[0].value_counts().index
# print(false_most_common_breeds_value)
# print(false_most_common_breeds_index)

most_common_breeds_duration_count = master_function("SELECT * FROM breed_duration LIMIT 10000", 2)
most_common_breeds_duration_value = master_function("SELECT * FROM breed_duration2 LIMIT 10000", 1)
most_common_breeds_duration_name = master_function("SELECT * FROM breed_duration2 LIMIT 10000", 0)
# df17 = pd.DataFrame(most_common_breeds_duration_name)
# most_common_breeds_duration_name = df17[0].value_counts().index
# most_common_breeds_duration_name = most_common_breeds_duration_name[0:10]
# print(most_common_breeds_duration_name)

height = master_function("SELECT * FROM dogs LIMIT 1000", 4)

received_per_day = master_function("SELECT * FROM results LIMIT 10000", 1)
df19 = pd.DataFrame(received_per_day)
received_per_day_value = df19[0].value_counts().values
received_per_day_index = df19[0].value_counts().index

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
                                title='Life Span / Breed Group Correlation per Breed '
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
                            data=[
                                dict(
                                    x=names_of_dogs,
                                    y=height,
                                    marker=dict(
                                        color='rgb(85, 177, 5)'
                                    ),
                                    name='Height',
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
                                title='Life Span / Height Correlation per Breed '
                            )
                        ),
                        id='life-span-height-breed'
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
                            data=[dict(
                                x=common_reactions_names.values.tolist(),
                                y=common_reactions.tolist(),
                                marker=dict(
                                    color='rgb(177, 35, 177)'
                                ),
                                name='Most common Reactions',
                                type='bar'
                            )],
                            layout=dict(
                                title='Most common Reactions'
                            )

                        ),
                        id='common-reactions'
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
                            title='Most Common Reactions Per Breed',
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
                                    x=most_common_breeds_duration_name,
                                    y=most_common_breeds_duration_value,
                                    name='Duration In Days',
                                    marker=dict(
                                        color='rgb(177, 35, 5)'
                                    ),
                                    type='bar'
                                )
                            ],
                            layout=dict(
                                title='Drugs / Arrwsties',
                                showlegends=True
                            )
                        ),
                        id='drugs-arrwsties-id'
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
