import pytest
from app import create_app

"""
Create setup configurations for flask app
"""

@pytest.fixture()
def app():
    """
    This fixture setups and configures the main
    """

    app = create_app()
    app.config.update({
        "TESTING": True
    })

    # todo: More config

    yield app

    # todo: Cleans up

@pytest.fixture()
def client(app):
    """
    This fixture returns a client instance of the app.
    """
    return app.test_client()