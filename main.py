from flask import Flask, jsonify, request

app = Flask(__name__)

#creating array of tasks with each task as a different object in it.
myTasks = [
     {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Do homework',
        'description': u'Maths, Science, English', 
        'done': False
    },
]

@app.route("/") 
def Homepage():
    return "Welcome to my to do list"

@app.route("/add-data", methods = ["POST"] )
def toDOList():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "Message":"Please provide some information..."
        } ,400)
    t = {
          'id': myTasks[-1]['id'] + 1,
          'title': request.json["Title"],
          'description': request.json.get("Description",""),
          'done': False
    }
    myTasks.append(t)
    return jsonify({
        "Status": "Success",
        "Message": "Task added successfully..."
    })

@app.route("/get-data")
def getData():
    return jsonify({
        "data": myTasks
    })

if (__name__ == "__main__"):
    app.run(debug = True)

