# %%
# Setup

import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.hellofresh.com/recipes/cobia-with-thai-style-coconut-curry-65e73ec8e0f6df055447ffcd"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# %%
# Title Finder

def getRecipeTitle(_soup):
    return _soup.find("title").text

# %%
# Ingredients Finder

def getIngredientsList(_soup):
    shippedIngredients = _soup.findAll("div", {"data-test-id": "ingredient-item-shipped"})

    output = []

    for chunk in shippedIngredients:
        units = chunk.div.nextSibling.contents[0].text
        ingy = {"amount": units.split(" ")[0],
                "units": units.split(" ")[1],
                "ingredient": chunk.div.nextSibling.contents[1].text}
        output.append(ingy)

    return output

# %%
# Steps Finder

def getSteps(_soup):
    steps = _soup.findAll("div", {"data-test-id": "instruction-step"})

    output = []

    for step in steps:
        stepNumber = step.find("span", {"type": "body-xl-regular"}).text

        description = step.find("span", {"type": "body-md-regular"}).text

        output.append({"step": stepNumber, "instructions": description})

    return output


# %%
# Cook Times Finder

def getCookTimes(_soup):
    total = _soup.find("span", {"data-translation-id": "recipe-detail.preparation-time"})

    prep = _soup.find("span", {"data-translation-id": "recipe-detail.cooking-time"}) # these tags seem to be backwards...

    return {"totalTime": total.parent.nextSibling.text, "prepTime": prep.parent.nextSibling.text}

# %%
# Fancy Output

title = getRecipeTitle(soup)
print(title)

print("-" * len(title))

timing = getCookTimes(soup)
print("Total Time: " + timing["totalTime"])
print("Prep Time: " + timing["prepTime"])

print("-" * len(title))

for out in getIngredientsList(soup): 
    print(out["ingredient"] + ": " + out["amount"] + " " + out["units"])

print("-" * len(title))

for step in getSteps(soup):
    print("Step " + step["step"] + ": ")
    print(step["instructions"])
    print()



