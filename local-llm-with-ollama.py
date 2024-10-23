# /// script
# requires-python = ">=3.13"
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

        Once you have that llm by default will not know to use it. The simplest way, assuming you're not _already_ using llm is to set it as the default, instead of OpenAI:

        ```
        llm models default llama3.2
        ```

        Then you can proceed with the other steps.

        _**note**:_ If you are running this in sandbox, you need to figure out how to install `llm-gpt4all`, `llm-ollama` into the sandbox virtual env, and THEN set the default, the code Marimo is running in the sandbox does not have access to the globally installed models installed with `llm install llm-ollama` and can't run `llm models default llama3.2`.
        """
    )
    return


@app.cell
def __():
    import subprocess

    subprocess.run(["llm", "install", "llm-gpt4all"])
    subprocess.run(["llm", "install", "llm-ollama"])
    subprocess.run(["llm", "models", "default", "llama3.2"])

    # globally installed models
    subprocess.run(["llm", "models", "list"])
    return (subprocess,)


@app.cell
def __():
    return


@app.cell
def __(llm):
    # list the models installed into this sandbox
    llm.get_models_with_aliases()
    llm.set_default_model("llama3.2")

    model = llm.get_model()
    # TODO:
    # figure out how to install the `llm-gpt4all`, `llm-ollama` into this sandbox, and set llma as as the default model
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
