# Give the class a name
class PersonalAssistant:

  # Add an __init__ function here
  def __init__(self):
    self.contacts = {
      'Chloe': 'Student', 'Guy': 'Water Conservation Horticulturalist', 'Roger': 'Retired Range Scientist', 'James': 'Owner/Operator at Grand Prismatic Seed'
    }
    self.todos = []

  # Complete the add_todo function code
  def add_todo(self, new_item):
    self.todos.append(new_item)
  
  # Complete the remove_todo function code
  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      #Get the todo_item index in list
      index = self.todos.index(todo_item)
      #pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo item is not in list!")
  
  # Complete the get_todos function code
  def get_todos(self):
    return self.todos
  
  # Complete the get_birthday function code
  def get_birthday(self, name):
    if name == "Chloe":
        print("Chloe's birthday is on January 2nd.")
    elif name == "Guy":
        print("Guy's birthday is March 30th.")
    elif name == "Roger":
        print("Roger's birthday is on January 25th.")
    elif name == "James":
        print("James's birthday is on October 16th.")
    else:
        print("There is no record of that person's birthday.")

  # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No existng contact with that name!"
    
# Code to test the class
assistant = PersonalAssistant()
assistant.add_todo("Pick up Christmas lights from the store on the way home.")
assistant.add_todo("Get the oil changed in the truck.")
print(assistant.get_todos())
assistant.remove_todo("Get the oil changed in the truck.")
print(assistant.get_todos())
print(assistant.get_contact("Guy"))
print(assistant.get_contact("Chelsea"))
print(assistant.get_birthday("Chloe"))