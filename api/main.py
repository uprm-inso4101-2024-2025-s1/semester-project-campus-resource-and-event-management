from flask import Flask, request, jsonify
from dbinterface import insert_student, insert_organization

app = Flask(__name__)

# Route for student sign-up
@app.route('/signup/student', methods=['POST'])
def signup_student():
    data = request.json
    student_id = data.get('student_id')
    email = data.get('email')
    password = data.get('password')

    if not student_id or not email or not password:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        insert_student(student_id, email, password)
        return jsonify({'message': 'Student registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Student ID already exists'}), 409
    except Exception as e:
        return jsonify({'message': 'Error occurred: ' + str(e)}), 500

# Route for organization sign-up
@app.route('/signup/organization', methods=['POST'])
def signup_organization():
    data = request.json
    organization_name = data.get('organization_name')
    email = data.get('email')
    password = data.get('password')

    if not organization_name or not email or not password:
        return jsonify({'message': 'Invalid input'}), 400

    try:
        insert_organization(organization_name, email, password)
        return jsonify({'message': 'Organization registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': 'Error occurred: ' + str(e)}), 500



class reqCounter():
    def __init__(self):
        self.count = 0
    
    def getCount(self):
        self.count += 1
        return self.count
    
reqCount = reqCounter()

@app.route("/api/")
def hello_world():
    resp = make_response(f"This is the server request # {reqCount.getCount()}", 200)

    # Setting CORS request headers
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp