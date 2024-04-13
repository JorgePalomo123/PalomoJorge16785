from flask import Flask, jsonify

app = Flask(__name__)
tasks = [
    {"id":1,"user":"omar","active":True},
    {"id":2,"user":"omar","active":False},
    {"id":3,"user":"omar","active":True},
    {"id":4,"user":"omar","active":False}

]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
