---
layout: computing
title: Computing - Text Editors
---

# Introduction to Text Editors for Young Programmers

Text is the raw material of the craft of programming.  You should become good at manipulating text.  The first thing you should do is pick a good cross-platform text editor and learn it well.  If you haven't already done so, this guide will help you choose one.  The next thing you should do is learn regular expressions, and the next thing after that is learn UNIX and one of its command shells, probably bash.

## Choosing a text editor

![http://xkcd.com/378/](http://imgs.xkcd.com/comics/real_programmers.png)


I used [Emacs](http://www.gnu.org/software/emacs/) for years, then tried [Sublime Text](http://www.sublimetext.com/) and [Atom](https://atom.io/) for class demonstrations, then switched back to Emacs.  I've also tried [Vim](http://www.vim.org/) and know basic vi, but nothing beats Emacs.  If you can't get used to Emacs or Vim, Atom or SublimeText are good choices. [Atom](https://atom.io/)'s user interface is almost a complete clone of [Sublime Text](http://www.sublimetext.com/), which is a good thing, but [Atom](https://atom.io/) uses much different technology, and is free and open source. However, Atom isn't the best choice for a data scientist becuase of its [inability to handle large files](https://github.com/atom/atom/issues/307).

Many people who insist on using Windows like [Notepad++](http://notepad-plus-plus.org/), but [Atom](https://atom.io/) and [Sublime Text](http://www.sublimetext.com/) are much better. If you are a computer science major you will use Unix during your studies, and if you're currently a Windows user you will almost certainly switch to a Unix (like Linux or Mac OS X) for your personal computing after learning more about computing.  So get in the habit of strongly preferring cross-platform software and open standards. (You should never use Microsoft Office, for example, because doing so locks *your* data in a data format owned by someone else and greatly reduces your flexibility. You will gain an appreciation for the power of plain text in this class.)

If you're going to get a computer science or engineering degree, you should learn [Emacs](http://www.gnu.org/software/emacs/) or [Vim](http://www.vim.org/), because they can be used in a terminal and are available on every UNIX platform, Windows, and Mac. [Emacs](http://www.gnu.org/software/emacs/) is the most powerful editor in existence, but it has a steep learning curve.

### **Recommendation for new programmers**: [Sublime Text](sublime.html)

## TABS Versus Spaces

![https://www.emacswiki.org/emacs/TabsSpacesBoth](../images/TabsSpacesBoth.png)

Never use TABs in source code.  Always indent with spaces.  The traditional meaning of TAB is to move the cursor to the next multiple of tab width (8 by the Java spec).  If you adopt, as most programming teams do, the convention of using spaces for all indentation and alignment (no TAB characters anywhere), then "tabbing" means inserting the required number of spaces to get to a multiple of tab width.  Since the Java code convention doesn't specify whether TAB characters or spaces are used for indentation, and that indentation should be 4 spaces, and that tabs be set every 8 spaces, it allows for an absurd case where a programmer using a feature-poor editor would be forced to hit the space bar 4 times when indenting to the first level of indentation.  Of course modern editors take care of these sorts of details, but most programmers completely eschew TAB characters to avoid such issues and to ensure that code looks consistent in any editor or display no matter how the tabs are set.  And most programmers set their editors to insert spaces for tabs.  Jamie Zawinski, a famous Emacs, Mozilla and Netscape hacker, has an informative write-up here: [http://www.jwz.org/doc/tabs-vs-spaces.html](http://www.jwz.org/doc/tabs-vs-spaces.html)

## Customizing your text editor

Having a go-to text editor improves your productivity in part because you can set up your editor with your preferred defaults.  Customization is important because many text editors and IDEs are configured with bad defaults.  Good programmers insist on writing code that is clear and consistently formatted.  Having a well-configured text editor helps you do that. At a minimum you should configure your text editor to:

- Indent with spaces instead of TABs
- Set indent (tab) width to 4
- Trim trailing white space at the end of lines
- Add a newline character to the end of files

We suggest that you also:

- Show a visual ruler at 80 columns
- Show line numbers
- Wrap lines at word boundaries (at 80 characters)
- Bind a key combination to automatically indent lines according to the guidelines for whatever language you're editing
- Bind a key to "go to" a specified line number

Visit one of the following pages to see how to customize your editors:

- [Emacs](emacs.html)
- [Sublime Text](sublime.html)


### Customizing Atom

First, be sure to familiarize yourself with basic Atom usage.  The [Getting Started](https://atom.io/docs/v0.124.0/getting-started) guide is enough to make you quite proficient.
In Atom Preferences, make sure the following are checked:

  - _Show Indent Guide_ draws a vertical line at your preferred line length column in editors.  Preferred line length should be set to 80.
  - _Show Invisibles_ draws greyed-out characters for spaces, TABs, hard returns.
  - _Show Line Numbers_ displays line numbers in the left gutter in editors.  Personal preference, but I find it useful.
  - _Soft Tabs_ causes the editor to insert spaces instead of TAB characters when you hit the TAB key.
  - _Soft Wrap_ wraps lines visually on word boundaries.  Together with _Show Line Numbers_ you get readable text and can still easily tell long single lines.
  - _Soft Wrap at Preferred Line Length_ wraps lines visually on word boundaries at your preferred line length.
