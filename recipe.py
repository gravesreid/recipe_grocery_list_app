import csv


#import the recipe lists first each recipe is stored in a csv file,
#so the quantity is in string format make a
#function to go through each recipe and convert the quantity to a float
def make_float(recipe_ing):
    new_list = recipe_ing
    for ingredient in new_list:
        ingredient[1] = float(ingredient[1])
    return new_list

#cosb for camelized onion swiss burgers
with open('caramelized_onion_swiss_burgers.csv', 'r', newline='') as csvfile:
    cosb_ing = list(csv.reader(csvfile, delimiter=','))
#convert strings to float for ingredient quantity
cosb_ing = make_float(cosb_ing)

#obcbt for one pan cheesy beef tortilla melts
with open('one_pan_cheesy_beef_tortilla_melts.csv', 'r', newline='') as csvfile:
    opcbt_ing = list(csv.reader(csvfile, delimiter=','))
#convert strings to float for ingredient quantity
opcbt_ing = make_float(opcbt_ing)

#csf for cantina steak fajitas
with open('cantina_steak_fajitas.csv', 'r', newline='') as csvfile:
    csf_ing = list(csv.reader(csvfile, delimiter=','))
#convert strings to float for ingredient quantity
csf_ing = make_float(csf_ing)

#csb for cheesy smashed burgers
with open('cheesy_smashed_burgers.csv', 'r', newline='') as csvfile:
    csb_ing = list(csv.reader(csvfile, delimiter=','))
#convert the strings to float for ingredient quantitity
csb_ing = make_float(csb_ing)

#ctgcc for creamy tomato-garlic chicken curry
with open('creamy_tomato_garlic_chicken_curry.csv', 'r', newline='') as csvfile:
    ctgcc_ing = list(csv.reader(csvfile, delimiter=','))
#convert the strings to float for ingredient quantitity
ctgcc_ing = make_float(ctgcc_ing)

#tcct for thai coconut curry tofu
with open('thai_curry_tofu.csv', 'r', newline='') as csvfile:
    tcct_ing = list(csv.reader(csvfile, delimiter=','))
#convert the strings to float for ingredient quantitity
tcct_ing = make_float(tcct_ing)

#scbt for sesame chili beef tenderloin
with open('sesame_chili_beef_tenderloin.csv', 'r', newline='') as csvfile:
    scbt_ing = list(csv.reader(csvfile, delimiter=','))
#convert str to float for quantity
scbt_ing = make_float(tcct_ing)

#ffobt for fancy french onion beef tenderloin
with open('fancy_french_onion_beef_tenderloin.csv', 'r', newline='') as csvfile:
    ffobt_ing = list(csv.reader(csvfile, delimiter=','))
#convert str to float for qnty
ffobt_ing = make_float(ffobt_ing)

#mwbs for meatballs with bulgogi sauce
with open('meatballs_with_bulgogi_sauce.csv', 'r', newline='') as csvfile:
    mwbs_ing = list(csv.reader(csvfile, delimiter=','))
#convert str to fload for qnty
mwbs_ing = make_float(mwbs_ing)

#opbev for one pan beef enchiladas verdes
with open('one_pan_beef_enchiladas_verdes.csv', 'r', newline='') as csvfile:
    opbev_ing = list(csv.reader(csvfile, delimiter=','))
opbev_ing = make_float(opbev_ing)

#sbc for southwest beef cavatappi
with open('southwest_beef_cavatappi.csv', 'r', newline='') as csvfile:
    sbc_ing = list(csv.reader(csvfile, delimiter=','))
sbc_ing = make_float(sbc_ing)

#pspics for pork sausage penne in creamy sauce
with open('pork_sausage_penne_in_creamy_sauce.csv', 'r', newline='') as csvfile:
    pspics_ing = list(csv.reader(csvfile, delimiter=','))
pspics_ing = make_float(pspics_ing)

#scpacsf for sweet chili pork and cabbage stir fry
with open('sweet_chili_pork_and_cabbage_stir_fry.csv', 'r', newline='') as csvfile:
    scpacsf_ing = list(csv.reader(csvfile, delimiter=','))
scpacsf_ing = make_float(scpacsf_ing)

# pscb for pork sausage cavatappi bolognese
with open('pork_sausage_cavatappi_bolognese.csv', 'r', newline='') as csvfile:
    pscb_ing = list(csv.reader(csvfile, delimiter=','))
pscb_ing = make_float(pscb_ing)

#psarbpp for pork sausage and red bell pepper pasta
with open('pork_sausage_and_roasted_bell_pepper_pasta.csv', 'r', newline='') as csvfile:
    psarbpp_ing = list(csv.reader(csvfile, delimiter=','))
psarbpp_ing = make_float(psarbpp_ing)

#mspb for moo shu pork bowls
with open('moo_shu_pork_bowls.csv', 'r', newline='') as csvfile:
    mspb_ing = list(csv.reader(csvfile, delimiter=','))
mspb_ing = make_float(mspb_ing)

# pccp for parmesan chive chicken and potatoes
with open('parmesan_chive_chicken_and_potatoes.csv', 'r', newline='') as csvfile:
    pccp_ing = list(csv.reader(csvfile, delimiter=','))
pccp_ing = make_float(pccp_ing)

# cddc for creamy dijon dill chicken
with open('creamy_dijon_dill_chicken.csv', 'r', newline='') as csvfile:
    cddc_ing = list(csv.reader(csvfile, delimiter=','))
cddc_ing = make_float(cddc_ing)

# csrics for chicken sausage rigatoni in creamy sauce
with open('chicken_sausage_rigatoni_in_creamy_sauce.csv', 'r', newline='') as csvfile:
    csrics_ing = list(csv.reader(csvfile, delimiter=','))
csrics_ing = make_float(cddc_ing)

# spmjc for sheet pan monterey jack chicken
with open('sheet_pan_monterey_jack_chicken.csv', 'r', newline='') as csvfile:
    spmjc_ing = list(csv.reader(csvfile, delimiter=','))
spmjc_ing = make_float(spmjc_ing)

# scscb for street cart style chicken bowls
with open('street_cart_style_chicken_bowls.csv', 'r', newline='') as csvfile:
    scscb_ing = list(csv.reader(csvfile, delimiter=','))
scscb_ing = make_float(scscb_ing)

# trwhc for truffle risotto with herbed chicken
with open('truffle_risotto_with_herbed_chicken.csv', 'r', newline='') as csvfile:
    trwhc_ing = list(csv.reader(csvfile, delimiter=','))
trwhc_ing = make_float(trwhc_ing)

# ccaba for crispy chicken and bacon alfredo
with open('crispy_chicken_and_bacon_alfredo.csv', 'r', newline='') as csvfile:
    ccaba_ing = list(csv.reader(csvfile, delimiter=','))
ccaba_ing = make_float(ccaba_ing)

# ssccr for southwest spiced chicken cumin rice
with open('southwest_spiced_chicken_cumin_rice.csv', 'r', newline='') as csvfile:
    ssccr_ing = list(csv.reader(csvfile, delimiter=','))
ssccr_ing = make_float(ssccr_ing)

# cogps for chicken over garlic parmesan spaghetti
with open('chicken_over_garlic_parmesan_spaghetti.csv', 'r', newline='') as csvfile:
    cogps_ing = list(csv.reader(csvfile, delimiter=','))
cogps_ing = make_float(cogps_ing)

# gccwfb for goat cheese chicken with figgy balsamic
with open('goat_cheese_chicken_with_figgy_balsamic.csv', 'r', newline='') as csvfile:
    gccwfb_ing = list(csv.reader(csvfile, delimiter=','))
gccwfb_ing = make_float(gccwfb_ing)

# abgpf for apricot balsamic glazed pork filet
with open('apricot_balsamic_glazed_pork_filet.csv', 'r', newline='') as csvfile:
    abgpf_ing = list(csv.reader(csvfile, delimiter=','))
abgpf_ing = make_float(abgpf_ing)

# clhpc for creamy lemon herb pork chops
with open('creamy_lemon_herb_pork_chops.csv', 'r', newline='') as csvfile:
    clhpc_ing = list(csv.reader(csvfile, delimiter=','))
clhpc_ing = make_float(clhpc_ing)

# cssps for chicken sausage sweet potato soup
with open('cssps.csv', 'r', newline='') as csvfile:
    cssps_ing = list(csv.reader(csvfile, delimiter=','))
cssps_ing = make_float(cssps_ing)

# bc for bruschetta chicken
with open('bruschetta_chicken.csv', 'r', newline='') as csvfile:
    bc_ing = list(csv.reader(csvfile, delimiter=','))
bc_ing = make_float(bc_ing)

# lgcagb for lemon garlic chicken and green beans
with open('lemon_garlic_chicken_and_green_beans.csv', 'r', newline='') as csvfile:
    lgcagb_ing = list(csv.reader(csvfile, delimiter=','))
lgcagb_ing = make_float(lgcagb_ing)

# pcc for pecan crusted chicken
with open('pecan_crusted_chicken.csv', 'r', newline='') as csvfile:
    pcc_ing = list(csv.reader(csvfile, delimiter=','))
pcc_ing = make_float(pcc_ing)

# btahc for balsamic tomato and herb chicken
with open('balsamic_tomato_and_herb_chicken.csv', 'r', newline='') as csvfile:
    btahc_ing = make_float(list(csv.reader(csvfile, delimiter=',')))

# spdocc for sheet pan dijon onion crunch chicken
with open('sheet_pan_dijon_onion_crunch_chicken.csv', 'r', newline='') as csvfile:
    spdocc_ing = make_float(list(csv.reader(csvfile, delimiter=',')))

# basdtp for broccoli and sun dried tomato pasta
with open('broccoli_and_sundried_tomato_pasta.csv', 'r', newline='') as csvfile:
    basdtp_ing = make_float(list(csv.reader(csvfile, delimiter=',')))

# tcccs for thai coconut curry chicken soup
with open('thai_coconut_curry_chicken_soup.csv', 'r', newline='') as csvfile:
    tcccs_ing = make_float(list(csv.reader(csvfile, delimiter=',')))

# ssbbqb for sweet and spicy bbq burgers
with open('sweet_and_spicy_bbq_burgers.csv', 'r', newline='') as csvfile:
    ssbbqb_ing = make_float(list(csv.reader(csvfile, delimiter=',')))

#define recipe class. Will have a name and list of ingredients
class Recipe:
    def __init__(self, name, ingredients, recipe_number):
        self.name = name
        self.ingredients = ingredients
        self.recipe_number = recipe_number

#make recipe objects from ingredient lists of each recipe
cosb = Recipe('Caramelized Onion Swiss Burgers', cosb_ing, 1)
opcbt = Recipe('One Pan Cheesy Beef Tortillas', opcbt_ing, 2)
csf = Recipe('Cantina Steak Fajitas', csf_ing, 3)
csb = Recipe('Cheesy Smashed Burgers', csb_ing, 4)
ctgcc = Recipe('Creamy Tomato-Garlic Chicken Curry', ctgcc_ing, 5)
tcct = Recipe('Thai Coconut Curry Tofu', tcct_ing, 6)
scbt = Recipe('Sesame Chili Beef Tenderloin', scbt_ing, 7)
ffobt = Recipe('Fancy French Onion Beef Tenderlion', ffobt_ing, 8)
mwbs = Recipe('Meatballs With Bulgogi Sauce', mwbs_ing, 9)
opbev = Recipe('One Pan Beef Enchiladas Verdes', opbev_ing, 10)
sbc = Recipe('Southwest Beef Cavatappi', sbc_ing, 11)
pspics = Recipe('Pork Sausage Penne in a Creamy Sauce', pspics_ing, 12)
scpacsf = Recipe('Sweet Chili Pork and Cabbage Stir Fri', scpacsf_ing, 13)
pscb = Recipe('Pork Sausage Cavatappi Bolognese', pscb_ing, 14)
psarbpp = Recipe('Pork Sausage and Roasted Bell Pepper Pasta', psarbpp_ing, 15)
mspb = Recipe('Moo Shu Pork Bowls', mspb_ing, 16)
pccp = Recipe('Parmesan Chive Chicken and Potatoes', pccp_ing, 17)
cddc = Recipe('Creamy Dijon Dill Chicken', cddc_ing, 18)
csrics = Recipe('Chicken Sausage Rigatoni in a Creamy Sauce', csrics_ing, 19)
spmjc = Recipe('Sheet Pan Monterey Jack Un-Fried Chickes', spmjc_ing, 20)
scscb = Recipe('Street Cart Style Chicken Bowls', scscb_ing, 21)
trwhc = Recipe('Truffle Risotto With Herbed Chicken', trwhc_ing, 22)
ccaba = Recipe('Crispy Chicken and Bacon Alfredo', ccaba_ing, 23)
ssccr = Recipe('Southwest Spiced Chicken and Cumin Rice', ssccr_ing, 24)
cogps = Recipe('Chicken Over Garlic Parmesan Spaghetti', cogps_ing, 25)
gccwfb = Recipe('Goat Cheese Chicken With Figgy Balsamic', gccwfb_ing, 26)
abgpf = Recipe('Aprcot Balsamic Glazed Pork Filet', abgpf_ing, 27)
clhpc = Recipe('Creamy Lemon-Herb Pork Chops', clhpc_ing, 28)
cssps = Recipe('Chicken Sausage and Sweet Potato Soup', cssps_ing, 29)
bc = Recipe('Bruschetta Chicken', bc_ing, 30)
lgcagb = Recipe('Lemon Garlic Chicken and Green Beans', lgcagb_ing, 31)
pcc = Recipe('Pecan Crusted Chicken', pcc_ing, 32)
btahc = Recipe('Balsamic Tomato and Herb Chicken', btahc_ing, 33)
spdocc = Recipe('Sheet Pan Dijon Onion Crunch Chicken', spdocc_ing, 34)
basdtp = Recipe('Broccoli and Sun-dried Tomato Pasta', basdtp_ing, 35)
tcccs = Recipe('Thai Coconut Curry Chicken Soup', tcccs_ing, 36)
ssbbqb = Recipe('Sweet and Spicy BBQ Burgers', ssbbqb_ing, 37)

#make a list of all the recipes. This list will be iterated through and compared with the primary recipe
grand_list = [cosb, opcbt, csf, csb, ctgcc, tcct, scbt, ffobt, mwbs, opbev, sbc, pspics, scpacsf, pscb, psarbpp, mspb, pccp, cddc, csrics, spmjc, scscb, trwhc, ccaba, ssccr, cogps, gccwfb, abgpf, clhpc, cssps, bc, lgcagb, pcc, btahc, spdocc, basdtp, tcccs, ssbbqb]

# make a list that contains all the ingredients in recipes on hand
master_ingredients = []
# iterate through the grand list, then through each ingredient name
for recipe in grand_list:
    for ingredient in recipe.ingredients:
        # make sure the ingredient isn't already in the master list of ingredients
        if master_ingredients.count(ingredient[0]) == 0:
            master_ingredients.append(ingredient[0])

# make a function to check ingredients on hand and tell the user what recipes contain them
def common_ing(ingredients_on_hand):
    # make list to store recipe name and number of common ingredients
    common_ingredients = []
    for recipe in grand_list:
        common_count = 0
        for ingredients in recipe.ingredients:
            for ing_on_hand in ingredients_on_hand:
                if ingredients[0].lower() == ing_on_hand.lower():
                    common_count += 1
        common_ingredients.append([recipe.name, common_count])
    return common_ingredients

# ask user if they want to see recipes based on the ingredients they have on hand
check_common_ingredients = input('Do you want to see what recipes have ingredients you already have? (y/n)')

# if input is y, show recipes with common ingredients
if check_common_ingredients == 'y':
    sorted_recipes = []
    # show the user what ingredients are in the recipes stored in the program
    print('Here are the ingredients in the recipe options:')
    for ingredient in master_ingredients:
        print(ingredient + ' :' + str(master_ingredients.index(ingredient)))
    # ask user how many ingredients to input
    num_ing = int(input('how many ingredients do you want to check?'))
    ingredients_on_hand = []
    for i in range(num_ing):
        ingredient = input('Enter ingredient # (the number printed after the ingredient you have) for ingredient #' +str((i + 1)) + ' :')
        ingredients_on_hand.append(master_ingredients[int(ingredient)])
    unsorted_recipes = common_ing(ingredients_on_hand)
    # find the max number of common ingredients
    max_num_comm = 0
    for recipe in unsorted_recipes:
        if recipe[1] > max_num_comm:
            max_num_comm = recipe[1]
    # go through the unsorted list and pull the ones with the most common ingredients first and add to the common list, then go down sequentially
    for i in range(max_num_comm,0,-1):
        for recipe in unsorted_recipes:
            if recipe[1] == i:
                sorted_recipes.append(recipe)
    # go through sorted recipes and print number of common ingredients
    for recipe in sorted_recipes:
        print(recipe[0] + ' has ' + str(recipe[1]) + ' ingredients you already have')

# make a function to add recipe ingredients
def add_recipe():
    #ask user for recipe name
    recipe_name = input('Type the name of your recipe: ')
    #ask user how many ingredients are in the recipe
    num_ing = int(input('How many ingredients are in the recipe? '))
    # make empty list to fill with recipe ingredients
    recipe_ing = []
    # iterate through and ask user for ingredient name, quantity, and unit, then put into recipe_ing
    for i in range(num_ing):
        ing_name = input('What is the name of ingredient \# ' + str(i) + '? ')
        ing_quant = float(input('What is the numerical quantity of the ingredient? '))
        ing_unit = input('What is the unit of measurement for the ingredient? ')
        recipe_ing.append([ing_name, ing_quant, ing_unit])
    # the recipe number is 1 + the length of the list of existing recipes
    recipe_number = len(grand_list) + 1
    return Recipe(recipe_name, recipe_ing, recipe_number)


#show user what to enter to select recipe
for recipe in grand_list:
    print(str(recipe.recipe_number) + ': ' + recipe.name)

#determine the primary recipe. This is the recipe the user wants, and then the program will tell the user
#the number of similar ingredients
primary_recipe = input('What recipe do you want to start with?\n')

#convert user input string to recipe object
for recipe in grand_list:
    if primary_recipe == str(recipe.recipe_number):
        primary_recipe = recipe

#make a function to count the number of similar ingredients in each recipe
def ingredient_count(recipe, recipe_compare):
    recipe_ingredients = []
    similar_count = 0
    for ingredient in recipe.ingredients:
        recipe_ingredients.append(ingredient[0])
    ingredients_to_compare = []
    for ingredient in recipe_compare.ingredients:
        ingredients_to_compare.append(ingredient[0])
    for i in range(len(recipe_ingredients)):
        if ingredients_to_compare.count(recipe_ingredients[i]) != 0:
            similar_count += 1
    return similar_count

#go through each recipe in the list of all the recipes and output the number of similar ingredients. it will be most convienent if the output is sorted. Make a list to store similar ingredients
unsorted_sim_ing = []
for recipe in grand_list:
    if recipe.name != primary_recipe.name:
        unsorted_sim_ing.append([recipe.name, str(ingredient_count(primary_recipe, recipe))])
        #print(recipe.name + ' has ' + str(ingredient_count(primary_recipe, recipe)) + ' similar ingredients' + '\n')

#now make a list for the sorted similar ingredients, then go through the unsorted list to populate
sorted_sim_ing = []
max_sim = 0 #initialize maximum similar ingredients to 0

# determine the recipe with the maximum number of similar ingredients
for ingredient in unsorted_sim_ing:
    if int(ingredient[1]) > max_sim:
        max_sim = int(ingredient[1])

#place the recipes with the most similar ingredients first in the sorted list
for ingredient in unsorted_sim_ing:
    if int(ingredient[1]) == max_sim:
        sorted_sim_ing.append(ingredient)

# iterate through sequentially from one less than max similar ingredients, and add them to the sorted list in descending order
for i in range(max_sim-1, -1, -1):
    for ingredient in unsorted_sim_ing:
        if int(ingredient[1]) == i:
            sorted_sim_ing.append(ingredient)

#print the number of common ingredients in each recipe. Go through the grand list to pull out the recipe number for each recipe for user convenience
for recipe in sorted_sim_ing:
    for recipe_2 in grand_list:
        if recipe_2.name == recipe[0]:
            index = recipe_2.recipe_number
    print('Recipe Number: (' + str(index) + ') ' + recipe[0] + ' has ' + recipe[1] + ' ingredients in common ')

#ask user how many recipes they want to pick
num_recipes = input('How many recipes do you want to pick in addition to the recipe you already selected? ')

#make list to store menu selections
recipe_index = [str(primary_recipe.recipe_number)]

#now let the user pick the recipes
for i in range(int(num_recipes)):
    recipe_index.append(input('Which recipe number do you want for menu number ' + str(i + 2) + ' : '))

#now make a list to store the actual recipes for the week, then loop through the list of recipes and fill the list
recipes_for_week = []
for index in recipe_index:
    for recipe in grand_list:
        if index == str(recipe.recipe_number):
            recipes_for_week.append(recipe)
#print the recipes for the week
print('Your Menu for this week: ')
for recipe in recipes_for_week:
    print(recipe.name)

print('Your Grocery List: ')
# make a function to make a grocery list for the recipes selected
def make_list(recipes):
    g_list_ingredients = []
    g_list_quantity = []
    g_list_unit = []
    #go through each recipe
    for recipe in recipes:
        #unpack the recipe into a list for ingredient, a list for quantity, and a list for units
        r_ingredient = []
        r_quantity = []
        r_unit = []
        for ingredient in recipe.ingredients:
            r_ingredient.append(ingredient[0])
            r_quantity.append(ingredient[1])
            r_unit.append(ingredient[2])
   #check if the ingredient is already in the grocery list
        for i in range(len(r_ingredient)):
            #use numerical index to simplify aligning the three lists
            #for each index, check if the ingredient is already on the grocery list
            if g_list_ingredients.count(r_ingredient[i]) == 0:
                g_list_ingredients.append(r_ingredient[i])
                g_list_quantity.append(r_quantity[i])
                g_list_unit.append(r_unit[i])
            # if it is already on the grocery list, we need to adjust the quantity for that ingredientbut first, we need to find the index of the specific ingredient, then use that index to update the quantity list
            else:
                for j in range(len(g_list_ingredients)):
                       if g_list_ingredients[j] == r_ingredient[i]:
                           g_list_quantity[j] += r_quantity[i]
    g_list = []
    for i in range(len(g_list_ingredients)):
        # when the unit is 'unit', make it '' for the output
        if g_list_unit[i].lower() == 'unit':
            if g_list_quantity[i] > 1:
                g_list_unit[i] = g_list_ingredients[i] + 's'
                g_list_ingredients[i] = ''
            else:
                g_list_unit[i] = g_list_ingredients[i]
                g_list_ingredients[i] = ''
        g_list.append([g_list_ingredients[i], g_list_quantity[i], g_list_unit[i]])
    for i in range(len(g_list)):
        print(str(g_list[i][1]) + ' ' + g_list[i][2] + ' ' + g_list[i][0])

make_list(recipes_for_week)
