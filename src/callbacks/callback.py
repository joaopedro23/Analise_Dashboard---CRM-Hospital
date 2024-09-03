from dash import Input, Output
from src.components.heatmap import generate_patient_volume_heatmap
from src.components.scatter_plot import generate_scatter_plot
from src.components.tables import create_table_figure, generate_patient_table
from src.data.data_loader import load_data

df, clinic_list, admit_list, day_list = load_data()

def register_callbacks(app):
    @app.callback(
        Output("patient_volume_hm", "figure"),
        [
            Input("clinic-select", "value"),
            Input("admit-select", "value"),
            Input("date-picker-select", "start_date"),
            Input("date-picker-select", "end_date"),
        ],
    )
    def update_patient_volume(clinic, admit_type, start_date, end_date):
        return generate_patient_volume_heatmap(df, start_date, end_date, clinic, admit_type, day_list)
    
    @app.callback(
    Output("wait_time_table", "children"),
    [
        Input("date-picker-select", "start_date"),
        Input("date-picker-select", "end_date"),
        Input("clinic-select", "value"),
        Input("admit-select", "value"),
    ],
)
    def update_table(start, end, clinic, admit_type, *args):
        start = start + " 00:00:00"
        end = end + " 00:00:00"

        filtered_df = df[(df["Clinic Name"] == clinic) & (df["Admit Source"].isin(admit_type))]
        filtered_df = filtered_df.sort_values("Check-In Time").set_index("Check-In Time")[start:end]
        departments = filtered_df["Department"].unique()

        # range_x for all plots
        wait_time_xrange = [
            filtered_df["Wait Time Min"].min() - 2,
            filtered_df["Wait Time Min"].max() + 2,
        ]
        score_xrange = [
            filtered_df["Care Score"].min() - 0.5,
            filtered_df["Care Score"].max() + 0.5,
        ]

        figure_list = []
        for department in departments:
            department_wait_time_figure = create_table_figure(department, filtered_df, "Wait Time Min", wait_time_xrange, "")
            figure_list.append(department_wait_time_figure)

        for department in departments:
            department_score_figure = create_table_figure(department, filtered_df, "Care Score", score_xrange, "")
            figure_list.append(department_score_figure)

        table = generate_patient_table(figure_list, departments, wait_time_xrange, score_xrange)
        return table

    