def day_one():
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
        print(challenge_1_total)

        ## Challenge 2 (WIP)
        ## Claude helped me with this one :facepalm:
        right_counts = {}
        for num in right_side:
            num = int(num)
            right_counts[num] = right_counts.get(num, 0) + 1


        challenge_2_similarity_score = 0
        for num in left_side:
            num = int(num)

            count = right_counts.get(num, 0)

            challenge_2_similarity_score += num * count

        print(challenge_2_similarity_score)


if __name__ == "__main__":
    day_one()