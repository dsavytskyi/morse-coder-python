from morse_alphabet import packages
import os
import time

class Encoder:
    interval = 175 

    def encodeToMorse(self, message):
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
        os.system('play -nq -t alsa synth {} sine {}'.format(mul/2, frequency))

encoder = Encoder()
