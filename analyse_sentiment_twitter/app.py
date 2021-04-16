import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from textwrap import dedent
from dash.dependencies import Input, Output, State
import plotly.express as px
from global_querie import *
import sqlite3
import plotly
import StreamTwitt as TTT
from assets.content import *
import pandas as pd
import threading


result_available = threading.Event()

########################## data ################################

app = dash.Dash(__name__, external_stylesheets=[
                dbc.themes.BOOTSTRAP], title='TweetFeeling')
server = app.server

########################## layout ################################


app.layout = html.Div(
    [title_block,
     dbc.Row(dcc.Markdown(markdown_text, highlight_config={"theme": "light"}
                          )
             ),
     tabs,
     html.Div(popover, hidden=True)]  # style={'width': '90%', 'marginLeft': 'auto', 'marginRight': 'auto'}
    ,  style={'width': '90%', 'marginLeft': 'auto', 'marginRight': 'auto', "position": "relative", 'top': '0px'})

########################## callback ################################
### On ne commente pas les fonctions callback qui n'ont pas vocations à être tulisé ailleurs et qui sont propre au focntionnement de cette page
### chaque focntion sous les callback prend en entrée les attributs des objets spécifiés dans les inputs et renvoie l'attribue spécifié de l'objet dans le output 


@ app.callback(
    [Output(component_id='tweet_redactor_output', component_property='children'),
     Output(component_id='keyword_output', component_property='children'),
     Output(component_id='selected_methode', component_property='children'),
     # Output(component_id='tweet_redactor_output',component_property='value'),
     # Output(component_id='keyword_output', component_property='value'),
     # Output(component_id='selected_methode', component_property='value')
     ],
    [Input(component_id='tweet_redactor_input', component_property='n_submit'),
     Input(component_id='search_words', component_property='n_submit'),
     Input(component_id='used_methode', component_property=('value'))],
    [State(component_id='tweet_redactor_input', component_property='value'),
     State(component_id='search_words', component_property='value'), ],
)
def update_output_div(tweet_redactor_submit, search_words_submit, method, tweet_redactor_input, search_words):
    '''
    Permet d'afficher le résulats des Input de l'uilisateur et de mettre à jour l'état des variables quand l'utilisateur appuie sur la touche 'entrée'
    '''
    if tweet_redactor_input == None or tweet_redactor_input == "":
        tweet_redactor_output = 'Aucun'
    else:
        tweet_redactor_output = tweet_redactor_input
    if search_words == None or search_words == "":
        keyword_output = 'Aucuns'
    else:
        keyword_output = search_words
    return tweet_redactor_output, keyword_output, method



@ app.callback([Output(component_id="used_methode", component_property="options"), ],
               [Input(component_id='tweet_redactor_output',
                      component_property='children'),
                Input(component_id='keyword_output',
                      component_property='children'),
                Input(component_id='selected_methode',
                      component_property='children'), ])
def update_buttons(tweet_redactor, keyword, selected):
    '''permet de rendre valable certaine méthode en focntion de ce que rentre l'utiisateur '''

    if (tweet_redactor == 'Aucun' and keyword == 'Aucuns'):
        return [disabled(True, True, True)]
    elif (tweet_redactor == "Aucun" and keyword != 'Aucuns'):
        return [disabled(False, True, True)]
    elif (tweet_redactor != "Aucun" and keyword == 'Aucuns'):
        return [disabled(False, False, False)]
    elif (tweet_redactor != "Aucun" and keyword != 'Aucuns'):
        return [disabled(False, False, False)]
    else:
        return [disabled(True, True, True)]


@ app.callback([Output(component_id="tab1_content", component_property="figure"),
                Output(component_id="tab2_content",
                       component_property="figure"),
                Output(component_id="reponse", component_property="children"),
                Output(component_id="nb_tweets",
                       component_property="children"),
                # Output(component_id="wordcloud", component_property="children")
                Output(component_id="tab1_div",
                       component_property="hidden"),
                Output(component_id="tab2_div", component_property="hidden"),
                Output(component_id="tab3_div", component_property="hidden"),
                Output(component_id="graph-update", component_property="disabled")],
               [Input("card-tabs", "active_tab"),
                Input(component_id='tweet_redactor_output',
                      component_property='children'),
                Input(component_id='keyword_output',
                      component_property='children'),
                Input(component_id='selected_methode',
                      component_property='children'),
                Input(component_id='nb_slider', component_property='value'),
                Input(component_id='tweet_redactor_input',
                      component_property='n_submit'),
                Input(component_id='search_words', component_property='n_submit'), ]
               )
def update_fig(tab, tweet_redactor, keyword, selected, nb_tweets, n_submit_tweet_redactor, n_submit_search_words):
    '''affiche les graphiques ou non en focntion de la page et met à jours les graphiques en fonctions des inputs
    '''
    Blank_figure = {'data': [], }

    if tab == 'week_page' and selected != None:

        ######page 1 ######

        hidden_fig3 = True
        if (tweet_redactor == 'Aucun' and keyword == 'Aucuns'):
            return Blank_figure, Blank_figure, dbc.Alert("Veuillez sélectionner un compte ou des mots clés", color="danger"), nb_tweets, True, True, hidden_fig3, True   
        elif (tweet_redactor != "Aucun" or keyword != "Aucuns"):

            df = main(nb_tweets, tweet_redactor, " AND ".join(
                list(keyword.split(', '))), selected)
            reponse = dbc.Alert("Requête correcte", color="success"),
            if "Sentiment" in df.keys():
                fig = px.line(df, y="Sentiment",)
                hidden_fig1 = False
            else:
                fig2 = Blank_figure
                reponse = popover
                hidden_fig1 = True
            if df["Sentiment_IA"].values[1] != None:
                fig2 = px.bar(df, x="Sentiment_IA")
                hidden_fig2 = False
            else:
                fig2 = Blank_figure
                reponse = dbc.Alert(
                    "Requête correcte, mais pas assez de tweets pour détailler les sentiments", color="warning")
                hidden_fig2 = True
            print(fig, fig2, reponse, nb_tweets, hidden_fig1,
                  hidden_fig2, hidden_fig3, True)
            return fig, fig2, reponse, nb_tweets, hidden_fig1, hidden_fig2, hidden_fig3, True

            ######page 2######

    elif tab == 'streaming_page':
        TTT.create_table()
        hidden_fig3 = False
        reponse = dbc.Alert("Streaming en cours", color="success"),
        fig = Blank_figure
        fig2 = Blank_figure
        hidden_fig1 = True
        hidden_fig2 = True
        return fig, fig2, reponse, nb_tweets, hidden_fig1, hidden_fig2, hidden_fig3, False

    else:
        print(Blank_figure, Blank_figure, dbc.Alert(
            "Veuillez entrer un sélection valide", color="danger"), nb_tweets, True, True, True,)
        return Blank_figure, Blank_figure, dbc.Alert("Veuillez entrer un sélection valide", color="danger"), nb_tweets, True, True, True, True


@ app.callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    ''''affiche le contenu du message d'erreur quand on clique dessus''' 
    if n:
        return not is_open
    return is_open


result_available = threading.Event()


@app.callback([Output(component_id='live-graph', component_property='figure'),
               Output(component_id='live-graph_line', component_property='figure')],
              [Input(component_id="tab3_div", component_property="hidden"),
               Input(component_id='keyword_output',
                     component_property='children'),
               Input(component_id='nb_slider', component_property='value'),
               Input(component_id='graph-update', component_property='n_intervals')])
def update_graph_scatter(tab3_div_hidden, keyword, nb_tweets, IT):
    '''met à jour le graphique du streaming à chaque n_interval et lance le streaming dans un thread différent'''
    Blank_figure = {'data': [], }
    if tab3_div_hidden == False:


        #print('----ici----')


        thread = threading.Thread(
            target=TTT.methode_4_extract(keyword, round(nb_tweets)))
        thread.start()

        # thread.join()  #pour attendre la fin du thread
        #print("-------end-------")

        conn = sqlite3.connect('BDD.db')
        #c = conn.cursor()

        # ici on ne prend pas en compte les mots clés encore :

        df = pd.read_sql(
            "SELECT * FROM sentiment", conn)
        # WHERE tweet LIKE '%e%' ORDER BY unix DESC LIMIT 1000".format(keyword)

        # conn.close()



        # df.sort_values('unix', inplace=True)
        # df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
        # df.dropna(inplace=True)


        # X = df.unix.values[-100:]
        # Y = df['Sentiment'].values[-100:]

        # ici on plot (a affiner ?) :

        data = plotly.graph_objs.Scatter(
            y=df["sentiment"], name='Scatter', mode='lines+markers')
        fig_line = {'data': [data]}

        fig = px.histogram(df[df['sentiment'] != 0], x="sentiment")

        # fig_line = {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(X), max(X)]),
        #                                           yaxis=dict(range=[min(Y), max(Y)]),)}

        return fig, fig_line

    else:

        return Blank_figure, Blank_figure


if __name__ == '__main__':
    app.run_server(debug=True)
