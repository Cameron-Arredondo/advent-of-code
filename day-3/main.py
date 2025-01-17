import re

def challenge_one() -> int:
    with open(file="day-3/memory.txt", mode="r", encoding="utf-8") as numbers:
        puzzle = numbers.read()

        multiply = re.findall(pattern=r"mul\((\d+),(\d+)\)",string=puzzle)

        list_of_sums = [int(sets[0]) * int(sets[1]) for sets in multiply]

        return sum(list_of_sums)

def challenge_two():
    pass


if __name__ == "__main__":
    print(challenge_one())