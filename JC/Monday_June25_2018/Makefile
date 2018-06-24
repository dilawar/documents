all : persentation


demo : ./hopfield_demo.py
	python $<


persentation : ./presentation.pdf


./presentation.pdf : ./presentation.md
	pandoc -t beamer $< -o $@
