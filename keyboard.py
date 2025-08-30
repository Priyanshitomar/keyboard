import random
from collections import defaultdict
import tkinter as tk

class NGramPredictor:
    def __init__(self, n=2):
        self.n = n
        self.ngrams = defaultdict(list)

    def train(self, corpus):
        tokens = corpus.split()
        for i in range(len(tokens) - self.n):
            key = tuple(tokens[i:i + self.n - 1])
            next_word = tokens[i + self.n - 1]
            self.ngrams[key].append(next_word)

    def predict(self, context):
        key = tuple(context.split()[-(self.n - 1):])
        possible_words = self.ngrams.get(key, [])
        if possible_words:
            return random.choice(possible_words)
        else:
            return "..."

#GUI Keyboard 

def build_keyboard_ui():
    # Train model
    corpus = """I love reading books. I love watching movies. I enjoy reading fiction and non-fiction. I like watching romantic comedies."""
    predictor = NGramPredictor(n=2)
    predictor.train(corpus)

    # Create GUI
    root = tk.Tk()
    root.title("Autocorrect Keyboard")
    root.geometry("600x200")

    # Widgets
    input_label = tk.Label(root, text="Type here:", font=("Arial", 14))
    input_label.pack()

    entry = tk.Entry(root, width=70, font=("Arial", 14))
    entry.pack(pady=10)

    prediction_label = tk.Label(root, text="Prediction: ", font=("Arial", 14), fg="blue")
    prediction_label.pack(pady=5)

    def on_key_release(event):
        text = entry.get().strip()
        if text:
            next_word = predictor.predict(text)
            prediction_label.config(text=f"Prediction: {next_word}")
        else:
            prediction_label.config(text="Prediction: ")

    entry.bind("<KeyRelease>", on_key_release)

    root.mainloop()


build_keyboard_ui()
