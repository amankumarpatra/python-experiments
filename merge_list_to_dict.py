"""
File Name: merge_list_to_dict.py
Author: Aman Kumar Patra
Description:
    This script demonstrates how to merge two lists into a dictionary
    using Python's built-in zip() and dict() functions.

Concept Used:
    - zip()
    - dict()
    - Functions
    - Basic error handling
"""


def merge_list_to_dict(keys_list, values_list):
    """
    Merges two lists into a dictionary.

    Parameters:
        keys_list (list): A list containing dictionary keys.
        values_list (list): A list containing dictionary values.

    Returns:
        dict: A dictionary created by pairing elements of both lists.

    Raises:
        ValueError: If the length of both lists is not equal.
    """

    # Check if both lists are of equal length
    if len(keys_list) != len(values_list):
        raise ValueError("Both lists must have the same number of elements.")

    # zip() pairs elements from both lists
    paired_data = zip(keys_list, values_list)

    # Convert zipped object into dictionary
    result_dictionary = dict(paired_data)

    return result_dictionary


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":

    # List of dictionary keys
    first_list = ['first_name', 'middle_name', 'last_name']

    # List of dictionary values
    second_list = ['Aman', 'Kumar', 'Patra']

    # Function call
    result = merge_list_to_dict(first_list, second_list)

    # Display output
    print("Generated Dictionary:")
    print(result)
