# MoveMultiByteWord

About
---
MoveMultiByteWord supported for sublime text 3.
It corresponds to move to each word of the cursor.

Installation
---
It's simple. Use Package Control.

Search MoveMultiByteWord


key Binding
---
This Package without .sublme-keymap.

Add Key Bindings to User config(Preferences -> Key Bindings - User)....
```javascript
    [
        { "keys": ["ctrl+left"], "command": "move_multi_byte_word", "args": {"forward": false}},
        { "keys": ["ctrl+right"], "command": "move_multi_byte_word", "args": {"forward": true}},
        { "keys": ["ctrl+shift+left"], "command": "move_sel_multi_byte_word", "args": {"forward": false}},
        { "keys": ["ctrl+shift+right"], "command": "move_sel_multi_byte_word", "args": {"forward": true}}
    ]
```
