from dash import html, dcc
from src.components.cards import description_card, generate_control_card
from src.components.tables import initialize_table
from src.data.data_loader import load_data

df, clinic_list, admit_list, day_list = load_data()
all_departments = df["Department"].unique().tolist()

app_layout = html.Div(
    id="app-container",
    children=[

        # Left column
        html.Div(
            id="left-column",
            className="four columns",
            children=[description_card(), generate_control_card(clinic_list, admit_list)]

        ),
        # Right column
        html.Div(
            id="right-column",
            className="eight columns",
            children=[
                # Patient Volume Heatmap
                html.Div(
                    id="patient_volume_card",
                    children=[
                        html.B("Patient Volume"),
                        html.Hr(),
                        dcc.Graph(id="patient_volume_hm"),
                    ],
                ),
                # Patient Wait time by Department
                html.Div(
                    id="wait_time_card",
                    children=[
                        html.B("Patient Wait Time and Satisfactory Scores"),
                        html.Hr(),
                        html.Div(id="wait_time_table", children=initialize_table(all_departments)),
                    ],
                ),
            ],
        ),
    ],
)
