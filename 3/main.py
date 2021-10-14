# imports
from dictionary_word_storage import Dictionary as Dictionary_dictionary
from tuple_word_storage import Dictionary as Tuple_dictionary
from list_word_storage import Dictionary as List_dictionary

import os

# static variables

implementations = {
    "list": List_dictionary,
    "tuple": Tuple_dictionary,
    "dictionary": Dictionary_dictionary
}


# general functions


def print_menu():
    print("""
        1: Insert
        2: Lookup
        3: Exit Program
    """)


def get_user_selection(informed=True) -> int:
    if not informed:
        return int(input("?:"))

    print_menu()
    return int(input("?:"))


def get_current_implementation():
    implementation_var = os.environ["impl"]
    return implementations[implementation_var]


# main loop

impl = get_current_implementation()()

while True:
    selection = get_user_selection()
    if selection == 1:
        impl.insert()
    elif selection == 2:
        impl.lookup()
    elif selection == 3:
        break
