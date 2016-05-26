***********************
MultibyteWordSeparators
***********************

About
=====
MultibyteWordSeparators supported for sublime text 3.
It corresponds to move to each word of the cursor.

Installation
=============
It's simple. Use Package Control.

Search MultibyteWordSeparators


key Binding
===========

.. code-block:: javascript

    [
        { "keys": ["ctrl+left"], "command": "multibyte_word_separators", "args": {"forward": false}},
        { "keys": ["ctrl+right"], "command": "multibyte_word_separators", "args": {"forward": true}},

        // selected
        { "keys": ["ctrl+shift+left"], "command": "sel_multibyte_word_separators", "args": {"forward": false}},
        { "keys": ["ctrl+shift+right"], "command": "sel_multibyte_word_separators", "args": {"forward": true}}
    ]


Usage
=====
Preferences > MultibyteWordSeparators > Settings - User

"Settings - Default" all text copy to Settings - User.

- Unicode of hexadecimal number 
- Regular expression

For example
    Add Space Group. It move cursor only space.

.. code-block:: javascript

  {
      "pattern" : {
        ...
  -       "latin": "[\u0030-\u0039\u0041-\u005A\u0061-\u007A\u0020\u005F]+",
  +       "latin": "[\u0030-\u0039\u0041-\u005A\u0061-\u007A\u005F]+",
          "latinSymbol": "[\u0021-\u002F\u003A-\u0040\u005B-\u005E\u0060\u00A5\u007B-\u007E\u203E]+",
          "czeroControls": "[\u0000-\u0009\u000B\u000C\u000E-\u001F]+",
          "controlCharacters": "[\u000A\u000D]+",
  +       "space": "[\u0020]+"
      }
  }
