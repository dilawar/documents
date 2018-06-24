all : persentation


demo : ./hopfield_demo.py
	python $<


persentation : ./presentation.pdf


./presentation.pdf : ./presentation.tex
	latexmk -pdf $<
