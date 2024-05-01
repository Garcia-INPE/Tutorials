# How to install and use PEP 8 Extension in VS Code (May/24)
by [JRM Garcia](https://garcia-inpe.github.io/) / [INPE](https://www.gov.br/inpe/pt-br) / [MCTI](https://www.gov.br/mcti/pt-br)

## Installing and configuring
1. In VS Code click on the Extension buttom in the left vertical bar
2. In the search bar, just below EXTENSION: MARKETPLACE, type: autopep8
3. Make sure the extension is produded by Microsoft and click the Install buttom
4. If you want to ensure that PEP 8 is applied for all your Python code in VS Code and auto-applied on save:
    * Menu View / Command Palette (or shift+option+P in Mac)
    * Type something in the search bar that allows you find for: <ins>**Preferences: Open User Settings (JSON)**</ins>
    * Edit the file respecting the existent main "{" and "}" symbols and include the auto-explainable entries:
> <pre>
> "[python]": {
>      "editor.defaultFormatter": "ms-python.autopep8",
>      "editor.formatOnSave": true
>      }
</pre>

## Using
1. If you used the step-4 recommended configuration above the file will autommatically formatted on Save
2. To format the entire active file (the document) (⇧⌥F)
3. To format the selected text (⌘K ⌘F)

### Resources
* [PyPI Autopep8](https://pypi.org/project/autopep8/)
* [VS Code / Code basics / Formatting](https://code.visualstudio.com/docs/editor/codebasics#_formatting)
* [PEP 8 official documentation](https://peps.python.org/pep-0008/) 
* [Microsoft Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)
