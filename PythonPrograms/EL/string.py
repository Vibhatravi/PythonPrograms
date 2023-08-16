while True:
    print("----MENU----\n1.Strip\n2.Split\n3.replace\n4.find\n5.join\n7.exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        string = input("Enter the String with Whitespaces: ")
        print(f"strip(): {string.strip()}")
    elif ch == 2:
        string = input("Enter the string to split: ")
        split_string = string.split(",")
        print(f"split(): {split_string}")
    elif ch == 3:

        string = input("Enter the string: ")
        new_string = string.replace(",", "-")
        print(f"replace(): {new_string}")
    elif ch == 4:
        string = input("Enter the string: ")
        index = string.find("World")
        print(f"find(): {index}")
    elif ch == 5:
        words = input("Enter the list of words to be joined: ")
        joined_string = "-".join(words)
        print(f"join(): {joined_string}")
    elif ch == 6 :
        string = input("Enter the string: ")
        is_all_digits = string.isdigit()
        print(f"isdigit(): {is_all_digits}")
    elif ch == 7 :
        break
    else:
        exit()