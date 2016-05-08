title: Stable-0.62-5 released
author: stealth
category: news
date: 2016-05-08
tags: [grimoire]
---
Stable grimoire version 0.62-5 has been released!

Shortly after **0.62-4** we're rolling out 0.62-5 for the stable grimoire branch. This security update includes fixes for recently discovered vulnerabilities in ImageMagick, OpenSSL, file, dhcpcd, imlib2, Exim, OpenLDAP, Wireshark, Linux-PAM, and others.

The tarballs have been signed and uploaded to our server and will be propogating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
Florian Franzmann (2):
      security-libs/linux-pam: version 1.2.1
      net/dhcpcd: version 6.10.0

Ladislav Hagara (7):
      openssl 1.0.2h, SECURITY_PATCH=33
      links-twibright 2.10
      links-twibright 2.12, SECURITY_PATCH=2
      linux 4.5.3
      imlib2 1.4.6
      imlib2 1.4.7
      file 5.23

Pavel Vinogradov (1):
      net/dhcpcd: version 6.8.2

Treeve Jelbert (10):
      libarchive: => 3.2.0  SECURITY FIX
      linux-pam - optional depends audit
      openldap: => 2.4.42
      openldap: => 2.4.44
      dhcpcd: => 6.8.1
      dhcpcd: => 6.9.0
      dhcpcd: => 6.9.1
      dhcpcd: => 6.9.2
      dhcpcd: => 6.9.3
      dhcpcd: => 6.10.1

Vlad Glagolev (38):
      imagemagick: => 6.9.3-10 [security]
      libressl: => 2.2.7 [security]
      basesystem: => 0.9.8
      openssh: updated source urls
      Revert "links-twibright: fixed build with libressl"
      gobby: 200K -> 4K magic
      upstart: 187K -> 47K magic
      net/tor.gpg: 168K -> 23K magic
      linux-pam: missed security update
      tk: moved to x11-toolkits section
      tk: corrected dependencies, kill xorg-libs
      tk: don't do useless doc-ing, cleaned up
      imlib2: => 1.4.9 [security]
      libressl: updated mirror to ftp.sourcemage.us
      simpleinit-msb: updated mirror to ftp.sourcemage.us
      btrfs-progs: updated mirror to ftp.sourcemage.us
      xinetd: updated mirror to ftp.sourcemage.us
      slim: updated mirror to ftp.sourcemage.us
      pcc: updated mirror to ftp.sourcemage.us
      ocfs2-tools: updated mirror to ftp.sourcemage.us
      tor: updated mirror to ftp.sourcemage.us
      trac-ldapplugin: updated mirror to ftp.sourcemage.us
      ardour3: updated mirror to ftp.sourcemage.us
      mercurial: => 3.8.1 [security]
      file: security update
      linux: => 3.2.80 (lts)
      linux: => 3.16.35 (lts)
      linux: => 4.4.9 (lts)
      linux: => 3.14.68 (lts)
      socat: => 1.7.3.1 [security]
      privoxy: => 3.0.24 [security]
      openldap: security update
      rsa: => 3.2.2
      rsa: => 3.3 [security]
      wireshark: => 1.12.11
      exim: => 4.87 [security]
      dhcpcd: security update
      VERSION: 0.62-5
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-4..stable-0.62-5`
