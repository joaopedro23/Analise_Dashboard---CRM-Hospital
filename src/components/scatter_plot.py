import dash_core_components as dcc
import plotly.graph_objs as go

def generate_scatter_plot(department_data, department_name):
    """Gera um gráfico de dispersão de tempo de espera vs. pontuação de atendimento para um departamento específico."""
    
    scatter_plot = go.Scatter(
        x=department_data["Wait Time Min"],
        y=department_data["Care Score"],
        mode="markers",
        marker=dict(
            size=10,
            color="rgba(152, 0, 0, .8)",
            line=dict(width=2, color="rgb(0, 0, 0)")
        ),
        text=department_data["Encounter Number"]
    )

    layout = go.Layout(
        title=f'{department_name} - Wait Time vs Care Score',
        xaxis=dict(title='Wait Time (minutes)'),
        yaxis=dict(title='Care Score'),
        hovermode="closest"
    )

    return dcc.Graph(
        figure={
            'data': [scatter_plot],
            'layout': layout
        }
    )
