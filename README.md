# 🧩 Tic Tac Toe Game 🥀

## 📌 Overview
A Python-based Tic Tac Toe game featuring single-player AI and multiplayer mode, built with a modular structure and clean game logic.

---

## 🎮 Features
- 👤 Player vs Player mode  
- 🤖 Player vs AI mode  
- 🧠 Basic AI decision system  
- 🧾 Win / draw detection  
- 🔄 Game reset after each round  
- 🎨 Turtle-based UI (if enabled)

---

## 🤖 AI Logic
The AI follows a simple priority system:

- Check if it can win → play winning move  
- Block opponent if they are about to win  
- Take center or corners for strategy  
- Otherwise pick a random valid move  

This makes the AI balanced and playable 🥀

---

## 🏗️ Project Structure

- `Tic_Tac_Toe.py` → Main game loop  
- `menu.py` → Menu and mode selection  
- `xo.py` → Core game logic (X and O handling)  
- `display.py` → Board rendering and UI  
- `write.py` → Text/messages system  
- `config.py` → Global settings (optional)

---

## ▶️ How to Run
```bash
python Tic_Tac_Toe.py
