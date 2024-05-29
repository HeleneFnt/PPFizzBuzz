from fizzbuzz import calculate_fizzbuzz
from bottle import route, run, template, request, static_file, error

# if __name__ == '__main__':


@route('/')
def todo_list():
    return template('fizzbuzz')


# Démarrage du serveur
run(host='localhost', port=8080, debug=True, reloader=True)
