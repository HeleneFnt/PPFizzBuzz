import subprocess
import requests
username = 'LnWatta'
token = 'c540db49e48e202108c4c7fd6c7a6ab2f6f9eca0'
console_id = 34018577
url= "LnWatta.pythonanywhere.com"

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))


result = subprocess.run(["pytest"], shell=True, capture_output=True, text=True)


def pushongit():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "test ok"])
    subprocess.run(["git", "push", "origin", "main"])

def pullOnServer():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{console_id}/send_input/'.format(
            username=username,
            console_id=console_id
        ),
        headers={'Authorization': 'Token {token}'.format(token=token),
                 'Content-Type': 'application/json'},
        json={'input': 'cd ~/mysite && git pull\n'}
    )

def reloadServer():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{url}/reload/'.format(
            username=username,
            url=url
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )





if result.returncode:
    print("test non passé")
else:
    print("test OK")
    pushongit()
    pullOnServer()
    reloadServer()

