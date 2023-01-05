import os
import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import textwrap
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

options = [
    {"label": "ib_insync", "value": "ib_insync, "},
    {"label": "ibapi", "value": "ibapi, "},
    {"label": "pandas", "value": "pandas, "},
    {"label": "numpy", "value": "numpy, "},
    {"label": "openai", "value": "openai, "},
    {"label": "dash", "value": "dash, "},
    {"label": "dash_bootstrap_components", "value": "dash_bootstrap_components, "},
    {"label": "flask", "value": "flask, "},
    {"label": "sqlalchemy", "value": "sqlalchemy, "},
    {"label": "sqlite3", "value": "sqlite3, "},
    {"label": "asyncio", "value": "asyncio, "},
    {"label": "datetime", "value": "datetime, "},
    {"label": "pytz", "value": "pytz, "},
    {"label": "random", "value": "random, "},
    {"label": "requests", "value": "requests, "},
    {"label": "matplotlib", "value": "matplotlib, "},
    {"label": "tensorflow", "value": "tensorflow, "},
    {"label": "random", "value": "random, "},
    {"label": "scipy", "value": "scipy, "},
    {"label": "scikit-learn", "value": "scikit-learn, "},
    {"label": "pytest", "value": "pytest, "},
    {"label": "seaborn", "value": "seaborn, "},
    {"label": "pyyaml", "value": "pyyaml, "},
    {"label": "tensorflow-gpu", "value": "tensorflow-gpu, "},
    {"label": "scikit-image", "value": "scikit-image, "},
    {"label": "Pillow", "value": "Pillow, "},
    {"label": "sympy", "value": "sympy, "},
    {"label": "spacy", "value": "spacy, "},
    {"label": "opencv-python", "value": "opencv-python, "},
    {"label": "Cython", "value": "Cython, "},
    {"label": "pygame", "value": "pygame, "},
    {"label": "pyglet", "value": "pyglet, "},
    {"label": "pytz", "value": "pytz, "},
    {"label": "PyQt5", "value": "PyQt5, "},
    {"label": "pyodbc", "value": "pyodbc, "},
    {"label": "pyOpenSSL", "value": "pyOpenSSL, "},
    {"label": "pywin32", "value": "pywin32, "},    
    {"label": "PyMySQL", "value": "PyMySQL, "}
    ]

accordion = html.Div(id='packages', children=[dbc.Accordion(start_collapsed=True,
    children=[html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        # Add the checklist to the accordion
                        dbc.Checklist(
                                options=options,
                                inline=True
                            )

                    ]
                ),
                id="collapse"
            )])
        ], 
    )],className='row')  

accordion2 = dbc.Accordion(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    # Add the checklist to the accordion
        html.Div([
                    html.P('POSSIBILITIES IGNORED', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                    dcc.Slider(
                        id='top_p',
                        min=0,
                        max=1,
                        step=0.01,
                        value=0.95,
                        marks={
                            0.2: {'label': '20%'},
                            0.4: {'label': '40%'},
                            0.6: {'label': '60%'},
                            0.8: {'label': '80%'}
                        },
                    )
                    ], className='row', style={'marginBottom':'0rem', 'marginTop':'0rem'}),
                    html.Div([
                        html.P("BEST OF", style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                        dcc.Slider(
                            id='n',
                            min=1,
                            max=5,
                            step=1,
                            value=1,
                            marks={
                                2: {'label': '2'},
                                3: {'label': '3'},
                                4: {'label': '4'},
                                5: {'label': '5'}                                         
                                }
                        )
                    ], className='row'),
                    html.Div([
                        html.H6('FREQUENCY PENALTY', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                        dcc.Slider(
                            id='frequency_penalty',
                            min=0,
                            max=2,
                            step=0.01,
                            value=0.15,
                            marks={
                                0.5: {'label': '25%'},
                                1: {'label': '50%'},
                                1.5: {'label': '75%'}
                            }
                        )
                    ], className='row'),
                    html.Div([
                        html.H6('PRESENCE PENALTY', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                        dcc.Slider(
                            id='presence_penalty',
                            min=0,
                            max=2,
                            step=0.01,
                            value=0.3,
                            marks={
                                0.5: {'label': '25%'},
                                1: {'label': '50%'},
                                1.5: {'label': '75%'},
                                        }
                                )
                    ], className='row'),
                    html.Div([
                        html.P('STOP TOKEN', style={'fontWeight':'bold', 'marginBottom':'0rem', 'paddingBottom':'0rem'}),
                        dcc.Textarea(
                            id='stop',
                            value='',
                            placeholder='Enter a stop token',
                            style={'width': '60%', 'height': '2rem', 'margin-left':'1rem', 'padding-right':'1rem', 'marginTop':'0rem', 'marginBottom':'.4rem'}
                        )
                    ], className='row'),
                    html.Div([
                            dcc.Store(
                                id='engine',
                                data='code-davinci-002'
                                # options=[
                                #     {'label': 'code', 'value': 'code-davinci-002'},                                                    
                                #     {'label': 'davinci', 'value': 'text-davinci-003'},
                                #     {'label': 'curie', 'value': 'text-curie-001'},
                                #     {'label': 'ada', 'value': 'text-ada-001'},
                                #     {'label': 'babbage', 'value': 'text-babbage-001'}
                                # ],
                                # style={'marginBottom':'.25rem'}
                            )
                        ], className='row')
                ]
            ),
            id="collapse2"
        )
    ], className='row', start_collapsed=True
)   

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server 
# Dash layout
app.layout = html.Div(className='container',
    children=[
        Html.Div([
            html.Img(src='https://fastfile.cloud/gptdevlogo.png', style={'height':'7%', 'width':'auto'}),
        ], className='row' style={'alignt-text':'left'}),
        html.Div([
            html.Hr(),
            html.Div(className='row', 
                children=[
                    html.Div(className='col-md-8', children=[
                        dcc.Textarea(
                            id='prompt',
                            value=str(''),
                            placeholder='Enter a prompt',
                            style={'width': '100%', 'height': '98.5%', 'marginBottom':'10px', 'paddingBottom':'10px'}
                        )
                    ]
                ),
                html.Div(className='col-md-4', 
                    children=[
                        html.Div(className='row',
                            children=[
                            html.Div(
                                className='row',
                                children=[
                                html.Div([
                                    html.P('Language', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                                    dcc.Dropdown(
                                        id='language',
                                        value='\* Language: Python 3 \r\n',
                                        options=[
                                            {'label': 'Python 3', 'value': '\* Language: Python 3 \r\n'},                                                    
                                            {'label': 'Node.JS', 'value': '\* Language: node.js \r\n'},
                                            {'label': 'SQL', 'value': '\* Language: SQL \r\n'},
                                            {'label': 'Typescript', 'value': '\* Language: TypeScript \r\n'},
                                            {'label': 'Bash', 'value': '\* Language: Bash \r\n'},
                                            {'label': 'Task Helper', 'value': '\* Goal: Complete the task you are given. \r\n Task: '}
                                        ],
                                        style={'marginBottom':'.25rem'}
                                    ),
                                    ], className='row'),
                                    html.Div([
                                    html.P('Packages', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                                    accordion
                                    ], className='row'),
                                    html.P('CREATIVITY', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                                    dcc.Slider(
                                        id='temperature',
                                        min=0,
                                        max=1,
                                        step=0.01,
                                        value=0.2,
                                        marks={
                                            0.25: {'label': '25%'},
                                            0.5: {'label': '50%'},
                                            0.75: {'label': '75%'}
                                        }
                                    )
                                ]
                            ),
                            html.Div([
                                    html.P('MAX TOKENS', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                                    dcc.Slider(
                                        id='max_tokens',
                                        min=48,
                                        max=4048,
                                        step=1,
                                        value=1548,
                                        marks={
                                            1048: {'label': '1000'},
                                            2048: {'label': '2000'},
                                            3048: {'label': '3000'}
                                        }
                                    )])
                                ]),
                            html.Div([
                                    html.P('OTHER OPTIONS', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                                    accordion2],className="row"),  
                        html.Br(),    

                                    ]
                                ),
                                                        html.Div([
                            html.Button('Generate', id='generate', n_clicks=0, className='btn btn-primary')
                            ], 
                        className='row justify-content-center'),
                        html.Div([
                            html.Pre(id='output', children='', style={'whiteSpace': 'pre-wrap'})
                            ], 
                        className='row justify-content-center')
                            ]
                        ),
                        
                    ] 
        )   
    ]
)

html.Div([
                            html.H5('Choices'),
                            dcc.Dropdown(
                                id='choices',
                                options=[
                                    {'label': '1', 'value': 1},
                                    {'label': '2', 'value': 2},
                                    {'label': '3', 'value': 3},
                                    {'label': '4', 'value': 4},
                                    {'label': '5', 'value': 5},
                                    {'label': '6', 'value': 6},
                                    {'label': '7', 'value': 7},
                                    {'label': '8', 'value': 8},
                                    {'label': '9', 'value': 9},
                                    {'label': '10', 'value': 10}
                                ],
                                value=1
                            )]),
# Dash callback
@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('generate', 'n_clicks')],
    [dash.dependencies.State('prompt', 'value'),
    dash.dependencies.State('temperature', 'value'),
    dash.dependencies.State('top_p', 'value'),
    dash.dependencies.State('n', 'value'),
    dash.dependencies.State('max_tokens', 'value'),
    dash.dependencies.State('frequency_penalty', 'value'),
    dash.dependencies.State('presence_penalty', 'value'),
    dash.dependencies.State('stop', 'value'),
    dash.dependencies.State('engine', 'data'),
    dash.dependencies.State('packages', 'children'),
    dash.dependencies.State('language', 'value')])
def update_output(n_clicks, prompt, temperature, top_p, n, max_tokens, frequency_penalty, presence_penalty, stop, engine, language, packages):
    if n_clicks > 0:
        response = openai.Completion.create(
            prompt= f"Language: {language} \r\n Packages: {packages} \r\n Goal: {prompt} \r\n\ Request: Achieve the goal by writing efficient code. \r\n */",
            temperature=temperature,
            top_p=top_p,
            n=n,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
            engine=engine

        )

        return textwrap.indent(response['choices'][0]['text'], '\u00A0\u00A0\u00A0')
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=False)
