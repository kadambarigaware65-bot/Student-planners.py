# Student-planners.py

# A collection of daily study planning ideas

import os
import random

SUBJECTS = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Computer Science",
    "English"
]

STUDY_TASKS = [
    "Revise your class notes.",
    "Solve five practice questions.",
    "Learn a new topic today.",
    "Complete your pending assignments.",
    "Review important formulas.",
    "Practice coding for 20 minutes."
]


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def show_subject():
    """Displays a randomly selected subject."""
    print("\nToday's Study Subject:")
    print(random.choice(SUBJECTS))


def show_task():
    """Suggests a small study task for today."""
    print("\nYour Study Task:")
    print(random.choice(STUDY_TASKS))


def main():
    """Runs the Study Planner application."""
    clear_screen()
    print("Welcome to Study Planner!")
    print("=" * 40)

    show_subject()
    show_task()

    print("\nStay focused and achieve your goals!")
    print("=" * 40)

    try:
        input("\nPress Enter to finish...")
    except (KeyboardInterrupt, EOFError):
        print("\nStudy session ended.")

    print("\nThank you for using Study Planner!")


if __name__ == "__main__":
    main()
