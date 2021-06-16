# pywebio input and output
from pywebio.input import *
from pywebio.output import *

# for button callbacks, partial method and pywebio session (for hold() method, see https://pywebio.readthedocs.io/en/latest/session.html#pywebio.session.hold)
from functools import partial
from pywebio.session import *

# pywebio with Flask
from pywebio.platform.flask import webio_view
from flask import Flask

app = Flask(__name__) # initiate Flask Web Server Gateway Interface (WSGI)

def pyglot():
    raw = textarea("""Input text here:""",rows=10, placeholder="Text in English")
    raw_list = raw.split(" ") # split text into list of individual words
    new_list = [] # store text with "the" replaced by questions
    response_list = [["Question","Review","Answer"]] # list to display table of question number, review of answer and answer buttons
    #answer_dict = {} # store dictionaries of each question's correct answer and answer review
    the_count = 0 # keep track of number of "the"s in text
    
    def review_answer(answer, question): # update answer review based on user's answer
        if answer == "the":
            click_result[question].reset("Question {} correct!".format(question+1))

        else:
            click_result[question].append("Question {} wrong, try again!".format(question+1))

    for word in raw_list:
        if word == "the":
            new_list.append("{}. _________ ".format(the_count+1))
            the_count += 1
        
        else:
            new_list.append(word)
    
    click_result = [output(put_text()) for i in range(the_count)]
    print(click_result)
    for i in range(the_count):
        response_list.append([str(i+1), click_result[i], put_buttons(["the", "-"], 
            onclick=partial(review_answer, question=i))])
    
    print(the_count)
    print(response_list)
    new = " ".join(new_list) # combine list of questions and words, with " " as separator

    put_row(
        [put_text(new),None,put_table(response_list)],size="50% 5% 45%"
    )

    hold() # allows callbacks ("partial" method) when buttons clicked, see https://pywebio.readthedocs.io/en/latest/session.html#pywebio.session.hold

app.add_url_rule('/', 'webio_view', webio_view(pyglot),
            methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS method

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)