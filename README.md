# Mint Green Recipes App

This project is for my girlfriend Alissa, who wanted something that would tell her what meals she could make with the ingredients she had on hand. She loves mint green.

Access it here (might be taken down at any time): https://mint-green-recipes.herokuapp.com/recipes/?ingredients=your,ingredients,go,here

This repo contains the server code for this site. This is written in Django; a React frontend is to come. The recipes are stored in a MongoDB via MongoDB Atlas (hosted on AWS). For more detail on tech used, see section below.

# Data Used

See corresponding data repo for Python code used for data cleaning and loading to MongoDB Atlas. Data for all recipes was pulled from a dataset I found on eightportions.com, called Recipe box. The website and its creator's GitHub repo for it can be found at the following links, respectively:

https://eightportions.com/datasets/Recipes/

https://github.com/rtlee9/recipe-box

Huge thanks to them for putting that together, this would not have been possible without them. The recipes are originally from Food Network, Epicurious, and Allrecipes.com; their program scraped that data. All rights to the recipes in this project ultimately go to each of those providers.