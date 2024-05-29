from fizzbuzz import calculate_fizzbuzz
from bottle import route, run, template, request, static_file, error, default_app


# if __name__ == '__main__':


@route('/')
def todo_list():
    return template('fizzbuzz')



application = default_app()# Démarrage du serveur distant
#run(host='localhost', port=8080, debug=True, reloader=True) #démarrage du serveur local
