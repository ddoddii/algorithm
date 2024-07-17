from collections import Counter


def main(word):
    word = word.lower()
    counts = Counter(word)
    sorted_counts = counts.most_common()
    if len(sorted_counts) > 1 and sorted_counts[0][1] == sorted_counts[1][1]:
        return "?"
    return sorted_counts[0][0].upper()


print(main("z"))
