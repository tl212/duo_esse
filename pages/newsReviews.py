import dash_html_components as html
from utils import Header
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pathlib
import pandas as pd

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


dk_data = pd.read_csv(DATA_PATH.joinpath("dk_data.csv"))

## Colours
color_1 = "#003399"
color_2 = "#00ffff"
color_3 = "#002277"
color_b = "#F8F8FF"

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6
            html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "Erat cras porta inceptos nibh sociis justo. Natoque mauris nunc etiam, dis quam, tempor consectetur ac \
                                    Pulvinar nunc vitae dui elit hac ante, facilisi, primis nascetur. Non nostra torquent ipsum ac amet",
                                            className="page-9h",
                                        ),
                                       # html.P(paragraph(), className="page-1i"),
                                        #html.P(paragraph(), className="page-1i"),
                                        html.H6(
                                            "The report indicates US$ 2.9 billion in suspicious activities.r \
                                        Baktelekom MMC was the mysterious largest contributor that used an account at IBA.",
                                            className="page-6c",
                                        ),
                                        html.Div(
                                            [
                                                dash_table.DataTable(
                                                    data=dk_data.to_dict(
                                                        "records"
                                                    ),
                                                    columns=[
                                                        {"id": c, "name": c}
                                                        for c in dk_data.columns
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            "if": {"row_index": "odd"},
                                                            "backgroundColor": color_b,
                                                        },
                                                        {
                                                            "if": {
                                                                "column_id": "Quarter"
                                                            },
                                                            "backgroundColor": color_2,
                                                            "color": "black",
                                                        },
                                                    ],
                                                    style_header={
                                                        "backgroundColor": color_1,
                                                        "fontWeight": "bold",
                                                        "color": "white",
                                                    },
                                                    fixed_rows={"headers": True},
                                                    style_cell={"width": "150px"},
                                                )
                                            ],
                                            className="page-1i",
                                        ),
                                    ],
                                    className="eleven columns",
                                )
                            ],
                            className="page-12a",
                        )
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),
    ]
)