# Unit Conversion Microservice

import zmq

# Unit conversion functions
def ft_to_m(num_feet):
    return {"num": round(num_feet * .3048, 2), "unit": "m", "code": 0}

def m_to_ft(num_m):
    return {"num": round(num_m * 3.28084, 2), "unit": "ft", "code": 0}

def min_to_h(num_min):
    return {"num": round(num_min / 60, 2), "unit": "h", "code": 0}

def h_to_min(num_h):
    return {"num": round(num_h * 60, 2), "unit": "min", "code": 0}

# Perform unit conversion specified by user and generate response
def determine_conv(orig_num, conv):
    match conv:
        case "ft_to_m":
            result = ft_to_m(orig_num)
        case "m_to_ft":
            result = m_to_ft(orig_num)
        case "min_to_h":
            result = min_to_h(orig_num)
        case "h_to_min":
            result = h_to_min(orig_num)
        case _:
            result = {"error": "Invalid conversion input.", "code": 1}
    return result

# Establish server and attach to port
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    print("Listening on 5557")
    # Get data from client
    data = socket.recv_json()
    # Ensure data includes number, then perform conversion
    try:
        num = float(data["num"])
    except ValueError as e:
        response = {"error": str(e), "code": 1}
        socket.send_json(response)
    else:
        response = determine_conv(num, data["conv"])
        socket.send_json(response)
