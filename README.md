This is a script to convert the website www.chesstactics.org into an ebook.

    python generate-markdown.py > book.md
    pandoc book.md -o book.epub --toc --toc-depth=3 --epub-chapter-level=3 --epub-cover-image=cover.jpg

Many thanks to Ward Farnsworth for making his book available free of charge
under a permissive license.

Predator at the Chessboard is licensed under CC BY-NC-ND 2.5:
https://creativecommons.org/licenses/by-nc-nd/2.5/

![screenshot](https://raw.githubusercontent.com/nathanj/predator-epub/master/screenshot.jpg)
