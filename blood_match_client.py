import requests

server = "http://vcm-7631.vm.duke.edu:5002"
patient_ids = requests.get("{}/get_patients/anb71".format(server))
print(patient_ids.text)
patient_ids = patient_ids.json()
recipient_id = patient_ids.get('Recipient')
recipient_blood_type = requests.get("{}/get_blood_type/{}".format(server, recipient_id))
donor_id = patient_ids.get('Donor')
donor_blood_type = requests.get("{}/get_blood_type/{}".format(server, donor_id))
print(recipient_blood_type.text)
print(donor_blood_type.text)

result = 0
if (recipient_blood_type == donor_blood_type):
    result = "Yes"
else:
    result = "No"

out_data = {"Name": "anb71", "Match": result}
results = requests.post("{}/match_check".format(server), json = out_data)
print(results.text)
