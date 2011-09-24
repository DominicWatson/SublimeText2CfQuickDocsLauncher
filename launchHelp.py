import sublime, sublime_plugin, webbrowser

class LaunchCfHelpCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward = True):
        word = ""
        for s in self.view.sel():
                word = self.view.word( s )
        
        s = sublime.load_settings("CfQuickDocs.sublime-settings")
        cfVersion = s.get('cf_version', 'cf9')


        webbrowser.open("http://cfquickdocs.com/" + cfVersion + "/#" + self.view.substr(word))