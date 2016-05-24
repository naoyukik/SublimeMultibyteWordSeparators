import sublime
import sublime_plugin
import re


def regularPattern():
    separate = '|'
    settings = sublime.load_settings("MultibyteWordSeparators.sublime-settings")
    rePattern = settings.get('pattern')

    pattern = separate.join(rePattern.values())
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


class SelMouseMultibyteWordSeparatorsCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward=False):
        self.view.run_command("multibyte_word_separators", {"forward": False})
        self.view.run_command("sel_multibyte_word_separators", {"forward": True})
