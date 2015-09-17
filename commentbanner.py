
"""This module provides the bannerComment plugin
class and supporting methods."""

import sublime
import sublime_plugin
# import textwrap


class BannerCommand(sublime_plugin.TextCommand):
    """create a fancy comment box around the text selection.
    - supports multi line selection
    - supports multi cursor selection
    """
    ROW_LENGTH = 77  # 80 - commenttags (like //) and space

    def run(self, edit):
        for region in self.view.sel():
            bannerText = self.view.substr(region)
            if bannerText:
                print(region.begin())
                self.view.erase(edit, region)
                self.view.insert(edit, region.begin(),
                                 self.full_screen_banner(bannerText))
                region_len = (region.begin() +
                              self.ROW_LENGTH*(2+len(self.lines)))
                self.view \
                    .selection \
                    .add(sublime.Region(region.begin(), region_len))
        # add the language dependend comment characters
        self.view.run_command("toggle_comment", False)

        # remove the selection of the cursor
        self.view.run_command("move", {"by": "characters", "forward": True})

    def full_screen_banner(self, string, symbol='*'):
        def outer_row():
            return (self.ROW_LENGTH - 1) * symbol + '\n'

        def inner_row():
            result = ""
            self.lines = string.splitlines()
            # textwrap.wrap(string)

            # center each line
            for line in self.lines:
                result += "{2} {0:^{1}}{2}\n".format(line, self.ROW_LENGTH-4,
                                                     symbol)
            return result
        return outer_row() + inner_row() + outer_row()
