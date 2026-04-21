def mergeAlternately(word1: str, word2: str) -> str:
    i, j = 0, 0
    result = []

    # Alternate characters
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    # Add remaining characters
    result.append(word1[i:])
    result.append(word2[j:])

    return "".join(result)