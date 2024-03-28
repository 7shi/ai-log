all:

conv:
	for html in *.html; do md=$${html%.html}.md; if [ ! -f $$md ]; then (python ../gemini2md.py $$html > $$md); fi; done
