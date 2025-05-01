from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
            isinstance(s, str) for s in strings
        ):
            raise TypeError("Input must be a list of strings")
        if not strings:
            return ""

        for word in strings:
            self.put(word)

        current = self.root
        prefix = []
        while True:
            if len(current.children) != 1 or current.value is not None:
                break
            char, next_node = next(iter(current.children.items()))
            prefix.append(char)
            current = next_node
        return "".join(prefix)


if __name__ == "__main__":
    trie = LongestCommonWord()
    sw1 = ["starfighter", "starship", "stardestroyer"]
    assert trie.find_longest_common_word(sw1) == "star"

    trie = LongestCommonWord()
    sw2 = ["jedi", "jedha", "jedibot"]
    assert trie.find_longest_common_word(sw2) == "jed"

    trie = LongestCommonWord()
    sw3 = ["darthvader", "darthmaul", "darthsidious"]
    assert trie.find_longest_common_word(sw3) == "darth"

    trie = LongestCommonWord()
    sw4 = ["luke", "leia", "lando"]
    assert trie.find_longest_common_word(sw4) == "l"

    trie = LongestCommonWord()
    sw5 = ["tatooine", "naboo", "mustafar"]
    assert trie.find_longest_common_word(sw5) == ""

    trie = LongestCommonWord()
    sw6 = list[str]
    assert trie.find_longest_common_word(sw6) == ""

    print("✅ All tests passed!")
