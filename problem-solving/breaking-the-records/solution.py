def breaking_the_records(scores):
    highest = 0
    record_highs = 0
    lowest = 0
    record_lows = 0

    for i in range(0, len(scores)):
        score = scores[i]

        if i == 0:
            highest = score
            lowest = score
        elif score > highest:
            highest = score
            record_highs += 1
        elif score < lowest:
            lowest = score
            record_lows += 1

    return [record_highs, record_lows]
