from pathlib import Path

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
        calibrationSum += lineCalibration(line)
    return calibrationSum

if __name__ == "__main__":
    with open('trebuchet.txt', 'r') as file:
        data = file.read()
    #txt = Path('trebuchet.txt').read_text()
    main(data)