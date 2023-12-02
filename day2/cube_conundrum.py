"""
Checks if game is valid. Returns true if valid, false if not.
"""
def gameCheck(line: str) -> bool:
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
    with open('cube_conunundrum_input.txt', 'r') as file:
        data = file.read()
    main(data)



