from dash.testing.application_runners import import_app


def test_one(dash_duo):
    app = import_app("src.app")
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("h1", "STF1 Data Analysis", timeout=4)