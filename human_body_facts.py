import random

facts = {
    "Brain": [
        "The brain controls thoughts, memory and movement.",
        "The human brain contains billions of neurons.",
        "The brain helps us process information."
    ],
    "Heart": [
        "The heart is a muscular organ.",
        "The heart pumps blood throughout the body.",
        "The human heart has four chambers."
    ],
    "Lungs": [
        "Humans normally have two lungs.",
        "The lungs help exchange oxygen and carbon dioxide.",
        "The diaphragm helps us breathe."
    ],
    "Bones": [
        "An adult human skeleton usually has 206 bones.",
        "Bones support and protect the body.",
        "Bone marrow produces blood cells."
    ],
    "Blood": [
        "Blood transports oxygen and nutrients.",
        "Red blood cells carry oxygen.",
        "White blood cells help fight infections."
    ],
    "Cells": [
        "Cells are the basic structural units of life.",
        "The nucleus contains most of a cell's DNA.",
        "Mitochondria produce much of the cell's usable energy."
    ]
}

print("=" * 40)
print("       WELCOME TO BIOVERSE")
print("  Explore the Amazing Human Body!")
print("=" * 40)

while True:
    print("\nChoose a topic:")

    for topic in facts:
        print("-", topic)

    print("- Random")
    print("- Exit")

    choice = input("\nEnter your choice: ").strip().title()

    if choice == "Exit":
        print("Thank you for exploring BioVerse!")
        break

    elif choice == "Random":
        topic = random.choice(list(facts.keys()))
        print("\n", topic, "Fact:")
        print(random.choice(facts[topic]))

    elif choice in facts:
        print("\n", choice, "Facts:")
        for fact in facts[choice]:
            print("•", fact)

    else:
        print("Invalid choice. Please try again.")
