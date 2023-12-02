"""
Outputs the power for a single game
"""
def powerGame(line: str) -> int:
    # Isolate section of line to check
    line = line.split(":")[1]

    # Split a game into its sets
    gameSets = line.split(";")

    # Determine the minimum number of cubes for each colour
    redMin = 0
    greenMin = 0
    blueMin = 0

    tempRed = 0
    tempGreen = 0
    tempBlue = 0

    # Within each set, check if rules are violated. If so, return False
    for sets in gameSets:
        redIndex = sets.find("red")
        greenIndex = sets.find("green")
        blueIndex = sets.find("blue")

        if redIndex != -1:
            if sets[redIndex - 3].isdigit():
                tempRed = int(sets[redIndex - 3: redIndex - 1])
            else:
                tempRed = int(sets[redIndex - 2])
        if greenIndex != -1:
            if sets[greenIndex - 3].isdigit():
                tempGreen = int(sets[greenIndex - 3: greenIndex - 1])
            else:
                tempGreen = int(sets[greenIndex - 2])
        if blueIndex != -1:
            if sets[blueIndex - 3].isdigit():
                tempBlue = int(sets[blueIndex - 3: blueIndex - 1])
            else:
                tempBlue = int(sets[blueIndex - 2])    
        if tempRed > redMin:
            redMin = tempRed
        if tempGreen > greenMin:
            greenMin = tempGreen
        if tempBlue > blueMin:
            blueMin = tempBlue

    return redMin * greenMin * blueMin

"""
Main function. Loops through each line and returns sum
"""
def main(input: str) -> int:
    powerSum = 0
    textMatrix = input.split('\n')
    for line in textMatrix:
        powerSum += powerGame(line)
    print(powerSum)
    return powerSum

if __name__ == "__main__":
    with open('cube_conundrum_input.txt', 'r') as file:
        data = file.read()
    main(data)



