PREFIX ?= /usr/local
DOCDIR ?= $(PREFIX)/share/2048-py/doc

all:
	@echo Run \'make install\' to install 2048-py
	@echo Run \'make uninstall\' to uninstall 2048-py

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p main.py $(DESTDIR)$(PREFIX)/bin/2048-py
	@mkdir -p $(DESTDIR)$(DOCDIR)
	@cp -p README.md $(DESTDIR)$(DOCDIR)
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/2048-py

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/2048-py
	@rm -rf $(DESTDIR)$(DOCDIR)
