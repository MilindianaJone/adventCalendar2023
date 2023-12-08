with open('engine_input.txt', 'r') as file:
    data = file.read()
textMatrix = data.split('\n')
matrixWidth = len(textMatrix[0])
matrixHeight = len(textMatrix)

"""
Returns true if special character, false otherwise
"""
def is_special(char: str) -> bool:
    if char.isdigit() or char == ".":
        return False
    return True

"""
Checks if index has adjacent special element
"""
def is_adjacent(lineIndex: int, numberLength: int, lineNumber: int) -> bool:
    # Check left
    if lineIndex != 0:
        if is_special(textMatrix[lineNumber][lineIndex - 1]):
            return True
        # Top left corner
        if lineNumber != 0:
            if is_special(textMatrix[lineNumber - 1][lineIndex - 1]):
                return True
        # Bottom left corner
        if lineNumber < matrixHeight - 1:
            if is_special(textMatrix[lineNumber + 1][lineIndex - 1]):
                return True
    # Check right
    if lineIndex + numberLength < matrixWidth - 1:
        if is_special(textMatrix[lineNumber][lineIndex + numberLength]):
            return True
        # Top right corner
        if lineNumber != 0:
            if is_special(textMatrix[lineNumber - 1][lineIndex + numberLength]):
                return True
        # Bottom right corner
        if lineNumber < matrixHeight - 1:
            if is_special(textMatrix[lineNumber + 1][lineIndex + numberLength]):
                return True

    # Check above
    if lineNumber != 0:
        for index in range(lineIndex, lineIndex + numberLength):
            if is_special(textMatrix[lineNumber - 1][index]):
                return True

    # Check below
    if lineNumber < matrixHeight - 1:
        for index in range(lineIndex, lineIndex + numberLength):
            if is_special(textMatrix[lineNumber + 1][index]):
                return True
            
    return False


"""
Checks each line for the gear sum. 
"""
def gearLine(line: str, lineNumber: int) -> int:
    # Stores the sum of the line
    lineSum = 0
    # Stores length of number found
    numberLength = 0
    # Stores current number found
    number = 0

    for lineIndex in range(len(line)):
        if numberLength > 0:
            numberLength -= 1
            continue

        char = line[lineIndex]
        if char.isdigit():
            numberLength = 1
            # Keep checking for more digits
            for num in line[lineIndex + 1: len(line)]:
                if not num.isdigit():
                    break
                numberLength += 1
            
            number = int(line[lineIndex: lineIndex + numberLength])

            # Check if this number has any adjacent elements
            if is_adjacent(lineIndex, numberLength, lineNumber):
                lineSum += number
                print(lineNumber, number)
            
        else:
            numberLength = 0

    return lineSum



"""
Main function. Loops through each line and returns the gear sum
"""
def main() -> int:
    gearSum = 0
    lineNumber = 0
    for line in textMatrix:
        gearSum += gearLine(line, lineNumber)
        lineNumber += 1
    print(gearSum)
    return gearSum

if __name__ == "__main__":
    main()