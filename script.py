
# Importing necessary packages
import yaml
import re, ssl
import urllib.request
import urllib.request as request
import time
from datetime import datetime


# Defining the input and output files
source_file_path = r"/Users/shohag/Desktop/programming_excercise/source.yaml"
urls = "ListOfWebLinks(URL)"
expression = "ListOfRegularExpression"
result = "findings.csv"

# MatchMaker is a class which takes the arguments like input and putput
class MatchMaker():
        
    def __init__(self, source, urls, expression, result):

        self.source = source
        self.urls = urls
        self.expression = expression
        self.result = result

    # Building a function under the class    
    def content_finder(self):     
        try:
            with open(self.result, "w") as wf:                                # write-file (wf)
                with open(self.source, "r") as rf:                            # read-file (rf)
                    df = yaml.load(rf, yaml.FullLoader)                       # source data loading (df)
                    
    # Defining the list of the web links (url) and regular expression (regexp) 
                    listed_urls = df.get(urls)                                # retrieving urls from the loaded data
                    listed_expressions = df.get(expression)                   # retrieving regular expression from the loaded data
                        

    # Matched contents are being extracted here
                    for url in listed_urls:
                        url_requested = urllib.request.Request(url)
                        responssive = urllib.request.urlopen(url_requested)
                        df_responssive = responssive.read()

    # Response time tracking method
                        unverified_cont = ssl._create_unverified_context()
                        running_time = datetime.now().strftime(" on %d-%m-%Y  at  %H:%M:%S")
                        start_time = time.time()
                        url_response = request.urlopen(url, context = unverified_cont)
                        data_reponse = url_response.read()
                        response_time = "%0.3f s" % (time.time() - start_time)
                        print(response_time)

                    
    # Putting the features together 
                        for regexp in listed_expressions:
                            matched_contents  = re.findall(regexp , str(data_reponse))
                            if not matched_contents:
                                print("There are no regular expression found: ", regexp)
                            else:    
                                for content in matched_contents:
                                    print(content)
                                    # Writing the outputs in the file
                                    print("Specific URL: ", url,  "\n Matched Contents: ", content, 
                                        "\n Running Time at: " , running_time, 
                                        " \n Response Time:", response_time, file = wf)
        except:
            print("The program is not execuatable!")

MatchMaker(source_file_path, urls, expression, result).content_finder()
