PLACEHOLDER = "[Names]"

with open(".//Input/Names/invited_names.txt", mode='r') as names:
    all_Names = names.readlines() # convert text into list

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt",mode='r')as letter:
    letter_contant = letter.read()
    for name in all_Names:
        stripedName = name.strip() # Remove unnecessary spaces
        newLetter = letter_contant.replace(PLACEHOLDER, stripedName) #Replace the word in file with new Word
        with open(f"./Output/ReadyToSend/letter_For_{stripedName}.txt",mode='w') as newLet:
            newLet.write(newLetter)

