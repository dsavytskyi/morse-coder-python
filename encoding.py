from morse_alphabet import packages
import platform
import os
import winsound
import time
import rsa_module

class Encoder:
    interval = 175 

    def encodeToMorse(self, message, useRSA, cipher):
        if useRSA == 1:
            message = cipher.encrypt(message)
            message = ''.join(hex(ord(x))[2:] for x in message)
            print(message)

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
        if platform.system() == 'Linux':
            os.system('play -nq -t alsa synth {} sine {}'.format(mul/2, frequency))
        elif platform.system() == 'Windows':
            winsound.Beep(frequency, mul*self.interval)

encoder = Encoder()
