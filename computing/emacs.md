---
layout: computing
title: Computing - Emacs
---

# Emacs

Emacs is the most powerful editor in existence. I don't say this as a joke. Emacs has a learning curve that you may not want to climb while you're also learning a new programming language, but I highly recommend taking the time to get started with Emacs the next time you have a break from school. Here are a few good resources:

- [A Guided Tour of Emacs](https://www.gnu.org/software/emacs/tour/)
- [Emacs Tutorial Series](https://mickael.kerjean.me/2017/03/18/emacs-tutorial-series-episode-0/)
- [One-Page Emacs Tutorial for Beginners](http://sachachua.com/blog/2013/05/how-to-learn-emacs-a-hand-drawn-one-pager-for-beginners/)
- [Emacs Rocks](http://emacsrocks.com/)
- [Tao of Emacs](http://www.howardism.org/Technical/Emacs/tao-of-emacs.html)

## Customizing Emacs

My [dotfiles](https://github.com/csimpkins/dotfiles) will give you a big head start on your Emacs configuration and your general Mac OS X and Ubuntu Linux configuration. If you're new to Emacs and don't want to bother with a more complex Emacs configuration, put the folloiwng in your `~/.emacs` or `~/.emacs.d/init.el` to cover the minumum we recommend and a little more:

```sh
(set-face-attribute 'default nil :height 140)
(setq-default indent-tabs-mode nil)
(add-hook 'before-save-hook 'delete-trailing-whitespace)
(setq-default visible-bell 1)
(setq-default show-paren-mode 1)
(if window-system (tool-bar-mode 0))
(if (boundp 'aquamacs-version) (tabbar-mode 0))
(set-scroll-bar-mode 'right)
(add-hook 'text-mode-hook 'turn-on-visual-line-mode)
(setq-default visual-line-fringe-indicators '(nil nil))
(setq-default word-wrap t)
(setq-default column-number-mode t)
(delete-selection-mode 1)
(setq-default ispell-program-name "/usr/local/bin/ispell")

;; UTF-8 everywhere
(prefer-coding-system 'utf-8)
(set-language-environment 'utf-8)
(set-default-coding-systems 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-selection-coding-system 'utf-8)

;; linum-mode everywhere, except where it doesn't belong
(require 'linum)
(setq-default linum-format "%4d ")
(setq linum-disabled-modes-list '(eshell-mode
                                  wl-summary-mode
                                  compilation-mode
                                  dired-mode
                                  speedbar-mode
                                  doc-view-mode))
(defun linum-on ()
  (unless (or (minibufferp)
              (member major-mode linum-disabled-modes-list)
            (and (not (eq (buffer-name) "*scratch*"))
                 (string-match "*" (buffer-name))))
    (linum-mode 1)))
(global-linum-mode 1)
(setq linum-eager nil)

;; Keybindings
(global-set-key (kbd "M-j") 'join-line)
(global-set-key (kbd "M-g") 'goto-line)

;; From http://www.emacswiki.org/emacs/SmoothScrolling
;; Scroll one line at a time (less "jumpy" than defaults)
(setq-default mouse-wheel-scroll-amount '(1 ((shift) . 1)))
(setq-default mouse-wheel-progressive-speed nil) ;; don't accelerate scrolling
(setq-default mouse-wheel-follow-mouse 't) ;; scroll window under mouse
(setq-default scroll-step 1) ;; keyboard scroll one line at a time

;; Account for size of gutter and fringes
(add-to-list 'initial-frame-alist '(width . 88))
(add-to-list 'default-frame-alist '(width . 88))
```
