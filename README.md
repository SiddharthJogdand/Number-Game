# 🎯 Number Guessing Game

Welcome to the **Number Guessing Game**, a fun and interactive console game where you try to guess a randomly generated number between 1 and 100! Play across three difficulty levels, request hints (at a score cost!), and track your high scores locally.

---

## 🕹️ How to Play

1. Choose a difficulty level:
   - **Easy**: 15 attempts, 3 hints  
   - **Medium**: 10 attempts, 2 hints  
   - **Hard**: 5 attempts, 1 hint

2. The game generates a secret number between 1 and 100.

3. You try to guess the number:
   - Type `'hint'` to get a clue (only after one guess).
   - Type `'quit'` to exit the game.

4. Your final score is calculated based on:
   - Remaining attempts (70%)
   - Hints used (30%)

5. High scores are saved in a local `high_scores.json` file for each difficulty level.

---

## 📦 Features

- 🎮 3 difficulty levels  
- 💡 Smart hints (odd/even, comparative feedback, and proximity)  
- 🧠 Score system based on performance  
- 🏆 Local high score tracking  
- 🔁 Option to replay anytime  

---

## 🧰 Requirements

- Python 3.x  
- No external dependencies

---

## 🚀 How to Run

Clone the repository and run the Python script:

```bash
git clone https://github.com/SiddharthJogdand/Number-Game.git
cd Number-Game
python number_game.py
```

---

## 📁 Files

| File              | Description                               |
|-------------------|-------------------------------------------|
| `number_game.py`  | Main game logic                           |
| `high_scores.json`| Stores high scores for each difficulty    |

---

## 📌 Example

```bash
Welcome to the Number Guessing Game!

Choose difficulty:
1. Easy (15 attempts, 3 hints)
2. Medium (10 attempts, 2 hints)
3. Hard (5 attempts, 1 hint)
Enter choice (1-3): 2

I'm thinking of a number between 1 and 100.
You have 10 attempts to guess it.
Type 'hint' for help or 'quit' to exit.
```

---

## 🤝 Contributing

Pull requests are welcome. If you'd like to suggest improvements or report bugs, feel free to open an issue!

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
