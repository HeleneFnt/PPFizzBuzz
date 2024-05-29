import subprocess
import requests
username = 'LnWatta'
token = 'c540db49e48e202108c4c7fd6c7a6ab2f6f9eca0'

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

#def pullOnServer():



if result.returncode:
    print("test non passé")
else:
    print("test OK")
    pushongit()
