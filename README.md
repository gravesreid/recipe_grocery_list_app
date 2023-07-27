# recipe_grocery_list_app
application that allows the user to select a menu of recipes for the week, with input from the user of ingredients on hand to help choose recipes. Makes a grocery list based on the recipes chosen.

## recipe ingredient formatting
recipe ingredients are stored in .csv format, with the ingredient name, ingredient quantity, and ingredient unit in each line of the .csv. At the beginning of the main script, all recipe ingredients are converted to a list to be placed in the recipe object for each recipe

## do you have ingredients on hand and want to select recipes based on what you have?
the first output is to ask the user if they have ingredients on hand that they would like to base their dinner menu off of. If the user inputs 'y', then the program outputs all ingredients that may apply to the recipe options. Then the user is asked how many ingredients they want the program to consider. The user then inputs the index corresponding to the ingredients they have. 

## here are the recipes with ingredients you already have
the program then outputs the name of the recipes that contain ingredientss the user has on hand, and how many ingredients the recipe has that the user has on hand

## pick the recipe to start with
the user is presented with a listing of the recipe options. The user is then asked to select the primary recipe for the menu. 

## here are your other options
the program then outputs a listing of the remaining recipe options and the number of common ingredients with the primary recipe. This enables selection of recipes with the desired number of common ingredients to the primary recipe. The user is then asked how many additional recipes are desired. The user then inputs the index for the remaining recipes

## here is your grocery list
the program outputs the grocery list to make all the recipes. The ingredients the user may have entered as being on hand are not entered, so the user can verify they have the correct quantity of the ingredients before removing them from the list

# Future capabilities
1) make an online grocery pickup order
2) allow ingredient substitutions
3) create new recipes with help from AI
4) suggest recipes based on user preferences from AI assistant
5) adjust recipes for desired macronutrient profile and recipe cost with AI assistant

