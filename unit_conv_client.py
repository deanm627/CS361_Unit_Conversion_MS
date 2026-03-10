import zmq

context = zmq.Context()

# Connect to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

# Sample data
test = {"num": 54, "conv": "min_to_h"}
socket.send_json(test)

# Get and print the response
response = socket.recv_json()
if response["code"] == 0:
    print(f"{response["num"]} {response["unit"]}")
else:
    print("An error occurred:", response["error"])
