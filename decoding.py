from morse_alphabet import packages
from joblib import Memory

memory = Memory('cache')

class Decoder:

    @memory.cache
    def decodeMorse(message, lang):
        messageSeparated = message.split()
        DecodedMessage = ''
        
        basePackages = {}

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
            
        return DecodedMessage

decoder = Decoder()