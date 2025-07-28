import spacy
import dateparser
import re
from dateparser.search import search_dates

nlp = spacy.load("en_core_web_sm")

def get_time_date_description(text):

    #finding time and dates and using setting to help with ambigous date like a saturday
    date_time_matches = search_dates(
        text,
        languages=["en"],
        settings={"PREFER_DATES_FROM": "future", "STRICT_PARSING": False}
    )

    # if we dont find a time or dates just give us 
    if not date_time_matches :
        return {"description": text.strip(), "date": None, "time": None, "weekday": None}

    # get a list of dates and times so this list them reverse them to have longest at top
    date_time_matches .sort(key=lambda x: len(x[0]), reverse=True)
    # since search_date return a tuple we need to variable to assign it 
    best_time_date_words, best_dt_object = date_time_matches [0]

    # making our description variable so it only tthe words so it takes out the date time words, then an prepositions then white spaces 
    description = re.sub(re.escape(best_time_date_words), "", text, flags=re.IGNORECASE)
    description = re.sub(r"\b(?:at|on|in|by|for|to)\b", "", description)
    description = re.sub(r"\s+", " ", description).strip()

    # get 3 objects for the time date n day if needed 
    date_str    = best_dt_object.date().isoformat()        
    time_str    = best_dt_object.time().strftime("%H:%M")   
    weekday_str = best_dt_object.strftime("%A")            

    # remember the quotes are ur key and android or w.e nees to spell them the same 
    return {
        "description": description,
        "date":        date_str,
        "time":        time_str,
        "weekday":     weekday_str
    }

# # ex
# result = get_time_date_description("meet Friday eve")
# print(result)
