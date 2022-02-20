import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from numpy import delete



# Using a service account to access the database
cred = credentials.Certificate(r'C:\Users\JohnX\Documents\Python Files\CSE 310\W06\noted-cider-341702-90c23edaa91d.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def initialize_test_entries():
    '''A few database entries that cover the three categories, useful for testing'''
    doc_ref = db.collection(u'meals').document(u'Waffles')
    doc_ref.set({
    u'meal': u'breakfast',
    u'carbs': u'9',
    })

    doc_ref = db.collection(u'meals').document(u'Bologna Sandwich')
    doc_ref.set({
        u'meal': u'lunch',
        u'carbs': u'35',
    })

    doc_ref = db.collection(u'meals').document(u'Cheeseburger')
    doc_ref.set({
        u'meal': u'dinner',
        u'carbs': u'42',
    })

def add_meal(meal_name):
    '''Adds a meal the the database, with no category set'''
    doc_ref = db.collection("meals").document(meal_name)
    doc_ref.set({
        u'meal':'uncategorized',
    })

def delete_meal(meal_name):
    '''Deletes an entire meal from the list of meals'''
    doc_ref = db.collection(u"meals").document(meal_name)
    doc_ref.delete()

def edit_meal_attribute(meal_name,attribute,new_value):
    '''Allows the user to edit a given attribute, replacing it with a new value'''
    doc_ref = db.collection("meals").document(meal_name)
    doc_ref.set({
        attribute:new_value,
    })

def display_meal_data(meal_name):
    '''Displays all the data stored within a provided meal's document'''
    desired_meal_ref = db.collection("meals").document(meal_name)
    desired_meal = desired_meal_ref.get()
    print("Information on " + meal_name + ":")
    print(desired_meal.to_dict() + "\n")

def display_all_by_meal_type(meal_type):
    '''Displays every meal within a provided category'''

    meals = db.collection(u'meals').where(u'meal', u'==', meal_type).stream()

    print("Here are all of your " + meal_type + " meals:")
    for meal in meals:
        print(f'{meal.id}')

def display_all():
    '''Displays all of the meals inside the collection'''
    meals = db.collection(u'meals')
    docs = meals.stream()

    print("Here are all of your meals:")
    for meal in docs:
        print(f'{meal.id}')

def database_interface_loop():
    '''Loops through the various program functions until the user inputs a desire to quit.'''
    running = True
    while running:
        print("Welcome to the meal-food manager system!")
        choice = input('You can choose to "list", "add", "edit", "remove", or "inspect" any of your meals. Enter "quit" to end the program\n').lower()
        if choice == "list":
            list_type = input('Would you like to list "all", or sorted by "category"?\n').lower()
            if list_type == "all":
                display_all()
            elif list_type == "category":
                meal_type = input('What category of meal would you like to list?\n').lower()
                display_all_by_meal_type(meal_type)
            else:
                print("That is an invalid input")
        elif choice == "add":
            meal_name = input("Enter a name for your new meal:\n")
            add_meal(meal_name)
        elif choice == "edit":
            edit_target = input("Which meal would you like to edit?\n")
            target_aspect = input("What aspect of " + edit_target + " would you like to change?\n")
            updated_value = input("What would you like " + edit_target + "'s new " + target_aspect + " to be?")
            edit_meal_attribute(edit_target,target_aspect,updated_value)
        elif choice == "remove":
            removal_target = input("Which meal do you wish to remove?\n")
            delete_meal(removal_target)
        elif choice == "inspect":
            inspection_target = input("Which meal do you wish to inspect?\n")
            display_meal_data(inspection_target)
        elif choice == "quit":
            print("Thanks for using the meal-food manager system!")
            running = False
        else:
            print("That is an invalid option, please type them exactly as they appear in the quotation marks.\n")

# Begin the program loop, end when receiving the proper input
database_interface_loop()