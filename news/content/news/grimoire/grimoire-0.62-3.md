title: Stable-0.62-3 released
author: stealth
category: news
date: 2016-04-02
tags: [grimoire]
---
Stable grimoire version 0.62-3 has been released!

After 11 months of polishing we're pleased to announce yet another security update for 0.62 stable branch. This will be one of the latest updates in the series before we go with 0.63, which will bring us GCC 5 and merged xorg-modular grimoire.

But this one is here to fix recent loud security bugs in glibc, openssl, openssh, git, wpa_supplicant, graphite2, ntp, and several others for those who go stable.  
The release also includes all the work related to our bugzilla spell (and all its dependent Perl modules) update.

The tarballs have been signed and uploaded to our server and will be propogating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
Eric Sandall (5):
      smgl-logo-0.2-for-2.6.31.patch: Add support for Linux 4.0.x
      nfs-utils: idmapd support requires DNOTIFY enabled in the kernel.
      ffmpeg-svn: Add for checking dependent libraries for all udpates as SVN is unversioned.
      nmap: ncat will not build against lua, only lua51
      lm_sensors: Added a mirror as lm-sensors.org has been down for a month

Florian Franzmann (20):
      crypto/nss: version 3.18
      devel/git: version 2.3.2
      devel/git: version 2.3.3
      devel/git: version 2.3.4
      devel/git: version 2.3.5
      devel/git: fix hash of html docs
      devel/git: version 2.5.2
      x11-toolkits/qt4: fix build with gcc 5
      crypto/openssl: version 1.0.1p, security update
      libs/libguess: depend on libmowgli
      kernels/linux: version 4.2
      kernels/linux: fix build of nvidia_driver
      chat-libs/loudmouth: fix build error due to missing space in CFLAGS
      graphics/nitrogen: fix LDFLAGS
      devel/perl: version 5.20.2
      devel/git: version 2.7.3
      devel/git: version 2.7.4
      crypto/openssl: version 1.0.2f, security update
      libs/glibc: fix CVE-2015-7547
      chat-im/licq: fix build error due to failed tests

Ismael Luceno (10):
      git 2.4.1
      git 2.4.3
      git 2.4.4
      git 2.4.5
      gitk: spell deprecated, part of git since long ago
      ntp 4.2.8p2, SECURITY_PATCH++
      lha: Fix installation
      wpa_supplicant: Internal TLS implementation depends on libtommath
      make: Add patch to fix segfault when calling make without arguments
      graphite2 1.3.3

Jeremy Blosser (1):
      openvpn: update init script to handle a symlinked config dir

Ladislav Hagara (53):
      linux 4.0.2
      nss 3.18.1
      wireshark 1.12.5, SECURITY_PATCH=53
      linux 4.0.3
      e2fsprogs 1.42.13, SECURITY_PATCH=1, CVE-2015-1572
      libssh 0.7.0, SECURITY_PATCH=4, CVE-2015-3146
      git 2.4.6
      git 2.6.0
      qt4 4.8.7, SECURITY_PATCH=7
      linux 4.0.5
      openssl 0.9.8zg, 1.0.1n, SECURITY_PATCH++
      wireshark 1.12.6, SECURITY_PATCH=54
      linux 4.1.0
      linux 4.1.1
      openssh 6.8p1
      openssh 6.9p1, SECURITY_PATCH=8
      nss 3.19.2
      firefox 39.0, SECURITY_PATCH=86
      openssl 1.0.1o
      linux 4.1.2
      sqlite: SQLITE_ENABLE_DBSTAT_VTAB option added
      linux 4.1.3
      linux 4.1.4
      firefox 40.0, SECURITY_PATCH=87
      wireshark 1.12.7, SECURITY_PATCH=55
      linux 4.1.5
      linux 4.1.6
      libgcrypt 1.6.4, SECURITY_PATCH=4
      firefox 40.0.2
      firefox 40.0.3, SECURITY_PATCH=88
      linux 4.2.1
      firefox 41.0, SECURITY_PATCH=89
      linux 4.2.2
      linux 4.2.3
      linux 4.2.4
      linux 4.2.5
      firefox 41.0.1
      linux 4.3.1
      linux 4.3.2
      linux 4.3.3
      openssh 7.0p1
      openssh 7.1p1
      openssh 7.1p2, SECURITY_PATCH=9, CVE-2016-0777 and CVE-2016-0778
      openssh 7.2p1
      libgcrypt 1.6.5, SECURITY_PATCH=5
      linux 4.4.1
      linux 4.4.2
      linux 4.4.3
      linux 4.4.4
      linux 4.4.5
      linux 4.5
      openssl 1.0.2g, SECURITY_PATCH=32
      encfs 1.8, Google Code -> GitHub

Pavel Vinogradov (29):
      libs/pcre: switched to gcc with CXX in *SUB_DEPENDS
      ftp/curl: version 7.41.0
      ftp/curl: version 7.42.1, SECURITY_PATCH++
      http/firefox: version 38.0, SECURITY_PATCH++
      http/firefox: version 38.0.1
      kernels/linux: version 4.0.4
      kernels/linux/HISTORY: fixed typo
      libs/pcre: switched to gcc with CXX in *SUB_DEPENDS
      devel/git: version 2.4.0
      http/firefox: version 38.0.5
      database/sqlite: version 3.8.9.0
      database/sqlite: version 3.8.10.1
      database/sqlite: version 3.8.10.2
      utils/grep: version 2.22, SECURITY_PATCH++
      kernels/linux: version 4.3
      http/firefox: version 42.0, SECURITY_PATCH++
      libs/nspr: version 4.10.10
      crypto/nss: updated 3.19 branch to 3.19.4
      libs/glibc: version 2.22, SECURITY_PATCH++
      ruby-raa/ruby-2.2: added patch to detect SSLv3 methods in open/libressl
      libs/boost: added patch to check for SSLv3 methods in system open/libressl
      devel/git: version 2.6.4
      devel/git: version 2.7.0
      kernels/linux: version 4.4
      crypto/openssh: version 7.2p2, SECURITY_PATCH++
      crypto/nettle: version 3.1
      graphics-libs/graphite2: version 1.3.5, SECURITY_PATCH++
      libs/glibc: version 2.23, SECURITY_PATCHH++
      python-pypi/django: version 1.9.2, SECURITY_PATCH++

Remko van der Vossen (10):
      glibc: support kernel headers 4.x
      kbd: make check dependency optional
      dspam: fix typo
      openwebmail: fix typo
      grub2: no such thing as NORMAL_COLOR
      wicd: no such thing as NORMAL_COLOR
      php4: no such thing as NORMAL_COLOR
      gnustep-make: no such thing as WARNING_COLOR
      maradns: no such thing as WARNING_COLOR
      nmap: no such thing as WARNING_COLOR

Thomas Orgis (21):
      wpa_supplicant: bump tp 2.4
      wpa_supplicant: add patch for that buffer overflow
      mtpfs: bump to 1.1 (old source gone)
      valgrind: make it build with current kernel and boost
      firefox: fixup of debugging/stripping and switch for the humongous SDK binaries,              also preferring -Os now to prevent frequent segfauls
      wvstreams: fix build again
      wvstreams: avoid crash with modern gcc
      wvdial: build fix (disable as-needed), sync compiler flags with wvstreams
      event: version 1.24 (builds with perl-5.22)
      event: use PERL_CPAN_URL
      wpa_supplicant: update to 2.5, fix nl80211 (SECURITY_PATCH++, as always)
      git: mark the current version as security update
      ca-certifcates: update to 20160104
      nettle: needs UP_TRIGGERS for incompatible upgrades
      valgrind: version 3.11 (needed for glibc-2.22)
      ca-certificates: make openssl-using apps (like wget) happy by refreshing those hash symlinks
      flickcurl: update to 1.26, fixing build against libcurl at that
      xdvik: build fix
      jamin: build fix
      liblrdf: fix with current raptor (dependent spells break otherwise)
      id3lib: fix patch download URL

Treeve Jelbert (58):
      clamav - extra depends
      clamav  0.98.7  SECURITY FIXES
      krb5-1.13.2  SECURITY FIX
      ruby-2.2-2.2.2 SECURITY FIX
      pcre: => 8.37
      git: => 2.5.0
      tzdata: => 2015d
      cups-2.0.3 SECURITY FIX
      ca-certificates: => 20150426
      librsvg2 - not depend atk, expat
      openssl: => 1.0.2d
      policykit-0.113 SECURITY FIX
      cups-filters: => 1.0.67
      cups-filters: => 1.0.68
      cups-filters: => 1.0.69
      cups-filters-1.0.71 SECURITY FIX
      cups-filters: => 1.0.73
      cups-filters: => 1.0.74
      cups-filters: => 1.0.76
      cups-filters: => 1.1.0
      cups-filters-1.2.0  SECURITY FIX
      cups-filters-1.5.0 SECURITY FIX
      libressl-2.2.1 SECURITY FIX
      libxml2-2.9.2 SECURITY FIX
      sqlite: => 3.8.11.1
      pixman: => 0.24.0
      pixman: => 0.24.2
      pixman: => 0.24.4
      pixman: => 0.26.0
      pixman: => 0.26.2
      libvdpau: => 0.9
      libvdpau: => 1.0
      libvdpau: => 1.1
      libvdpau-1.1.1 SECURITY FIX
      ruby-2.2.3 - SECURITY FIX
      tzdata: => 2015g
      ca-certificates - fix for libressl
      curl-7.45.0 SECURITY FIX
      libxml2-2.9.3 SECURITY FIXES +++
      libsndfile-1.0.26 SECURITY FIX
      ruby-2.2-2.2.4 SECURITY FIX
      git: => 2.6.3
      krb5-1.14 SECURITY FIX
      libgphoto2 - improve UP_TRIGGERS
      giflib5: => 5.1.1
      giflib5-5.1.2 SECURITY FIX
      libzip-1.1 SECURITY FIX
      curl-7.47.0 SECURITY FIX
      nettle: => 3.1.1
      nettle-3.2  SSECURITY FIX
      curl - tweak
      libssh: => 0.7.2
      libssh-0.7.3 SECURITY FIX
      libssh2: => 1.6.0
      libssh2-1.7.0 - SECURITY FIX
      libotr: => 4.1.0
      libotr-4.1.1 - SECURITY FIX
      krb5-1.14.1 SECURITY FIX

Vlad Glagolev (170):
      exporter-tiny: new spell, exporter with the features of Sub::Exporter
      list-moreutils: => 0.410
      try-tiny: => 0.22
      module-runtime: => 0.014
      module-implementation: => 0.09
      params-validate: => 1.18
      class-singleton: => 1.5
      list-allutils: new spell, combines List::Util and List::MoreUtils in one bite-sized package
      datetime-timezone: => 1.88
      timedate: => 2.30
      datetime: => 1.18
      datetime: => 1.18
      test-leaktrace: new spell, traces memory leaks
      template-toolkit: => 2.26
      module-pluggable: => 5.1
      email-date-format: => 1.005
      email-simple: => 2.206
      email-address: => 1.907
      mro-compat: new spell, mro::* interface compatibility for Perls < 5.9.5
      email-abstract: => 3.008
      email-send: => 2.201
      mime-types: => 2.09
      email-messageid: => 1.405
      email-mime-contenttype: => 1.018
      email-mime-encodings: => 1.315
      email-mime: => 1.929
      perl-cgi: => 4.15
      email-mime-modifier: spell deprecated, it's a part of email-mime now
      bugzilla: => 4.0.18 [security]
      bugzilla: corrected a typo in CONFIGURE
      mailtools: => 2.14
      weakref: spell deprecated, it's a part of perl now
      mail-internet: spell deprecated, it's a part of mailtools now
      xml-twig: => 3.49
      weakref: added missing CONFLICTS
      mail-internet: added missing CONFLICTS
      mime-tools: => 5.506
      email-reply: => 1.203
      email-mime-attachment-stripper: => 1.317
      mdp: => 0.7.4
      email-mime-modifier: spell deprecated, it's a part of email-mime now
      linux: => 3.12.42 (lts)
      Revert "xml-parser-expat: => 2.42_01"
      xml-parser-expat: => 2.44
      weakref: spell deprecated, it's a part of perl now
      mail-internet: spell deprecated, it's a part of mailtools now
      mailtools: => 2.14
      weakref: added missing CONFLICTS
      mail-internet: added missing CONFLICTS
      util-linux: fixed a failure in PREPARE for the boxes without util-linux installed on them, ok flux@
      libmpc: fixed install phase in dispel-less cases, ok flux@
      linux: => 3.10.77 (lts)
      linux: => 3.14.41 (lts)
      linux: => 3.18.13 (lts)
      linux: => 3.19.7 (stable)
      mariadb: => 5.5.42
      mariadb: => 5.5.43 [security]
      bitlbee: => 3.4
      lzma-utils: spell deprecated, in favour of xz-utils, ok flux@
      tar: LZMA -> xz-utils
      gzip: LZMA -> xz-utils
      automake: LZMA -> xz-utils
      linux: LZMA -> xz-utils
      xinetd: security update
      xinetd: updated source urls
      rpm2targz: LZMA -> xz-utils
      gnutls: LZMA -> xz-utils
      gdk-pixbuf2: LZMA -> xz-utils
      xen: => 4.4.2 [security]
      linux: => 3.19.8 (eol)
      linux: => 3.14.42 (lts)
      linux: => 3.10.78 (lts)
      linux: => 3.2.69 (lts)
      mpd: updated dependencies
      gnupg: fixed debug info output via official patch
      php: => 5.4.41 (stable)
      linux: => 3.10.79 (stable)
      linux: => 3.14.43 (stable)
      bbswitch: build/install for a new kernel
      mailx: security + compatibility update
      hplip: => 3.15.4
      dovecot: security update
      postgresql: => 9.3.7 [security]
      Revert "libs/pcre: switched to gcc with CXX in *SUB_DEPENDS"
      pcre: that was a security update
      patchreader: => 0.9.6
      math-random-isaac: new spell, Perl interface to the ISAAC PRNG algorithm
      bugzilla: => 4.2.15 [security]
      bugzilla: => 4.2.16 [security]
      git: => 2.6.1 [security]
      proxychains-ng: => 4.9 [security]
      freetype2: fixed dependencies
      harfbuzz: fixed dependencies
      pillow: fixed build with system zlib
      glibc: added missing required dependency -- binutils
      monit: => 5.12
      monit: => 5.12.2
      monit: => 5.13
      cyrus-sasl: => 2.1.26 [security]
      cyrus-sasl: extended init script by adding custom arguments variable
      openssl: => 1.0.2e (1.0), 0.9.8zh (0.9)
      ltrace: fixed source url & website
      sqlite: => 3.8.8.3
      sqlite: fixed multijob build
      pixman: complete header workaround
      lighttpd: => 1.4.36 [security]
      linux: => 3.10.84 (lts)
      django: => 1.8.3 (stable), 1.4.21 (legacy) [security]
      genshi: dropped obsolete gpg sig
      linux: => 3.10.85 (lts)
      libev: => 4.20 + avoid conflict with libevent
      linux: => 3.2.71 (lts)
      linux: => 3.4.108 (lts)
      linux: => 3.10.87 (lts)
      trac: => 0.12.7 [security]
      linux: => 3.4.109 (lts)
      linux: => 3.10.90 (lts)
      linux: => 3.12.49 (lts)
      ruby-1.9: conflicts rake
      ruby-json: new spell, Ruby extension for JSON
      rubygem-json: deprecate the spell in favour of ruby-json
      puppet: rubygem-json -> ruby-json
      ircd-ratbox: => 3.0.9 [security]
      speedtest-cli: => 0.3.2
      ulimits: => 0.3.1
      ulimits: => 0.3.2
      ulimits: fixed a typo in HISTORY
      wireshark: => 1.12.8 [security]
      gdk-pixbuf2: security update
      bzip2: added missing symlink
      libjpeg-turbo: fixed docs and examples dir
      Revert "ejabberd: depends SSL"
      ejabberd: openssl -> SSL
      Revert "licq: depends SSL"
      licq: openssl -> SSL
      Revert "psi: depends SSL"
      Revert "fingerprint: depends SSL"
      Revert "xchat-gnome: depends SSL"
      xchat-gnome: openssl -> SSL
      Revert "znc: depends SSL"
      znc: security update, openssl -> SSL
      Revert "ptlib: depends SSL"
      ptlib: openssl -> SSL
      Revert "pwlib: depends SSL"
      Revert "proftpd: depends SSL"
      proftpd: openssl -> SSL
      Revert "libzdb: depends SSL"
      libzdb: openssl -> SSL
      Revert "gnustep-base: depends SSL"
      gnustep-base: openssl -> SSL
      Revert "libircclient: depends SSL"
      libircclient: openssl -> SSL
      libircclient: moved to chat-libs
      Revert "ecore: depends SSL"
      ecore: openssl -> SSL
      Revert "eet: depends SSL"
      eet: openssl -> SSL
      Revert "tpm-tools: depends SSL"
      perl: incremented missed security patch
      epdfview: added fixes from BLFS; fixed build with recent poppler
      unifont: => 8.0.01
      encfs: => 1.8.1
      valgrind: added glibc dependency
      Revert "libs/glibc: version 2.23, SECURITY_PATCHH++"
      linux: => 4.1.20 (lts)
      portaudio19: fixed multijob build
      talloc: added missing dependency
      gst-ffmpeg: use check_tmp_noexec()
      gst-ffmpeg: don't do useless doc'ing
      VERSION: 0.62-3
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-2..stable-0.62-3`
