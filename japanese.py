__all__ = ["randjap"]

from random import sample, randint, getrandbits, choices

randbool = lambda: getrandbits(1)


def chance(a: int) -> bool:
    """One in `a` chance."""
    return not randint(0, a)


# all info taken from NipponGo: Introduction
romaji = {
    "consonants": "kstnhmyrwgzdbp",
    "vowels": "aiueo",
    "illegal": {
        # normal
        "si": "shi",
        "ti": "chi",
        "tu": "tsu",
        "hu": "fu",
        # illegal glides
        "yi": "yu",
        "ye": "yo",
        # voiced
        "zi": "ji",
        "di": "ji",
        "du": "zu",
        # illegal w
        "wo": "o",
        "wu": "tsu",
        "we": "de",
        "wi": "chi",
    },
    "doubled": "ptsk",
    "nasal": "n",
}


def correct(syllable, first=False, alphabet=romaji):
    illegal = alphabet["illegal"]
    doubled = alphabet["doubled"]

    if syllable in illegal.keys():
        return illegal[syllable]

    if not first and syllable[0] in doubled and chance(4):
        # one in four chance to double the consonant
        syllable = syllable[0] + syllable

    if chance(6):
        # one in six chance to add a nasal syllable
        syllable += alphabet["nasal"]

    return syllable


def randjap(
    alphabet=romaji,
    min_vowels=3,
    max_vowels=5,
    max_consonants=7,
):
    """
    Generate a random (possibly non-existent) Japanese-sounding word.
    """

    result = ""

    vowels = choices(alphabet["vowels"], k=randint(min_vowels, max_vowels))
    consonants = sample(
        alphabet["consonants"], k=randint(len(vowels), max_consonants)
    )

    first = True
    if chance(3):
        first = False
        result += vowels.pop()

    for con in consonants:
        if not vowels:
            if con == alphabet["nasal"]:
                result += con
            break

        result += correct(con + vowels.pop(), first)
        first = False
    return result


if __name__ == "__main__":
    try:
        for _ in range(int(input("How many? "))):
            print(randjap(), end=", ")
        print("")
    except Exception as exc:
        print(f"[ERROR] {exc}")
        print("")
