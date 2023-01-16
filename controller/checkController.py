from flask import Flask, request, jsonify

app = Flask(__name__)

def find_most_plays(category, most_plays_category):
    if category["plays"] > most_plays_category["plays"]:
        most_plays_category = category
        #agr category k andar sb category nhi ho tu loop main na jaye
    return  most_plays_category

def top_category():
    data = request.get_json()
    most_plays_category = {"plays": 0}
    for category in data["categories"]:
         most_plays_category = find_most_plays(category, most_plays_category)
         
    return jsonify({
        "Most Played Category": {
            "Category Name": most_plays_category['name'],
            "Number of Plays": most_plays_category['plays']
        }
    })

if __name__ == "__main__":
    app.run()