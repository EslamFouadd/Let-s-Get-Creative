def trick_or_treating_mad_libs():
    # Mad Libs template
    story = """
    It was Halloween night, and I was ready for some [adjective] trick-or-treating.
    I put on my [costume] and grabbed my [noun], then headed out into the [adjective] night.
    As I walked down the street, I saw [number] [plural_noun] jumping out from behind bushes and scaring people.
    I decided to avoid them and went to the [place] instead.
    At the [place], I got lots of [adjective] candy and even saw a [noun] that was giving out [adjective] treats.
    After filling up my [container] with goodies, I headed back home feeling [emotion].
    It was definitely a [adjective] Halloween!
    """

    # Prompt the user for input
    adjective = input("Enter an adjective: ")
    costume = input("Enter a Halloween costume: ")
    noun = input("Enter a noun (e.g., pumpkin, flashlight): ")
    number = input("Enter a number: ")
    plural_noun = input("Enter a plural noun: ")
    place = input("Enter a place (e.g., haunted house, pumpkin patch): ")
    container = input("Enter a container (e.g., bucket, pillowcase): ")
    emotion = input("Enter an emotion (e.g., excited, scared): ")

    # Fill in the blanks with user input
    completed_story = story.replace("[adjective]", adjective)\
                            .replace("[costume]", costume)\
                            .replace("[noun]", noun)\
                            .replace("[number]", number)\
                            .replace("[plural_noun]", plural_noun)\
                            .replace("[place]", place)\
                            .replace("[container]", container)\
                            .replace("[emotion]", emotion)

    # Display the completed Mad Lib
    print("\nYour Trick-or-Treating Mad Lib:\n" + completed_story)

# Run the Trick-or-Treating Mad Libs Generator
trick_or_treating_mad_libs()
