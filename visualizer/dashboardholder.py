import dash
from dash import dcc, html
from visualizer.simple_page_home import simple_page_home
from visualizer.simple_page import simple_page
from visualizer.simple_page2 import simple_page2
from visualizer.simple_page3 import simple_page3
from dash.dependencies import Input, Output

class dashboardholder:
    def __init__(self, dataframe):
        self.data_frame = dataframe
        # Initialize Dash app with suppress_callback_exceptions=True
        self.app = dash.Dash(__name__, suppress_callback_exceptions=True)

        # Set up the initial layout with dcc.Location
        self.app.layout = html.Div([
            dcc.Location(id='url', refresh=False),  # Track the URL
            html.Div(id='page-content'),  # Content changes based on the URL
        ])

        # Define the callback for URL changes
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            if pathname == '/':
                return simple_page_home(self.app)  # Default page
            elif pathname == '/page-1':
                return simple_page(self.app, self.data_frame)  # Page 1
            elif pathname == '/page-2':
                return simple_page2(self.app, self.data_frame)  # Page 2
            elif pathname == '/page-3':
                return simple_page3(self.app, self.data_frame)  # Page 3
            else:
                return simple_page_home(self.app)  # Fallback to default

    def run(self):
        self.app.run_server(debug=True)
