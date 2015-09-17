Comment Banner
==============

Add a fancy *-box to each selection in Sublime Text. The box fits in 80
chars including the language dependend comment symbol.
    - supports multi line selection
    - supports multi cursor selection

The default hotkey is The default hotkey is <kbd>alt</kbd> <kbd>shift</kbd> <kbd>b</kbd>

Usage
-------

Select the text you like to box.

Type the shortcut.


Examples
----------

	test

	<select the word test>
	<press hotkey>

	result:

	********
	* test *
	********


Known Issues
-------
- lines that contain more than 76 chars to do not wrap automatically. This will
  be added in a later version.
- the comment boxes aren't formatted correctly for HTML-files. This problem
  occurs because of the length of the comment tag. You can easily fix it
  manually. I'm assuming this plugin isn't very useful in HTML. 
