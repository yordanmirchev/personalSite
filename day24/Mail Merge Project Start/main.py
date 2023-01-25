#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_names():
    with open("Input/Names/invited_names.txt") as file:
        names = []
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n','')
            line.strip()
            names.append(line)

        return names

def prepare_letter(name):
    with open("Input/Letters/starting_letter.txt") as file:
        return file.read().replace(PLACEHOLDER, name)

def save_letter(name):
    with open(f"Output/ReadyToSend/letter_to_{name}", mode="w") as file:
        file.write(prepare_letter(name))


names = read_names()

for name in names:
    save_letter(name)