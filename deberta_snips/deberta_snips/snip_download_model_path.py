from transformers import DebertaV2Tokenizer, AutoModelForSequenceClassification

# Remote model repo and local save path
nlp_model_path_abu = "kaantureyyen/deberta-snips"
local_path_abu     = "./model_files/deberta_snips"

# Load the slow SentencePiece tokenizer
tokenizer = DebertaV2Tokenizer.from_pretrained("microsoft/deberta-v3-small")

# Load the fine-tuned intent classification model
model = AutoModelForSequenceClassification.from_pretrained(nlp_model_path_abu)

# Save both for local offline use
tokenizer.save_pretrained(local_path_abu)
model.save_pretrained(local_path_abu)

# print(f"Successfully saved tokenizer and model to {local_path_abu}")
