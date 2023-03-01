import requests

out_data = {
   "name": "Alexa Bolin",
   "net_id": "anb71",
   "e-mail": "anb71@duke.edu"
   }
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)
print(r.status_code)
print(r.text)
