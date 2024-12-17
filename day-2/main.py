def challenge_one():
    with open(file="reports.txt", mode="r", encoding="utf-8") as numbers:
        list_of_numbers = numbers.readlines()
        reports = [report.strip("\n").split() for report in list_of_numbers]
        safe_reports = []

        for report in reports:
            report = [int(num) for num in report]


            is_increasing = all(report[i + 1] > report[i] for i in range(len(report) - 1))
            is_decreasing = all(report[i + 1] < report[i] for i in range(len(report) - 1))

            consistent_diff = all(
                1 <= abs(report[i + 1] - report[i]) <= 3
                for i in range(len(report) - 1)
            )

            if (is_increasing or is_decreasing) and consistent_diff:
                safe_reports.append(report)

        return len(safe_reports)

print(challenge_one())


def challenge_two():
    pass
