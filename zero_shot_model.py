from transformers import pipeline

#  NL intents
INTENTS = [
  "set a reminder",
  "play music",
  "book a restaurant",
  "get the weather",
  "add to a playlist",
  "An attack is happening",
  "search for creative work"
]

# Zero-shot classifier with context
clf = pipeline(
  "zero-shot-classification",
  model="facebook/bart-large-mnli",
  hypothesis_template="The user request is to {}."
)

examples = [
  "Set workout for jungle gym at 2",
  "Play some jazz",
  "choke slam from the big show",
  "Book a table at the Italian restaurant",
  "Remind me to call mom at 6 PM",
  "Draw a picture of naruto"
]

for t in examples:
  out = clf(t, candidate_labels=INTENTS)
  print(f"{t!r} → {out['labels'][0]} ({out['scores'][0]:.2f})")
