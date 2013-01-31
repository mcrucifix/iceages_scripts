clean:
	rm -f *.aux *.Rout

RCMD=R CMD BATCH 
PYCMD=python 
TEXCMD=pdflatex

PYDIR=Py
RDIR=R

astro.pdf: $(PYDIR)/astro.py
	$(PYCMD) $(PYDIR)/astro.py

vdpfit.pdf: $(RDIR)/vdpfit.R
	$(RCMD) $(RDIR)/vdpfit.R


figure1.pdf: $(RDIR)/figure1.R
	$(RCMD) $(RDIR)/figure1.R

pullback_others.pdf: $(PYDIR)/pullback_others.py
	$(PYCMD) $(PYDIR)/pullback_others.py


card_others.pdf: $(PYDIR)/card_others.py
	$(PYCMD) $(PYDIR)/card_others.py


card_others_sup.pdf: $(PYDIR)/card_others_sup.py
	$(PYCMD) $(PYDIR)/card_others_sup.py

strob_periodic.pdf: $(PYDIR)/strob.py
	$(PYCMD) $(PYDIR)/strob.py


