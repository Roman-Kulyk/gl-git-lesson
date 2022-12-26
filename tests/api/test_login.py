import requests

def test_http_status_code200():
    r = requests.get('https://docs.github.com/en/get-started/quickstart/hello-world')
    assert r.status_code == 200
        
def test_user_exists():
    r = requests.get('https://api.github.com/users/defunkt')
    assert r.json()['login'] == 'defunkt'
    assert r.json()['id'] == 2

def test_user_does_not_exists():
    r = requests.get('https://api.github.com/users/defunktgasgsfgsfsfgsgs')
    assert r.status_code == 404
    assert r.json()['message'] == 'Not Found'