import gradio as gr
import json
def ask_llm(prompt):

    fake_response = """
    {
        "answer": "This is a simulated LLM response."
    }
    """

    result = json.loads(fake_response)

    return result["answer"]

def chatbot(prompt):
    return ask_llm(prompt)
demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Textbox(label="LLM Response"),
    title="AI Prompt Playground",
    description="My first Gradio app"
)
demo.launch()
