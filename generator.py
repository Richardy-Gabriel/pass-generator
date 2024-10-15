import random
import string

class PasswGenerator:
    def __init__(self, length, include_number=True, include_simbol=True):
        self.length = length
        self.include_number = include_number
        self.include_simbol = include_simbol

        # Create the character set with the selected options
        self.character = ''

        self.character += string.ascii_letters
        if self.include_number:
            self.character += string.digits
        if self.include_simbol:
            self.character += string.punctuation
    

    def generatorPass(self):
        # Check that the character set is selected
        if not self.character:
            raise ValueError("You must select at least one character type!")

        # Generate password with length and available characters
        return ''.join(random.choice(self.character) for _ in range(self.length))

# Examples of use
generator = PasswGenerator(length=21, include_number=True, include_simbol=True)

print(f"Generated Password: {generator.generatorPass()}")
