import json 
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def reverse_name():

    name = request.values.get("name")
    j_name = {
        "name":name,
        }
    for k,v in j_name.items():
        j_name[k]=v[::-1]
  
    return jsonify(j_name)

# app.route("/")
# def rname():
#     name = request.values.get("name")
#     f_name ={
#         "name":name
#     }
#     return jsonify(rname)



if __name__=="__main__":
    app.run(
         debug =True
         )

# @app.route("/")
# def reverse_name():
#     data = request.get_json()
#     name = data.get("name", None)
#     reversed_name = name[::-1]
#     print({'reversed_name': reversed_name})

#     return jsonify({'reversed_name': reversed_name})

# if __name__=="__main__":
#     app.run(
#         debug =True
#         

# @app.route("/")
# def reverse_name():
#     msg = '{"name":"deva"}'
#     message = json.loads(msg)
#     for k,v in message.items():
#         if not k.startswith("_"):
#             if 'deva' in v:
#              message[k]=v[::-1]
#              print(json.dumps(message))
#         return jsonify(message)


# if __name__=="__main__":
#     app.run(
#          debug =True)

