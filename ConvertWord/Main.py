import ConsonantUtils
import SpecialEnd


def main():
    while True:
        word = raw_input("Enter 1 word: ")
        word = word.lower()
        consonant = ConsonantUtils.get_consonant(word)
        part_one_vi = consonant["vi"]
        part_one_jp = consonant["jp"]
        if len(word) > 1:
            part_two_vi = word[len(part_one_vi)]
        else:
            part_two_vi = ""
        part_end = SpecialEnd.get_special_end(word)
        if part_end != False:
            part_end_vi = part_end["vi"]
            part_end_jp = part_end["jp"]
            part_three = word[len(part_one_vi) + len(part_two_vi): len(word) - len(part_end_vi)]
        else:
            part_three = word[len(part_one_vi) + len(part_two_vi): len(word)]
            part_end_jp = ""
        print(part_one_jp + part_two_vi + part_three + part_end_jp)


if __name__ == "__main__":
    main()
