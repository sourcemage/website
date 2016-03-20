title: Stable-0.62-1 released
author: stealth
category: news
date: 2015-03-13
tags: [grimoire]
---
Stable grimoire version 0.62-1 has been released!

It contains fixes for [openssl](https://www.openssl.org) → [libressl](http://www.libressl.org) migration as well as several security updates.  
As per [this post](http://lists.ibiblio.org/pipermail/sm-discuss/2015-March/021938.html), the SSL implementations are not fully compatible and interchangable, so if you find any issue about it, feel free to report back – the fixes will be included in the next release.

The tarballs have been signed and uploaded to our server and will be propogating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.


Following updates were integrated[^0]:

```
Eric Sandall (5):
      puppet: Fixed to match renamed tarball
      puppet: Add puppet-master init.d script
      rubygem-json: Added Ruby extension for JSON
      puppet: Added init script for puppet agent
      puppet: Runtime dependency on rubygem-json

Florian Franzmann (1):
      audio-soft/vorbis-tools: fix WEB_SITE

Ismael Luceno (2):
      putty 0.64, SECURITY_PATCH++
      wget: Fix linking issues

Ladislav Hagara (2):
      wireshark 1.12.4, SECURITY_PATCH=52
      wget 1.16.2

Pavel Vinogradov (8):
      http/webkitgtk: version 2.4.8, SECURITY_PATCH++
      graphics-libs/libvisio: added dependencies on boost, icu and librevenge
      chat-im/pidgin-libnotify: added fix to build against current libnotify
      libs/nspr: version 4.10.8
      crypto/nss: version 3.17.4
      http/firefox: version 36.0, SECURITY_PATCH++
      http/firefox: version 36.0.1, SECURITY_PATCH++
      http/firefox: yet another fix of LDFLAGS in BUILD

Thomas Orgis (1):
      qjackctl: fix build when old qmake is around

Treeve Jelbert (2):
      libressl: => 2.1.3
      krb5-1.13.1 SECURITY FIX

Vlad Glagolev (22):
      avfs: configuration fixes
      qt4: fixed syntax error in DEPENDS
      libressl: => 2.1.4
      Revert "cadaver: depends SSL"
      cadaver: use SSL provider
      libressl: added SOURCE2 for gpg signature
      libressl: PREPARE -> UP_TRIGGERS
      stunnel: fixed build with libressl
      libressl: post-update fixes
      pcre: re-enabled build of static libraries
      socat: fixed build with LibreSSL
      python: fixed build with libressl
      links-twibright: fixed build with libressl
      exim: use SSL provider (build against libressl confirmed)
      pyopenssl: corrected work with libressl
      ldns: added libressl build support
      openssl: added proper upgrading procedure to libressl
      libressl: added proper upgrading procedure from openssl
      tzdata: => 2015a
      wget: => 1.16.3
      seamonkey: => 2.33 [security]
      VERSION: 0.62-1
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-0..stable-0.62-1`
