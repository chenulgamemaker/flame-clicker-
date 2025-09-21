# minimal_flameclicker.py

def main():
    print("🔥 Welcome to FireClicker Game! 🔥")
    flame_points = 0

    while True:
        print(f"\nYou have {flame_points} Flame Points.")
        action = input("Press Enter to generate Flame Points, or type 'q' to quit: ").strip().lower()

        if action == 'q':
            print("Thanks for playing FireClicker! Bye!")
            break
        else:
            flame_points += 1
            print("You clicked and earned 1 Flame Point!")

if __name__ == "__main__":
    main()
