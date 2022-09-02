def count_batteries_by_usage(cycles):
    low=0 # variable for the low charging unit
    medium=0 # variable for the medium charging unit
    high=0   # variable for the high charging unit
    for i in cycles:
        if i<400:
            low+=1
        elif 400<i<919:
            medium+=1
        elif i>920:
            high+=1
        else:
            print("Enter a valid input")
    return {
    "lowCount":low,
    "mediumCount": medium,
    "highCount": high
           }


def test_bucketing_by_number_of_cycles():
    print("Counting batteries by usage cycles...\n");
    counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
    assert(counts["lowCount"] == 2)
    assert(counts["mediumCount"] == 3)
    assert(counts["highCount"] == 1)
    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_number_of_cycles()
