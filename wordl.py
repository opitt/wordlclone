from rich.console import Console
from rich.theme import Theme

def validate_guess(guess, word):
    return "".join(
        "1" if g == w else "?" if g in word else "0" for g, w in zip(guess, word)
    )

def load_words(fromfile=True):
    from re import fullmatch
    from pathlib import Path
    return [word.upper() for word in Path("wordlist.txt").read_text(encoding="utf8").rstrip().split("\n") 
            if None != fullmatch("[a-zA-Z]{5}", word)]

def get_random_word(wordlist):
    from random import choice
    return choice(wordlist)

def valid_to_emoji(valid):
    #python -m rich.emoji | grep square
    return "".join(":white_large_square:" if c =="0" else ":yellow_square:" if c == "?" else ":green_square:" for c in valid)

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]{headline}[/]\n")

def game_over(guesses, word):
    refresh_page("Game Over")
    show_guesses(guesses, word)
    console.print(f"The correct word was", justify="center")
    console.print(f"[bold green]{word}[/]", justify="center")
    if word in guesses:
        msg = "You won."
        style = "bold green"
    else:
        msg = "You loose."
        style = "bold red"
    console.print(f"[{style}]{msg}[/]\n", justify="center")

def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        valid = validate_guess(guess, word)
        for letter,validator in zip(guess,valid):
            if letter == "_":
                style = "dim"
            elif validator == "1":
                style = "bold white on green"
            elif validator == "?":
                style = "bold white on yellow"
            else:
                style = "white on #666666"
            styled_guess.append(f"[{style}]{letter}[/]")
    
        console.print("".join(styled_guess),justify="center")

def game():
    WORDS = load_words()
    WORD = get_random_word(WORDS)
    ROUNDS = 2
    guesses = ["_"*5] * ROUNDS

    refresh_page(":wave:Welcome to [bold red]Wordl Clone[/red bold] :copyright:opitt")
    show_guesses(guesses,WORD)
    for round in range(1, ROUNDS+1):
        guess = console.input(f"Guess the word: ").upper()
        guesses[round-1]= guess
        if WORD==guess:
            break
        refresh_page(f"Guess {round+1} of {ROUNDS}")
        show_guesses(guesses,WORD)
    
    game_over(guesses, WORD)

if __name__ == "__main__":
    console = Console(width=40, theme=Theme({"warning":"red on yellow"}))
    game()
