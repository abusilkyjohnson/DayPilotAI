from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load and save the model locally
nlp_model_path_abu = "kaantureyyen/deberta-snips" #set variable to hugging face model
local_path_abu = "./model_files/deberta_snips"

# Download tokenizer from base model and model from fine-tuned repo
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-small")
model = AutoModelForSequenceClassification.from_pretrained(nlp_model_path_abu)

# Save both locally
tokenizer.save_pretrained(local_path_abu)
model.save_pretrained(local_path_abu)
