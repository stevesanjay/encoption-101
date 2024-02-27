from random import randint
from flask import Flask , request

r_no = Flask(__name__)

@r_no.route("/")
def random_score():
    name = request.values.get("name")
    random_score= randint(1,100)
    data = {
        "name":name,
        "random_score":random_score,
    }
    return data


if __name__=="__main__":
    r_no.run(host='0.0.0.0',
    port=4890,debug =True
         
)
