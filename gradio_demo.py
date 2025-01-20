import gradio as gr

def add_sentences(sent1, sent2):
    return sent1 + ' '+ sent2

# Define the interface
demo = gr.Interface(
    fn=add_sentences, 
    inputs=[
        gr.Textbox(label="Input 1"), gr.Textbox(label="textbox")
        ], # Create two numerical input fields where users can enter numbers
    outputs=gr.Textbox(value="",label="Output")# Create numerical output fields
)

# Launch the interface
demo.launch(server_name="0.0.0.0", server_port= 7860)