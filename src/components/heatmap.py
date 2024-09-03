import numpy as np
from dash import dcc
import datetime

def generate_patient_volume_heatmap(df, start, end, clinic, admit_type, day_list):
    filtered_df = df[(df["Clinic Name"] == clinic) & (df["Admit Source"].isin(admit_type))]
    filtered_df = filtered_df.sort_values("Check-In Time").set_index("Check-In Time")[start:end]

    x_axis = [datetime.time(i).strftime("%I %p") for i in range(24)]
    y_axis = day_list

    z = np.zeros((7, 24))
    annotations = []

    for ind_y, day in enumerate(y_axis):
        filtered_day = filtered_df[filtered_df["Days of Wk"] == day]
        for ind_x, x_val in enumerate(x_axis):
            sum_of_record = filtered_day[filtered_day["Check-In Hour"] == x_val]["Number of Records"].sum()
            z[ind_y][ind_x] = sum_of_record
            annotation_dict = dict(
                showarrow=False,
                text="<b>" + str(sum_of_record) + "<b>",
                x=x_val,
                y=day,
                font=dict(family="sans-serif"),
            )
            annotations.append(annotation_dict)

    data = [
        dict(
            x=x_axis,
            y=y_axis,
            z=z,
            type="heatmap",
            hovertemplate="<b> %{y}  %{x} <br><br> %{z} Patient Records",
            showscale=False,
            colorscale=[[0, "#caf3ff"], [1, "#2c82ff"]],
        )
    ]

    layout = dict(
        margin=dict(l=70, b=50, t=50, r=50),
        font=dict(family="Open Sans"),
        annotations=annotations,
        xaxis=dict(
            side="top",
            ticklen=2,
            tickfont=dict(family="sans-serif"),
            tickcolor="#ffffff",
        ),
        yaxis=dict(
            side="left", tickfont=dict(family="sans-serif"), ticksuffix=" "
        ),
        hovermode="closest",
        showlegend=False,
    )
    return {"data": data, "layout": layout}
