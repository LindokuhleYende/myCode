# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number
# of arguments each time.
sandwich_list = []
def sandwiches(*ingredients):
    print(f"This is what I want in my sandwich: {', '.join(ingredients)}")

sandwiches("tomato", "cheese")
sandwiches("bacon", "sauce", "chips")
sandwiches("cheese", "polony", "egg", "russian")
