# Encryption Program V1
########################### Logic #############################
import random
import string
chars = " " + string.ascii_letters + string.digits + string.punctuation
# shuffledChars = ''.join(random.sample(chars, len(chars)))    # To Shuffle a string
shuffledChars = "NJoFyU&+%p):e;G6*DCl3rBAR1-bHiK},/78! m0'nPgLTE=M\"~k2w[v@jz4s_du?ca9It.`OZ^\\xYV<Q>$S{|h#Xfq(W5]" # use \ before " or \ to print double quote or \

def encryption():
        encryptedMessage = "" # The best way
        message = input("Enter the message you want to encrypt: ")
        for char in message:
            charIndex = chars.index(char)
            encryptedMessage += shuffledChars[charIndex] # The best way
            # print(encryptedMessage, end="") # Not the best
        print(f"The encrypted message is: {encryptedMessage}")

def decryption():
    decryptedMessage = "" # The best way
    message = input("Enter the message you want to decrypt: ")
    for char in message:
        charIndex = shuffledChars.index(char)
        decryptedMessage += chars[charIndex] # The best way
        # print(decryptedMessage, end="") # Not the best
    print(f"The decrypted message is: {decryptedMessage}")

def main():
    while True:
        encryption()
        print("*********************************")
        decryption()
        print("*********************************")
        check = input("Do you want to continue? (Y/N): ").upper()
        if check == "N":
            print("Thank you for using the Encryption Program 👋")
            break 
###############################################################
if __name__ == "__main__":
    print("*********************************")
    print("        Encryption Program       ")
    print("*********************************")
    main()
    print("*********************************")
