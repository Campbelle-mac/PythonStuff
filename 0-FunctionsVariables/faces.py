def face(ans):
    ans1 = ans
    ans1 = ans1.replace(":)", "🙂")
    ans1 = ans1.replace(":(", "☹️")
    return ans1


def main():
    ans = input("")
    result = face(ans)
    print(result)


main()
