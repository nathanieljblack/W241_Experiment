class EmailAgent(object):
    
    def __init__(self, name, email, password):
        """Email agent to email the observations in the block"""
        self.name = name
        self.email = email
        self.password = password
                
    def create_email(self, from_addr, to_addr, email_body, subj, url):
        """Create an email using given address, subject, and URL"""
        message = "From: %s\r\nTo: %s\r\nSubject: %s\n\n" % (from_addr, to_addr, subj)
        message += email_body + '\n\n'
        message += url
        return message