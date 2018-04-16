import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
        if len(entries) > 0:
            max_id = 0
            for entry in entries:
                if int(entry["id"]) > max_id:
                    max_id = int(entry["id"])
            next_id = str(max_id + 1)
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
        next_id += 1
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    print(id)
    global entries, GUESTBOOK_ENTRIES_FILE
    f_open = open(GUESTBOOK_ENTRIES_FILE, "r")
    entries = json.loads(f_open.read())
    f_open.close()
    updated_entries = []
    for entry in entries:
        if entry["id"] != id:
            updated_entries.append(entry)
    entries = updated_entries
    f_open = open(GUESTBOOK_ENTRIES_FILE, "w")
    f_open.write(json.dumps(entries))
    f_open.close()
