all: stamp

stamp:
	touch $(CURDIR)/stamp

clean:
	rm -f $(CURDIR)/stamp

install:
	install -d $(DESTDIR)/usr/bin
	install $(CURDIR)/usr/share/bin/reicast $(DESTDIR)/usr/bin
	cp -r $(CURDIR)/usr/share $(DESTDIR)/usr/share

uninstall:
	rm $(DESTDIR)/usr/bin/reicast
	rm -rf $(DESTDIR)/usr/share/reicast