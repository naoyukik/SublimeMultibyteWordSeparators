import sublime_plugin
import re


def regularPattern():
    separate = '|'
    re_pattern = {
        'cjk': '[\u3400-\u9FFF\uF900-\uFAFF]+',
        'hiragana': '[\u3040-\u309F]+',
        'katakana': '[\u30A1-\u30FA\u30FC-\u30FE]+',
        'kanaSymbol': '[\u30A0\u30FB]',
        'cjkSymbol': '[\u3000-\u3020]+',
        'fullDigit': '[\uFF10-\uFF19]+',
        'fullLatin': '[\uFF21-\uFF3A\uFF41-\uFF5A]+',
        'halfCjkPunctuation': '[\uFF61-\uFF65]',
        'halfKatakana': '[\uFF66-\uFF9F]',
        'fullSymbol': '[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF60\uFFE0-\uFFE6\u005C\u00A2\u00A3\u00A7\u00A8\u00AC\u00B0\u00B1\u00B4\u00B6\u00D7\u00F7\u2010\u2015\u2016\u2018\u2019\u201C\u201D\u2020\u2021\u2025\u2026\u2030\u2032\u2033\u203B\u2103]+',
        'halfSymbol': '[\uFFE8-\uFFEE]',
        'latin': '[\u0030-\u0039\u0041-\u005A\u0061-\u007A\u0020\u005F]+',
        'latinSymbol': '[\u0021-\u002F\u003A-\u0040\u005B-\u005E\u0060\u00A5\u007B-\u007E\u203E]+',
        'controlCharacters': '[\u000D\u000A-\u000C]'
    }
    pattern = separate.join(re_pattern.values())
    reCompile = re.compile(u''+pattern)
    return reCompile


def wordParse(text):
    reCompile = regularPattern()
    return reCompile.findall(text)

class MultibyteWordSeparatorsCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=False):
        self.view.run_command("move", {"by": "words", "forward": forward, "extend": True})
        for region in self.view.sel():
            cursorWord = self.view.substr(region)
            self.moveCursor(cursorWord, forward)
            break

    def moveCursor(self, text, courseA):
        results = wordParse(text)
        if len(results) <= 0:
            self.view.run_command("move", {"by": "characters", "forward": courseA})
            return True
        setIndex = -1
        courseB = True
        if courseA is True:
            setIndex = 0
            courseB = False
        length = len(results[setIndex])
        self.view.run_command("move", {"by": "characters", "forward": courseB})
        while length > 0:
            self.view.run_command("move", {"by": "characters", "forward": courseA})
            length -= 1
        return results


class SelMultibyteWordSeparatorsCommand(sublime_plugin.TextCommand):

    def run(self, edit, forward=False):
        for region in self.view.sel():
            cursorWord = self.view.substr(region)
            defSelWord = wordParse(cursorWord)
        self.view.run_command("move", {"by": "words", "forward": forward, "extend": True})
        for region in self.view.sel():
            cursorWord = self.view.substr(region)
            self.moveCursor(cursorWord, forward, defSelWord)
            break

    def moveCursor(self, text, courseA, defSelWord):
        whileList = []
        defSetIndex = 0
        results = wordParse(text)
        length = len(defSelWord)

        if courseA is True:
            setIndex = 0
            courseB = False
            while length > 0:
                if results[setIndex] == defSelWord[defSetIndex]:
                    whileList.append(len(defSelWord[defSetIndex]))
                    results.pop(0)
                defSetIndex += 1
                length -= 1
        else:
            setIndex = -1
            courseB = True
            while length > 0:
                if results[-1] == defSelWord[length-1]:
                    whileList.append(len(defSelWord[length-1]))
                    results.pop()
                length -= 1

        if len(results) <= 0:
            self.view.run_command("move", {"by": "characters", "forward": courseA, "extend": True})
            return True

        whileList.append(len(results[setIndex]))
        self.view.run_command("move", {"by": "characters", "forward": courseB})
        for x in whileList:
            while x > 0:
                self.view.run_command('move', {"by": "characters", "forward": courseA, "extend": True})
                x -= 1
        return True
