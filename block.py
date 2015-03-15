import random
import smtplib
import datetime
import time
import csv

class Block(object):
    """Represents the combination of race and social status"""
    def __init__(self, postings, race, social_status):
        self.postings = postings
        self.race = race
        self.social_status = social_status
        self.sender_email = ''
        
        #Potential Variables
        if self.race == 'white':
            self.names = ['Daniel','Dylan','Dustin','David','Drew']
        elif self.race == 'black':
            self.names = ['DeAndre','DeShawn','Demetrius','Dorian','Darnell']
        else:
            raise Exception
        
        if self.social_status == 'high':
            self.jobs = ['an attorney',
                        'an actuary',
                        'a radiologist',
                        'an electrical engineer',
                        'a software developer',
                        'an investment banker',
                        'a mechanical engineer',
                        'a management consultant',
                        'a dentist',
                        'a physicist']
                        
            self.sender_school = " graduate "
       
        elif self.social_status == 'low':
            self.jobs = ['a chef', 
                        'a dietetic technician',
                        'a fitness trainer',
                        'a social worker',
                        'a police officer',
                        'an elementary school teacher',
                        'a reporter',
                        'a medical assistant',
                        'an insurance appraiser',
                        'a waiter']
            
            self.sender_school = " "
       
        else:
            raise Exception
        
        #Email addresses that we will send from
        self.email_senders = {'Daniel':'field.experiments.w241@gmail.com',
                        'Dylan':'field.experiments.w241@gmail.com',
                        'Dustin':'field.experiments.w241@gmail.com',
                        'David':'field.experiments.w241@gmail.com',
                        'Drew':'field.experiments.w241@gmail.com',
                        'DeAndre':'field.experiments.w241@gmail.com',
                        'DeShawn':'field.experiments.w241@gmail.com',
                        'Demetrius':'field.experiments.w241@gmail.com',
                        'Dorian':'field.experiments.w241@gmail.com',
                        'Darnell':'field.experiments.w241@gmail.com'
                        }  
        
        #Need to update this with new email addresses and passwords                
        self.email_password = '*******'
        
    
    
    def generate_sender(self):
        """Generates a random name, job, and email message"""
        sender_name = random.sample(self.names, 1)[0]
        sender_job = random.sample(self.jobs, 1)[0]
        sender_email = self.email_senders[sender_name] 
        email_body = "I'm writing to inquire about your ad on Craigslist. I recently finished" + self.sender_school \
                    + "school and took a job as " + sender_job + " and I am looking for a place to live.\n\n" \
                    + "If the If the apartment is still available, I would like to schedule a showing for next week.\n\n" \
                    + "Thanks,\n" + sender_name
        return sender_name, sender_job, sender_email, email_body, self.race, self.social_status
                    
    def create_email(self, from_addr, to_addr, email_body, subj, url):
        """Create an email using given address, subject, and URL"""
        message = "From: %s\r\nTo: %s\r\nSubject: %s\n\n" % (from_addr, to_addr, subj)
        message += email_body + '\n\n'
        message += url
        return message
        
    #def send_email(self):
    #    """Attempts to send email"""
    #    try:
    #        server = smtplib.SMTP('smtp.gmail.com', 587)
    #        server.ehlo()
    #        server.starttls()
    #        server.ehlo
    #        server.login(self.sender_email, self.email_password) 
    #        server.sendmail(self.sender_email, self.receiver_email, self.message)
    #        server.quit()
    #        email_result = 'Success', str(datetime.datetime.now()), self.message
    #    except smtplib.SMTPException as error:
    #        email_result = error, str(datetime.datetime.now()), self.message
    #    time.sleep(1)
    #    return email_result
    
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
                    
    def run_process(self):
        #Loops through each posting and attempts to send an email. Writes result and time back to posting
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo
        
        
        for posting in self.postings:
            #Unpack generate_sender into components
            self.postings[posting]['sender_name'], \
            self.postings[posting]['sender_job'], \
            self.postings[posting]['sender_email'], \
            self.postings[posting]['email_body'], \
            self.postings[posting]['sender_race'], \
            self.postings[posting]['sender_social_status'] = self.generate_sender()
            
            message = self.create_email(self.postings[posting]['sender_email'],self.postings[posting]['email'],self.postings[posting]['email_body'],self.postings[posting]['title'], self.postings[posting]['url'])

            try:
                if self.postings[posting]['sender_email'] == self.sender_email:
                    pass
                else:
                    server.login(self.postings[posting]['sender_email'], self.email_password) 
                    self.sender_email = self.postings[posting]['sender_email']
                    
                server.sendmail(self.postings[posting]['sender_email'], self.postings[posting]['email'], message)
                
                self.postings[posting]['result'] = 'Success'
                self.postings[posting]['emailsent'] = str(datetime.datetime.now())
                time.sleep(0.6)
            except smtplib.SMTPException as error:
                self.postings[posting]['result'] = error
                self.postings[posting]['emailsent'] = str(datetime.datetime.now())
                time.sleep(13)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo
                self.sender_email = ''

        server.quit()
        self.write_email_messages()
        self.write_email_results()
