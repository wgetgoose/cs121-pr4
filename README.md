# README

# 🔦 Cave of Despair

> A TUI-based exploration game where you, the player, have mysteriously fallen into the “Cave of Despair”. Explore the catacombs, discovering new items, fighting bosses, and divulging in the lore within the walls.
> 

## ⭐ Important Information

All the changes made to the original starter code can be tracked at the Github repo located here: [https://github.com/wgetgoose/cs121-pr4](https://github.com/wgetgoose/cs121-pr4). All code is located under the `src` dir. Additionally, a graphical representation of the game map can be found and opened using LibreOffice Draw. Also note that I worked on this project solo. Lots of additional modules and changes have been introduced, and you can compare the codebases directly by accessing the `starter-code` dir.

## ➕ Added Features

1. Animated printing to terminal
2. “Note” items, which can be read
3. “Weapon” items, which are used in combat sequences
4. “Potion” items, which can heal the player
5. 10% Critical Hit chance during combat sequences
6. Pickup and Drop items from inventory
7. Custom user name
8. Revised situation display
9. Inventory max size of 5
10. Use of text files for storing long strings that are displayed to user
11. User input character is ASCII formatted, so it “blinks”
12. Ability to save game, including
    1. Multiple save files
    2. Ability for user to select save file on load
    3. Using a save file skips the intro sequence
13. An expanded (not randomly generated) map
14. “Use” command, allowing players 

## 🚧 Planned Improvements

- [ ]  Dialogue sequence during combat sequences
- [ ]  Allow player to try and “run” from fight (with random success chance)

## 🔴 Current Oversights/Bugs

- [ ]  Reduce case sensitivity by implementing `lower()` on various
- [ ]  Do not allow player to load save after dying
- [ ]  No code comments