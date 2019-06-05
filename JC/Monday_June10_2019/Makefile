all : presentation.pdf


presentation.pdf : presentation.pandoc 
	pandoc -t beamer $< -o $@
