MoveMultiByteWord
---
Sublime Text 3向けのマルチバイト文字列に対応した単語移動をサポートするパッケージです。  
マルチバイト文字(主に日本語)を判別し、単語移動を出来るようにしました。

インストール
---
現在のところ、Package Controlに対応していません。  
BitbucketからMercurialを使用してSublime Text 3のPackages配下にDLしてください。

    hg clone ssh://hg@bitbucket.org/dat/movemultibyteword

キーバインド
---
このパッケージには.sublime-keymapは含めていません。  
"Preferences -> Key Bindings - User" でキーバインドを下記のように追加してください。

    [
        { "keys": ["ctrl+left"], "command": "move_multi_byte_word", "args": {"forward": false}},
        { "keys": ["ctrl+right"], "command": "move_multi_byte_word", "args": {"forward": true}},
        { "keys": ["ctrl+shift+left"], "command": "move_sel_multi_byte_word", "args": {"forward": false}},
        { "keys": ["ctrl+shift+right"], "command": "move_sel_multi_byte_word", "args": {"forward": true}}
    ]

制限
---
- 改行コードをまたいだ単語選択移動には対応していません。
- マウスでの単語選択には対応していません。
