# MultibyteWordSeparators

About
---
MultibyteWordSeparators supported for sublime text 3.
It corresponds to move to each word of the cursor.

Installation
---
It's simple. Use Package Control.

Search MultibyteWordSeparators


key Binding
---
```javascript
    [
        { "keys": ["ctrl+left"], "command": "multibyte_word_separators", "args": {"forward": false}},
        { "keys": ["ctrl+right"], "command": "multibyte_word_separators", "args": {"forward": true}},

        // selected
        { "keys": ["ctrl+shift+left"], "command": "sel_multibyte_word_separators", "args": {"forward": false}},
        { "keys": ["ctrl+shift+right"], "command": "sel_multibyte_word_separators", "args": {"forward": true}}
    ]
```
