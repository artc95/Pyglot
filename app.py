from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *

app = Flask(__name__)

def pyglot():
    raw = textarea("""THE OR NO THE?\n
    Input text here to create the/- cloze passage:""",rows=10, placeholder="Text in English")
    raw_list = raw.split(" ") # split text into list of individual words
    new_list = [] # to store question if word == "the"
    the_count = 1 # keep track of number of "the"s in text
    for word in raw_list:
        if word == "the":
            new_list.append("[{}. the / - ]".format(the_count))
            the_count += 1
        
        else:
            new_list.append(word)
    
    new = " ".join(new_list) # combine list of questions and words, with " " as separator
    put_text(new)

app.add_url_rule('/', 'webio_view', webio_view(pyglot),
            methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS method

if __name__ == '__main__':
    app.run(host='localhost', port=80)