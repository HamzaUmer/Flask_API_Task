from flask import Flask, request, jsonify

app = Flask(__name__)

def find_most_plays(category, most_plays_category, most_plays_subcategory):
    if category["plays"] > most_plays_category["plays"]:
        most_plays_category = category
        #agr category k andar sb category nhi ho tu loop main na jaye
    for subcategory in category.get("subcategories", []):
        most_plays_subcategory, most_plays_category = find_most_plays(subcategory, most_plays_category, most_plays_subcategory)
    if not category.get("subcategories"):
        if category["plays"] > most_plays_subcategory["plays"]:
            most_plays_subcategory = category
    return most_plays_subcategory, most_plays_category

def top_category_and_leaf():
    data = request.get_json()
    most_plays_category = {"plays": 0}
    most_plays_subcategory = {"plays": 0}
    for category in data["categories"]:
        most_plays_subcategory, most_plays_category = find_most_plays(category, most_plays_category, most_plays_subcategory)
    return jsonify({
        "Most Played Category": {
            "Category Name": most_plays_category['name'],
            "Number of Plays": most_plays_category['plays']
        },
        "Most Played Subcategory": {
            "Category Name": most_plays_subcategory['name'],
            "Number of Plays": most_plays_subcategory['plays']
        }
    })

if __name__ == "__main__":
    app.run()
