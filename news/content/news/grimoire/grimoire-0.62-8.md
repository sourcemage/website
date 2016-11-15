title: Stable-0.62-8 released
author: stealth
category: news
date: 2016-11-14
tags: [grimoire]
---
Stable grimoire version 0.62-8 has been released!

We're pleased to announce an important security update for 0.62 stable grimoire which also includes critical fixes for the Linux kernel.

The tarballs have been signed and uploaded to our master server and will be propagating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
David C. Haley (4):
      net/bind: => 9.10.4-P4, SECURITY_PATCH++
      net/bind-toold: => 9.10.4-P4
      net/tor.gpg: project keys refreshed
      net/tor: => 0.2.8.9, 0.2.9.4-alpha; both SECURITY_PATCH++

Eric Sandall (2):
      youtube-dl: Updated to 2016.03.06
      monit: Updated to 5.14

Florian Franzmann (6):
      utils/youtube-dl: version 2015.08.28
      x11/xautolock: fix compile error, add bug-fix patches
      crypto/cryptopp: version 564
      gnome3-libs/gcr: version 3.16.0
      x11-toolkits/gtk+2: version 2.24.30
      net/tor: version 0.2.6.9 and 0.2.7.1-alpha

Ismael Luceno (9):
      jansson 2.7
      cryptopp 563
      Revert "x11-toolkits/gtk+2: removed fix for gtk-doc"
      gtk+2: Do not try to fix ref. manpage rules
      tor 0.2.7.5 (devel)
      torsocks 2.1.0
      tor: torify now depends on torsocks
      sudo: Update WEB_SITE
      sudo 1.8.13

Pavel Vinogradov (8):
      utils/youtube-dl: version 2016.04.24
      utils/youtube-dl: version 2016.05.10
      utils/youtube-dl: version 2016.06.12
      kernels/linux: versions 4.4.26 and 4.7.9
      ftp/curl: version 7.51.0, SECURITY_PATCH++
      x11-toolkits/gtk+2: version 2.24.28
      x11-toolkits/gtk+2: removed fix for gtk-doc
      x11-toolkits/gtk+2: version 2.24.31, SECURITY_PATCH++

Treeve Jelbert (2):
      qpdf: => 5.1.2
      qpdf: => 6.0.0

Vlad Glagolev (61):
      mpv: dropped deprecated flags
      slim: optionally install systemd service
      ferm: => 2.3
      ferm: optionally install systemd service
      werkzeug: added missing suggest dep - pyopenssl
      Revert "werkzeug: added missing suggest dep - pyopenssl"
      werkzeug: => 0.10.4
      ndg_httpsclient: new spell, enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
      pysocks: new spell, Python SOCKS client module
      requests: added missing dependencies
      requests: corrected hashsum for 2.10.0 tarball
      Revert "loudmouth: depends SSL"
      loudmouth: use SSL provider
      loudmouth: don't install docs twice
      keepnote: added missing dep
      linux: => 4.1.34 (lts)
      linux: => 4.7.8 (stable)
      linux: => 4.4.25 (lts)
      linux: => 3.18.43 (lts)
      linux: => 3.12.64 (lts)
      linux: updated defaults for stable and lts kernel branches
      linux: => 4.7.10 (stable)
      linux: => 4.4.27 (lts)
      linux: => 3.16.38 (lts)
      linux: => 3.12.66 (lts)
      linux: => 3.10.104 (lts)
      linux: => 3.2.83 (lts)
      linux: updated defaults for stable branch
      linux: => 3.18.44
      linux: => 4.1.35
      znc: fixed build with LibreSSL
      nginx: added http_sub_module
      linux: => 3.4.113 (lts)
      mtr: fixed row coloring with dark themes
      linux: => 4.4.28 (lts)
      qpdf: security update
      linux: => 4.4.29 (lts)
      linux: => 4.4.30 (lts)
      cryptopp: => 5.6.5 [security]
      seahorse: fixed dependencies
      seahorse: fixed broken build
      seahorse: dropped obsolete stuff
      seahorse: corrected openldap dependency
      nodejs: added compatibility with LibreSSL
      nodejs: => 0.10.48 [security]
      nodejs: updated forgotten checksum
      ca-certificates: => 20161102
      linux: => 4.4.31 (lts)
      linux: => 3.12.67 (lts)
      libxslt: security update
      net/tor.gpg: 47K -> 32K magic
      tor: => 0.2.6.10
      gegl: updated source url
      babl: updated source url
      gimp-help-2: updated source url
      perl-gimp: updated source url
      gegl: fixed build with ffmpeg & asciidoc
      sudo: => 1.8.18p1 [security]
      monit: => 5.15
      monit: => 5.20.0 [security]
      VERSION: 0.62-8
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-7..stable-0.62-8`
