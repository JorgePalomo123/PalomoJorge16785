from flask import Flask, jsonify
import platform
import subprocess

local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%)"') do @echo %a""")
hostname = platform.node()

app = Flask(__name__)
tasks = [
    {'ip':local, 'hostname':hostname}

]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
