"""
Experiment 3: Route Distance Calculator
Author: Aman Kumar Patra

Description:
    This experiment demonstrates conditional logic
    and dictionary data handling in Python.

    The function calculates distance either:
    - Directly from 'distance'
    - OR using speed × time
"""

def route_info(data_dict):
    """
    Calculates route distance based on available data.

    Parameters:
        data_dict (dict): Dictionary containing route information.

    Returns:
        str: Message containing calculated distance or error message.
    """

    # Case 1: Direct distance provided
    if 'distance' in data_dict and isinstance(data_dict['distance'], (int, float)):
        return f"Distance to your destination is {data_dict['distance']} km"

    # Case 2: Calculate distance using speed × time
    elif 'speed' in data_dict and 'time' in data_dict:
        if isinstance(data_dict['speed'], (int, float)) and isinstance(data_dict['time'], (int, float)):
            distance = data_dict['speed'] * data_dict['time']
            return f"Distance to your destination is {distance} km"

    # Case 3: Invalid or missing data
    return "No distance information is available."


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":

    route_dict1 = {
        'distance': 50
    }

    route_dict2 = {
        'speed': 30,
        'time': 1
    }

    print(route_info(route_dict1))
    print(route_info(route_dict2))
