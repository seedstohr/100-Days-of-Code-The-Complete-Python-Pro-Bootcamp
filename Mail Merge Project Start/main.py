invitees = []

with open("./Input/Names/invited_names.txt", "r") as invitee_file:
    for line in invitee_file:
        invitees.append(line.strip())

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    temp_letter = letter_file.read()

for invitee in range(len(invitees)):
    temp_letter = temp_letter
    custom_letter = temp_letter.replace('[name]', invitees[invitee])
    with open(f"./Output/ReadyToSend/letter_for_{invitees[invitee]}.txt", "w") as letter_file:
        letter_file.write(custom_letter)
        