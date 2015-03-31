import csv
import random
from block import Block
class Experiment(object):
    
    def __init__(self, input_file, sample_size):
        #filename = 'test_emails.txt'
        self.filename = input_file
        
        self.all_posting_ids = []
        self.postings = {}
        with open(self.filename, 'rU') as f:
            reader = csv.reader(f)
            reader.next()
            for row in reader:

                if row[3] != '':
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
        
        #Randomize the IDs
        if len(self.all_posting_ids) < sample_size:
            self.sample_size = len(self.all_posting_ids)
        else:
            self.sample_size = sample_size

        self.random_sample_ids = random.sample(self.all_posting_ids, self.sample_size)
        #random.shuffle(self.all_posting_ids)

        #Split into blocks
        self.white_high_ids = self.random_sample_ids[0::4]
        self.white_low_ids = self.random_sample_ids[1::4]
        self.black_high_ids = self.random_sample_ids[2::4]
        self.black_low_ids = self.random_sample_ids[3::4]

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
            
if __name__ == '__main__':
    pilot = Experiment('cle_test.csv', 120)
    