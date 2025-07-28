from transformers import pipeline

# #  NL intents
# INTENTS = [
#   "set a reminder",
#   "play music",
#   "book a restaurant",
#   "get the weather",
#   "add to a playlist",
#   "An attack is happening",
#   "search for creative work"
# ]

# # Zero-shot classifier with context 
# clf = pipeline(
#   "zero-shot-classification",
#   model="facebook/bart-large-mnli", # allow model to retrieved NLI model
#   hypothesis_template="The user request is to {}." # override due hypothesis by default expecting a in line label "{}", this allows to seperate premise/label to hypothesis
# )

# examples = [
#   "Set workout for jungle gym at 2",
#   "Play some jazz",
#   "choke slam from the big show",
#   "Book a table at the Italian restaurant",
#   "Remind me to call mom at 6 PM",
#   "Draw a picture of naruto",
#   "appointment to attend"
# ]


# for text in examples:
#   out = clf(text, candidate_labels=INTENTS)
#   print(f"{text!r} → {out['labels'][0]} ({out['scores'][0]:.2f})")

INTENTS = [
]

#  (NER) or token classification for parse the text block text zero shot 
ner = pipeline(
  "token-classification" ,
  model="dslim/bert-base-NER",
  aggregation_strategy="simple"
)

text = "I have a meeting at 3pm on saturday"
result = ner(text)
print("NER Results:", result)
