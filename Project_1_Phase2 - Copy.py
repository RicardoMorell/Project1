### ADD YOUR TEAM NAME, STUDENTs ID AND SECTION NUMBER BELOW ###
# TEAMNAME:
# STUDENT1 NAME:
# STUDENT1 ID:
# STUDENT2 NAME:
# STUDENT2 ID:
# SECTION:
############      DEFINE CONSTANTS BELOW      ############


# 1. Prompt user for input of ingredients available
# 2. ask user what they'd like to make (from options)
# 3a. If sufficient ingredients remain, subtract ingredients used, and present remaining amount. Go to step 2
# 3b. Otherwise tell the user they don't have enough ingredients, go to step 2.
# THE FOLLOWING LIST CONTAINS THE UNITS OF THE INGREDIENTS
units = ['cups', 'tablespoons', '', 'cups', 'teaspoons', 'teaspoons', 'slices', '', '', '']
# THE FOLLOWING LIST CONTAINS THE NAMES OF THE INGREDIENTS
ingredients = ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']
# YOU WILL USE THE FOLLOWING LIST TO SAVE THE INGREDIENTS
pantry = []

# THE FOLLOWING ARE EXAMPLES OF RECIPES - OBSERVE THE ORDER OF THE INGREDIENTS IS THE SAME THAN THE ORDER OF THE PANTRY
# banana pancakes require 1 cup of flour, 2 tablespoons sugar, 1 egg, 1 cup of milk, 3 teaspoons cinnamon,
# 2 teaspoon baking powder, 0 bread, 2 bananas
banana_pancake_recipe = [1, 2, 1, 1, 3, 2, 0, 2, 0, 0]
# peach crepes require 1 cup of flour, 0 tablespoons sugar, 1 egg, 1 cup of milk, 2 teaspoons cinnamon,
# 0 teaspoon baking powder, 0 bread, 0 bananas, 0 apples, 3 peaches
peach_crepe_recipe = [1, 0, 1, 1, 2, 0, 0, 0, 0, 3]

# apple pie requires 2 cups of flour, 4 tablespoons sugar, 2 eggs, 0.5 cup milk, 1 teaspoon cinnamon,
# 1 teaspoon baking powder, 0 bread, 0 banana, 5 apples, 0 peaches
apple_pie_recipe = [2, 4, 2, 0.5, 1, 1, 0, 0, 5, 0]

# french_toast_recipe requires 0.5 cups of flour, 3 tablespoons sugar, 3 eggs, 0.5 cup milk, 2 teaspoon cinnamon,
# 0 teaspoon baking powder, 8 bread, 0 banana, 0 apples, 0 peaches
french_toast_recipe = [0.5, 3, 3, 0.5, 2, 0, 8, 0, 0, 0]

# scrambled_eggs requires 0 cups of flour, 0 tablespoons sugar, 4 eggs, 0.5 cup milk, 0 teaspoon cinnamon,
# 0 teaspoon baking powder, 2 bread, 0 banana, 0.5 apples, 1 peaches
scrambled_eggs = [0, 0, 4, 0.5, 0, 0, 2, 0, 0.5, 1]

menu = [banana_pancake_recipe, peach_crepe_recipe, apple_pie_recipe, french_toast_recipe, scrambled_eggs]
menu_list = ["banana pancake", "peach crepe", "apple pie", "french toast", "scrambled eggs with toast and fruits"]


# the following funciton allow to enter the ingredients
def pantry_ingredients(units, ingredients):
    for i in range(len(units)):
        unit = units[i]
        if unit:
            unit += ' of '
        ingredient = ingredients[i]
        item = input(f'How many {unit}{ingredient} do you have? ')
        pantry.append(int(item))


# uncomment the line below and write the body of the function that allow to prin the content of the pantry
def show_pantry():  # this function show the ingredients of an exisiting pantry
    for y in range(len(pantry)):
        unit = units[y]
        if unit:
            unit += ' of '
        ingredient = ingredients[y]
        print(f'{pantry[y]} {unit}{ingredient} ')


# you don't need to modify this function for phase 1
def recipe_menu():
    print("What would you like to cook? Here's the recipe book:")
    for i in range(len(menu_list)):
        print(i + 1, ". ", menu_list[i], sep="")

    print(i + 2, ". Nevermind, I don't want to cook anything (Exit).", sep="")
    option = int(input("Select an option by typing its number here:"))
    return option


# uncomment the line below and write the code to verigy if the option is valid, if the option is valed get the recipe from
# the list menu usind the list index, and return the recipe and break the loop, if option is 6 terminate the progeam
# if the option is not valid keep asking the user to enter a valid option while showing the recipe menu
def valid_option(option):
    while option not in [1, 2, 3, 4, 5, 6]:
        print("Not a valid option!")
        option = recipe_menu()
    if option == 6:
        return option
    else:
        return menu[option - 1]


# uncomment the line below and write the code to verify if there are enough ingredients in the pantr
# to cookd the slected recipe, use substraction of the pantry and recipe lists
# if there is not enough element show a message that indicate there are not enough ingredients
# if there is enough ingreidients then show a happy mesaje and uptade the pantry
# hint: you can replace the pantry with a anew pantry

def pantry_update(recip):
    new_pantry = [] + pantry
    for i in range(len(new_pantry)):
        if new_pantry[i] >= recip[i]:
            new_pantry[i] = new_pantry[i] - recip[i]
        elif new_pantry[i] < recip[i]:
            print("Not enough ingredients!")
            return pantry
    print("Hope you enjoy it!")
    return new_pantry


#New added in phase 2
def mult_pantry(recipe):
    mult = int(input("How many serving? "))
    for m in range(len(recipe)):
        recipe[m] = recipe[m] * mult
    return recipe


# YOU DON'T NEED TO MODIFY THE FOLLOWING LINES OF CODE CALL ALL TEH FUNCTIONS TO PERFORM THE REQUIERMENTS OF PHASE 1,
# IF YOUR FUCNITONS ARE IMPLENTED CORRECTELY THE OUTPUT WOULD CORRESPOND TO THE EXAMPLES SHOW IN THE VIDEO
# AND IN THE PROJECT INSTRUCTIONS
# 1. Prompt user for input of ingredients available
# ONCE YOU IMPLEMENT THE FUNCITON UNCOMMEN THE FOLLOWING BLOCK

pantry_ingredients(units, ingredients)
while True:
    # 2. ask user what they'd like to make (from options)-COMMENT
    option = recipe_menu()
    print(f'You selected option {option}')
    # call the corresponding function to verify the selected option is valid-COMMENT
    recipe = valid_option(option)
    if recipe == 6:
        break
    #Multiplication of recipe
    quantity = mult_pantry(recipe)
    # if the option is valid and want to cook (diffent to 6)-COMMENT
    pantry = pantry_update(quantity)
    # -COMMENT 3a. If sufficient ingredients remain, subtract ingredients used, and present remaining amount. Go to step 2# ingredients =
    # -COMMENT ['flour', 'sugar', 'eggs', 'milk', 'cinnamon', 'baking powder', 'bread', 'bananas', 'apples', 'peaches']
    print("Here's what's left in the pantry: ")
    show_pantry()