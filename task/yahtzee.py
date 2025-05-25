import random


#def is to create function
def roll_dice(keep=[]):
    # Roll dice (5 total - keep any the player wants)
    return keep + [random.randint(1, 6) for _ in range(5 - len(keep))]

def show_dice(dice):
    print("Your dice:", dice)

def choose_keep(dice):
    # Ask which dice to keep (positions: 1 to 5)
    keep = []
    keep_input = input("Enter dice positions to keep (e.g. 1 3 5), or press Enter to keep none: ")
    if keep_input.strip() == "":
        return []
    positions = keep_input.split()
    for pos in positions:
        if pos.isdigit():
            index = int(pos) - 1
            if 0 <= index < len(dice):
                keep.append(dice[index])
    return keep

def get_score_options(dice):
    # Calculate simple scores
    scores = {}
    for i in range(1, 7):
        scores[f"{i}s"] = dice.count(i) * i
    scores["Chance"] = sum(dice)
    return scores

def choose_score(scores, used):
    # Let the player pick a category
    print("\nAvailable categories:")
    for name, value in scores.items():
        if name not in used:
            print(f"- {name}: {value}")
    while True:
        choice = input("Pick a category: ")
        if choice in scores and choice not in used:
            return choice
        print("Invalid or already used. Try again.")

def play_yahtzee():
    used_categories = []
    total_score = 0

    print("🎲 Welcome to Simple Yahtzee!")
    for round in range(3):  # You can change to 13 for full game
        print(f"\n--- Round {round + 1} ---")
        dice = roll_dice()
        show_dice(dice)

        # Up to 2 re-rolls
        for _ in range(2):
            keep = choose_keep(dice)
            dice = roll_dice(keep)
            show_dice(dice)

        options = get_score_options(dice)
        chosen = choose_score(options, used_categories)
        round_score = options[chosen]
        total_score += round_score
        used_categories.append(chosen)
        print(f"✅ You scored {round_score} in {chosen}")

    print("\n🎉 Game Over!")
    print(f"🏆 Your total score: {total_score}")

# Start game
play_yahtzee()
