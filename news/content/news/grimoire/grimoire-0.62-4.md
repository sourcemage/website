title: Stable-0.62-4 released
author: stealth
category: news
date: 2016-04-30
tags: [grimoire]
---
Stable grimoire version 0.62-4 has been released!

It is not that big as the previous one, but still has some important security updates for Git-related parts in Mercurial (because of recently found security issues in Git), NodeJS, GnuTLS stack, NTP, Django, LigHTTPD, PostgreSQL and several others.
It also includes the most recent Linux kernel updates for stable and long-term branches.

The tarballs have been signed and uploaded to our server and will be propogating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
Eric Sandall (2):
      init.d: Allow setting RUN_SIZE
      init.d: Fix RUN_SIZE comment to match reality

Florian Franzmann (4):
      graphics-libs/graphite2: version 1.3.7
      devel/nodejs: remove sub-dependency on openssl 1.0
      libs/libtasn1: version 4.5
      crypto/gnutls: versions 3.3.21

Ismael Luceno (2):
      nodejs 0.10.44, SECURITY_PATCH++
      libtasn1 4.7

Justin Boffemmyer (1):
      lua-forge/luaexpat: updated to 1.3.0

Ladislav Hagara (3):
      libgcrypt SECURITY_PATCH=6
      linux 4.5.2
      libtasn1 4.3

Pavel Vinogradov (2):
      lua-forge/lpeg: version 1.0.0
      kernels/linux: version 4.5.1

Thomas Orgis (1):
      ntp: version 4.2.8p7 (security fixes)

Treeve Jelbert (4):
      libgcrypt: => 1.7.0
      giflib-5.1.4 - SECURITY FIX
      libtasn1: => 4.2
      libtasn1-4.8 -  SECURITY FIX CVE-2016-4008

Vlad Glagolev (42):
      mercurial: => 3.3.2
      mercurial: => 3.3.3
      mercurial: => 3.4
      mercurial: => 3.5
      mercurial: => 3.5.1
      mercurial: => 3.5.2
      mercurial: => 3.6
      mercurial: => 3.7.3 [security]
      graphite2: security update
      gst-libav-1.0: fixed dependencies & build with protected /tmp
      uget: switched to flexible gstreamer dependencies
      optipng: => 0.7.6 [security]
      django: => 1.9.3 (stable), 1.4.22 (legacy) [security]
      django: => 1.9.4 (stable) [regression]
      gsettings-desktop-schemas: => 3.14.2
      newsyslog: added offset patch
      lpeg: corrected dependency
      seamonkey: fixed multi-gstreamer dependency
      hatta: => 1.6.7
      pgpdump: => 0.30 [security]
      openssl: added 7DF9EE8C public key, required for 0.9 branch
      lighttpd: => 1.4.37
      lighttpd: => 1.4.39 [security]
      postgresql: => 9.3.8
      postgresql: => 9.3.12 [security]
      sqlite: fixed source url
      bugzilla: added sqlite support
      perl-cgi: => 4.28
      email-mime: => 1.937
      perl-cgi: forgotten HISTORY entry
      libcap: corrected dependencies
      linux: => 4.1.22 (lts)
      linux: => 4.4.8 (lts)
      linux: => 3.10.101 (lts)
      linux: => 3.2.79 (lts)
      gnutls: missed security updates for GNUTLS-SA-2015-4, GNUTLS-SA-2015-3 and GNUTLS-SA-2015-2
      linux: => 4.1.23 (lts)
      linux: => 3.18.32 (lts)
      linux: => 3.14.67 (lts)
      linux: => 3.12.59 (lts)
      linux: => 3.4.112 (lts)
      VERSION: 0.62-4
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-3..stable-0.62-4`
