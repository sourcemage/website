title: Stable-0.62-6 released
author: stealth
category: news
date: 2016-10-01
tags: [grimoire]
---
Stable grimoire version 0.62-6 has been released!

This important security & stability update contains fixes for many system-wide critical spells, including but not limited to: openssl/libressl, curl, wget, bind, dhcp, gnupg, openssh, redis, libxml2, libxslt, c-ares, libarchive.

It also has latest updates for all Linux kernel branches (stable, LTS and EOL).

Other changes include: mpop spell update to simplify process of switching to our new developer e-mail setup, return of ifenslave script (as a spell) and fixes for missing dependencies and providers.

Big THANKS to all who was working on it over the last 5 months!

The tarballs have been signed and uploaded to our master server and will be propagating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
David C. Haley (8):
      Spell Update: bind 9.10.1-P1 -> 9.10.3-P4
      Spell Update: bind security_patch++
      Spell Updated: dhcp 4.2.6 -> 4.3.4
      Spell Update: dhcp security_patch++
      bind: => 9.10.4-P2, security_patch++
      bind-tools: => 9.10.4-P3 (security)
      bind: => 9.10.4-P3 (security)
      ifupdown: => 0.8.13

Eric Sandall (7):
      net/ifenslave: Added to configure network interfaces for bonding
      nfs-utils: Use correct CONFIG_NFS_V4 check for NFSv4
      nfs-utils: Check for CONFIG_NFS_V4 and CONFIG_NFS_V4_1 as needed
      ifupdown: Fix location of /sbin/ip (was hardcoded to /bin/ip)
      ifupdown: Updated to 0.8.12
      ifupdown: WEB_SITE refreshed
      ifupdown: Formatting cleanup

Florian Franzmann (15):
      ftp/wget: provide DOWNLOADER
      ftp/curl: version 7.48.0
      graphics/graphicsmagick: version 1.3.21
      graphics/graphicsmagick: version 1.3.22
      kernels/linux: version 4.7.3
      kernels/linux: version 4.7.4
      graphics/graphicsmagick: version 1.3.25, security update
      x11/xscreensaver: remove relic signature file
      ftp/curl: version 7.50.3, security update
      libs/libxml2: fix null-pointer dereference
      crypto/openssl: version 1.0.2i, security update
      libs/libxslt: version 1.1.29
      libs/libxslt: libxslt-1.1.28.tar.gz.sig removed
      crypto/openssl: version 1.0.2j, security update
      net/ifupdown: version 0.7.54

Ismael Luceno (1):
      ifupdown: Fix permissions on installed docs, PATCHLEVEL++

Jeremy Blosser (1):
      mail/mpop: update to 1.2.5

Ladislav Hagara (13):
      linux 4.5.4
      linux 4.6
      linux 4.6.1
      linux 4.6.4
      linux 4.7
      linux 4.7.1
      linux 4.7.2
      gnupg 1.4.20
      gnupg 1.4.21, SECURITY_PATCH=13
      libgcrypt 1.7.3, SECURITY_PATCH=7
      libksba 1.3.3
      wget 1.17.1
      openssh 7.3p1, SECURITY_PATCH=11

Pavel Vinogradov (8):
      kernels/linux: version 4.6.3
      crypto/libgcrypt: version 1.7.2
      ftp/wget: version 1.17
      ftp/wget: version 1.18, SECURITY_PATCH++
      ftp/curl: version 7.49.1, SECURITY_PATCH++
      chat-im/pidgin: version 2.10.12
      chat-im/pidgin: version 2.11.0, SECURITY_PATCH++
      ftp/curl: version 7.50.2

Remko van der Vossen (1):
      run-parts: version 4.7

Thomas Orgis (6):
      init.d: version 2.2.14, fixing devices script for proper version logic
      linux: remove now-bogus optional dependency on xz-utils
      gst-plugins-ugly-1.0: do not enforce disabled x264
      libowfat: version 0.30 (security update, after 7 years)
      ifupdown: update to 0.8.10
      run-parts: update and install to /bin

Treeve Jelbert (7):
      ibarchive-3.2.1  SECURITY FIX
      libksba-1.3.4   SECURITY FIX
      libxml2-2.9.4 SECURITY FIX +++
      curl: => 7.50.0
      curl-7.50.0  SECURITY FIX
      curl - fix bad depends flag for libssh2
      graphicsmagick-1.3.24 SECURITY FIX

Vlad Glagolev (68):
      libressl: => 2.2.9 [security]
      git: fixed SSL check
      encfs: added missing dependency
      ldns: fixed build with libressl
      wpa_supplicant: fixed build with libressl
      python-cryptography: added missing SSL dependency
      requests: => 2.7.0
      requests: => 2.10.0
      neon: added davfs check
      libarchive: added gvfs to up_trigger
      liblrdf: added missing SSL dependency
      linux: => 4.1.27 (lts)
      linux: => 4.5.7 (lts)
      linux: added missing history note
      linux: smgl patch compat 4.1-4.6
      gst-plugins-bad-1.0: added missing libvdpau dependency
      gst-plugins-bad-1.0: added missing fluidsynth dependency
      lighttpd: => 1.4.41 [security]
      lighttpd: dropped outdated sha512
      loop-aes: => 3.7c
      loop-aes: => 3.7d
      loop-aes: => 3.7e
      loop-aes: => 3.7f
      loop-aes: => 3.7g
      loop-aes: => 3.7h
      loop-aes: => 3.7i
      ratbox: => 3.0.10
      ircd-ratbox: corrected history typo
      dconf: dropped useless dependency
      wpa_supplicant: corrected dbus build flags and configs
      luajit: => 2.0.4
      luajit: provides LUA
      dbus: implemented reload function in the init script
      wpa_supplicant: added forgotten patchlevel
      linux: smgl logo patch compat for 4.7
      wireshark: => 1.12.13 [security]
      ettercap: => 0.8.2
      ettercap: swap to upstream defaults
      ffmpeg: corrected selection for program disabling
      ifupdown: install dummy files to protect hook dirs
      linux: => 4.7.5 (stable)
      ifenslave: added excluded file
      mpop: post-update fixes
      wmctrl: killed xorg-libs
      openssl: added newline
      libxslt: this was a security release
      ifenslave: dropped partially-erroneous check
      linux: => 4.1.33 (lts)
      linux: => 4.7.6 (stable)
      linux: => 4.4.23 (lts)
      linux: => 3.2.82 (lts)
      linux: => 3.10.103 (lts)
      linux: => 3.12.63 (lts)
      linux: => 3.16.37 (lts)
      linux: => 3.18.42 (lts)
      linux: => 3.14.79 (eol)
      django: => 1.9.10 [security]
      linux: latest.defaults updated for 4.7.6
      redis: security update
      redis: added missing patch for security update
      c-ares: => 1.12.0 [security]
      libowfat: post-update fixes
      ifupdown: => 0.8.16
      run-parts: => 4.8
      mupdf: => 1.9a [security]
      mupdf: security update
      mupdf: rebuild spells depending on static libs
      VERSION: 0.62-6
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-5..stable-0.62-6`
