#Racial Discrimination in Competitive Housing Markets

##Scraper instructions
Please install scrapy using:
  pip install scrapy

To run the scraper:
```
cd scrapy\<yourcity\>

scrapy crawl \<yourcity\>
```

It will take some time (perhaps about 10 min) to run as there is some builtin time delays to avoid blocking of the scraper. If it runs fine, there will be a scrapy.log file generated which has log messages from the run - this comes in handy if there is any problem in the run. There will be a .csv file generated which contains the relevant postings.

##Email Setup  

###Create 4 Email addresses
e.g.  
* Jamal Jones (jamal.jones1789@gmail.com)  
* Greg Baker (greg.baker1789@gmail.com)  
* Jamal Jones (jamal.jones1790@gmail.com)  
* Greg Baker (greg.baker1790@gmail.com)  

###CHANGE THE ACCOUNT SETTINGS ON THE GMAIL ACCOUNT
https://docs.google.com/document/d/1mxmIrZBapWtat5GFDYYqqhh7h2aG504XuAIV2U6v8BA/edit?usp=sharing

###Python Scripts

There are several Python scripts to run the process:  
* emailagent.py - simple object to hold email sender
* emailaddresses.py - THIS NEEDS  TO BE UPDATED WITH YOUR EMAIL ADDRESSES AND PASSWORDS
* block.py - this object does most of the email functions
* experiment.py - main class to run the experiment. Input textfile and # of emails as arguments.

To run the script,
* Make sure you changed the gmail settings
* Update emailaddresses.py with your email addresses and passwords
* Place your input file in the same directory as the Python scripts
* In the bottom of the experiment.py script, change the filename to your filename.
* Run the command below

```
python experiment.py
```
It should take several minutes (~5) to send out all of the emails. There is an intentional delay to prevent Gmail rate limits. Results will be stored in the "email_results" and "email_errors" folders (several CSV files).

### Automatically read emails and get outcome

* Try (sudo) pip install imaplib, email, whatever_you_need
* Put csv for an email from Nate's email sending script under reademail directory
* python reademail.py --email_address \<email\> --email_password \<password\> --csv_input \<white_low.csv\> --csv_output \<white_low_out.csv\>
* Run four times for your four email accounts

After run, please check the following scenarios in your Gmail Inboxes:

* Subject has special characters;
* Owner sends under another new subject;
* Finally, check the total number of valid incoming emails to see if it matches the generated csv file

###Input Items

*Names*  
* Jamal Jones  
* Greg Baker  

*High-Paying Jobs*
* 'a data scientist'  
* 'a physician'  
* 'a dentist'  
* 'an IT manager'  
* 'a lawyer'  
* 'a financial manager'  
* 'an architect'  
* 'a pilot'  

*Low-Paying Jobs*  
* 'a chef'  
* 'a dietetic technician'  
* 'a fitness trainer'  
* 'a social worker'  
* 'a police officer'  
* 'an elementary school teacher'  
* 'a reporter'  
* 'a medical assistant'  
* 'an insurance appraiser'  
* 'a waiter'  

The high-paying jobs say they finished "graduate school" while the low-paying jobs say they finished "school".

###Example Email  

>I'm writing to inquire about your ad on Craigslist. I recently finished [graduate school/school] and took a job as [high job/low job] and I am looking for a place to live.
>
>If the apartment is still available, I would like to schedule a showing for next week.
>
>Thanks,
>[Greg Baker/Jamal Jones]

##Group Members
* Charlie Carbery (carberyc@gmail.com)
* Malini Mittal (malini.mittal@gmail.com)
* Tao Mao (tao.mao@ischool.berkeley.edu)
* Nate Black (nathaniel.j.black@gmail.com)
* Vineet Gangwar (vineet.gangwar@gmail.com)

##Experimental Design and Protocol
The experiment will measure discrimination (racial and social class) in the rental housing market. The subjects, landlords looking to rent out their properties, for the experiment will be obtained from Craigslist. The audit experiment will implement a factorial 2 X 2 design. The experiment will be run in five cities for a week, from Sunday to Saturday. For each city, at the end of each day we will randomly sample landlords and then use complete random assignment to equally assign them to the four treatment conditions. The sample size will be determined by the pilot study. We will use sample function of R for randomization. The treatment will be in the form of an email response to the ad on Craigslist. The name of the sender will convey the race. We will also include information such as education level and employer name of the sender to convey social class. After the treatment, we will wait for a week for responses to come in.

The primary outcome variable will be binary. It will be 1 if there is an email response from the subject. The content of the response will not be considered. We will also measure a secondary outcome variable - the amount of the time the subject takes to respond. We will measure the following covariates: rental price, type of property (apartment, house etc), size of property (measure in number of bedrooms), type of landlord (individual or rental company), number of hours between ad posting and treatment, city, location type (whether urban or suburban). Location type has driven the selection of cities.

##Cities
* Cleveland
* San Jose
* Raleigh
* New York City
* Chicago


##Software
We will be using a Scrapy (Python) crawler to scrape the relevant data off of the craigslist.org websites. There will be one crawler for each city, and each will extract information like the price, posting URL, location, posting date, email, etc. All of this data will be stored in JSON files. 

We have created a crawler for one city as a proof of concept. It still needs to be refined to extract more information.

We need to write another script which will read the JSON files created above, and extract just the emails to store in another file, to make it easier to randomize the sample selection. 


##E-mail Scripts
We will utilize a total of four different scripts for the experiment. There will be two different manuscripts that will each vary by the responder name. We are exploring several different potential scripts that will incorporate information about the responders in a subtle manner. The scripts will include information such as type of employment, education level, credit history, and/or grammar. The script(s) will be an integral part of the experiment; therefore, we are planning on testing multiple scripts in the pilot experiment.

##Pilot
During the week of March 16th, we plan on running a pilot for our experiment. We have three main goals we hope to accomplish in our pilot. First, we hope to identify and remedy any technical problems before running the actual experiment. Specifically, we will pay close attention to our automatic response tool. Second, we will pay close attention to response rate in order to determine the proper sample size for our actual experiment. Based on the response rate, we will make the appropriate calculations to ensure our experiment has enough power. Specifically, we will monitor for low response rates, which will in turn necessitate a large sample size for our experiment. Lastly, we will track covariates to establish whether blocking is necessary for our experiment. While we are planning on addressing most heterogeneity problems via randomization, if there are any striking trends (apartment price for example), we may choose to use blocking or restrict our sample space for the actual experiment.


The pilot will be run over two days in one housing market (Washington DC). Each day, we will respond to 100 ads. On the first day, the experimenter will respond manually to each ad. On the second day, we will use our script to generate automatic responses.

##Gmail Setup
https://docs.google.com/document/d/1mxmIrZBapWtat5GFDYYqqhh7h2aG504XuAIV2U6v8BA/edit?usp=sharing

##Pilot Email Addresses
* Jamal Jones (jamal.jones1789@gmail.com)
* Greg Baker (greg.baker1789@gmail.com)


