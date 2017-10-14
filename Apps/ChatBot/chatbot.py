"""
ChatBot program by SonowalzLabs
Supervised machine learning.
"""

from mp import MessageProcessor

# Run the program!
if __name__ == '__main__':
    print("Press 'x' to Exit!")
    inputmsg = input("Hello! I am Brahma. How can I help you?\n")
    if inputmsg != 'x' and inputmsg != '':
        print(MessageProcessor.process_input(inputmsg))
    else:
        print("Goodbye!")