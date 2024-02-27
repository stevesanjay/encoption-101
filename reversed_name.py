
# import json
from flask import Flask , request

reversed_name = Flask(__name__)

@reversed_name.route("/")
def reverse_name():
    name = request.values.get("name")
    rev_name = name[::-1]
    # print("reversed_name":rev_name) 
    data ={
        "name":name,
        "reverse_name":rev_name 
        }
    return data 

if __name__=="__main__":
    reversed_name.run(host='0.0.0.0',
    port=4890,debug =True
         
)






