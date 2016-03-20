title: Stable-0.13 released
author: sandalle
category: news
date: 2007-08-16
tags: [grimoire]
---
The routine continues: Stable grimoire version 0.13 has been released! As usual, users of stable merely need to run `sorcery system-update`.
Spells listed on the [0.13 release page](/Grimoire/stable/0.13) were tested and qualified to have no known defects of "gating" severity at the time of this release.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.13.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.13.tar.bz2.asc>.

I would like to thank Mathieu Lonjaret (lejatorn) for helping test spells and Chris Dombroski (cdombroski) for volunteering to shepherd this release.

In case anyone is interested, here's the shortlog between 0.12 and 0.13[0]:

```
Alexander Tsamutali (1):
      python-devel/networkx: new spell, software for complex networks

Andraž Levstik (44):
      ushare: version update 1.0
      quill: update to 0.2.7
      tor: version update and upstream sigs
      tor: forgot the keyring
      metalog: update to 0.8
      drm: temporary fix until a new libdrm is out
      dovecot: update to 1.0.2
      libstatgrab: version update, upstream gpg
      bwm-ng: version update
      net/darkstat: new spell, ntop like monitor but less issues
      net/ipfm: new spell, ip flow monitor
      net/maradns: version update
      x11/slim: version update
      dzen2: update to 0.6.0
      devel/lazarus: delinting DETAILS
      libs/dosemu: delinting DETAILS
      perl-cpan/file-which: delinting DETAILS
      python-devel/cherrypy: delinting DETAILS
      telephony/decibel: delinting DETAILS
      telephony/libtelepathy: delinting DETAILS
      utils/strigi: delinting DETAILS
      latex/xcolor: delinting DETAILS
      dzen2: update to 0.6.1
      gkrellm2: version update 2.3.0
      gkrellm2: hash changed due to a new tarball, was missing a french.po
      gkrellm2: hash update de.po this time
      comix: fixups for POST and PRE _REMOVE
      audio-soft/gnump3d: new spell, streaming server in perl
      xpenguins: starting move from games
      forgot ChangeLOg
      xpenguins_themes: starting move from games
      xpenguins-applet: starting move from games
      tor: version update
      dzen2: update to 0.7.0
      pinot: version update
      w3m: update to 0.5.2
      w3m: some revamping
      xmms2_jump: new xmms2 client
      Cleaning up ChangeLog
      exim: use _list not _multi     (cherry picked from commit 2250df8730d0f24fad1116775f4715884621d984)
      dovecot: update to 1.0.3, MANAGESIEVE update     (cherry picked from commit 139ea0ffccf0d5a85c3f077dcdf9377395a1a8b0)
      dovecot: forgot the SECURITY_PATCH     (cherry picked from commit 233359d398299342dcc10fa5a367aa77d9ec57c9)
      tor: version update and SECURITY update     (cherry picked from commit e49d9bf2427f564bb460fc78542fdab1afedc615)
      tor: update dev to 0.2.0.4-alpha, SECURITY_PATCH++     (cherry picked from commit 1d88004f49b8a487e659edf66ee67fa62076235f)

Arjan Bouter (5):
      amanda: updated to 2.5.2p1
      elation: added desktop file
      evidence: added desktop file
      express: added desktop file
      vacation: new spell, email autoresponder (think out-of-office reply)

Arwed von Merkatz (14):
      vlc: added optional_depends on x264
      exaile: updated to 0.2.10
      exaile: install to /usr
      transcode: patch to work with current ffmpeg-svn, bug #13866
      gst-plugins-ugly: updated to 0.10.6
      gst-plugins-bad: updated to 0.10.5
      gst-plugins-good: added missing wavpack dependency
      mjpegtools: install a missing header
      cdrtools: fixed patch
      vala: new spell, compiler for the gobject type system
      vala: updated to 0.1.2
      video/whaawmp: new spell
      automake-1.4: made it work with current automake
      automake-1.7: made it work with current automake

David Kowis (2):
      cacti: added the official patches
      Nagios: Update to latest version and include the contrib directory in /usr/share

David Michael Leo Brown Jr (17):
      linux updated realtime preempt patchset
      linux updated latest maintenance patches
      Sorry already done...
      linux updated to 2.6.22
      linux updated ck patches
      linux updated maintenance patches
      linux updated realtime preempt patches
      linux updated pre 2.6 kernel patches
      kvm updated to 31
      kvm updated to 33
      util-linux added util-linux-ng option for using 2.13
      util-linux fixed url got the wrong one
      uml_utilities updated to 20060622
      uml_utilities added BUILD file back with just make and fixed source dir
      xscreensaver updated to 5.03
      linux updated mm patches
      linux updated latest 2.6.16 maintenance patches

Elisamuel Resto (8):
      net/poptop: version bump to 1.3.4, removed PATCHLEVEL
      mail/c-client: version bump to 2006j2 (Bug #13902)
      mail/imap: version bump to 2006j2 (Bug #13902)
      mail/c-client: added secondary SOURCE_URL for older releases (they update and send non-current releases here).
      mail/imap: added secondary SOURCE_URL for older releases (they update and send non-current releases here).
      net/fail2ban: version bump to 0.8.0, add patch for injection of arbitrary hosts via ssh rules
      libs/elfutils: update to 0.128, fix bug #13767, fix upgrade error, update sigs     (cherry picked from commit a2f86b5c2a44d421f04dd67303636d3189d435fd)
      libs/elfutils: fixed a typo in SOURCE2_URL[1]     (cherry picked from commit 68f129d59181eb8cd3e5548f661f2071cdc9a792)

Eric Sandall (42):
      VERSION: 0.13-test
      etk_extra: Added a spell for dxtra ETK widgets outside of ETK core
      linux: Updated latest maintenance patch to 2.6.21.6
      linux: Added maintenance patch 2.6.20.15
      man-pages: Updated to 2.61
      etk_extra: Depends on CVS
      engycad: E17-based CAD shell
      cdrtools: Updated to 2.01.01a29
      fox: Updated to 1.6.28
      nfs-utils: Updated to 1.1.0 (for util-linux-ng later on)
      autogen: Updated to 5.9.1
      stellarium: Updated to 0.9.0
      wxgtk: Animate is invalid for stable release
      Bug #13869 (wavpack updated to 4.41.0)
      libmp4v2: Added from Bug #13868
      Bug #13870 (easytag update)
      cdrtools: Updated to 2.01.01a30
      ripmime: Updated to 1.4.0.7
      thunderbird: Fix broken symlinks (Bug #13846)
      dhcpcd: DEPENDS was missing +x
      dhcpcd: Create /var/lib/dhcpc (Bug #11614)
      basesystem: Depend on PAGER, not less specifically. Last part of Bug #12857
      ecore: Depends on dbus now (Bug #13871)
      iproute2: Updated to 2.6.22-070710
      cksfv: Updated to 1.3.11
      cksfv: Adding missing signature (Bug #13877)
      man-pages: Updated to 2.62
      sunbird: Updated to 0.5 (lightning)
      sunbird: Patches from Gentoo for various issues
      sunbird: Build default extensions and disable xpfe. Works now :)
      sudo: Updated to 1.6.9
      scilab: Updated to 4.1.1
      gperiodic: Updated to 2.0.10
      man-pages: Updated to 2.63
      exim: Added optional dependency on dovecot for auth
      exim: Clean up CONFIGUREd dependencies to be REAL dependencies :)
      sudo: Updated to 1.6.9p1
      kmymoney2: Updated to 0.8.7
      sudo: Updated to 1.6.9p2
      VERSION: 0.13-rc
      VERSION: 0.13-0
      VERSION: 0.13-1

Ethan Grammatikidis (5):
      version bump & url fixes for monotone
      util-linux: added patches to build on arm with glibc
      util-linux/BUILD: forgot a detail. Fixed
      util-linux: Moved patches & sedits from BUILD to PRE_BUILD
      celestia: work-around for a configure bug that prevented celestia from running.

Florian Franzmann (3):
      fonts/jmk-x11-fonts: new spell
      latex/{europecv,unicode}: new spells
      doc/xpdf: added security related patch, cf. http://www.kde.org/info/security/advisory-20070730-1.txt

George Sherwood (38):
      liferea: Updated stable to version 1.2.19
      gnucash:  Updated to version 2.1.5
      squeeze: depends dbus-glib
      xfce-utils: depends which.  startxfce4 fails if which is not present.
      silc-client: Updated to version 1.1.2
      liferea: Updated devel to version 1.4-RC1
      ktorrent: Updated to version 2.2
      gimp: Updated stable to version 2.2.16
      imagemagick: Updated to version 6.3.5-0
      gimp: Updated stable to version 2.2.17
      mysql:  Updated stable to version 5.0.45
      gnucash: Updated to version 2.2.0.  configure-fix.diff updated for version 2.2.0
      snort: Updated to version 2.7.0
      dhcp: Updated to version 3.0.6
      liferea: Updated stable to version 1.2.20
      e2fsprogs: Updated to version 1.40.2.  Added SOURCE2_IGNORE
      liferea: Updated devel to version 1.4-RC2
      squid: Updated to 2.6.STABLE14
      psi: Updated devel to 0.11-RC2.  Updated BUILD to work with new configure
      imagemagick: Updated to version 6.3.5-1
      xchat-gnome: Updated to version 0.18.  Removed incorporated patch.
      seamonkey: Updated to version 1.1.3.  SECURITY_PATCH++
      sqlite: Updated to version 3.4.1
      phpmyadmin: Updated to vesion 2.10.3
      imagemagick: Updated to version 6.3.5-2
      micq: Updated to version 0.5.4.2
      krusader: Updated to version 1.80.0
      liferea: updated devel to 1.4-RC3
      sonata: Updated to version 1.2.2
      lighttpd: Updated to version 1.4.16.  SECURITY_PATCH++
      imagemagick: Updated to version 6.3.5-3
      ktorrent:  Updated to version 2.2.1
      spamassassin: Updated to version 3.2.2
      tcpdump: Updated to version 3.9.7
      lftp: Updated to version 3.5.12
      xfsprogs: Updated to version 2.9.3
      doxygen: Updated to version 1.5.3
      gtk-sharp-2: Downgraded to version 2.10.0.  That is the version that is     listed as stable on mono's website and 2.10.1 caused at least     Bug 13900.(cherry picked from commit 8b52367656992968312d48ef45c8d4ea86141c96)

Jaka Kranjc (12):
      snort: converted to upstream signature checking
      namazu: 2.0.17 and gpg
      gss: 0.0.21
      gss: gpg signed
      gss: .22
      xmlto: converted to upstream gpg
      sdl: upstream gpg
      qtiplot: 0.9rc3
      bash: fix 3rd url #13913
      guile: added libtool dependency #13933     (cherry picked from commit 4d37e0039c040522c181c28857d4338d9761e6b6)
      init.d: fix my workaround for #13363     thanks Arwed     (cherry picked from commit db66920cc0b3fb42c5cef6450a1076a0024aa0bb)
      sorcery-pubkeys: added my key     (cherry picked from commit 50ed67deb649b2c989eaaf6d7518299aeeb671e9)

Juuso Alasuutari (8):
      phasex 0.10.3
      rsbac-admin: Updated to 1.3.4, added sub-package selection, did some URL and misc fixing.
      shorewall 3.4.5
      shorewall: deleted obsolete services file
      zzuf: New spell, an application input fuzzer.
      libsndfile: patch to build against flac >= 1.1.4
      libsndfile: actually added flac patch
      flac-tools 0.0.11

Ladislav Hagara (39):
      claws-mail 2.10.0
      tea 17.0.0
      p7zip 4.48
      claws-mail-extra-plugins 2.10.0
      xvid 1.1.3
      krb5: SECURITY_PATCH++
      libksba 1.0.2
      libassuan 1.0.2
      wireshark 0.99.6, SECURITY_PATCH++
      gnupg-exp 2.0.5
      pinentry 0.7.3
      squirrelmail 1.4.10a
      mail/squirrelmail-gpg: new spell, G/PGP Encryption Plugin for SquirrelMail
      seahorse 2.19.5 (devel)
      links-twibright 2.1pre29
      openct 0.6.12
      opensc 0.11.3
      gpgme 1.1.5
      krb5 1.6.2
      multitail 5.2.0
      nss 3.11.7
      nspr 4.6.7
      man-pages-cs 0.17.20070715
      firefox 2.0.0.5, SECURITY_PATCH=9
      thunderbird 2.0.0.5, SECURITY_PATCH=8
      openldap 2.3.37
      sylpheed 2.4.4
      ethtool 6
      firefox 2.0.0.6, SECURITY_PATCH=10
      libidn 1.0
      tea 17.1.0
      gjots2 2.3.7
      linux-pam 0.99.8.1
      ncftp 3.2.1
      libnxml 0.18.0
      libmrss 0.18.0
      rsstail 1.3
      phppgadmin 4.1.3     (cherry picked from commit c579018aa87576888856ded02293cc53b3a68141)
      thunderbird 2.0.0.6     (cherry picked from commit a6a316c84f91688287ec5d0562c1cd963c8fd03f)

Martin Spitzbarth (10):
      libpri: updated to 1.4.1, converted to upstream signature checking
      asterisk: updated to 1.4.7.1, added libpri as an optional dependency
      asterisk: updated to 1.4.8, SECURITY_PATCH++, fixes bug 13899
      blender: install plugins, scripts and locales during cast
      obconf: updated to 2.0.2
      openbox: updated to 3.4.3
      asterisk: updated to 1.4.9, SECURITY_PATCH++, second try at bug 13899
      asterisk: updated to 1.4.10, SECURITY_PATCH++     (cherry picked from commit 3277b29d85732f4c851b00645e9dcca802baa3a6)
      asterisk: fixed download url and mirrors     (cherry picked from commit 1c22ceac05ce3e7c24b835e5628e0e472605a116)
      asterisk-addons: fixed download url and mirrors     (cherry picked from commit ce5ddd6c51ec0930c1c696a14e5b0efebfc8701e)

Mathieu Lonjaret (5):
      gliv: new spell
      gliv: new spell
      gtk-gnutella: 0.96.4
      curl: 7.16.4
      curl: SECURITY_PATCH++

Philippe Caseiro (1):
      Updating mp3info spell to version 8.0.5a

Pol Vinogradov (13):
      audio-players/mpd:
      audio-players/sonata:
      editors/scite:
      net/firehol:
      net/iproute2:
      x11/xneur:
      gnome2-apps/gxneur:
      kde-apps/kxneur: new spell, KDE frontend to X Neur Switcher
      kde-apps/kxneur:
      x11-libs/wine:
      disk/anyfs-tools:
      x11-libs/wine:
      cluster/ocfs2-tools:

Remko van der Vossen (2):
      devel/slang: 2.1.1
      i18n/anthy: version 9100

Robin Cook (47):
      libgnomedb3: renamed from libgnomedb-dev
      gnumeric: changed libgnomedb-dev libgnomedb3
      gtkhtml2: updated to 3.14.3
      eel2: updated to 2.18.3
      gnome-desktop: updated to 2.18.3
      libwnck: updated to 2.18.3
      gnome-menus: updated to 2.18.3
      gnome-session: update to 2.18.3
      gnome-panel: updated to 2.18.3
      gnome2-user-docs: updated to 2.18.2
      evolution-data-server: updated to 1.10.3
      nautilus2: updated to 2.18.3
      file-roller: updated to 2.18.4 and renamed from file-roller2
      file-roller: some clean up from the rename
      libgnomedb3: some cleanup from the rename
      libgda3: added missing y in CONFLICTS
      evolution: updated to 2.10.3
      poppler: updated to 0.5.9
      evince: updated to 0.8.2
      evolution-data-server: updated to 1.10.3.1
      evolution-exchange: updated to 2.10.3
      gdm2: updated to 2.18.3
      gedit: updated to 2.18.2
      pygtk2: updated to 2.10.5
      evince: updated to 0.8.3
      file-roller: fix fat finger in SOURCE_DIRECTORY
      apache22: added missing modules and added option to build modules shared
      gnome-speech: updated to 0.4.15
      pygtk2: updated to 2.10.6
      libgsf: updated to 1.14.5
      goffice-dev: updated to 0.4.1
      guilib: updated to 1.2.1
      glib2: updated to 2.12.13
      cairomm: updated to 1.4.2
      gtk+2: updated to 2.10.14
      gmime: updated to 2.2.10
      wpa_supplicant: corrected to build if using devel version
      sawfish2: update to 1.3.1
      sawfish2: actually remove PREPARE
      guile-gtk: added INSTALL for make_single
      pango: updated to 1.16.5
      vte: updated to 0.16.7
      gnome-speech: updated to 0.4.16
      orbit2: updated to 2.14.8
      librsvg2: updated to 2.18.0
      goffice-dev: updated to 0.4.2
      gnumeric: updated devel version to 1.7.11

Treeve Jelbert (165):
      wireless_tools-29.pre22
      perl-gtk2-1.145
      perl-cairo-1.041
      fuse-2.7.0
      reetype2-2.3.5
      ocrad-0.17
      ed-0.6
      avahi-0.6.20
      kdelibs4-3.91.0
      kdepimlibs4-3.91.0
      /kdebase-3.91.0
      git-1.5.2.3
      tellico-1.2.12
      kdeadmin4-3.91.0
      kdeautils4-3.91.0
      kdenetwork4-3.91.0
      kdenetwork4-3.91.0
      itools-0.16.1
      kdemultimedia4-3.91.0
      kdepim4-3.91.0
      kdegames4-3.91.0
      kdegraphics4-3.91.0
      decibel-0.4.0
      telepathy-sofiasip-0.3.22
      xaralx-0.7r1777
      kde4 - update FUNCTIONS
      kdebase4 - update depends
      kdegraphics4 - update depends
      kdenetwork4 - update depends
      kdepim4 - update depends
      kdesdk4-3.91.0
      kde4-profile-3.91.0
      new spell : eigen
      ca2-2.0.0-beta7
      poppler - add qt4 support
      koffice2-1.9.91
      koffice2 - rm redundant files
      koffice2 - fix TRIGGERS
      djview4-4.1
      libmusicbrainz-2.1.5
      libmusicbrainz3-3.0.1
      python-musicbrainz2-0.4.1
      e2fsprogs-1.40.1
      freeimage-393
      0.5.2
      kdebase4 - fix typo in BUILD
      luca-1.02
      kdemultimedia4 - updated DEPENDS
      kipi-plugins-0.1.4
      xmltv-0.5.46
      libnl-1.0-pre6
      ntfs-3g-1.710
      fpc-2.1.4
      exiv2-0.15
      m4-1.4.10
      libdaemon-0.12
      new spells: fpcsrc, qt4pas, lazarus
      clamav-0.91
      heyu2-2.0.0
      wpa_supplicant - 0.4.10 / 0.5.8 / 0.6.0
      decibel - update svn location
      dar-2.3.4
      itools-0.16.2
      cups-1.2.12
      qwt5   5.0.2
      qt4 - add back PROVIDES
      FUNCTIONS - extra functions
      qwtplot3d-0.2.7
      git-1.5.2.4
      FUNCTIONS - fix typo
      wine-0.9.41
      p7zip-4.49
      libmng-1.0.10
      stlport -update hash
      telepathy-mission-control-4.30
      cupsddk-1.2.0
      clamav-0.91.1
      neon-0.26.4
      star-1.5a83
      openrpt-2.1.0
      newt-0.52.7-1.fc8
      qt4pas-V1.43_Qt4.3.0
      pysqlite-2.3.5
      heyu2-2.0.1
      motion-3.2.8
      turbogears-1.0.3
      kid-0.9.6
      turbokid-1.0.2
      pastescript-1.3.5
      turbojson-1.1
      decoratortools-1.5
      ed-0.7
      firebird - remove services file
      pysqlite - update sourcehash - upstream change
      itools-0.16.3
      /partimage - update depends
      lm_sensors-2.10.4
      ogre-1-4-3
      devil-1.6.8-rc2
      turbogears-1.0.3.2
      sqlalchemy-0.3.10
      beautifulsoup-3.0.4
      freevo-1.7.2
      zopeinterface-3.3.0
      celementtree - fix depends
      kid - update depends
      deprecate kde-apps/digikamplugins
      deprecate kde-apps/digikamplugins
      flac-1.1.4
      twinkle-1.1
      klear-0.6.1
      k3b-i18n-1.0.3
      k3b-1.0.3
      kde4 - update dependencies
      kdelibs4 - update dependencies
      clucene-0.9.19
      digikam - remove conflicts
      ploticus-233-3
      tesseract-2.00
      sip-snapshot-20070714
      pyqt4-4-snapshot-20070723
      qt4pas-V1.44_Qt4.3.0
      boost-1_34_1
      flac-1.2.0
      ragel-5.23
      pbzip2-1.0.2
      lshw-B.02.11
      kino-1.1.0
      dabo-0.8.1
      sqlobject-0.9.1
      itools-0.16.4
      libvorbis-1.2.0
      p7zip-4.51
      mldonkey-2.9.0
      syslog-ng-2.0.5
      wine-0.9.42
      openrpt-2.2.0
      lcms-1.17
      tellico-1.2.13
      kaffeine-0.8.5
      fontforge-20070723
      archive-tar-1.32
      archive-zip-1.20
      compress-zlib-2.005
      libgphoto2-2.4.0
      gphoto2-2.4.0
      sip-4.7
      pyqt-3.17.3
      pyqt4-4.3
      gtklp-1.2.4
      qt4pas-V1.45_Qt4.3.0
      bobcat-1.16.0
      nyevent-2.54
      /decibel-0.5.0
      libisofs-0.2.8
      libburn-pykix-0.3.8
      kdegraphics - fix CVE-2007-3387     (cherry picked from commit a9a185d01a2c6958f97be4c8cf0f85f2600dac7d)
      koffice - fix CVE-2007-3387     (cherry picked from commit 5bb8d0bf6322682eee87f2354230b8df9bdac1ee)
      qt-x11   - CVE-2007-3388     (cherry picked from commit 783e4577f95aa6d9497d63ed485aca78f2553157)
      glibc - fix bug #13925     (cherry picked from commit f7a732831e8fdcec1b0ab64587ae5ca69446d4c0)
      glibc - fix typo     (cherry picked from commit 9d60d4806b419a5b8d4cb4b640a10b192f83541c)
      libtunepimp-0.5.3     (cherry picked from commit 3bc6ceb5cb0ec4f1c1a70b4c34acb5baefe5fe8c)
      libofa-0.9.3
      util-linux  - fix bug #13926
      util-linux - fix typo     (cherry picked from commit 1b978b5317e71b389cc6819f00e150cbdc35f610)
```

[0] Generated with: `git shortlog --no-merges stable-0.12-9..stable-0.13-1`
