from morse_alphabet import packages
import rsa_module

class Decoder:

    def decodeMorse(self, message, lang, useRSA, cipher):
        messageSeparated = message.split()
        DecodedMessage = ''
        
        basePackages = {}

        if useRSA == 1:
            lang = 'English'

        for package in packages:
            if package.IfBasePackage == True:
                basePackages.update(package.inverse())

        for package in packages:
            if package.name == lang:
                packageInverted = package.inverse()
                for char in messageSeparated:
                    if char in packageInverted:
                        DecodedMessage += packageInverted[char]
                    elif char in basePackages:
                        DecodedMessage += basePackages[char]
                    else:
                        DecodedMessage += "<CNF>"
            else: continue
        
        if useRSA == 1:
            DecodedMessage = cipher.decrypt(bytearray.fromhex(DecodedMessage.lower()).decode())

        return DecodedMessage

decoder = Decoder()