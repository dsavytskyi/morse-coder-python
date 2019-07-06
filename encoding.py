from morse_alphabet import packages
import winsound
import time
from joblib import Memory

memory = Memory('cache')

class Encoder:
    interval = 175 

    @memory.cache
    def encodeToMorse(message):
        encodedMessage = ''
        charFound = True
        for char in message[:]:
            for package in packages:
                if char.upper() in package.alphabet:
                    encodedMessage += (package.alphabet[char.upper()] + ' ')
                    charFound = True
                    break
                else:
                    charFound = False
            if charFound == False:
                encodedMessage += '<CNF> '
        
        return encodedMessage

    def play_text(self, txt):
        for char in txt:
            if char == ' ':
                time.sleep(self.interval/1000)
            elif char == '.':
                self.beep(1)
            elif char == '-':
                self.beep(3)
            elif char == '/':
                time.sleep(7*self.interval/1000)
        return None

    def beep(self, mul):
        frequency = 1000
        winsound.Beep(frequency, mul*self.interval)

encoder = Encoder()