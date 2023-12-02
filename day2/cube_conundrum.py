"""
Checks if game is valid. Returns true if valid, false if not.
"""
def gameCheck(line: str) -> bool:
    # Isolate section of line to check
    line = line.split(":")[1]

    # Split a game into its sets
    gameSets = line.split(";")

    # Within each set, check if rules are violated. If so, return False
    for sets in gameSets:
        redIndex = sets.find("red")
        greenIndex = sets.find("green")
        blueIndex = sets.find("blue")

        if redIndex != -1:
            if sets[redIndex - 2] > 12:
                return False
        if greenIndex != -1:
            if sets[greenIndex - 2] > 13:
                return False
        if blueIndex != -1:
            if sets[blueIndex - 2] > 14:
                return False
    return True

"""
Main function. Loops through each line and returns sum
"""
def main(input: str) -> int:
    gameSum = 0
    textMatrix = input.split('\n')
    for index, line in enumerate(textMatrix):
        if gameCheck(line):
            gameSum += index + 1
    print(gameSum)
    return gameSum

if __name__ == "__main__":
    with open('cube_conundrum_input.txt', 'r') as file:
        data = file.read()
    main(data)



