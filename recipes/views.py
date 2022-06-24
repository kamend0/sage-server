from django.shortcuts import render
from django.http import JsonResponse
import pymongo
import environ
import re
# import pandas as pd


##################
# ESTABLISHING MONGODB CONNECTION
##################

env = environ.Env()
environ.Env.read_env()
# environ.Env.read_env('../config/.env')

client = pymongo.MongoClient(env("CONNECTION_STRING"))
db = client['recipesApp']
recipes = db['recipes']


##################
# HELPER FUNCTIONS
##################

def convert_to_regx(l):
    # l is a list of strings
    r_l = []
    for i in l:
        r_l.append(re.compile(i, re.IGNORECASE))
    return r_l

def score_recipe(client_ing, rec_ing):
    # client_ing is list of ingredients provided by client
    # rec_ing is list of ingredients in the result recipe from loop
    # returns score as float between [0.0, 1.0]
    score = 0
    try:
        for ci in client_ing:
            if (any(ci in ri for ri in rec_ing)):
                score += 1
        return (score / len(client_ing))
    except:
        return 0

def get_recipes_from_db(ing_list):
    # ing_list is list of ingredients; need to be converted to regex
    # returns dictionary
    recipe_results = {}
    for index, recipe in enumerate(recipes.find({ "ingredients" : { "$all" : convert_to_regx(ing_list) } })):
        match_score = score_recipe(client_ing = ing_list, rec_ing = recipe['ingredients'])
        recipe_results[index] = {'title' : recipe['title'],
                                 'ingredients' : recipe['ingredients'],
                                 'instructions' : recipe['instructions'],
                                 'match' : match_score}

    return recipe_results


##################
# VIEWS
##################

# $in: return documents that match any in the list
# $all: return documents that match all in the list

def get_unordered_recipes(request):
    ingredients = (request.GET.get('ingredients', '')).split(",")
    try:
        if ((request.GET.get('order', '')).lower() == "true"):
            order_result = True
        else:
            order_result = False
    except:
        order_result = False
    
    matching_recipes = get_recipes_from_db(ing_list = ingredients)

    return JsonResponse(matching_recipes, safe = False)