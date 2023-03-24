from pymodm import connect
from PatientModel import Patient
import ssl
from secrets import mongodb_acct,mongodb_pass

connect("mongodb+srv://{}:{}@bme547.t0fjj13.mongodb.net/"
            "health_db?retryWrites=true&w=majority".format(mongodb_acct,
                                                           mongodb_pass),
            ssl_cert_reqs=ssl.CERT_NONE)


def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    patient_id = 234
    patient_name = "Test"
    patient_blood_type = "O+"
    answer = add_patient_to_db(patient_id, patient_name, patient_blood_type)
    x = Patient.objects.raw({"_id": patient_id}).first()
    x.delete()
    assert answer.patient_id == patient_id


def test_add_test_to_db():
    #ARRANGE
    from health_db_server import add_test_to_db
    patient_id = 123
    patient_name = "Test"
    patient_blood_type = "O+"
    from health_db_server import add_patient_to_db
    add_patient_to_db(patient_id, patient_name, patient_blood_type)

    #ACT
    test_name = "HDL"
    test_value = 150
    add_test_to_db(patient_id, test_name, test_value)

    #ASSERT
    x = Patient.objects.raw({"_id": patient_id}).first()
    answer = x.tests
    expected = [[test_name, test_value]]
    assert answer == expected
