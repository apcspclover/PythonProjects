
def character_Quiz():
    print("𝘞𝘩𝘪𝘤𝘩 𝘤𝘩𝘢𝘳𝘢𝘤𝘵𝘦𝘳 𝘢𝘳𝘦 𝘺𝘰𝘶 ♡₊?")
    print("Answer the questions to figure out what character you are")
    ans = input("Are you an introvert or extrovert?")
    if ans == "introvert":
            ans = input("Are you silent or quiet?")
            if ans == "silent":
                ans = input("Are you a homebody or a wanderer?")
                if ans == "homebody":
                    print("You are smiski˙⋆✮")
                    if ans == "wanderer":
                        print("You are Moomin ☾໋")
                    else:
                        print("Please answer the question correctly")
            if ans == "quiet":
                ans = input("Are you genuine or kind?")
                if ans == "genuine":
                    print("You are Totoro˖⋆࿐")
            else:
                print("Please answer the question correctly")
    if ans == "extrovert":
            ans = input("Are you salty or sweet?")
            if ans == "sweet":
                ans = input("Would you rather have a bow or a star?")
                if ans == "star":
                    print("You are Kirby")
                    if ans == "bow":
                        print("You are Hello Kitty 𝜗𝜚 ࣪˖ ִ𐙚")
            if ans == "salty":
                ans = input("Are you fiery or chill?")
                if ans == "fiery":
                    print("You are Calcifer")
                    if ans == "chill":
                        print("You are Snoopy .*-")
                else:
                    print("Please answer the question correctly")
            else:
                print("Please answer the question correctly")
    else:
        print("Please answer the question correctly")
character_Quiz()

