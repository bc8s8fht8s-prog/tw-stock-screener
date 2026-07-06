from flask import Flask, render_template, request
import json
import math

app = Flask(__name__)

PAGE_SIZE = 50


@app.route("/")
def index():

    with open("data/result.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    page = request.args.get("page", default=1, type=int)

    total = len(data["stocks"])

    total_pages = max(1, math.ceil(total / PAGE_SIZE))

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    start = (page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE

    stocks = data["stocks"][start:end]

    return render_template(
        "index.html",
        data=data,
        stocks=stocks,
        page=page,
        total_pages=total_pages,
        start=start + 1 if total > 0 else 0,
        end=min(end, total),
    )


if __name__ == "__main__":
    app.run(debug=True)