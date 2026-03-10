# Unit Conversion Microservice

Converts number from one unit to a different unit specified by user/client 

## Uses ZeroMQ
```
import zmq

context = zmq.Context()

# Connect to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")
```

## Request Format
Dictionary of {"num": number, "conv": conversion}  

Available conversions:  
"ft_to_m", "m_to_ft", "min_to_h", "h_to_min"

Example: 
```
test = {"num": 54, "conv": "min_to_h"}
socket.send_json(test)
```

## Response Format
JSON with number, unit, and success code (0)  
{"num": converted_number, "unit": unit_converted_to, "code": 0}

If error occurred, then code will be 1 with error message  
{"error": error_msg, "code": 1}

Example: 
```
response = socket.recv_json()
if response["code"] == 0:
    print(f"{response["num"]} {response["unit"]}")
else:
    print("An error occurred:", response["error"])
```
