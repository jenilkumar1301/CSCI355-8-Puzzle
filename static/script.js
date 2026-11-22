
let board = [1, 2, 3, 4, 5, 6, 7, 8, 0];

const boardElement = document.getElementById("board");
const randomBtn = document.getElementById("randomBtn");
const solveBtn = document.getElementById("solveBtn");
const statusElement = document.getElementById("status");
const moveCount = document.getElementById("moveCount");

// Display the puzzle board
function drawBoard() {
    boardElement.innerHTML = "";

    for (let i = 0; i < board.length; i++) {
        const tile = document.createElement("div");

        if (board[i] === 0) {
            tile.className = "tile empty";
            tile.textContent = "";
        } else {
            tile.className = "tile";
            tile.textContent = board[i];
        }

        boardElement.appendChild(tile);
    }
}

// Disable or enable both buttons
function setButtonsDisabled(disabled) {
    randomBtn.disabled = disabled;
    solveBtn.disabled = disabled;
}

// Wait between animation moves
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Request a random board from Flask
async function randomizeBoard() {
    setButtonsDisabled(true);
    statusElement.textContent = "Randomizing puzzle...";
    moveCount.textContent = "";

    try {
        const response = await fetch("/random");
        const data = await response.json();

        if (!response.ok || data.error) {
            throw new Error(data.error || "Randomize failed.");
        }

        if (!Array.isArray(data.board) || data.board.length !== 9) {
            throw new Error("Invalid board received.");
        }

        board = data.board;
        drawBoard();

        statusElement.textContent = "Puzzle randomized!";
    } catch (error) {
        statusElement.textContent = "Error: " + error.message;
    } finally {
        setButtonsDisabled(false);
    }
}

// Request and animate the solution
async function solvePuzzle() {
    setButtonsDisabled(true);
    statusElement.textContent = "Solving puzzle...";
    moveCount.textContent = "";

    try {
        const response = await fetch("/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ board: board })
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            throw new Error(data.error || "Solve failed.");
        }

        if (!Array.isArray(data.steps) ||
            data.steps.length === 0) {
            throw new Error("Invalid solution received.");
        }

        const totalMoves = data.steps.length - 1;
        statusElement.textContent = "Animating solution...";

        for (let i = 0; i < data.steps.length; i++) {
            board = data.steps[i];
            drawBoard();

            moveCount.textContent =
                "Move " + i + " of " + totalMoves;

            if (i < data.steps.length - 1) {
                await sleep(500);
            }
        }

        statusElement.textContent = "Puzzle Solved!";
    } catch (error) {
        statusElement.textContent = "Error: " + error.message;
    } finally {
        setButtonsDisabled(false);
    }
}

// Connect buttons to functions
randomBtn.addEventListener("click", randomizeBoard);
solveBtn.addEventListener("click", solvePuzzle);

// Show the initial solved board
drawBoard();
moveCount.textContent = "Move 0 of 0";
statusElement.textContent = "Ready to play!";
