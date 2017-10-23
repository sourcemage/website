title: Stable-0.62-11 released
author: stealth
category: news
date: 2017-10-22
tags: [grimoire]
---
Stable grimoire version 0.62-11 has been released!

This release brings a lot of security updates to our 0.62 stable grimoire branch.

The tarballs have been signed and uploaded to our master server and will be propagating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

Following updates were integrated[^0]:

```
Eric Sandall (2):
      grub2: Depends on bison and flex (found from fresh install)
      linux: Depends on some LZMA for 4.x maintenance patches

Florian Franzmann (13):
      ftp/curl: version 7.54.1, security update
      crypto/openssl: version 1.0.2l
      utils/libnotify: version 0.7.7
      net/openvpn: version 2.3.9
      net/openvpn: version 2.3.10
      net/openvpn: version 2.3.11
      net/openvpn: version 2.3.12
      libs/pcre: version 8.40
      net/tcpdump: version 4.8.1
      net/tcpdump: version 4.9.2, security update
      net/libpcap: version 1.8.1
      crypto/dropbear: version 2015.67
      libs/libxml2: version 2.9.5, security update

Ismael Luceno (9):
      bluez5 5.37
      axel: Use apply_patch_dir
      axel 2.13.1
      axel 2.14
      axel 2.14.1
      axel 2.15, SECURITY_PATCH++
      wpa_supplicant: Use sorcery CFLAGS
      wpa_supplicant: Install tools to /sbin
      wpa_supplicant: PATCHLEVEL++

Ladislav Hagara (3):
      tcpdump 4.7.4
      libpcap 1.7.3
      libpcap 1.7.4

Pavel Vinogradov (8):
      crypto/libgcrypt: disabled -Ofast if in CFLAGS, cosmetic fixes
      crypto/libgcrypt: version 1.7.6
      crypto/libgcrypt: version 1.7.7
      devel/python: version 2.7.13
      devel/python: version 2.7.14
      crypto/libgcrypt: SECURITY_PATCH++ for 1.7.8, (CVE-2017-7526)
      crypto/gnupg: version 1.4.22, SECURITY_PATCH++
      ruby-raa/ruby-2.2: version 2.2.8, SECURITY_PATCH++

Remko van der Vossen (5):
      openssl: build using arch from selected archspec
      kbd: depends on libtool
      perl: build using arch from selected archspec
      net/network-manager: depend on DEVICE-MANAGER instead of udev
      net/network-manager: fix typo s/CRYPT/CRYPTO/

Thomas Orgis (5):
      expat: version 2.2.1 (several security fixes)
      kbd: avoid installation of UTF-8 test file that may confuse castfs
      kbd: gettext needed as long as we run autoreconf
      lame: version 3.100, ++SECURITY_PATH
      wpa_supplicant: fix CLI path in init script (for status)

Treeve Jelbert (19):
      libgcrypt: => 1.7.5
      libusb - tweak UP_TRIGGERS
      kbd: => 2.0.3
      network-manager - depends CONSOLE-MANAGER
      openvpn.gpg = updated
      libgcrypt: => 1.7.8
      libnl-3.3.0 SECURITY FIX
      pcre: => 8.41 SECURITY FIX
      c-ares: => 1.13.0  SECURITY FIX
      GraphicsMagick-1.3.26 SECURITY FIX
      libsndfile: => 1.0.27
      libsndfile-1.0.28 SECURITY FIX
      libzip: => 1.1.3
      libzip: => 1.3.0   SECURITY FIX
      libzip - tweak depends
      ruby-2.2 - extra conflict
      dropbear: => 2017.75  SECURITY FIXES
      dnsmasq: => 2.75
      dnsmasq-2.78 - SECURITY FIX

Vlad Glagolev (38):
      libgcrypt: this was a security update
      libnotify: dropped unneeded gtk+3
      glibc: security update
      openvpn: => 2.3.18 [security]
      python: security bump
      libgcrypt: => 1.7.9 [security]
      compress-raw-zlib: => 2.074
      compress-raw-zlib: deprecated spell in favour of perl
      newsbeuter: => 2.9
      newsbeuter: security update
      mailman: => 2.1.14 [security]
      mailman: configure CGI GID
      mailman: corrected home directory for mailman account
      bluez5: => 5.40
      bluez5: dropped deprecated var
      bluez5: => 5.46
      bluez5: => 5.47 [security]
      axel: => 2.12
      axel: fixed '--with-openssl' flag
      axel: corrected SSL flags
      wpa_supplicant: => 2.6 [security]
      linux: => 3.10.105 (lts)
      linux: => 4.8.17 [eol]
      linux: => 4.9.58 [lts]
      linux: smgl logo patch compatibility with kernel 4.8 & 4.9
      linux: => 4.4.94 [lts]
      linux: drop outdated patches in 4.4 branch
      linux: => 4.1.45 [lts]
      linux: drop outdated patches in 4.1 branch
      linux: => 3.18.77 [eol]
      linux: drop outdated patches in 3.18 branch
      linux: => 3.16.49 [lts]
      linux: drop outdated patches in 3.16 branch
      linux: => 3.10.107 [lts]
      linux: => 3.2.94 [lts]
      linux: drop outdated patches in 3.2 branch
      loop-aes: => 3.7k
      VERSION: 0.62-11
```

[^0]: Generated with: `git shortlog --no-merges stable-0.62-10..stable-0.62-11`
