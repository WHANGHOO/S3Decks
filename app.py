from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Function to load existing entries from the file
def load_entries():
    try:
        with open("entries.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save entries to the file
def save_entries(entries):
    with open("entries.json", "w") as file:
        json.dump(entries, file)

# Route for the main page
@app.route("/", methods=["GET", "POST"])
def index():
    # Load current entries
    entries = load_entries()

    if request.method == "POST":
        name = request.form.get("name")
        deck = request.form.get("deck")
        level = request.form.get("level")

        if name:
            # Overwrite or add the new entry
            entries[name] = {"deck": deck, "level": level}
            save_entries(entries)  # Save the updated entries

    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
