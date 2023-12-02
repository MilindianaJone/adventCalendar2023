"""
Detects the calibration value of a single line
Including if word representation of digit found
"""
def wordLineCalibration(line: str) -> int:
    starting = 0
    startingIndex = 0
    ending = 0
    endingIndex = 0

    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    #Determine starting number
    for char in line:
        if char >= '1' and char <= '9':
            starting = ord(char) - 48
            break
        startingIndex += 1

    for index, number in enumerate(numbers):
        if line.find(number) != -1 and line.find(number) < startingIndex:
            startingIndex = line.find(number)
            starting = index + 1
    
    #Reverse string to determine ending
    line = line[::-1]

    #Reverse numbers array
    for index in range(len(numbers)):
        numbers[index] = numbers[index][::-1]

    #Determine ending number
    for char in line:
        if char >= '1' and char <= '9':
            ending = ord(char) - 48
            break
        endingIndex += 1
    
    for index, number in enumerate(numbers):
        if line.find(number) != -1 and line.find(number) < endingIndex:
            endingIndex = line.find(number)
            ending = index + 1
    
    return starting*10 + ending

"""
Detects the calibration value of a single line
"""
def lineCalibration(line: str) -> int:
    starting = 0
    ending = 0
    startingFound = False
    for char in line:
        if char >= '1' and char <= '9':
            if not startingFound:
                starting = ord(char) - 48
                startingFound = True
            ending = ord(char) - 48
    calibration = starting*10 + ending
    return calibration

"""
Main function. Loops through each line and returns sum
"""
def main(input: str) -> int:
    calibrationSum = 0
    textMatrix = input.split('\n')
    for line in textMatrix:
        calibrationSum += wordLineCalibration(line)
    return calibrationSum

if __name__ == "__main__":
    with open('trebuchet.txt', 'r') as file:
        data = file.read()
    main(data)