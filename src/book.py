import json
import backend
import requests


def scan_book(rfid):

    parameters = {
        'rfid': rfid,
    }

    print(parameters)

    response = backend.request('scan_book', data=parameters)

    jsonobject = json.loads(response.text)


    if jsonobject["error"]:
        raise ConnectionError('Feil i databasen: ' + jsonobject["error"])

    #Check for error by each book, for instance that the book was not found in the database
    for i in jsonobject["status"]:
        if i["error"]:
            raise ConnectionError('Feil i databasen: ' + i["error"])

    return jsonobject


def get_book_info(bookrfid):
    parameters = {
        'rfid': bookrfid,
    }

    response = backend.request('get_book_info', data=parameters)
    jsonobject = json.loads(response.text)

    if jsonobject["error"]:
        raise ConnectionError('Feil i databasen: ' + jsonobject["error"])

    return jsonobject


def give_feeback(userrfid, bookrfid, ratingtype, value):
    parameters = {
        'user_rfid': userrfid,
        'book_rfid': bookrfid,
        'type': ratingtype,
        'value': value,
    }

    response = backend.request('give_feedback', data=parameters)
    jsonobject = json.loads(response.text)

    if jsonobject["error"]:
        raise ConnectionError('Feil i databasen: ' + jsonobject["error"])

    return jsonobject


def google_books():
    r = requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:9788245003642')
    jsonobject = json.loads(r.text)

