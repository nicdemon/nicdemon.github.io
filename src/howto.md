# Gemini answer to: myst-parser custom directive
MyST Parser, when used within Sphinx, allows for the creation of custom directives to extend the functionality of MyST Markdown. These custom directives are essentially Python classes that inherit from Sphinx's Directive class (or its subclasses) and are registered with Sphinx.

### Creating a Custom Directive:

Define the Directive Class.

Create a Python class that inherits from ``sphinx.util.docutils.Directive``. This class will contain the logic for parsing and rendering your custom directive.

```
from docutils.parsers.rst import Directive, directives
from docutils import nodes

class MyCustomDirective(Directive):
    # Define arguments and options for your directive
    required_arguments = 1  # Number of required arguments
    optional_arguments = 1  # Number of optional arguments
    has_content = True      # Whether the directive has content block
    option_spec = {         # Define options and their types
        'my_option': directives.unchanged,
    }

    def run(self):
        # Access arguments, options, and content
        arg1 = self.arguments[0]
        option_value = self.options.get('my_option')
        content = '\n'.join(self.content)

        # Create Docutils nodes based on your logic
        # For example, create a paragraph node with the content
        paragraph_node = nodes.paragraph(text=f"Argument: {arg1}, Option: {option_value}, Content: {content}")
        return [paragraph_node]
```

Register the Directive with Sphinx.
In your Sphinx project's ``conf.py`` file, use the ``app.add_directive()`` method within a ``setup()`` function to register your custom directive.

```
def setup(app):
    app.add_directive("mycustom", MyCustomDirective)
```

Here, ``"mycustom"`` is the name you will use to invoke the directive in your MyST Markdown files.

### Using the Custom Directive in MyST Markdown:

Once registered, you can use your custom directive in your MyST Markdown files like this:

```{mycustom} required_argument_value
:my_option: option_value
This is the content of my custom directive.
It can span multiple lines.
```

### Key Points:

* docutils.parsers.rst.Directive: This is the base class for all Sphinx directives.
* ``required_arguments``, ``optional_arguments``, ``has_content``: These class attributes define the structure of your directive's arguments and content.
* ``option_spec``: This dictionary defines the available options for your directive and their parsing functions (e.g., directives.unchanged, directives.flag, directives.uri).
* ``run()`` method: This method contains the core logic of your directive. It processes arguments, options, and content, and returns a list of Docutils nodes that will be inserted into the document.
* ``app.add_directive()``: This Sphinx application method is used to register your custom directive with a specific name.