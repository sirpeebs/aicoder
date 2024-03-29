import os
import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import textwrap
import openai

# OpenAI API key
openai.api_key =os.getenv('OPENAI_API_KEY')
# Dash app

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server 
# Dash layout
app.layout = html.Div(className='container',
    children=[
        html.Div([
            html.Center([
            html.Img(src='https://fastfile.cloud/logos/gptdevlogo.png', style={'max-width':'20%', "margin-bottom":"1%", 'height':'auto','margin-top':'1%'}, className='center'),
        ]),
            # html.Hr(),
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
                                            value='',
                                            placeholder='Choose Language You Code In',
                                            options=[
                                                {'label': 'Python 3', 'value': '# Python 3'},                                                    
                                                {'label': 'Node.JS', 'value': '// node.js'},
                                                {'label': 'SQL', 'value': '# SQL'},
                                                {'label': 'Typescript', 'value': '// TypeScript'},
                                                {'label': 'Shell Script', 'value': '# Shell'},
                                                {'label': 'Not Coding, Standard GPT-3.5', 'value': 'regular_gpt'}
                                            ],
                                            style={'marginBottom':'.25rem'}
                                        ),
                                        ], className='row'),
                                        html.P('Creativity', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                                        dcc.Slider(
                                            id='temperature',
                                            min=0,
                                            max=1,
                                            step=0.01,
                                            value=0.12,
                                            marks={
                                                0.25: {'label': '25%'},
                                                0.5: {'label': '50%'},
                                                0.75: {'label': '75%'}
                                            }
                                        )
                                    ]
                                ),
                                html.Div([
                                    html.P('In-the-Box Thinking', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
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
                                        html.P("Repsonse is Best Result of ___ trys", style={'fontWeight':'bold', 'marginBottom':'0rem'}),
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
                                        html.H6('Resistance to Repeating Anything', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
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
                                        html.H6('Resistance to Echoing a Repaet', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
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
                                        html.P('Expected Words in Response', style={'fontWeight':'bold', 'marginBottom':'0rem'}),
                                        dcc.Slider(
                                            id='max_tokens',
                                            min=48,
                                            max=3990,
                                            step=1,
                                            value=441,
                                            marks={
                                                1048: {'label': '800'},
                                                2048: {'label': '1600'},
                                                3048: {'label': '2400'}
                                            }
                                        )
                                    ], className='row'),
                                    html.Div([
                                        html.P('Repsonse Stop Symbol', style={'fontWeight':'bold', 'marginBottom':'0rem', 'paddingBottom':'0rem'}),
                                        dcc.Textarea(
                                            id='stop',
                                            value='',
                                            placeholder='Enter a stop token',
                                            style={'width': '60%', 'height': '2rem', 'margin-left':'1rem', 'padding-right':'1rem', 'marginTop':'0rem', 'marginBottom':'.4rem'}
                                        )
                                    ], className='row'),
                                    html.Div([
                                            dcc.Store(
                                                id='engine'
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
        ),
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
    dash.dependencies.State('language', 'value')])
def update_output(n_clicks, prompt, temperature, top_p, n, max_tokens, frequency_penalty, presence_penalty, stop, language):
    if n_clicks > 0:
        if language == 'regular_gpt':
            model='text-davinci-003'
            prompt_value={prompt}
        else:
            model='text-davinci-003'
            prompt_value= f'Setup as an expert coder in {language} who writes flawless code when given a requested goal.\r\nRequested Goal: {prompt}'

        response = openai.Completion.create(
            prompt=prompt_value,
            temperature=temperature,
            top_p=top_p,
            n=n,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
            engine=model

        )

        return textwrap.indent(response['choices'][0]['text'], '\u00A0\u00A0\u00A0')
    else:
        return ''

if __name__ == '__main__':
    app.run_server()
