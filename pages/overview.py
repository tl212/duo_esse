import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


contributors_10 = pd.read_csv(DATA_PATH.joinpath("contributors_10.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Executive Summary"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    This report summarises suspicious activity characteristics of money laundering activities based on a dataset containing 16940 transactions over a period of \
                                    30 months, from June, 2012 to December, 2014 containing transactions from \
                                    the Danske Bank’s Estonian branch. At the core of the suppoused scheme the analysis point to four bank accounts belonging to \
                                    to four shell companies registered in the UK. \
                                    The report indicates US$ 2.9 billion in suspicious activities. \
                                    Baktelekom MMC was the mysterious largest contributor that used an account at IBA \
                                    to transfer US$ 1.4 billion into only two of the four shell companies. It is not clear where \
                                    Baktelekom’s money came from – perhaps loans from the government, the Azerbaijan Central Bank, \
                                    or the IBA itself.\
                                    What’s clear is that it didn’t earn it. The company has no website and no evident commercial activity, \
                                    making it highly likely that it was not the original source of the money, \
                                    but rather a holding vehicle for money that came from elsewhere. The company’s name appears \
                                    to be designed to confuse people and make them think it’s related to Baktelecom, a major Azerbaijani \
                                    mobile phone operator (the names differ by one letter). \
                                    Baktelekom transferred money 530 times from 2013 to 2014, with transactions occurring every other day \
                                    and sometimes even three times in one day. The smallest single transfer was just $138,000 while the largest was \
                                    over US$ 6 million, with the total amounting to US$ 1.4 billion over that period. \
                                    The second-largest contributor was Faberlex LP, a UK company that sent in over US$ 169 million. \
                                    Faberlex LP is owned by Maharram Ahmadov, 51, an Azerbaijani citizen who also owns, on paper, \
                                    two of the core Azerbaijani Laundromat companies, Hilux Services LP and Polux Management LP. \
                                    Registration documents filed with the UK company registry confirm that Faberlex, Hilux, and Polux \
                                    share two of the same secretive offshore companies as shareholders. \
                                    Ahmadov’s passport, personal details, phone number and signatures are attached to the dossier \
                                    that Hilux and Polux filed to open the accounts. \
                                    The problem is that Ahmadov is not a billion-dollar financier and businessman. \
                                    He is actually a modest driver in Baku, the capital of Azerbaijan. \
                                    He lives in a humble makeshift home in the Gushchuluq neighborhood, an area of small poultry farms \
                                    on the outskirts of the capital. \
                                    The third-largest contributor to the Laundromat, to the tune of $105 million, is Jetfield Networks Limited. \
                                    \
                                    IBA, which clearly played a pivotal role in the Laundromat, is also a big player in the Azerbaijani economy. \
                                    It is the largest retail bank in Azerbaijan by loan volume, providing loans, credit, deposits, \
                                    and current accounts to nearly 750,000 customers. This is a significant number in Azerbaijan, \
                                    a country with a population less than 10 million. \
                                    \
                                    It is possible that Baktelekom’s money came from IBA loans, which have a problematic history. \
                                    \
                                    At least one businessman has claimed ownership of one of the four companies at the core of the \
                                    schema, though there is no evidence to support this unlikely assertion. \
                                    Hafiz Mammadov is head of the Baghlan Group, one of the Caspian country’s largest business conglomerates. \
                                    The group rose to international prominence this year when the New Yorker exposed its involvement in the \
                                    development of the Trump Tower in Baku.\
                                    \
                                    In 2014, when they pinned the “Azerbaijan-Land of Fire” logo on their chests, the players of RC LENS, one of France’s oldest football clubs, were unaware of the financial burden attached to the slogan on their red and yellow jerseys. One year earlier, the club had been bought by Mammadov. \
                                    He has pinned the same logo on the chests of Atletico Madrid’s players and tried to buy Sheffield Wednesday F.C., \
                                    a British football club. Mammadov’s forays into the world of European football were an important part of Azerbaijan’s efforts to improve its international image despite the human rights violations that were taking place back home. \
                                    But, though he promised to invest big money in RC LENS, Mammadov failed to deliver in a timely manner. Beginning in 2014, he started postponing the investment payments he had promised to the club. \
                                    \
                                    On Sept 18, 2014, one of its four core companies, Hilux Services LP, transferred $2 million to RCL Holding, the company that formally owned Hafiz Mammadov’s club. \
                                    According to its bank filings, Hilux stated it would be receiving money from the International Bank of Azerbaijan. But Hilux’s Estonian bank account at Danske Bank was owned by the blue-collar driver, Ahmadov, who was likely a proxy unaware how he was being used by the real masterminds behind the schema.\
                                    \
                                    On the day the RC LENS received the $2 million installment, $10.3 million was fed into Hilux’s \
                                    Danske Bank account from the two biggest funders of the Laundromat. Faberlex LP contributed \
                                    US$ 2.8 million and Baktelekom MMC sent US$7.6 million.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Top 10 Contributors"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(contributors_10)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Baktelekom Payouts",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "06/2012",
                                                        "12/2012",
                                                        "06/2013",
                                                        "12/2013",
                                                        "06/2014",
                                                        "12/2014"
                                                    ],
                                                    y=[
                                                        "21.67",
                                                        "11.26",
                                                        "15.62",
                                                        "8.37",
                                                        "11.11",
                                                        "19.11"
                                                    ],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Polux Management LP"
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "06/2012",
                                                        "12/2012",
                                                        "06/2013",
                                                        "12/2013",
                                                        "06/2014",
                                                        "12/2014"
                                                    ],
                                                    y=[
                                                        "21.83",
                                                        "11.41",
                                                        "15.79",
                                                        "8.50",
                                                        "13.54"
                                                    ],
                                                    marker={
                                                        "color": "#dddddd",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Hilux Services LP",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Hypothetical growth of $10,000",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=[
                                                        "2008",
                                                        "2009",
                                                        "2010",
                                                        "2011",
                                                        "2012",
                                                        "2013",
                                                        "2014",
                                                        "2015",
                                                        "2016",
                                                        "2017",
                                                        "2018",
                                                    ],
                                                    y=[
                                                        "10000",
                                                        "7500",
                                                        "9000",
                                                        "10000",
                                                        "10500",
                                                        "11000",
                                                        "14000",
                                                        "18000",
                                                        "19000",
                                                        "20500",
                                                        "24000",
                                                    ],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Polux",
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                width=340,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0277108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                xaxis={
                                                    "autorange": True,
                                                    "linecolor": "rgb(0, 0, 0)",
                                                    "linewidth": 1,
                                                    "range": [2008, 2018],
                                                    "showgrid": False,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    "range": [0, 30000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 10,
                                                    "ticks": "outside",
                                                    "title": "$",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Price & Performance (%)",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(df_price_perf)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Risk Potential", className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("risk_reward.png"),
                                        className="risk-reward",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
