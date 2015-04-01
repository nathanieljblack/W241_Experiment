import random
import smtplib
import datetime
import time
import csv
import os
from emailagent import EmailAgent
from emailaddresses import EmailAddresses

class Block(object):
    """Represents the combination of race and social status"""
    def __init__(self, postings, race, social_status):
        self.postings = postings
        self.race = race
        self.social_status = social_status
        self.error_messages = {}
        email_addresses = EmailAddresses()
        
        #Potential Variables
        if self.race == 'white':
            self.name = 'Greg Baker'
        elif self.race == 'black':
            self.name = 'Jamal Jones'
        else:
            raise Exception
        
        if self.social_status == 'high':
            self.jobs = ['a data scientist',
                        'a physician',
                        'a dentist',
                        'an IT manager',
                        'a lawyer',
                        'a financial manager',
                        'an architect',
                        'a pilot']
                        
            self.sender_school = " graduate "
       
        elif self.social_status == 'low':
            self.jobs = ['a chef', 
                        'a dietetic technician',
                        'a fitness trainer',
                        'a social worker',
                        'an elementary school teacher',
                        'a reporter',
                        'a medical assistant',
                        'an insurance appraiser',
                        'a waiter']
            
            self.sender_school = " "
       
        else:
            raise Exception
        
        #Assign an email agent
        if self.race == 'white' and self.social_status == 'high':
            self.email_agent = EmailAgent(self.name, email_addresses.white_high_email[0], email_addresses.white_high_email[1])
        elif self.race == 'white' and self.social_status == 'low':
            self.email_agent = EmailAgent(self.name, email_addresses.white_low_email[0], email_addresses.white_low_email[1])
        elif self.race == 'black' and self.social_status == 'high':
            self.email_agent = EmailAgent(self.name, email_addresses.black_high_email[0], email_addresses.black_high_email[1])
        elif self.race == 'black' and self.social_status == 'low':
            self.email_agent = EmailAgent(self.name, email_addresses.black_low_email[0], email_addresses.black_low_email[1])
        else:
            raise Exception
        
    def generate_sender(self):
        """Generates a random name, job, and email message"""
        sender_job = random.sample(self.jobs, 1)[0]
        email_body = "I'm writing to inquire about your ad on Craigslist. I recently finished" + self.sender_school \
                    + "school and took a job as " + sender_job + " and I am looking for a place to live.\n\n" \
                    + "If the apartment is still available, I would like to schedule a showing for next week.\n\n" \
                    + "Thanks,\n" + self.email_agent.name
        return self.email_agent.name, sender_job, self.email_agent.email, email_body, self.race, self.social_status
    
    def write_email_messages(self):
        """Writes messages to file"""
        time_of_file = str(datetime.datetime.now())
        with open(self.race + '_' + self.social_status + '_email_messages_' + time_of_file + '.csv', 'wb') as f:
            w = csv.writer(f)
            for posting in self.postings:
                w.writerow([self.postings[posting]['email_body']])
                w.writerow(["\n\n"])
                
    def write_email_results(self):
        """Writes results to file"""
        time_of_file = str(datetime.datetime.now())
        with open(self.race + '_' + self.social_status + '_email_results_' + time_of_file + '.csv', 'wb') as f:
            w = csv.writer(f)
            w.writerow(['id',
                        'title',
                        'url',
                        'price',
                        'email',
                        'location',
                        'date',
                        'housing',
                        'result',
                        'emailsent', 
                        'sender_race',
                        'sender_social_status',
                        'sender_name',
                        'sender_job',
                        'sender_email'])
            
            for posting in self.postings:
                w.writerow([self.postings[posting]['id'], 
                            self.postings[posting]['title'],
                            self.postings[posting]['url'],
                            self.postings[posting]['price'],
                            self.postings[posting]['email'],
                            self.postings[posting]['location'],
                            self.postings[posting]['date'],
                            self.postings[posting]['housing'],
                            self.postings[posting]['result'],
                            self.postings[posting]['emailsent'],
                            self.postings[posting]['sender_race'],
                            self.postings[posting]['sender_social_status'],
                            self.postings[posting]['sender_name'],
                            self.postings[posting]['sender_job'],
                            self.postings[posting]['sender_email']])
                            
    def write_errors(self):
        """Writes errors to file"""
        time_of_file = str(datetime.datetime.now())
        if bool(self.error_messages):
            with open(self.race + '_' + self.social_status + '_email_errors_' + time_of_file + '.csv', 'wb') as f:
                w = csv.writer(f)
                for posting in self.error_messages:
                    w.writerow([posting, self.error_messages[posting]])
    
    def start_server(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo 
        self.server.login(self.email_agent.email, self.email_agent.password)
        
    
    def run_process(self):
        #Loops through each posting and attempts to send an email. Writes result and time back to posting
        self.start_server()

        for posting in self.postings:
            #Unpack generate_sender into components
            self.postings[posting]['sender_name'], \
            self.postings[posting]['sender_job'], \
            self.postings[posting]['sender_email'], \
            self.postings[posting]['email_body'], \
            self.postings[posting]['sender_race'], \
            self.postings[posting]['sender_social_status'] = self.generate_sender()
            
            message = self.email_agent.create_email(self.postings[posting]['sender_email'],
                                                    self.postings[posting]['email'],
                                                    self.postings[posting]['email_body'],
                                                    self.postings[posting]['title'],
                                                    self.postings[posting]['url'])

            try:
                self.server.sendmail(self.postings[posting]['sender_email'], self.postings[posting]['email'], message)
                self.postings[posting]['result'] = 'Success'
                self.postings[posting]['emailsent'] = str(datetime.datetime.now())
                time.sleep(1.5)
                
            except smtplib.SMTPException as error:
                self.postings[posting]['result'] = error
                self.error_messages[posting] = error
                self.postings[posting]['emailsent'] = str(datetime.datetime.now())
                time.sleep(6)
                self.start_server()

        self.server.quit()

        def mkdirp(directory):
            if not os.path.isdir(directory):
                os.makedirs(directory)
        
        mkdirp('email_results')
        os.chdir('email_results')
        self.write_email_results()
        os.chdir('..')

        mkdirp('email_errors')
        os.chdir('email_errors')
        self.write_errors()
        os.chdir('..')
        time.sleep(3)
