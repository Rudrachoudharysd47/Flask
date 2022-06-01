from flask import Flask,jsonify,request
tasks = [
    {
    "Contact":"9875640327",
    "name":"Raju",
    "done":False,
    "ID":1
},{
    "Contact":"9897110810",
    "name":"Anand",
    "done":False,
    "ID":2
}]
app = Flask(__name__)
@app.route("/hello")
def hellowworld():
    return "hellow world"
@app.route("/get-data")
def gettask():
    return jsonify(
        {
            "data":tasks
        }
    )
@app.route("/add-data",methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data in json"
        }),400
    task = {
        "ID":tasks[-1]["ID"]+1,
        "title":request.json["title"],
        "description":request.json["description"],
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"succes",
        "message":"task added"
    })
app.run(debug = True)


