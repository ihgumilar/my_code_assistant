# %% [markdown]
# ## Libraries

# %%
import config_api
import os
import google.generativeai as palm
from google.api_core import client_options as client_options_lib
from google.api_core import retry

PALM_API_KEY = config_api.PALM_API_KEY


# %% [markdown]
# # MetaClass & MyCodeAssistant Class

# %%
class MetaClass(type):

    """MetaClass for MyCodeAssistant class.

    This class configures the palm client and sets the model to be used.
    """

    def __new__(cls, name, bases, attrs):

        """Class construction.

        Configures the palm client and sets the model to be used.

        Args:
            name (str): Class name.
            bases (tuple): Base classes.
            attrs (dict): Class attributes.

        Returns:
            object: New class instance.
        """

        # Class construction
        palm.configure(
            api_key=PALM_API_KEY,
            transport="rest",
            client_options=client_options_lib.ClientOptions(
                api_endpoint=os.getenv("GOOGLE_API_BASE"),
            )
        )

        return super(MetaClass, cls).__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):

        """Class call.

        Returns:
            object: New class instance.
        """

        return super(MetaClass, cls).__call__(*args, **kwargs)


class MyCodeAssistant(metaclass=MetaClass):

    """MyCodeAssistant class.

    This class generates code using the palm client.
    """

    def __init__(self):

        """Class initialization.

        Sets the model to be used.
        """

        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        self.models = models
        self.model_bison = self.models[0] if self.models else None

    @retry.Retry()
    def generate_text(self, prompt, model=None, temperature=0.0):

        """Generates text using the palm client.

        Args:
            prompt (str): Prompt text.
            model (palm.Model, optional): Model to be used. Defaults to None.
            temperature (float, optional): Temperature for text generation. Defaults to 0.0.

        Returns:
            palm.GenerateTextResponse: Generated text response.
        """

        if model is None:
            model = self.model_bison

        return palm.generate_text(prompt=prompt, model=model, temperature=temperature)

    @classmethod
    def generate_code(cls, priming: str, question:str, decorator:str):

        """Generates code using the palm client.

        Args:
            priming (str): Getting the LLM ready for the type of task you'll ask it to do.
            question (str): A specific task or code.
            decorator (str): How to provide or format the output.

        Returns:
            str: Generated code.
        """
        print("Please be patient...AI is working for you ;)")
        print("Always double check my generated code because you are a SuperBeing !")
        print("****************************************************************")
        print("")
        print("")

        prompt_template = """
            {priming}

            {question}

            {decorator}

            Your solution:
        """
        
        prompt = prompt_template.format(
            priming=priming,
            question=question,
            decorator=decorator)


        prompt = prompt_template.format(
            priming=priming,
            question=question,
            decorator=decorator)

        myCodeInstance = cls()

        completion = myCodeInstance.generate_text(prompt)

        return completion.result