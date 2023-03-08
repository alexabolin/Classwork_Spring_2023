from flask import Flask, request, jsonify

db = {}

app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "tests": []}
    db[id] = new_patient
    print(db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get input data
    in_data = request.get_json()
    # Call other functions
    answer, status_code = new_patient_driver(in_data)
    # Return a response
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    # Validate input
    validation = validate_input_data(in_data, ["name", "id", "blood_type"],
                                     [str, int, str])
    if validation is not True:
        return validation, 400
    # Do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return answer
    return "Patient successfully added", 200


def validate_input_data(in_data, expected_keys, expected_types):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True


def add_test_to_db(id, test_name, test_result):
    db[id]["tests"].append((test_name, test_result))
    print(db)


@app.route("/add_test", methods=["POST"])
def post_add_test():
    # Get input data
    in_data = request.get_json()
    # Call other functions
    answer, status_code = add_test_driver(in_data)
    # Return a response
    return jsonify(answer), status_code


def add_test_driver(in_data):
    # Validate input
    validation = validate_input_data(in_data, ["id", "test_name",
                                               "test_result"],
                                     [int, str, int])
    if validation is not True:
        return validation, 400
    does_id_exist = does_patient_exist_in_db(in_data["id"])
    if does_id_exist is False:
        return "Patient id {} does not exist in database"
    # Do the work
    add_test_to_db(in_data["id"], in_data["test_name"], in_data["test_result"])
    # Return answer
    return "Test successfully added", 200


def does_patient_exist_in_db(id):
    if id in db:
        return True
    else:
        return False


@app.route("/get_results", methods=["GET"])
def get_results():
    # Get input data
    in_data = request.get_json()
    # Call other functions
    answer, status_code = get_results_driver(in_data)
    # Return a response
    return jsonify(answer), status_code


def get_results_driver(in_data):
    id = in_data["id"]
    results = db[id]["tests"]
    print(results)
    return "Results gathered", 200


if __name__ == "__main__":
    app.run()
