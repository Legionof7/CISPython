##########################
# CIS 117 Python Programming:  Lab #4
#
# Objects and Classes
#
##########################

class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.body = ""

    def append(self, line):
        self.body += line + "\n"

    def toString(self):
        email = "From: {}\nTo: {}\n{}\n".format(self.sender, self.recipient, self.body)
        return email
        
##########################
#Run
#
#From: Justin
#To: John
#For Christmas, I would like:
#World peace    
#Video games
##########################
