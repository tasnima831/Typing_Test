Typing Test Game (Tkinter)
A fun and interactive Typing Speed Test application built using Python and the Tkinter GUI library. Users can test and improve their typing speed by typing words displayed on the screen within a selected time frame. The game includes multiple difficulty levels, a score tracker, and a high score feature.

🖥️ Features
🧑‍💻 Username entry for personalization.
⏱️ Selectable timer (15s, 30s, 45s, 60s).
🔀 Random words based on difficulty:
Easy
Medium
Hard
🎨 Colorful random word display.
🧠 Score tracking: hits, misses, total score.
🏆 High score saved to file.
🔄 Retry option after game ends.
👁️‍🗨️ Moving banner text animation.
🗂️ Project Structure
project/
│
├── main.py           # Main application file
├── word.py           # Contains the word lists
├── highscore.txt     # Stores high score (auto-generated)
└── README.md         # Project documentation
📄 word.py Example
Create a word.py file with the following content:

# word.py

easy_words = ['cat', 'dog', 'apple', 'fish', 'sun', 'book']
medium_words = ['python', 'window', 'laptop', 'flower', 'object']
hard_words = ['framework', 'algorithm', 'multithreaded', 'inheritance']
▶️ How to Run
Make sure Python 3.x is installed.
Download or clone the project.
Ensure main.py and word.py are in the same folder.
Run the app using:
python main.py
💾 High Score
Saved in highscore.txt.
Auto-created if not present.
📌 Requirements
No external libraries needed. Uses only:

tkinter
random
These come preinstalled with Python.

📜 License
Free to use for learning and personal projects.

🙌 Credits
Developed as a simple Python GUI project to boost typing speed through an engaging interface.
