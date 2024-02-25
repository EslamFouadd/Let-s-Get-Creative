def mad_libs():
    # Mad Libs template
    story = "Once upon a time, there was a [adjective] [noun] who loved to [verb]."

    # Prompt the user for input
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    # Fill in the blanks with user input
    completed_story = story.replace("[adjective]", adjective)\
                            .replace("[noun]", noun)\
                            .replace("[verb]", verb)

    # Display the completed Mad Lib
    print("\nYour Mad Lib:\n" + completed_story)

# Run the Mad Libs Generator
mad_libs()
