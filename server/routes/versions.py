import json
from os import listdir, remove
from flask import request, render_template


def mainPage():
    # LoadAllVersions()
    return render_template('index.html')


def GetVersions():
    cards = []
    for versionFile in listdir('./db'):
        with open('./db/%s' % versionFile) as source:
            # print(card)
            cards.append(json.load(source))
    return json.dumps(cards)


def ModifyVersion(id):
    if request.method == 'POST':
        payload = request.get_json()
        card = {
            "id": payload.get('id'),
            "author": payload.get('author'),
            "date": payload.get('date'),
            "notes": payload.get('notes'),
        }
        if not card["id"]:
            return "Data is corrupted", 400
        with open('./db/%s.json' % id, 'w', encoding='utf-8') as destination:
            json.dump(card, destination, ensure_ascii=False, indent=2)
        return 'created version', 201
    elif request.method == 'DELETE':
        for versionFile in listdir('./db'):
            if versionFile == '%s.json' % id:
                remove('./db/%s' % versionFile)
                break
        return 'deleted version', 204
    elif request.method == 'PUT':
        payload = request.get_json()
        notes = payload.get('notes'),
        UpdateVersionNotes(id, notes)
        return 'Changed Successfully', 204


def UpdateVersionNotes(id, notes):
    with open('./db/%s.json' % id) as source:
        version = json.load(source)
    version["notes"] = "%s" % notes
    with open('./db/%s.json' % id, 'w', encoding='utf-8') as destination:
        json.dump(version, destination, ensure_ascii=False, indent=2)
