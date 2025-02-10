def find_anagrams(word: str, candidates: list[str]):

    result = []
    word_list = list(word.lower())
    word_list.sort()
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
        candidate_list = list(candidate.lower())
        candidate_list.sort()
        if candidate_list == word_list:
            result.append(candidate)

    return result
