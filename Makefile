.SUFFIXES: .md .html .pdf
.PRECIOUS: %.pdf %.html
.PRECIOUS: 

.md.html: 
	pandoc --toc --mathjax=js/MathJax.js\
          --template=impress-template.html\
          -V impress-url=impress.js -s -t html5\
          -f markdown --section-divs -o $@ $<

