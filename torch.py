import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

model.eval()

tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id


def generate_text(prompt, max_length=100, temperature=0.6,top-k=50):
    input_ids= tokenizer.encode(prompt,return_tensors="pt")
    output = model.generate(input_ids, max_length= max_length, temperature=temperature, top_k= top_k, pad_token_id= tokenizer.eos_token_id,do_sample= True,)

    generated_text = tokenizer.decode(output[0] , skip_special_tokens= True)
    return generated_text


