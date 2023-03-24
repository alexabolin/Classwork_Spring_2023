from flask import Flask, request, jsonify
import logging
from pymodm import connect
from pymodm import errors as pymodm_errors
from PatientModel import Patient
import ssl
from secrets import mongodb_acct, mongodb_pass


app = Flask(__name__)


def init_server():
    logging.basicConfig(filename="server.log", filemode="w")
    connect("mongodb+srv://{}:{}@bme547.t0fjj13.mongodb.net/"
            "health_db?retryWrites=true&w=majority".format(mongodb_acct,
                                                           mongodb_pass),
            ssl_cert_reqs=ssl.CERT_NONE)


def add_patient_to_db(id, name, blood_type):
    new_patient = Patient(patient_id = id,
                          patient_name = name,
                          blood_type = blood_type)
    save_patient = new_patient.save()
    return save_patient


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
    x = Patient.objects.raw({"_id": id}).first()
    x.tests.append((test_name, test_result))
    save_x = x.save()
    return save_x


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
    try:
        db_item = Patient.objects.raw({"_id": id}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return True


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results(patient_id):
    # Get input data
    # Call other functions
    answer, status_code = get_results_driver(patient_id)
    # Return a response
    return jsonify(answer), status_code


def get_results_driver(patient_id):
    validation = validate_input_data_get(patient_id)
    if validation is not True:
        return validation, 400
    # patient = db[int(patient_id)]
    return patient["tests"], 200


def validate_input_data_get(patient_id):
    try:
        patient_num = int(patient_id)
    except ValueError:
        return "Patient ID should be an integer"
    if does_patient_exist_in_db(patient_num) is False:
        return "Patient ID of {} does not exist in database".format(
                                                        patient_num)
    return True


if __name__ == "__main__":
    init_server()
    app.run()
