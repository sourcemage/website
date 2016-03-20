title: Stable-0.62-2 released
author: stealth
category: news
date: 2015-05-02
tags: [grimoire]
---
Stable grimoire version 0.62-2 has been released!

This is mostly a security update accumulated a lot of security fixes including those for Mozilla stuff, Xorg libraries, Nginx, NTP and OpenSSL/LibreSSL.  
It also contains more corrections for 0.61 → 0.62 upgrading path, as well as a brand new [Linux kernel](http://www.kernel.org) **4.0** (thanks to Ladislav "lace" Hagara for it).

The update also introduces our fresh [castfs](/castfs) [0.6.2](/news/castfs-0-6-2/) released recently, and as you may have noticed [Sorcery](/Sorcery) **1.15.4** released several days ago includes one important fix for multiple triggers of a spell, so the recommended update procedure is:

1. `sorcery update`
2. `scribe update stable` (if you're running stable grimoire)
3. `cast -c castfs`
4. `sorcery upgrade`

I'd like to thank Thomas Orgis (sobukus) for helping with this update hard. Really hard.

The tarballs have been signed and uploaded to our server and will be propogating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
Florian Franzmann (9):
      archive/p7zip: version 9.38.1
      devel/python3: install python3 symlink
      net/ntp: remove dead SOURCE_URL
      http/firefox: version 36.0.4
      http/firefox: downgrade sup dependency on nss to 3.17
      add security fixes from LFS
      graphics/lcms: fix CVE-2013-4276
      remove redundant PATCHLEVEL
      remove redundant PATCH_LEVEL

Ismael Luceno (4):
      qtiplot: Fix WEB_SITE and trim whitespace
      qtiplot: Fix SOURCE_URL[0]
      tk: Fix TK_SRC_DIR in tkConfig.sh
      idjc: Switch dependency from jack to JACK-DRIVER

Ladislav Hagara (10):
      libpcap 1.7.2
      tcpdump 4.7.3, SECURITY_PATCH=1
      openssl 0.9.8zf, 1.0.1m, SECURITY_PATCH++
      firefox 37.0, SECURITY_PATCH=82
      linux 3.19.1
      linux 3.19.2
      linux 3.19.3
      linux 4.0.0; cast -r linux if you want it
      firefox 37.0.2, SECURITY_PATCH=84
      linux 4.0.1

Pavel Vinogradov (3):
      disk/btrfs-progs: fixed the git branch fetching/updating
      http/firefox: version 37.0.1, SECURITY_PATCH++
      xfce/thunar: version 1.6.6     (cherry picked from commit d848b33ffb95ad658264763a44fd37b6161d10ff)

Sukneet Basuta (1):
      firefox: only disable tests if pgo is not enabled     mozconfig: remove --disable-tests, pgo requires it     Makefile.in-pgo.patch, bug999496_change1f10a8067853.patch: removed, no longer applies

Thomas Orgis (59):
      ntp: bump to 4.2.8p1 for SECURITY
      evolution-data-server: missing depends
      gtkhtml2: missing depends
      harfbuzz: add ICU sub depends
      poppler: gtk+2 -> gtk+3
      webkitgtk3: needs harfbuzz with ICU
      ladspa: as-needed exception
      libgcrypt: enable static lib
      p11-kit: needs libtasn1
      strigi: disable as-needed
      kdelibs4: add docbook-xsl depends (complains violently otherwise)
      p11-kit: depends on libffi, too
      FUNCTIONS: added get_spell_provider_file
      pyqt4: fix build
      dbus-c++: switch to released version 0.9.0 (identical to most recent git head)
      sip: define $PYTHON to make it build
      pyqt4: syntax fix
      sip: today
      libxml2: unified $PYTHON
      dbus: reduce attack surface by not picking up glib for tests during build
      kdepimlibs4: more dependencies
      virtuoso: enforce libiodbc if python (could that be PYTHON?)
      meterbridge: more resolute autotools regeneration, fixing strange erratic build failures
      xz-utils: no conflict with lzip
      thunderbird: bump to 31.2.0
      term-readline-gnu: update to 1.26
      cryptsetup-luks: hotfix for -lpthread
      cryptsetup-luks: no exporting
      thunderbird: missing HISTORY entries
      thunderbird: depend on same nss as firefox
      cairo: disable fragile xlib-xcb
      cairo: add --disable-xlib-xcb properly
      cairo: fix list_add usage (what a shame)
      thunderbird: bump to 31.5.0
      thunderbird: SECURITY_PATH++
      nasm: bump to 2.11.08, fixing syslinux build
      FUNCTIONS: more robust waf_build     (cherry picked from commit 3fd574c7a86894b1c963f8589d1d0b9632f3497e)
      dbus-python: really install for the chosen PYTHON     (cherry picked from commit 7bcb424fc67392c6ee93578842fe4065ddcedf24)
      jack: needs db     (cherry picked from commit 7a3e902773ce9f2279f362a8751cc9e67b5ee06c)
      pyqt4: needs dbus-python     (cherry picked from commit 49b66acfd302cdb27e48ef8517c139403759c92f)
      python: ensure existens of python2 command (as per PEP 394)     (cherry picked from commit 54b9638e12e784ea9b0ff60ea20beabc8ff42d51)
      python3: ensure existens of python3 command (as per PEP 394)     (cherry picked from commit c0c6181c26f6fa125e8344e77b208a75379d52d3)
      guitarix2: use waf_build     (cherry picked from commit b563039e2f5ac93aef082a9a9ba6e6b09c903094)
      timidity: apply patch to make jack output work with alsa sequencer     (cherry picked from commit cbf9c9b800c5df0c56c671feadaca3176120e4f5)
      timidity: completed HISTORY entry     (cherry picked from commit 30fc41cd65363c8f899a1913db66260942becd5e)
      python: add warning about not making it the default pythin     (cherry picked from commit 81d5b7157c0d4b7305c984aec032df210a8b6384)
      python3: warn about making it primary     (cherry picked from commit d717f6c43e1ccf999a69f40c7880c57939231a39)
      python: the word is primary, not default     (cherry picked from commit f6bf58ffc5b1fe777087c9b114d3d66c0de4c0fc)
      basesystem: version 0.9.7, needs pkgconfig     (cherry picked from commit 38f6508461e120526bd6cdc642b1c8ccd4087adc)
      ardour3: optimize!     (cherry picked from commit d95e870c4e44601a9220f7fe493e151e63426eab)
      ardour3 needs CXX
      libtirpc: fix build with libgssglue
      libtirpc: better fix for also making spells using libtirpc work (p.ex. rpcbind)
      libxi: depends libxfixes
      qtbase: conflict with itself, like the others
      libssh: remove broken option for libgcrypt
      samba: install pkgconfig files
      powertop: version 2.7, also fixing build since upstream of old version seems changed
      transcode: fix build by removing leftover SCRIBBLED from previous commit here

Treeve Jelbert (12):
      cups: => 2.0.2
      cups-filters: => 1.0.65
      shared-mime-info: => 1.4
      libssh2: => 1.5.0 SECURITY FIX
      libfakekey - fix build
      randrproto: => 1.4.0
      randrproto: => 1.4.1
      libxrandr: => 1.3.2
      libxrandr: => 1.4.0
      libXrandr-1.4.1 SECURITY FIX
      libxrandr: => 1.4.2
      chrony-1.31.1 SECURITY fix

Vlad Glagolev (170):
      icu: fixed UP_TRIGGERS for correct upgrade
      gnome-icon-theme: added missing gtk+2 dependency
      adwaita-icon-theme: added missing dependencies
      Revert "x11-libs/fontconfig: version 2.11.92"
      Revert "xchat: depends SSL"
      xchat: use SSL provider
      gettext: add glibc-related triggers
      xlockmore: => 5.46, fixed syntax error in CONFIGURE
      gpgme: a branch has nothing to do with GnuPG 2.*, see README
      shared-mime-info: added missing dependency
      Revert "gvfs 1.23.4"
      gvfs: => 1.22.3
      vile: fixed build
      parted: fixed build
      icu: added libicudata to the triggers
      added 911A4C02 public key (Internet Systems Consortium, Inc. (Signing key, 2015-2016) <codesign@isc.org>)
      bind-tools: => 9.10.2
      gajim: added missing suggest dependency -- bind-tools
      enum34: new spell, support for enumerations
      python-cryptography: new spell, Python cryptographic recipes and primitives
      pyopenssl: added missing runtime dependency -- python-cryptography
      icu: added libxml2 and raptor to check for triggering
      icu: corrected sorting in triggers
      libffi: rewritten UP_TRIGGERS
      easytag: removed libffi
      at-spi2-core: removed libffi
      atk: removed libffi
      gdk-pixbuf2: removed libffi
      exo: removed libffi
      eggdbus: removed libffi
      gtk+2: removed libffi
      pango: removed libffi
      Revert "doc/evince: version 3.15.4"
      evince: => 3.14.2
      gtk3-nocsd: new spell, hack to disable gtk+ 3 client side decoration
      klavaro: added missing glib2 dependency
      iproute2: added check triggers for iptables
      libiodbc: added missing dependency -- glib2
      xfce4-panel: added glib2 required dependency
      Revert "gnome-vfs2: depends SSL"
      gnome-vfs2: fixed dependencies
      bpython: added missing dependency
      aubio: added triggers for upgrading
      requests: new spell, Python HTTP for Humans
      volatiles: added fonts.dir/fonts.scale exceptions
      gstopwatch: use LDFLAGS
      libxfont: => 1.4.9 [security]
      guvcview: added missing dependencies
      ipsec-tools: fixed build & added missing dependency
      valgrind: => 3.10.1
      Revert "poppler: gtk+2 -> gtk+3"
      poppler: fixed dependencies
      slim: updated website & source url; added another mirror
      sox: => 14.4.2
      wicd: added missing pytz dependency
      git: fixed resurrection
      seamonkey: => 2.33.1 [security]
      libressl: => 2.1.6 [security]
      fixed build of pppol2tp.so with recent glibc
      seamonkey: corrected build process
      added check_tmp_noexec() to check secured /tmp partitions
      openntpd: => 5.7p4
      added missing space in check_tmp_noexec()
      xxkb: use check_tmp_noexec()
      tightvnc: use check_tmp_noexec()
      ffmpeg: use check_tmp_noexec()
      castfs: => 0.6.2
      castfs: prepare build toolchain for scm branch
      libxfont: added forgotten version change
      xautolock: use check_tmp_noexec()
      zlib: fixed castfs usage
      init.d: fixed castfs usage
      ffmpeg: unforce libcdio-paranoia dependency
      groff: fixed app-defaults directory detection
      btrfs-progs: respect system-wide flags
      fbnews: fix closing parenthesis parsing
      php: fixed build with new freetype2 (legacy/previous branch)
      ruby-1.9: fixed dependencies & flags
      rubygems: conflicts with ruby-1.9
      rrdtool: prevented from installation of broken symlinks which annoys cleanse
      gcc: added missing glib2 dependency
      libffi: added check for glibmm
      gtk-xfce-engine: added missing glib2 dependency
      libgnomeui: added missing glib2 dependency
      libxfcegui4: added missing glib2 dependency
      xfce4-dict: added missing glib2 dependency
      gconf2: added missing glib2 dependency
      gtk-xfce-engine: removed irrelevant HISTORY entry
      kernel.gpg: added C4790F9D public key
      linux: support 3.0 kernels' verification
      freeradius: added init script config
      linux: => 3.0.101 (3.0)
      linux: => 3.2.68 (lts)
      linux: => 3.4.106 (lts)
      linux: => 3.10.73 (lts)
      linux: => 3.12.39 (lts)
      linux: => 3.14.37 (lts)
      linux: => 3.18.10 (lts)
      accel-ppp: => 1.9.0
      ipsec-tools: fixed isakmp ph1 port setting
      Revert "nginx: Update stable to 1.6.2 and devel to 1.7.9"
      nginx: => 1.6.2 (stable), 1.7.11 (devel) [security]
      tor: => 0.2.5.12 [security]
      net-ssleay: => 1.68
      leafpad: accumulated fixes
      bbswitch: => 0.8
      linux: => 3.10.74 (lts)
      linux: => 3.12.40 (lts)
      linux: => 3.14.38 (lts)
      linux: => 3.18.11 (lts)
      linux: => 3.19.4 (stable)
      python-pypi/FUNCTIONS: fixed arguments' passing to the root FUNCTIONS
      pillow: => 2.8.1
      php: => 5.4.40 (stable) [security]
      linux: => 3.10.75 (lts)
      linux: => 3.14.39 (lts)
      linux: => 3.19.5 (lts)
      linux: => 3.4.107 (lts)
      mcelog: => 114
      seamonkey: added ability to build with system icu
      fixed check_tmp_noexec for tmp-less systems
      do not force noexec option in check_tmp_noexec()     (cherry picked from commit f5aaec3e15bbd63e6b21454982a5f353755f2fb6)
      stunnel: => 5.14 [security]
      mksh: => R50e
      mksh: => R50f [security]
      librsvg2: removed libffi     (cherry picked from commit 609291c8571fd8a9683b4f929671e740d5786b94)
      librsvg2:  added a warning about vala dependency making gobject-introspection non-optional     (cherry picked from commit 4e56e866658f3a59dab887d06b5f47559ef085b8)
      at-spi2-atk: removed libffi     (cherry picked from commit f5ce2e77b5b43153e6cc114d74db4881273b61db)
      gnutls: resurrected migration procedure
      siege: updated source url
      ffmpeg: fixed build of legacy branch
      xine-lib: fixed ffmpeg dependency
      Revert "audacious-plugins needs libbinio"
      audacious-plugins: post-update fixes
      nfs-utils: fixed build on lvm-less systems
      libarchive: added missing lzo dependency
      gvfs: added missing optional libarchive dependency
      qemu: fixed /var/run location
      webkitgtk: rollback to 1.10.2 sadly because of incompatible compiler
      webkitgtk3: rollback to 1.10.2 sadly because of incompatible compiler
      webkitgtk: fixed build with bison 3.0
      adwaita-icon-theme: added missing dependencies
      webkitgtk3: fixed build with bison 3.0
      webkitgtk: fixed build with system icu
      webkitgtk3: fixed build with system icu
      libiodbc: patchlevel++
      libgnomeui: added missing libxml2 dependency
      thunar-vfs: added missing glib2 dependency
      xorg-server: fixed build with upgrading of libgcrypt and further upgrades of all crypto libraries (because of missing actual dependencies)
      xorg-server: 1.8 didn't have support for nettle yet
      gvfs: added missing libsecret dependency (required for keyring)
      libgcrypt: added missing trigger for libgnome-keyring
      virtualgl: use SSL provider
      linux: => 3.18.12 (lts)
      iproute2: fixed dependencies
      xorg-server: removed junk of the previous patch
      cherrypy: => 3.7.0
      linux: => 3.19.6 (stable)
      linux: => 3.14.40 (lts)
      linux: => 3.10.76 (lts)
      ucl: build shared library
      upx: post-update fixes
      test-simple: conflicts with modern perl
      test-harness: conflicts with modern perl
      archive-tar: conflicts with modern perl
      linux: => 3.12.41 (lts)
      archive-tar: spell deprecated, it's a part of perl now
      test-harness: spell deprecated, it's a part of perl now
      test-simple: spell deprecated, it's a part of perl now
      VERSION: 0.62-2
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-1..stable-0.62-2`
