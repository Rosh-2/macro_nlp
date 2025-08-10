import re
import gradio as gr

def email(sentence):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, sentence)  
    
    if emails:
        code_example = f"""
import re

pattern = r'{pattern}'
re.findall(pattern, "{sentence}")
# Output: {emails}
"""
        return f"{code_example}"
    else:
        return "No email found in the sentence."

with gr.Blocks() as demo:
    gr.Markdown("### Email Extractor - Shows Code")
    inp = gr.Textbox(label="Enter a sentence containing an email:")
    out = gr.Textbox(label="Result (with code)", lines=8)
    btn = gr.Button("Extract Email")

    btn.click(fn=email, inputs=inp, outputs=out)

demo.launch()
