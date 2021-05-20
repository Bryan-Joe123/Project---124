from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")

def HelloWorld():
    return("Hello World")

contactWithAnS = [{
    'id': 1,
    'name': u'rajun',
    'contact': u'123456789',
    'done': False   
},
{
    'id': 2,
    'name': u'kthon',
    'contact': u'987654321',
    'done': False
}]

@app.route("/add-data",methods=["POST"])

def addcontact():
    if(not request.json):
        return(jsonify({"status":"ERROR","message":"PLEASE PROVIDE THE DATA PLEASEEEE"},400))
    
    contact={
        'id': contactWithAnS[-1]['id'] + 1,
        'name': request.json['title'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    contactWithAnS.append(contact)
    return(jsonify({"status":"Sucsess","message":"YaY You HaVe doNe It!1!"}))

@app.route("/get-data",methods=["GET"])

def getcontact():
    return(jsonify({"data":contactWithAnS}))

if (__name__ == "__main__"):
    app.run()