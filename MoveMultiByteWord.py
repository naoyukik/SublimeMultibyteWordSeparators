import sublime, sublime_plugin
import re

def regularPattern():
    reCjk         = '[\u3400-\u9FFF\uF900-\uFAFF]+'
    reHiragana    = '[\u3040-\u309F]+'
    reKatakana    = '[\u30A0-\u30FA\u30FC-\u30FE]+'
    reCjkSymbol   = '[\u3000-\u3020]+'
    reMultiSymbol = '[\u005C\u00A2\u00A3\u00A7\u00A8\u00AC\u00B0\u00B1\u00B4\u00B6\u00D7\u00F7\u2010\u2015\u2016\u2018\u2019\u201C\u201D\u2020\u2021\u2025\u2026\u2030\u2032\u2033\u203B\u2103]+'
    reLatin       = '[\u0030-\u0039\u0041-\u005A\u0061-\u007A\u0020\u005F]+'
    reLatinSymbol = '[\u0021-\u002F\u003A-\u0040\u005B-\u005E\u0060\u00A5\u007B-\u007D\u203E]+'
    reCompile = re.compile(u''+reCjk+'|'+reHiragana+'|'+reKatakana+'|[\u30FB]+|[\u30FF]+|'+reCjkSymbol+'|'+reLatin+'|'+reLatinSymbol+'|'+reMultiSymbol)
    return reCompile

def wordParse(text):
    reCompile = regularPattern()
    return reCompile.findall(text)

class MoveMultiByteWordCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=False):
        self.view.run_command("move", {"by": "words", "forward": forward, "extend": True})
        for region in self.view.sel():
            cursor_word = self.view.substr(region)
            if forward == True:
                self.moveCursor(cursor_word, True)
            else:
                self.moveCursor(cursor_word, False)
            break

    def moveCursor(self, text, courseA):
        results = wordParse(text)
        print(results)
        if len(results) <= 0:
            self.view.run_command("move", {"by": "characters", "forward": courseA})
            return True
        set_index = -1
        courseB   = True
        if courseA == True:
            set_index = 0
            courseB   = False
        length = len(results[set_index])
        self.view.run_command("move", {"by": "characters", "forward": courseB})
        while length > 0:
            self.view.run_command("move", {"by": "characters", "forward": courseA})
            length -= 1
        return results
