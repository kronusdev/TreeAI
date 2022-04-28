from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

prompt = "What is my favorite color?"

res = generator(prompt, max_length=100, do_sample=True, temperature=0.9)

print(res[0]['generated_text'])