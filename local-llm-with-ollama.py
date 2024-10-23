# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "llm==0.16",
#     "llm-gpt4all",
#     "llm-ollama",
#     "marimo",
#     "markdown==3.7",
#     "rich==13.9.3",
# ]
# ///

import marimo

__generated_with = "0.9.1"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import llm
    return llm, mo


@app.cell
def __(mo):
    mo.md(
        """
        ## What's this? 

        This is an interactive Marimo notebook, designed to use Ollama, for experimenting with generative AI using local models, and with a specific focus on small lanaguge models like Llama3.2 from Meta. 

        You can use this notebook to connect to a local model run with Ollama, and run chat sessions.

        You then need to run the following command in your terminal to fetch the 2Gb model.

        ```
        ollama pull llama3.2
        ```

        Once you have that, you can use the `llm` package installed when this Marimo notebook is run in sandbox mode to connect to the locally running instance of llama 3.2. This means you can now run `llm` commands against it, and crucially make Marimo  work with it.
        """
    )
    return


@app.cell
def __(llm):
    # list the models installed into this sandbox. Uncomment this to sanity check that you have access
    # to the necessary model
    # llm.get_models_with_aliases()

    # set our default to a local llama model, not OpenAI
    llm.set_default_model("llama3.2")

    # bring the model into the scope of the notebook, so we can refer to it in other cells
    model = llm.get_model()
    return (model,)


@app.cell
def __(mo):
    mo.md(
        """
        ## Starting a chat session

        Marimo has a nifty chat widget, that lets you use the `llm` package as the endpoint.

        To use it, you need to pass in a callable, like a function that accepts a list of messages, and then returns a string of rendered text that represents the last response from the LLM.

        You can use the chat widget below - give it ago!
        """
    )
    return


@app.cell
def __(mo, model):
    conversation = model.conversation()

    def rendered_chat(messages, config):
        """
        A function to call to return answer to the last prompt.
        Returns an llm.models.Response object
        """
        content = conversation.prompt(messages[-1].content)
        rendered_markdown = mo.md(content.text())

        return rendered_markdown

    chat = mo.ui.chat(rendered_chat)
    chat
    return chat, conversation, rendered_chat


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
