"""
Experiment 2: Update Car Information using **kwargs
Author: Aman Kumar Patra

Description:
    This experiment demonstrates how to use **kwargs
    to accept dynamic keyword arguments and update a dictionary.
"""

def update_car_info(**kwargs):
    """
    Dynamically updates car information.

    Parameters:
        **kwargs: Arbitrary keyword arguments representing car attributes.

    Returns:
        dict: Updated car dictionary with availability status.
    """

    # Store incoming keyword arguments as dictionary
    car = dict(kwargs)

    # Add additional information
    car['is_available'] = True

    return car


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":

    result = update_car_info(
        brand='Toyota',
        price=20000
    )

    print("Updated Car Information:")
    print(result)
