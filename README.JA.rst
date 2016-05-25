***********************
MultibyteWordSeparators
***********************

プラグインについて
==================
| Sublime Text 3向けのマルチバイト文字列に対応した単語移動をサポートするパッケージです。
| マルチバイト文字(主に日本語)を判別し、単語移動を出来るようにしました。
| 形態素解析を使用して単語を判別しているわけではなく、文字種を判別して移動させています。
|
| 以前は MoveMultiByteWord という名前で公開していましたが変更しました。この変更に伴い、コマンド名も変更されています。


インストール
==================
Package Contorolに登録しています。下記の名前で検索できます。

MultibyteWordSeparators

キーバインド例
==================
このプラグインの初期設定のキーバインドは、Sublime Textの初期のカーソル移動を上書きします。
もし変更を行いたい場合、下記のcommandを使用して変更してください。

.. code-block:: javascript

    [
        // 左へカーソルを動かす設定時、forwardをfalseへ
        { "keys": ["ctrl+left"], "command": "multibyte_word_separators", "args": {"forward": false}},
        // 右へカーソルを動かす設定時、forwardをtrueへ
        { "keys": ["ctrl+right"], "command": "multibyte_word_separators", "args": {"forward": true}},

        // 選択しながらカーソルを動かす
        { "keys": ["ctrl+shift+left"], "command": "sel_multibyte_word_separators", "args": {"forward": false}},
        { "keys": ["ctrl+shift+right"], "command": "sel_multibyte_word_separators", "args": {"forward": true}}
    ]

設定例
======
MultibyteWordSeparators.sublime-settings で設定することによって、セパレータの文字列を変更することが可能です。

自分の設定を使用するには、下記から設定ファイルを開きます。今回の例では Space をセパレータとして追加し、スペースのみで移動が区切られるように設定します。

Preferences > MultibyteWordSeparators > Settings - User

Userのファイルには、Settings -Default のpatternを一度丸ごとコピーしてください。patternの設定が全て上書きされます。

- 文字はunicodeで設定を行います。
- 正規表現で設定を行います。最後の+が無いと繰り返し文字列をヒットしません。
- キーはプラグインの処理上は使用していません。正規表現のグループを識別しやすいように使用していますので、グループを増やす場合、キーも新しく追加出来ます。

.. code-block:: javascript

  {
      "pattern" : {
          ～～～～省略～～～～
  -       "latin": "[\u0030-\u0039\u0041-\u005A\u0061-\u007A\u0020\u005F]+",
  +       "latin": "[\u0030-\u0039\u0041-\u005A\u0061-\u007A\u005F]+",
          "latinSymbol": "[\u0021-\u002F\u003A-\u0040\u005B-\u005E\u0060\u00A5\u007B-\u007E\u203E]+",
          "czeroControls": "[\u0000-\u0009\u000B\u000C\u000E-\u001F]+",
          "controlCharacters": "[\u000A\u000D]+",
  +       "space": "[\u0020]+"
      }
  }
