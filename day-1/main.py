def part_one():
    ## Challenge 1
    with (open(file="numbers.txt", mode="r", encoding="utf-8") as numbers):
        list_of_numbers = numbers.read().split()
        right_side = list_of_numbers[1::2]
        left_side = list_of_numbers[0::2]
        sorted_right_side = sorted(right_side)
        sorted_left_side = sorted(left_side)
        assert len(sorted_right_side) == len(sorted_left_side)
        list_of_diffs = []
        for index, _ in enumerate(sorted_left_side):
            right_number = int(sorted_right_side[index])
            left_number = int(sorted_left_side[index])
            if left_number < right_number:
                difference = right_number - left_number
            else:
                difference =left_number - right_number
            list_of_diffs.append(difference)
            #print(list_of_diffs)

        assert len(list_of_diffs) == len(list_of_numbers) / 2
        challenge_1_total = sum(list_of_diffs)
        #print(challenge_1_total)

        ### Challenge 2 (WIP)
        total = []
        occurences = []
        keys = {}
        for left_number in left_side:
            for right_number in right_side:
                if left_number == right_number:
                    keys[left_number] = occurences.append(right_number)}

                relative = left_number * int(len(occurences))
        print(occurences)
                #print(relative)
                #total.append(relative)

        #print(sum(total))
                #similarity_score =left_number * occurences
                #print(occurences)
                #print(similarity_score)
                #if left_number == right_number:





if __name__ == "__main__":
    part_one()