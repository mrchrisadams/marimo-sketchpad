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
    import markdown
    import rich
    return llm, markdown, mo, rich


@app.cell
def __(mo):
    mo.md(
        """
        ## For this to work, you need ollama installed, and to have pulled down the llama3.2 model

        This is not too complicated though. If you visit  the [Ollama](https://ollama.com/) website, you can download the installer.

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

        So, that's what `rendered_chat()` below does.

        While the returned text from the LLM is markdown, it still needs to be rendered. This is why we call the `markdown()` to turn the markdown text into html, to render on the page.
        """
    )
    return


@app.cell
def __(markdown, mo, model):
    conversation = model.conversation()

    def rendered_chat(messages, config):
        """
        A function to call to return answer to the last prompt.
        Returns an llm.models.Response object
        """
        content = conversation.prompt(messages[-1].content)

        # TODO: not every element in markdown appears to be rendered right
        # see why this is in future
        rendered_markdown = markdown.markdown(content.text())

        return rendered_markdown

    chat = mo.ui.chat(rendered_chat)
    chat
    return chat, conversation, rendered_chat


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
