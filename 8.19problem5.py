import string

quote = """
Dont let the fear of the time it will take to accomplish something stand in the way of doing it. The time will pass anyway; we might just as well put that passing time to the best use.
"""

def analyse_seq(seq, ch):
    """ Remove punctuation, break sequence into a list of words
    Count number of words in sequence that contain "e" letter """
    count = 0
    ct_ch = 0
    processing_t = ""
    """First of all, we remove punctuation in our quote
    Then add into new sequence "processing_t" """
    for letter in seq:
        if letter not in string.punctuation:
            processing_t += letter

    """Break sequence into a list of words
    Then count them if each item in loop equal with our character"""
    for i in processing_t.split():
        count += 1 
        if (ch in i) == True:
            ct_ch += 1 

    rating = round(ct_ch/count*100,1)  

    """Print announcement of our data analysis"""
    print(('Your text contains {0} words, of which {1} ({2}%) contain an "{3}".').format(count, ct_ch, rating, ch))


analyse_seq(quote, "e")
