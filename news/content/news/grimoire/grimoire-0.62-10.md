title: Stable-0.62-10 released
author: stealth
category: news
date: 2017-06-10
tags: [grimoire]
---
Stable grimoire version 0.62-10 has been released!

It is a regular security update for the 0.62 stable grimoire.

The tarballs have been signed and uploaded to our master server and will be propagating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
David C. Haley (1):
      archive/cabextract: => 1.6, SECURITY_PATCH++

Eric Sandall (1):
      rpcbind: Updated to 0.2.3

Florian Franzmann (10):
      graphics-libs/tiff: version 4.0.6
      devel/python: create python symlink
      perl-cpan/digest-hmac: version 1.03
      ftp/curl: version 7.52.0, security update
      crypto/openssl: version 1.0.2k, security update
      archive-libs/libarchive: version 3.3.0, security update
      ftp/curl: version 7.53.0, security update
      archive-libs/libarchive: version 3.3.1, security update
      ftp/curl: version 7.53.1
      libs/libtasn1: version 4.10

Ismael Luceno (2):
      bitlbee 3.4.2
      FUNCTIONS: Add a function for applying patches

Pavel Vinogradov (12):
      devel/python: version 2.7.10
      devel/python: version 2.7.11
      devel/python: version 2.7.12, SECURITY_PATCH++
      ftp/curl: version 7.52.1, SECURITY_PATCH++
      crypto/openssh: version 7.4p1, SECURITY_PATCH++
      chat-im/pidgin: version 2.12.0, SECURITY_PATCH
      ftp/curl: version 7.54.0, SECURITY_PATCH++
      graphics-libs/tiff: version 4.0.8, SECURITY_PATCH++
      utils/sudo: version 1.8.20
      utils/sudo: version 1.8.20p1, SECURITY_PATCH++
      utils/sudo: version 1.8.20p2
      libs/libtasn1: version 4.9

Remko van der Vossen (1):
      expat: 2.2.0 - fixes CVE-2013-0340, CVE-2015-1283

Treeve Jelbert (9):
      tiff: => 4.0.4
      setuptools: => 14.3.1
      setuptools: => 16.0
      setuptools: => 18.0.1
      libsrtp: => 1.4.4
      /libsrtp-1.5.4 - SECURITY FIX
      audiofile - SECURITY FIX
      miniupnpc: => 2.0.20170509  SECURITY FIX
      libtasn1: => 4.12   SECURITY FIX

Vlad Glagolev (27):
      tiff: => 4.0.7 [security]
      tiff: added LZMA dep
      Revert "python: fixed build with libressl"
      lockfile: => 0.12.2
      cadaver: fixed building with neon 0.30
      moved gschemas.compiled from volatiles to excluded
      Revert "giflib: depends libice, libsm, libx11"
      giflib: added libx11 optional dependency
      zlib: added SF mirror
      Revert "fontconfig: added missing dependencies"
      fontconfig: added dependencies coming from freetype2 linking
      pil: use UP_TRIGGERS
      pillow: conflicts with pil
      Revert "newsyslog: added offset patch"
      rsync: correct reload() handling in the init script
      oidentd: use init script config
      vsftpd: made libcap optional dependency
      libtirpc: security update
      rpcbind: security update
      jmk-x11-fonts: updated source url; fixed build with protected /tmp
      bitlbee: => 3.5.1 [security]
      redis: switch to login environment
      libvpx: added missing dependency (which)
      postgresql: => 9.4.12 [security]
      audiofile: updated source url & website
      libarchive: fixed build with libressl
      VERSION: 0.62-10
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-9..stable-0.62-10`
