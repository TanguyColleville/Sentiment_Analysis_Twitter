import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
from textwrap import dedent



markdown_text = dedent('''
>*Version 1.0 - Réalisé par Tanguy Colleville, Oscar Volgler, Louis Moser & Ghislain Flichy* \n
*Vous trouverez [ici](https://gitlab-cw2.centralesupelec.fr/ghislain.flichy/analyse_sentiment_twitter) le projet sur Gitlab.*
''')
logo_path = "assets/TweetFeeling_CS_Twitter.png"
encoded_logo = base64.b64encode(open(logo_path, 'rb').read())

###
logo = html.Img(
    src='data:image/png;base64,{}'.format(encoded_logo.decode()), height="90",)


##

title_block = dbc.Row([
    dbc.Col(html.Div([html.H1("TweetFeeling",), html.H5("Analyse de l'opinion sur un sujet donné à travers Twitter")],
                     style={'margin': 'auto'}), width='auto'),
    dbc.Col(html.Div(logo, style={'margin': 'auto'}), width='auto'),
],
    justify="around",
    className='TitleBlock',
)

##

tweet_redactor = dbc.FormGroup(
    [
        dbc.Label("Compte Twitter", width=4),
        dbc.Col(
            [
                dbc.Input(type="text", id="tweet_redactor_input",
                          placeholder="@CentraleSupelec, @EmmanuelMacron ..."),
            ],
            width=8,
        ),
    ],
    row=True,
)

###

key_words = dbc.FormGroup(
    [
        dbc.Label("Mots Clés", width=4),
        dbc.Col(
            dbc.Input(
                type="text",
                id="search_words",
                placeholder="Evènement, conférence ...",
            ),
            width=8,
        ),
    ],
    row=True,
)

##

option_list = [{"label": "Tous les tweets", "value": 1, }, {
    "label": "Retweets (des 5 derniers Tweets de l'émetteur)", "value": 2, }, {"label": "Réponses (aux 5 derniers Tweets de l'émetteur)", "value": 3, }, ]
##

def disabled(a, b, c):
    """retourne l'options pour dbc.RadioItems qui grise les radios boutons dans la liste
     entrée : True or False pour griser ou ne pas griser le bouton
     sortie : attribut "options" (liste de dictionnaire )  de dbc.RadioItems
    """
    return ([{"label": "Tous les tweets", "value": 1, "disabled": a}, {"label": "Retweets (des 5 derniers Tweets de l'émetteur)", "value": 2, "disabled": b}, {"label": "Réponses (aux 5 derniers Tweets de l'émetteur)", "value": 3, "disabled": c}, ])

##

methode = dbc.FormGroup(
    [
        dbc.Label("Type de recherche", width=4),
        dbc.Col(
            dbc.RadioItems(
                id="used_methode",
                options=option_list,
            ),
            width=8,
        ),
    ],
    row=True,
)


##


slider_title = html.Div(dbc.Row(
    [html.Div("Nombre de tweets :  "), html.Div(id='nb_tweets')]))

##


slider = html.Div([slider_title, dcc.Slider(
    min=150,
    max=400,
    step=1,
    value=200,
    id='nb_slider',
)])


##

form = dbc.Form([tweet_redactor, key_words, methode, slider])
conf = dbc.Alert(
    html.Div(
        [
            html.Div(
                dbc.Row(
                    [
                        html.Div(
                            'Compte actuellement sélectionné : \t '),
                        html.Div(
                            id='tweet_redactor_output')
                    ]
                )
            ),
            html.Div(
                dbc.Row(
                    [
                        html.Div(
                            'Mots  clss actuellement sélectionnés : \t '),
                        html.Div(id='keyword_output')
                    ]
                )
            ),
            html.Div(
                dbc.Row(
                    [
                        html.Div(
                            ' Type de recherche actuellement sélectionné : \t '),
                        html.Div(id='selected_methode')
                    ]
                )
            ),
        ]
    ), color='light'
)


##


confirmation = [dbc.Card(
    dbc.CardBody(conf), className="mt-3")]
tab_content = [dbc.Card(
    dbc.CardBody(form), className="mt-3",)]
##


figure_stream_line = dcc.Graph(
    figure={'data': []}, id='live-graph_line', animate=False)

##

figure_stream = [dcc.Graph(figure={'data': []}, id='live-graph', animate=False),
                 dcc.Interval(id='graph-update', interval=2*1000, disabled=True)]

##

tabs = dbc.Card(
    [
        dbc.CardHeader(style={'backgroundColor': '#EEEEEE', "inverse": 'True'},
                       children=[dbc.Tabs(
                           [
                               dbc.Tab(label="Tweets de la semaine",
                                       tab_id="week_page"),
                               dbc.Tab(label="Tweets en live",
                                       tab_id='streaming_page'),
                           ],
                           id="card-tabs",
                           card=True,
                           active_tab="week_page"
                       )]
                       ),
        dbc.CardBody(
            dbc.Row([
                dbc.Col(html.Div(tab_content, id="card-content")),
                dbc.Col(html.Div(confirmation, id='confirmation')),
            ])
        ),
        html.Div(children=[dcc.Graph(id='tab1_content')],
                 id='tab1_div', hidden=False),
        html.Div(children=[dcc.Graph(id='tab2_content')],
                 id='tab2_div', hidden=False),
        html.Div([html.Div(children=figure_stream_line), html.Div(
            children=figure_stream)], id='tab3_div', hidden=True),
        # html.Div(html.Img(id="wordcloud"),
        html.Div(id="reponse")
    ], style={'width': '100%'},
)


##


spinners = html.Div(dbc.Container(
    [
        dbc.Row(dbc.Col(dbc.Spinner(spinner_style={
            "width": "6rem", "height": "6rem"}), width=2), justify='center', align='center')
    ],
    style={'height': '20vh'}
)
)


##

popover = html.Div(
    [
        dbc.Button(
            "Erreur API", id="popover-target", color="danger"
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader("ERREUR API : Trop de requête "),
                dbc.PopoverBody(
                    "Le compte developpeur Twitter dispose d'un accès gratuit à l'API et est donc limité en nombre de requêtes. Essayez plus tard"),
            ],
            id="popover",
            is_open=False,
            target="popover-target",
        ),
    ]
)

##


