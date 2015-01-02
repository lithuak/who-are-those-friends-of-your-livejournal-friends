# -*- coding: utf-8 -*-
import pickle
from collections import Counter
import requests

me = "<your lj here>"

def save_fof(data):
    with open('data/' + me + '.fof.pickle', 'wb') as f:
        pickle.dump(data, f)

def load_fof():
    with open('data/' + me + '.fof.pickle', 'rb') as f:
        return pickle.load(f)

def get_friends(user):
    r = requests.get("http://www.livejournal.com/misc/fdata.bml?user=" + user)
    return r.text

def parse_friends(txt):
    return [s[2:] for s in txt.split("\n") if s.startswith(">")]

def get_fof():
    my_friends = parse_friends(get_friends(me))
    d = {me: my_friends}
    for f in my_friends:
        print f
        d[f] = parse_friends(get_friends(f))
    save_fof(d)

def analyze():
    fof = load_fof()
    my = set(fof.pop(me))
    t = Counter([f for ff in fof.itervalues() for f in ff])
    for u, i in t.most_common():
        print u, i,
        if u not in my:
            print "*!",
        print

if __name__ == "__main__":
    get_fof()
    print "----- And now for somth. compl. diff. ------"
    analyze()
