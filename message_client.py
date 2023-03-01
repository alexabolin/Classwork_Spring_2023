import requests

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/anb71")
print(r.text)

out_data = {"user": "ak559", "message": "Hey gurlllll"}
t = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json = out_data)
