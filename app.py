from dash import Dash, html
from src.layout.layout import app_layout
from src.callbacks.callback import register_callbacks

app = Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.layout = app_layout
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
