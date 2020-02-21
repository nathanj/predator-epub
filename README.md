This is a script to convert the website www.chesstactics.org into an ebook.

    python generate-markdown.py > book.md
    pandoc book.md -o book.epub --toc --toc-depth=3 --epub-chapter-level=3 --epub-cover-image=cover.jpg
