import copy

index = [
    "1m",
    "2m",
    "3m",
    "4m",
    "5m",
    "6m",
    "7m",
    "8m",
    "9m",
    "1p",
    "2p",
    "3p",
    "4p",
    "5p",
    "6p",
    "7p",
    "8p",
    "9p",
    "1s",
    "2s",
    "3s",
    "4s",
    "5s",
    "6s",
    "7s",
    "8s",
    "9s",
    "1z",
    "2z",
    "3z",
    "4z",
    "5z",
    "6z",
    "7z",
]


def menziJudge(num, pai):
    if num == 0:
        return True
    pai_copy = copy.deepcopy(pai)
    for i in range(27):
        if pai_copy[i] >= 3:
            pai_copy[i] -= 3
            if menziJudge(num - 1, pai_copy):
                return True
            pai_copy[i] += 3
        if (
            i % 9 < 7
            and pai_copy[i] > 0
            and pai_copy[i + 1] > 0
            and pai_copy[i + 2] > 0
        ):
            pai_copy[i] -= 1
            pai_copy[i + 1] -= 1
            pai_copy[i + 2] -= 1
            if menziJudge(num - 1, pai_copy):
                return True
            pai_copy[i] += 1
            pai_copy[i + 1] += 1
            pai_copy[i + 2] += 1
    return False


def menziJudgeWithZ(pai):
    pai_copy = copy.deepcopy(pai)
    num = 4
    for i in range(27, 34):
        if pai_copy[i] == 0:
            continue
        elif pai_copy[i] == 3:
            num -= 1
        else:
            return False
    return menziJudge(num, pai_copy)


def hupaiJudge(pai):
    pai_copy = copy.deepcopy(pai)

    # qiduizi
    duizicnt = 0
    for x in pai_copy:
        if x == 0:
            continue
        elif x == 2:
            duizicnt += 1
        else:
            duizicnt = 0
            break
    if duizicnt == 7:
        return True

    # guoshi
    if (
        pai_copy[0] > 0
        and pai_copy[8] > 0
        and pai_copy[9] > 0
        and pai_copy[17] > 0
        and pai_copy[18] > 0
        and pai_copy[26] > 0
        and pai_copy[27] > 0
        and pai_copy[28] > 0
        and pai_copy[29] > 0
        and pai_copy[30] > 0
        and pai_copy[31] > 0
        and pai_copy[32] > 0
        and pai_copy[33] > 0
    ):
        return True

    # normal
    for i in range(34):
        if pai_copy[i] >= 2:
            pai_copy[i] -= 2
            if menziJudgeWithZ(pai_copy):
                return True
            pai_copy[i] += 2

    # noHU
    return False


def tingpaiJudge(pai):
    pai_copy = copy.deepcopy(pai)

    noting = True
    for i in range(34):
        if pai_copy[i] < 4:
            pai_copy[i] += 1
            if hupaiJudge(pai_copy):
                noting = False
                print(index[i])
            pai_copy[i] -= 1
    if noting:
        print("noting")


def parse_mahjong_input(input_str):
    pai = [0] * 34
    type_start = {
        "m": 0,
        "p": 9,
        "s": 18,
        "z": 27,
    }

    current_digits = ""
    for char in input_str:
        if char.isdigit():
            # char is digit, collect
            current_digits += char
        elif char in type_start:
            # is m/p/s/z, start to process current_digits
            if not current_digits:
                raise ValueError(f"No number in front of {char} !")

            start_idx = type_start[char]
            for digit in current_digits:
                num = int(digit)
                if char == "z" and (num < 1 or num > 7):
                    raise ValueError(f"Invalid {num}z!")
                if char != "z" and (num < 1 or num > 9):
                    raise ValueError(f"Invalid {num}{char}!")

                pai[start_idx + (num - 1)] += 1

            # process finish, go to the next type
            current_digits = ""
        else:
            raise ValueError(f"Invalid {char}!")

    if current_digits:
        raise ValueError(f"Missing m/p/s/z")

    return pai


def main():
    input_str = input("Input mahjong pai string:")
    pai = parse_mahjong_input(input_str)
    tingpaiJudge(pai)


if __name__ == "__main__":
    main()
