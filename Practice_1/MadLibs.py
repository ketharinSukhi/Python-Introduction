print("WELCOME TO MAD LIBS GAME !!")
def mad_lids():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    story = f"One day, a {adjective} {noun} decided to {verb} at the {place}. It was the best day ever!"
    print("Here is mad lids story : " ,story)
def main():
    mad_lids()

if __name__ == "__main__":
    main()