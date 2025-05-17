from flask import Flask, request, jsonify
from stats import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def analyse_text():
    if request.method == "GET":
        return """
            <h1>Upload text</h1>
            <form action="/" method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit" value="Analyse">
            </form>
        """
    
    # analysis
    if "file" not in request.files:
        return "No file provided", 400

    text = request.files["file"].read().decode("utf-8")
    
    word_count = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sorted_dict(char_counts)

    # alphabetical only
    alpha_chars = [
        {"char": d["char"], "count": d["num"]}
        for d in sorted_chars
        if d["char"].isalpha()
    ]

    return jsonify({
        "word_count": word_count,
        "character_count": alpha_chars
    })

if __name__ == "__main__":
    app.run()
