title: Stable-0.62-9 released
author: stealth
category: news
date: 2016-11-16
tags: [grimoire]
---
Stable grimoire version 0.62-9 has been released!

This quick update fixes important dependency bug for ifupdown spell, along with vulnerabilities in libarchive, pcre, apache22 and rsync.

The tarballs have been signed and uploaded to our master server and will be propagating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
Florian Franzmann (2):
      archive-libs/libarchive: version 3.2.2
      archive-libs/libarchive: bump SECURITY_PATCH

Ismael Luceno (1):
      dosfstools 3.0.28

Justin Boffemmyer (1):
      tmux: 2.2

Ladislav Hagara (1):
      tmux 2.0

Treeve Jelbert (5):
      pcre: => 8.38
      pcre: => 8.39
      dosfstools: => 3.0.26
      dosfstools: => 4.0
      libnl - new url

Vlad Glagolev (10):
      tmux: dropped deprecated sig
      apache22: => 2.2.31 [security]
      apache22: fixed build with libressl
      mysql-python: added missing ssl dependency
      pcre: security update
      rsync: => 3.1.2 [security]
      lynx: updated website & source url
      dosfstools: corrected dependency
      ifupdown: added missing dependency
      VERSION: 0.62-9
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-8..stable-0.62-9`
