1. In VS Code click on the Extension buttom in the left vertical bar
2. In the search bar, just below EXTENSION: MARKETPLACE, type: autopep8
3. Make sure the extension is produded by Microsoft and click the Install buttom
4. If you want to ensure that PEP 8 is applyied for all your Python code in VS Code:
    * Menu View / Command Palette (or shift+option+P in Mac)
    * Type something in the search bar that allows you find for: **Preferences: Open User Settings (JSON)**
    * Edit the file respecting the existent main "{" and "}" symbols and include:
<pre>
    "[python]": {
        "editor.defaultFormatter": "ms-python.autopep8",
        "editor.formatOnSave": true
        }
</pre>
