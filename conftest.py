from config.config import Config
from applications.api.github_api import GitHubAPI
import pytest

@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubAPI(Config.base_url, 'v1')
    yield github_api_client
    print('END-UP TEST')