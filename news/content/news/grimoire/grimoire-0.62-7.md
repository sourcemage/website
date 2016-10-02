title: Stable-0.62-7 released
author: stealth
category: news
date: 2016-10-02
tags: [grimoire]
---
Stable grimoire version 0.62-7 has been released!

This quick post-[stable-0.62-6](/news/grimoire-0-62-6/) release fixes a segfault in the hwclock binary introduced by util-linux regression update.

The tarballs have been signed and uploaded to our master server and will be propagating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
Florian Franzmann (2):
      utils/util-linux: version 2.26.2
      utils/util-linux: version 2.27.1

Treeve Jelbert (1):
      util-linux: => 2.27

Vlad Glagolev (4):
      bashdoc: corrected dependencies
      util-linux: => 2.27.1 (aes)
      util-linux: added forgotten hashsum
      VERSION: 0.62-7
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-6..stable-0.62-7`
