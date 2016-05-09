# MultibyteWordSeparators

プラグインについて
---
Sublime Text 3向けのマルチバイト文字列に対応した単語移動をサポートするパッケージです。  
マルチバイト文字(主に日本語)を判別し、単語移動を出来るようにしました。  
形態素解析を使用して単語を判別しているわけではなく、文字種を判別して移動させています。

以前は MoveMultiByteWord という名前で公開していましたが変更しました。この変更に伴い、コマンド名も変更されています。

インストール
---
Package Contorolに登録しています。下記の名前で検索できます。

MultibyteWordSeparators

キーバインド例
---
このプラグインの初期設定のキーバインドは、Sublime Textの初期のカーソル移動を上書きします。
もし変更を行いたい場合、下記のcommandを使用して変更してください。

```javascript
    [
        // 左へカーソルを動かす設定時、forwardをfalseへ
        { "keys": ["ctrl+left"], "command": "multibyte_word_separators", "args": {"forward": false}},
        // 右へカーソルを動かす設定時、forwardをtrueへ
        { "keys": ["ctrl+right"], "command": "multibyte_word_separators", "args": {"forward": true}},

        // 選択しながらカーソルを動かす
        { "keys": ["ctrl+shift+left"], "command": "sel_multibyte_word_separators", "args": {"forward": false}},
        { "keys": ["ctrl+shift+right"], "command": "sel_multibyte_word_separators", "args": {"forward": true}}
    ]
```
