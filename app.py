
import random
from flask import Flask, render_template, request, jsonify
from solver import GOAL, get_neighbors, solve_puzzle

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_board():
    board = GOAL
    previous = None

    for i in range(20):
        choices = get_neighbors(board)

        if previous in choices:
            choices.remove(previous)

        previous = board
        board = random.choice(choices)

    return jsonify({"board": list(board)})


@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json(silent=True) or {}
    board = data.get("board")

    if not isinstance(board, list) or len(board) != 9:
        return jsonify({"error": "Invalid board"}), 400

    if any(type(n) is not int for n in board):
        return jsonify({"error": "Board must contain numbers"}), 400

    if sorted(board) != list(range(9)):
        return jsonify({"error": "Invalid puzzle numbers"}), 400

    steps = solve_puzzle(board)

    if not steps:
        return jsonify({"error": "Puzzle cannot be solved"}), 400

    return jsonify({
        "steps": steps,
        "moves": len(steps) - 1
    })


if __name__ == "__main__":
    app.run(debug=True)
