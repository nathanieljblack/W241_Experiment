import csv
import random
from block import Block
class Experiment(object):
    
    def __init__(self, input_file):
        #filename = 'test_emails.txt'
        self.filename = input_file
        
        self.all_posting_ids = []
        self.postings = {}
        with open(self.filename, 'rb') as f:
            reader = csv.reader(f)
            reader.next()
            for row in reader:
                self.all_posting_ids.append(row[4])
                
                self.postings[row[4]] = {'title':row[0],
                    'url':row[1],
                    'price':row[2],
                    'email':row[3],
                    'id':row[4],
                    'location':row[5],
                    'date':row[6],
                    'housing':row[7]
                    }
        
        #Split into White/Black
        self.white_ids = random.sample(self.all_posting_ids, len(self.all_posting_ids)/2)
        self.black_ids = [x for x in self.all_posting_ids if x not in self.white_ids]
        
        #Split races into statuses
        self.white_high_ids = random.sample(self.white_ids, len(self.white_ids)/2)
        self.white_low_ids = [x for x in self.white_ids if x not in self.white_high_ids]
        
        self.black_high_ids = random.sample(self.black_ids, len(self.black_ids)/2)
        self.black_low_ids = [x for x in self.black_ids if x not in self.black_high_ids]
        
        #Split the postings based on posting ids
        self.white_high_postings = {i:self.postings[i] for i in self.white_high_ids}
        self.white_low_postings = {i:self.postings[i] for i in self.white_low_ids}
        
        self.black_high_postings = {i:self.postings[i] for i in self.black_high_ids}
        self.black_low_postings = {i:self.postings[i] for i in self.black_low_ids}
        
        #Create blocks
        white_high_block = Block(self.white_high_postings, 'white', 'high')
        white_low_block = Block(self.white_low_postings, 'white', 'low')
        
        black_high_block = Block(self.black_high_postings, 'black', 'high')
        black_low_block = Block(self.black_low_postings, 'black', 'low')
        
        self.blocks = [white_high_block, white_low_block, black_high_block, black_low_block]
        
        #Send emails and write results to file
        for block in self.blocks:
            block.run_process()
        