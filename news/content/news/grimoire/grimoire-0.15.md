title: Stable-0.15 released
author: sandalle
category: news
date: 2007-11-20
tags: [grimoire]
---
Stable grimoire version 0.15 has been released!

As usual, users of stable merely need to run `sorcery system-update`. Spells listed on the [0.15 release page](/Grimoire/stable/0.15) were tested and qualified to have no known defects of "gating" severity at the time of this release. The tarballs have been signed and uploaded to our server and will be propogating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.15.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.15.tar.bz2.asc>.

I would like to thank Jaka Kranjc (lynx) and Mathieu Lonjaret (lejatorn) for helping test spells.

In case anyone is interested, here's the shortlog between 0.14 and 0.15[0]:

```
Alexander Tsamutali (12):
      x11-toolkits/kiwi: updated to 1.9.18
      haskell/haskell-x11: updated to 1.2.3
      haskell/haskell-x11-extras: updated to 0.4
      windowmanagers/xmonad: updated to 0.4
      devel/ghc: added option for quick unoptimised build
      python-devel/rabbyt: new spell, fast sprite library for Python
      python-devel/ipython: updated to 0.8.1
      Revert "changing all haskell spells to depend on GHC rather than ghc"
      devel/darcs: now depends on ghc instead of GHC
      devel/haddock: now depends on ghc instead of GHC
      kde-apps/kdevelop: now depends on ghc instead of GHC
      corrected small typos in previous commits

Andraž Levstik (65):
      jpilot: update to 0.99.9 and upstream gpg
      mobile/gnokii: version update
      audio-soft/gnupod: version update
      wxgtk-no-unicode: various patches from gentoo that just make it work a     lot better, if anyone wants to see if any are optional/not needed feel     free to do so
      exim: update to 4.68
      dovecot: update to 1.0.5, update to the patches and sieve
      mobile/powermgmt-base: added spell, basic powermanagment tools from     debian bug #13996
      forgot ChangeLog
      mobile/laptop-detect: new spell, detect if running on a laptop, bug #13997
      mobile/acpi-support: new spell, various acpi scripts for laptops,     bug #13998
      mobile/laptop-mode-tools: update, bug #13995
      gnu/ada: update to 4.2.2
      gnu/fortran: update to 4.2.2
      gnu/g++: update to 4.2.2
      gnu/gcc: update to 4.2.2
      gnu/gcj: update to 4.2.2
      gnu/objc: update to 4.2.2
      mobile/acpi-support: missing depends on radeontool
      xmlrpc-c: cleaned up the spell and updated to latest stable version
      audio-libs/libmp3splt: new spell, library to split mp3/ogg files
      audio-players/mp3splt: version update, slpits into libmp3splt
      gnump3d: version update 3.0
      osmo: update to 0.1.1
      openmotif: moving to z-rejejcted, non-Free license
      audio-creation/snd/: openmotif depends now on z-rejected
      audio-creation/ceres3/: openmotif depends now on z-rejected
      editors/nedit/: openmotif depends now on z-rejected
      ftp/aria2: version update
      mail/dovecot: version update
      mobile/gnokii: version update
      mobile/libsyncml; fixup source urls, version updates
      mobile/libopensync; fixup source urls, version updates
      mobile/libopensync-plugin-syncml; fixup source urls, version updates
      mobile/libopensync-plugin-synce; fixup source urls, version updates
      mobile/libopensync-plugin-sunbird; fixup source urls, version updates
      mobile/libopensync-plugin-python; fixup source urls, version updates
      mobile/libopensync-plugin-palm; fixup source urls, version updates
      mobile/libopensync-plugin-opie; fixup source urls, version updates
      mobile/libopensync-plugin-moto; fixup source urls, version updates
      mobile/libopensync-plugin-kdepim; fixup source urls, version updates
      mobile/libopensync-plugin-irmc; fixup source urls, version updates
      mobile/libopensync-plugin-gpe; fixup source urls, version updates
      mobile/libopensync-plugin-google-calendar; fixup source urls, version     updates
      mobile/libopensync-plugin-gnokii; fixup source urls, version updates
      mobile/libopensync-plugin-file; fixup source urls, version updates
      mobile/libopensync-plugin-evolution2; fixup source urls, version updates
      mail/exim: added support for demime
      dovecot: 1.0.7 update
      kazehakase: version update 0.5.0
      dovecot: updated managesieve patch
      alpine: minor cleanup of BUILD and moving stuff to DEPENDS
      tor: update devel and stable
      libburn-pykix: update to 0.4.0
      libburn-pykix: update to 0.4.0
      dovecot: managesieve patch update 8.3
      dovecot: managesieve patch update 8.3
      anubis: version update 4.1
      monit: update to 4.10
      anubis: version update 4.1
      monit: update to 4.10
      groups: added shadow group
      pam_sotp: new spell, a simple One Time Password PAM module
      groups: minor fix
      security-libs/otpw: new spell, A one-time password login package
      otpw: remove stack-protector

Arjan Bouter (27):
      putty: added desktopfiles
      directfb: various fixes
      rt2500_driver: fixed source dir for cvs builds
      ffmpeg-svn: added swscale option
      typo3: version bump and depends fix
      ffmpeg-svn: added forgotten CONFIGURE, sorry!
      wired: version 0.5
      libsmbios: added spell
      Changelog: I didn't forget the changelog entry for libsmbios. It was on my     todo-list. really! ;)
      dynamite: new spell, pkware extraction libs and tools
      orange: new spell, creates installable cab files
      Changelog: I never forget ChangeLog...
      synce-usb-rndis-lite: new spell usb rndis driver
      cdfs: version 2.6.23, still does not build here
      synce-libsynce: version 0.10.0
      synce-odccm, synce-vdccm: new spells, synce-dccm is split
      synce-dccm: split of *dccm spells
      synce-vdccm, synce-odccm: added PROVIDES for dccm split
      synce-librapi2: version 0.10.0
      synce-rra: version 0.10.0
      synce-serial: version 0.10.0
      synce-libsynce: re-added the long description
      audio_burn: made cdrecord and vorbistools optional and cleaned up DEPENDS
      xmms2: fixed ecore_config naming
      sdl_mixer: fixed (lib)mikmod depends
      dri: added mach64 support
      evolution: it installs unversioned schemas now

Arwed von Merkatz (32):
      howl: fixed compile with current kernel headers, bug 14028
      xawtv: fixed to work with xorg-modular, bug 13014
      howl: forgot to commit the removed BUILD
      goggles: updated to 0.9.1
      pwlib: fixed to work without alsa, bug 14029
      mplayer: use TRACK_ROOT for confdir
      libatomic_ops: new spell
      pulseaudio: updated to 0.9.6
      paprefs: new spell
      alsa-plugins: added optional_depends on pulseaudio
      pavucontrol: new spell
      xmms-pulse: new spell
      gst-pulse: new spell
      xine-lib: added optional_depends on pulseaudio
      pulseaudio: deleted old sig
      mplayer: dependency fixes for live, polypaudio and pulseaudio
      totem: updated to 2.20.1
      ada: updated to 4.2.1
      fortran: updated to 4.2.1
      g++: updated to 4.2.1
      gcc: updated to 4.2.1
      gcj: updated to 4.2.1
      objc: updated to 4.2.1
      Revert "Revert "firefox 2.0.0.8, SECURITY_PATCH=12""
      glibc: remove /usr/include/{asm,asm-generic,linux} symlinks on install
      man: fixed man paths so it doesn't take 5+ seconds to launch man
      gimp: updated to 2.4.1
      pulseaudio: updated to 0.9.7
      pavucontrol: updated to 0.9.5
      paprefs: updated to 0.9.6
      xmms-pulse: updated to 0.9.4
      gst-pulse: updated to 0.9.5

Bearcat M. Sandor (3):
      Initial spell for sndpeak version 1.3.  I set it up as compiling for alsa. You can compile it for jack, but the make command is different.
      updated for new spell sndpeek
      Fixed typo in DEPENDS so it found the kde4 directory

David Kowis (1):
      thunderbird: removing unnecessary depends on gnome-panel     Pulling the entire gnome tree in for thunderbird is t3h 3v1l!

David Michael Leo Brown Jr (35):
      linux updated latest pre 2.6 kernel to rc9
      updated kvm to 45
      linux updated to latest 2.6.23
      kvm updated to 46
      linux updated mm and maintanence patches
      linux updated realtime preempt patches
      fixed url for realtime patches
      fixed signature url
      linux updated reiser4 patches
      linux updated various maintenance patches
      linux added updated smgl-logo patch
      linux updated build process to call out to the linux makefile only twice instead of several places
      linux fixed syntax error in build file
      glibc updated glibc kernel headers to the new version
      forgot a syntax error in FUNCTIONS file
      output correct sum format so cast will detect it
      playing around with the api SOURCEN isn't exported when its set in DETAILS so it didn't work at all before
      Revert "playing around with the api SOURCEN isn't exported when its set in DETAILS so it didn't work at all before"
      Revert "output correct sum format so cast will detect it"
      Revert "forgot a syntax error in FUNCTIONS file"
      Revert "glibc updated glibc kernel headers to the new version"
      glibc updated kernel headers to new version of kernel
      kvm updated to version 47
      gcc added location of linker change when compiling on lib64 systems
      linux updated pre 2.6 kernel patches to 2.6.24-rc1
      dvd+rw-tools fixed undefined INT_MAX from newer glibc headers
      linux updated realtime preempt patchset
      kvm updated to 48
      drm do the depmod against the kernel version in question
      kvm updated to 49
      coreutils glibc 2.7 as well as 2.6 internalize futimens
      kvm updated to 50
      kvm fixed install of bad target
      linux updated realtime preempt patches
      linux updated misc maintenance patches

Elisamuel Resto (15):
      mail/postfix: updated to 2.4.5 (VDA-ng 2.4.5)
      net/bind: DEPENDS removed, DETAILS changed to not require gcc34
      net/shorewall: updated to 4.0.5
      net/shorewall-common: updated to 4.0.5
      net/shorewall-docs-html: updated to 4.0.5
      net/shorewall-docs-xml: updated to 4.0.5
      net/shorewall-lite: updated to 4.0.5
      net/shorewall-perl: updated to 4.0.5
      net/shorewall-shell: updated to 4.0.5
      utils/which: version bump 2.16 -> 2.18
      mail/alpine: new spell, lightweight terminal mail reader like pine
      python-devel/hellanzb: new spell, python usenet file downloader
      net/shorewall and related spells: fix HISTORY file for last update, entry got added to bottom
      archive/par2cmdline: fix for gcc4
      python-devel/bittorrent-bencode: add setuptools to DEPENDS

Eric Sandall (51):
      VERSION: 0.15-test
      conky: Updated to 1.4.7
      meld: Updated to 1.1.5.1
      conky: Optionally depends on wireless_tools for WLAN support
      qtparted: Fails install with multiple make jobs
      FUNCTIONS: Copied get_kernel_config and friends from z-rejected/FUNCTIONS
      ieee80211: Moved from z-rejected (not removed from z-rejected until 2007-12-07)
      mac80211: Added Intel's modified mac80211 wireless subsystem
      iwlwifi: Added Intel's new wireless driver (unlike ipw3945, no userspace daemon is used)
      ieee80211: Remove BUILD code copied from mac80211
      ieee80211: Removed extraneous spaces at end of lines
      iwlwifi: Submit correct HISTORY file
      iwlwifi: Also depends on ieee80211 to work properly
      ieee80211: Added correct linux .config modfication code to BUILD
      iwlwifi: Does *not* need ieee80211, it was a fluke that fixed it
      smgl-fhs: Fix X11 symlinks (commented in Bug #13777)
      smgl-fhs: More fixes to make sure the symlink is not doubled (e.g. /usr/X11R6/lib/X11/X11)
      smgl-fhs: Fix X11 modules (fixes DRI for me)
      smgl-fhs: fhs_mkdir already applies INSTALL_ROOT
      smgl-fhs: Use TRACK_ROOT for symlinks (thanks Jaka :))
      madwifi: SVN URL changed
      sudo: Updated to 1.6.9p6
      vbetool: x86_64 requires CONFIG_IA32_EMULATION and --with-x86emu
      laptop-mode-tools: Cleanup strange characters in init script and cleanup provided install script to not muck with services
      hdparm: Check if the file exists before using it, print the starting tag and the return value
      hdparm: By default have init be quiet, just like our other scripts
      acpi-support: Remove force-reload(), it's causing errors doing boot
      acpi-support: Change LICENSE -> LICENSE[0]
      laptop-mode-tools: Remove force-reload, causes bootup errors
      laptop-mode-tools: Don't look in /usr/local for modules
      laptop-mode-tools: Fix comparing integer to string
      Revert "shadow 4.0.18.1"
      groups: Added netdev:160: for avahi (See https://bugzilla.redhat.com/show_bug.cgi?id=219218)
      avahi: Create netdev group See https://bugzilla.redhat.com/show_bug.cgi?id=219218     Increment PATCHLEVEL to apply fix
      thomas.leonard.gpg: Moved to section level for other Rox apps
      rox-lib2: Added ROX-Apps shared code library
      rox-video-thumbnail: Added ROX-App for video thumbnails via mplayer
      Revert "thomas.leonard.gpg: Moved to section level for other Rox apps"
      thomas.leonard.gpg: Moved from rox to section for other Rox apps
      kvm: Hasn't needed gcc34 for a while (thanks arachnist)
      iwlwifi: 2.6.22+ now includes mac80211 required for iwlwifi
      iwlwifi: Check for CONFIG_FW_LOADER and CONFIG_MAC80211
      iwlwifi: Make that 2.6.23, as that's what I tested with
      Revert "firefox 2.0.0.8, SECURITY_PATCH=12"
      libcdio: Updated to 0.78.2 and use upstream gnu.gpg key
      libsigsegv: Updated to 2.4 (fixes sigalstack check in ./configure with gcc 4.2 and glibc 2.6)
      gnu.gpg: Imported FDAA9CC7 Sam Steingold <sam.steingold@gmail.com> from ftp://ftp.gnu.org/gnu/gnu-keyring.gpg for clisp 2.42
      clisp: Updated to 2.42 (new, unverified upstream key)
      clisp: unset fix no longer required
      VERSION: 0.15-rc
      VERSION: 0.15-0

Florian Franzmann (6):
      windowmanagers/fvwm: updated to 2.5.23
      windowmanagers/fvwm: removed the patchset, fetch it directly
      chat-im/{micq,climm}: deprecated micq in favour of climm
      libs/gloox: new spell
      libs/gloox: added a missing dependency, fixed another and improved the description.
      libs/gloox: moved to chat-libs

George Sherwood (48):
      imagemagick: Updated to version 6.3.6-0
      gscan2pdf: Updated to version 0.9.17
      imagemagick: Updated to version 6.3.6-1
      sqlite: Updated to version 3.5.1
      lyx: Updated to version 1.5.2
      liferea: Updated to version 1.4.5b
      geany: Updated to version 0.12
      hunspell: Updated to version 1.1.12
      code-browser: Updated to version 2.18
      snort: Updated to version 2.8.0.  Updated with new signing key.
      proftpd: Updated to version 1.3.1. Removed old multi-version code     from DETAILS.
      db: Updated to version 4.6.19
      irssi: Updated to version 0.8.12
      qt4: Updated to version 4.3.2. Removed incoporated patch.
      imagemagick: Updated to version 6.3.6-2
      xfwm4: Added upstream patch to fix xfce4 lockups. PATCHLEVEL++
      imagemagick: Updated to version 6.3.6-3
      qca2: Updated to version 2.0.0. Fixed SOURCE_URL
      lynx: Upstream uses releases, but also links it to an unversioned     tarball.  Changed spell to use released tagged tarball. Too     many failed hashes.
      tar: Updated to version 1.19.  Removed upstream incorporated     patch.
      gimp: Updated to version 2.4.0.  Cleaned up DEPENDS for version     2.4.0
      kdevelop: Updated to version 3.5.0
      centerim: Updated to version 20071022
      pidgin: Updated to version 2.2.2
      db: Updated to verison 4.6.21
      ircd-hybrid: Updated to version 7.2.3
      miau: Updated to version 0.6.5
      licq: Updated to version 1.3.5-rc3
      devede: Updated to version 3.3
      abiword: Cleaned up DEPENDS. Can now build devel version without     gnomelibs, but with no printing.
      licq: Updated to version 1.3.5
      goffice-0.5: Added depends libart_lgpl
      gnumeric: Updated DEPENDS to all gnumeric devel to build without     all the gnome libs.  For gnumeric prints also seems to work     without gnome.
      liferea: Updated to version 1.4.6
      tmsnc: Updated to version 0.3.2
      imagemagick: Updated to version 6.3.6-5
      firefox: Updated to version 2.0.0.9. Patch updated also.
      doxygen: Updated to version 1.5.4
      phpmyadmin: Updated to version 2.11.2
      imagemagick: Updated to version 6.3.6-6
      gnomeicu: Updated to version 0.99.14
      psi: Updated to version 0.11
      qca-openssl: Updated to version 2.0.0-beta1.  Added compilation     and build fix.
      sqlite: Updated to version 3.5.2.  Updated SOURC_URL and WEB_SITE
      seamonkey: Updated to version 1.1.6
      imagemagick: Updated to version 6.3.6-8
      php: Updated to version 5.2.5. SECURITY_PATCH++(cherry picked from commit a7b8b5b8792311949588da99f51998836fdd4ec1)
      samba: Updated to version 3.0.27.  SECURITY_PATCH++

Jaka Kranjc (37):
      gcc: 4.2.0     g++ and fortran in the queue
      g++: 4.2.0
      fortran: 4.2.0
      objc: 4.2.0
      ada: 4.2.0
      gcj: 4.2.0
      gcj: add some new depends
      bzr: 0.91 #14045         partial patch from Arvid Norlander
      bzrtools: 0.91.0 #14045
      bzr: made bzrtools suggested to avoid a circular dependency
      enchant: 1.3.0
      cpan: 1.9203 #14051
      xdialog: fixed up and simplified
      xdialog: made gtk+2 required #14043
      kipi-plugins: added arts for disabling #14038
      gwenview: added arts for disabling #14039
      wxgtk: self-conflict #14031
      koffice: added which, needed for kexi docs script #14063
      fluxbox: 1.0
      kde4/FUNCTIONS: factorised common code, indented, fixed update_databases
      seems like this section has a history of its own
      links: update #14022     patch from Martin Klein
      links: 1.00pre21
      libs/ruby-gettext: native Language Support library and tools for Ruby #14073     spell by Cathal Mc Ginley
      libs/ruby-amazon: lib for fetching data from Amazon Web Services #14074
      devel/yaz:     A toolkit for Z39.50/SRW/SRU clients and servers
      a Ruby binding to the ZOOM toolkit #14076
      gnome2-apps/alexandria: GNOME app for managing book collections #14077     spell by Cathal Mc Ginley
      recordmydesktop: 0.3.6
      gtk-recordmydesktop: 0.3.6
      vlock: updated to newest stable and spent some QuAlity time with it
      hal: removed hal-info #14079 (circular dependency and wrong)     (cherry picked from commit 11385724c82e11b7886133d3e8662bfe2780203c)
      Revert "hal-info: correction for enable/disable WLAN killswitch support : removed DEPENDS to avoid a circular dependency, added a config_query_option in CONFIGURE instead"
      hal-info: force_depends on older hal versions, needs 0.5.10+ #14079     other part of the bug     (cherry picked from commit 2fef37cc35fd8a2d15b80037cc9ddd303c5f102d)
      hal: added a force_depends on glibc, needs newer kernel headers than those          that came with glibc 2.4 #14080     (cherry picked from commit ea55a114457eebe25080f8e3709effc50b47f55e)
      openal: fix runtime gcc 4.2 brokeness     fix source* for scm version (switch to svn)     (cherry picked from commit ffff4bd3b39a0cdcbc7497d1cb068fda98861f23)
      as mentioned in the ml:     Revert "reetype2-2.3.5"

Julien ROZO (25):
      kmobiletools : updated version to 0.5.0-beta3, corrected WEB_SITE
      bluez-libs : updated version to 3.19 by applying patch from bug 14023 (http://bugs.sourcemage.org/show_bug.cgi?id=14023), corrected WEB_SITE
      bluez-utils : updated version to 3.19 by applying patch from bug 14024 (http://bugs.sourcemage.org/show_bug.cgi?id=14024), corrected WEB_SITE
      bluez-gnome : updated version to 0.14 by applying patch from bug 14025 (http://bugs.sourcemage.org/show_bug.cgi?id=14025)
      smartmontools : there was a missing "p" in the init.d/smartd script, in the phrase "Stopping smartd"
      kdebluetooth : updated spell to 1.0_beta8, added depends obexftp
      kmobiletools : corrected sha512 sum
      openobex : corrected WEB_SITE
      obexftp : corrected WEB_SITE
      libmal : updated to version 0.44, corrected licence to MPL
      kdesvn: spell updated to version 0.14.0, now builds with cmake
      libconfig : new spell, version 1.2
      ntfsprogs : depends on libconfig if crypto is enabled
      bluez-libs : updated version to 3.20
      bluez-utils : updated version to 3.20
      bluez-hcidump : updated version to 1.40, fix bug 14059
      hal-info: optionally depends on hal (>= 0.5.10) for WLAN killswitch support
      hal-info: oops ! I forgot to commit modified HISTORY
      hal-info: correction for enable/disable WLAN killswitch support : removed DEPENDS to avoid a circular dependency, added a config_query_option in CONFIGURE instead
      bluez-utils: updated to version 3.22
      bluez-libs: updated to version 3.22
      k9copy: updated spell to 1.2.0
      virtualbox-module: moved from utils to kernels; added an INSTALL script with udev rule to put the right permissions on /dev/vboxdrv
      ntp: added a TRIGGERS script, making ntp to be casted on openssl update, if crypto support is enabled
      links: casted on openssl update only if HTTPS support is enabled

Juuso Alasuutari (7):
      jackdmp: corrected WEB_SITE
      mplayer: Removed redundant and broken libdts dependency. Apparently libdca is the _same_     library with a new name: libdts and libdca have the same WEBSITE and the site doesn't     mention libdts. In any case mplayer now uses libdca for DTS support.
      kdebase: Removed warning about paths in kdmrc, they have been made xorg-modular-compliant.
      qjackctl: Added CVS version.
      jack-keyboard: New spell, virtual keyboard that uses JACK MIDI.
      kdelibs4: fixed bug #14053
      pkgconfig: Optionally depend on glib2 to use system GLib. Build takes only 1/10th of the time and executable is half the     size than with included glib.

Ladislav Hagara (66):
      less 408
      claws-mail 3.0.2
      http://www.virtualbox.org/wiki/Linux%20build%20instructions     virtualbox needs bcc and bcc is only a part of our dev86.     bin86 doesn't provide it.     http://lists.ibiblio.org/pipermail/sm-commit/2007-September/012707.html
      claws-mail-extra-plugins: fixed WEB_SITE
      sylpheed 2.4.7
      libpng 1.2.21
      git 1.5.3.4
      pciutils 2.2.7     now provides "make install-lib", I use it     it don't install some .h files, I hope we don't need them     (i386-io-linux.h, internal.h, pread.h, sysdep.h)
      e16 0.16.8.10
      iso-codes 1.5
      man-pages 2.66
      libidn 1.2
      openssl 0.9.8f
      cracklib 2.8.12
      linux-pam 0.99.9.0
      less 409
      m2crypto 0.18.2
      unicap 0.2.17
      ucview 0.16
      camorama 0.19
      tea 17.3.3
      udev 116
      lshw B.02.12.01
      pktstat 1.8.4
      ecryptfs-utils 26
      wtf 20071004
      gv 3.6.3
      seahorse 2.20.1
      shadow 4.0.18.1
      firefox 2.0.0.8, SECURITY_PATCH=12     I can run it only as root, as a normal user I have some problem.     Only my problem?
      openssl 0.9.8g
      bmpx 0.40.13
      virtualbox 1.5.2
      virtualbox-module 1.5.2
      tea 17.3.5
      phpmyadmin 2.11.1.2
      locale - fixed character maps [Bug 14044]
      lftp 3.5.15
      gnupg-interface 0.36
      seamonkey 1.1.5, SECURITY_PATCH=8
      crypto/paperkey: new spell, an OpenPGP key archiver
      pciutils 2.2.8
      crypto/gpgdir: new spell, recursively encrypts/decrypts directories using a GPG key
      keychayn 2.6.8
      dhcpcd 3.1.7
      gnutls 2.0.2, make 2.0 default GNUTLS_BRANCH
      opencdk: make 0.6 default OPENCDK_BRANCH
      thunderbird: ENIGMAIL 0.95.4
      xca 0.6.4
      gnomint 0.1.5, new spell, a certification authority management tool
      usbutils 0.73
      sox 14.0.0
      gawk 3.1.6
      lm_sensors 2.10.5
      curl 7.17.1
      e_dbus: SOURCE_URL was changed
      libgpg-error 1.6
      links-twibright 2.1pre31
      cups 1.3.4
      gnomint 0.3.1
      gnomint 0.3.2
      xsensors 0.60
      alsaplayer 0.99.80
      phpmyadmin 2.11.2.1, SECURITY_PATCH=9     (cherry picked from commit 29feaf541a0fb96ed8c9f20149fa4722802b3384)
      thunderbird 0.95.5
      thunderbird 2.0.0.9

Lalo Martins (10):
      updating pidgin-encryption urls, and adding purple-plugin-pack
      new spell: bittorrent-bencode
      new spell: linuxdcpp
      ChangeLog update for linuxdcpp
      ChangeLog update for bittorrent-bencode (retroactive)
      Fixed xulrunner on non-ia32
      changing all haskell spells to depend on GHC rather than ghc
      disk/gnomebaker -> 0.6.2
      new spell: devel/spidermonkey
      oops, seems I committed some debugging output yesterday -- how     embarrassing

Martin Spitzbarth (11):
      asterisk: Updated to 1.4.12.1
      asterisk.gpg: added key 64FAEBC5 to the keyring
      asterisk-addons: Updated to 1.4.3
      dosfstools: Updated to 2.11
      cpufrequtils: added use of INSTALL_ROOT, minor changes
      hnb: added INSTALL_ROOT, fixed path for manpages
      klibc: fixed path for manpages
      squid: added INSTALL_ROOT, fixed path for manpages
      audacity: added INSTALL_ROOT, fixed path for manpages
      asterisk: forgot to remove a patch file from the grimoire
      asterisk: Updated to 1.4.13, SECURITY_PATCH++, Bug 14035

Mathieu Lonjaret (20):
      bittorrent: 5.0.9
      libtorrent: added dht support, openssl optional, cleaned out stuff
      rtorrent: added dht support
      proftpd: 1.3.1rc3
      fsp: update to 2.8.1b24, added conf file and docs
      fspclient: update to 0.91.0
      dmenu: 3.3
      dwm: 4.5
      libixp: 0.3
      alsaplayer: 0.99.90-rc3
      libtorrent: dht patch defaults to no, explanation for openssl
      rtorrent: dht patch defaults to no, depends on automake-1.9
      xmlrpc-c: bogus configure for unicode
      rtorrent: added xmlrpc-c opt dep
      libtorrent: 0.11.9 (and dht disabled, no patch for this version available yet)
      rtorrent: 0.7.9 (and dht disabled)
      libixp: added devel version pulled with hg
      wmii: explanation for dmenu depends
      wmii: update to 20071003, libixp dep, plan9port opt dep
      libixp: created DEPENDS, added mercurial dep

Philippe Caseiro (6):
      Updating deluge spell to version 0.5.6
      Updating deluge's DETAILS to version 0.5.6.1
      Updating deluge's HISTORY
      Updating deluge spell to version 0.5.6.2
      Fixing deluge spell with new SOURCE-DIRECTORY value
      Fixing my name on HISTORY file :D

Pol Vinogradov (30):
      xfce/xfburn: new spell, a GUI CD burning frontend for XFCE
      http/gnash:
      http/gnash:
      libs/sdl_gfx:
      video/mplayer:
      disk/fuse:
      x11/xneur:
      gnome2-apps/gxneur:
      kde-apps/kxneur:
      audio-drivers/alsa-driver:
      audio-drivers/alsa-firmware:
      audio-drivers/alsa-lib:
      audio-drivers/alsa-oss:
      audio-drivers/alsa-plugins:
      audio-drivers/alsa-tools:
      audio-drivers/alsa-utils:
      audio-drivers/pyalsa:
      libs/ode:
      video/vlc:
      utils/watchdog:
      utils/watchdog:
      http/iceweasel: new spell, the GNU version of the Firefox browser
      http/gnash:
      gnome2-libs/librsvg2:
      video/vlc:
      utils/watchdog:
      shell-term-fm/mc:
      http/iceweasel:
      disk/hdparm:
      graphics-libs/rmagick:

Remko van der Vossen (8):
      crypto/signing-party: 4.0.12
      perl-cpan/class-methodmaker: 2.0.8
      Added my key (Remko van der Vossen/1ccf3307) to the gurus keyring
      chat-im/centerim: 20071003
      chat-im/centerim: Forgot signature file in commit a497588837633d3ee42cb0fa34bbca8c4fd7126a
      disk/cdlabelgen: 4.0.0 and made man pages install in $BASEDIR/share/man
      disk/cdlabelgen: moved Makefile fix to PRE_BUILD
      disk/cdlabelgen: add default_pre_build back into PRE_BUILD

Robin Cook (92):
      gtk-doc: updated to 1.9
      gcalctool: updated to 5.20.1
      telepathy: updated to 0.2.0
      libtelepathy: removed sig file accidently added.
      telepathy-glib: updated to 0.6.0
      telepathy-mission-control: updated to 4.42
      telepathy-glib: remove unneccessary sig file
      passepartout: New Spell
      libwpd: new spell
      libwps: new spell
      libwpd: corrected keywords
      libwpg: new spell
      glibmm: updated to 2.14.1
      gtkmm2: updated to 2.12.1
      libsoup: updated to 2.2.101
      galculator: updated to 1.3.1
      devhelp: updated to 0.16.1
      bug-buddy2: updated to 2.20.1
      orca: updated to 2.20.0.1
      libgringotts: updated to new site etc.
      gringotts: updated to 1.2.9pre2
      gnome2-user-docs: upated to 2.20.1
      libgnomecanvas: updated to 2.20.1
      orbit2: updated to 2.14.10
      glib2: updated to 2.14.2
      pango: updated to 1.18.3
      gail: update to 1.20.1
      libgnome: updated to 2.20.1
      libgnomeui: updated to 2.20.1
      libbonobo: 2.20.1
      libsoup: updated to 2.2.102
      gconf2: updated to 2.20.1
      gtkhtml2: updated to 3.16.1
      evolution-data-server: updated to 1.12.1
      vino: 2.20.1
      gnome-spell: updated to 1.0.8
      at-spi: updated to 1.20.1
      gnome-themes: updated to 2.20.1
      gnome-keyring: updated to 2.20.1
      gnome-control-center: updated to 2.20.1
      gnome-system-monitor: updated to 2.20.1
      gnome-menus: updated to 2.20.1
      gnome-session: updated to 2.20.1
      gnome-desktop: updated to 2.20.1
      dasher: updated to 4.6.1
      gdm2: updated to 2.20.1
      libwnck: updated to 2.20.1
      gtk-engines2: updated to 2.12.2
      gnome-games2: updated to 2.20.1
      gnome-panel: updated to 2.20.1
      evolution: updated to 2.12.1
      gtk+2: updated to 2.12.1
      gtksourceview: updated to 2.0.1
      libgnome: updated to 2.20.1.1
      libgnomeui: updated to 2.20.1.1
      accerciser: updated to 1.0.1
      gok: updated to 1.3.7
      gcalctool: updated to 5.20.2
      tomboy: updated to 0.8.1
      deskbar-applet: updated to 2.20.1
      file-roller: 2.20.1
      gedit: updated to 2.20.2
      eog2: updated to 2.20.1
      gthumb2: updated to 2.10.7
      gedit: updatedto 2.20.3
      epiphany: updated to 2.20.1
      epiphany-extensions: updated to 2.20.1
      evolution-exchange: updated to 2.12.1
      evince: updated to 2.20.1
      sound-juicer: updated to 2.20.1
      gnome-pilot: changed control-center2 to gnome-control-center
      libgnomecanvas: updated to 2.20.1.1
      java-access-bridge: added missing depends at-spi and libbonobo
      goffice-0.5: updated to 0.5.1
      jigdo: updated to 0.7.3
      jigdo: actually delete PRE_BUILD
      gnumeric: updated devel version to 1.7.13
      libgda3: updated to 3.1.2
      libgnomedb3: updated to 3.1.2
      mergeant: updated to 0.67
      glibmm: updated to 2.14.2
      anjuta: updated to 2.2.2
      poppler-data: updated to 0.1.1
      libsoup: updated to 2.2.103
      orca: updated to 2.20.1
      gimp-help-2: updated to 0.13
      gst-pulse: added lynx as optional depends
      paprefs: added lynx as optional depends
      pavucontrol: added lynx as optional depends
      goffice-0.5: updated to 0.5.2
      gnumeric: updated devel to 1.7.14
      svgalib: add patch to compile with 2.6.23 kernel     (cherry picked from commit c30e04b1e1903ee31ddfd97f82b5c978247a7141)

Thomas Orgis (3):
      devede: update to 3.2, also fixing checksum failure
      unsermake: switch to a mirrored tarball; SVN is dead
      kdenlive: Fix the install by using the 0.5-1 source tarball; now depends on unsermake.

Treeve Jelbert (166):
      digikam-0.9.3-beta1
      flamerobin-0.8.0
      fuse - fix for latest kernel
      wine-0.9.47
      libkdcraw-0.1.2
      kipi-plugins-0.1.5-beta1
      soprano-1.95.0-beta2
      cheetah-2.0
      poppler-0.6.1
      gdb-6.7
      libiodbc-3.52.6
      ksquirrel-libs-0.7.2
      ksquirrel-0.7.2
      partimage-0.6.7_beta2
      libpng  1.2.22
      qt4pas-V1.53_Qt4.3.1
      libquicktime-1.0.1
      perl-cairo-1.043
      dazuko-2.3.4
      ntfsprogs-2.0.0
      perl-gtk2-1.161
      perl-glib-1.161
      kipi-plugins - remove imlib2 dependency
      cupsddk-1.2.3
      ntfs-3g-1.1004
      arts-1.5.8
      kdelibs-3.5.8
      kde-i18n-3.5.8
      kde-profile-3.5.8
      kdebase-3.5.8
      kdeadmin-3.5.8
      kdenetwork-3.5.8
      qt4 - update snapshot version
      kdepim-3.5.8
      kdeaccessibility-3.5.8
      kdeaddons-3.5.8
      kdeartwork-3.5.8
      kdebindings-3.5.8
      kdeedu-3.5.8
      kdemultimedia-3.5.8
      kdesdk-3.5.8
      kdetoys-3.5.8
      kdewebdev-3.5.8
      kdeutils-3.5.8
      kdegraphics-3.5.8
      kdegames-3.5.8
      qdbm-1.8.76
      fuse-2.7.1
      firebird-2.1.0.16780-Beta2
      kdegames - missing hash
      sqlalchemy-0.4.0
      kdelibs4-3.94.0
      kdepimlibs4-3.94.0
      kde4-l10n
      kde4-profile
      kdebase-workspace4
      kdegames4-3.94.0
      kdegraphics4-3.94.0
      flamerobin-0.8.1
      kdebase - fix install
      kdegames - fix hash
      flamerobin - missing BUILD
      strigi - update profile script
      gramps-2.2.9
      kde4 - section files
      kdeedu4-3.94.0
      kdemultimedia4-3.94.0
      kdeutils-3.94.0
      kdetoys4-3.94.0
      kdeadmin4-3.94.0
      splix-1.0.2
      kdenetwork4-3.94.0
      kde4/plasma - new spell
      kdebase4-3.94.0
      kdepim4-3.94.0
      kdebindings4-3.94.0
      koffice2-1.9.94
      clucene - fix install of config.h
      sword-1.5.10
      kdeaccessibility4-3.94.0
      kdesdk4-3.94.0
      newt-0.52.7-4.fc8
      qt4pas-V1.54_Qt4.3.1
      imlib2 -fix bug #14062
      kde4/FUNCTIONS
      wine-0.9.48
      paste-1.5
      kmplayer-0.10.0a
      mercurial-0.9.5
      libzip-0.8
      kdeutils4 - extra depends
      dejavu-ttf-2.21
      ntfs-3g-1.1030
      add kde4 group
      kdebase-workspace4  - update desktop settings
      kdebase-workspace4 - fix typo
      strigi-0.5.7
      gdb-6.7.1
      redland - db is optional
      telepathy-sofiasip-0.4.3
      sofia-sip-1.12.7
      hal-0.5.10
      hal-info-20071030
      dbus-python-0.82.3
      kdelibs-3.95.0
      kdepimlibs4-3.95.0
      kdebase-workspace4-3.95.0
      plasma-3.95.0
      kdebase4-3.95.0
      kdebase4-runtime-3.95.0
      kde4-l10n-3.95.0
      kde4-profile-3.95.0
      kdegames4-3.95.~
      kdegraphics4-3.95.0
      kde4/KDE_DEPENDS - update depends
      kdebase-workspace4 - fix syntax
      kdeadmin4-3.95.0
      kdemultimedia4-3.95.0
      kdenetwork4-3.95.0
      kdeutils4-3.95.0
      kdeedu4-3.95.0
      kdebase-workspace4 - update kde4.sh
      kdetoys4-3.95.0
      kdesdk4-3.95.0
      kde4 - update depends
      kdepim4-3.95.0
      kdebindings4-3.95.0
      kdeaccessibility4-3.95.0
      util-linux-2.13.0.1
      git-1.5.3.5
      turbojson-1.1.1
      pastedeploy-1.3.1
      turbogears-1.0.4b2
      setuptools-0.6c7
      simplejson-1.7.3
      digikam-0.9.3-beta2
      photoprint  0.3.6
      xml-simple-2.18
      xml-sax-expat-0.39
      xml-sax-0.16
      module-init-tools-3.4
      turbogears - adjust depends
      k3b-1.0.4
      k3b-i18n-1.0.4
      odbcjdbc-beta-2.0.0144
      elixir  0.4.0
      dabo-0.8.2
      sptk-3.5.6
      ksquirrel-libs-0.7.3
      ksquirrel-0.7.3
      psmisc-22.6
      kpowersave-0.7.3
      faac-1.26
      faad2-2.6.1
      kphotoalbum-3.0.2
      openfst-beta-20070801
      xaralx-0.7r1783
      ntfs-3g-1.1104
      version-0.74
      x264-20071104-2245
      xmltv-0.5.50
      ksquirrel-0.7.4
      ksquirrel-libs-0.7.4
      koffice - security update     (cherry picked from commit f6e59095654134f506789badf9662ae497f99f67)
      kdegraphics - secrity fix #14089     (cherry picked from commit e34a627f28528886475ee58ba01452e56ae4c717)
      poppler-0.6.2   forgotten files     (cherry picked from commit 3f7a3956b42d3dca3ea42ec3bd665ad0f432f84e)

Vlad Glagolev (13):
      acpid: updated to version 1.0.6
      acpid: fixed history for PRE_BUILD
      leafpad: update to 0.8.12
      tagtool: updated to 0.12.3
      rapidsvn: updated to 0.9.4 + lots of fixes
      xlockmore: update to 5.25 + cleanup
      poedit: updated to 1.3.7     added myself to gurus.gpg
      added my key
      poedit: delete sig of the previous source
      transmission: fast and powerful BitTorrent client. added (0.91).
      asunder: simple GTK+2 CD ripper and encoder. added (0.9).
      tkdvd: GUI for dvd+rw-tools written in TCL/Tk. added (4.0.7).
      thunar: dep-fixes     libxfcegui4: dep-fixes     ChangeLog: 'new spells' log for my previous commits (sorry)
```

[0] Generated with: `git shortlog --no-merges stable-0.14-3..stable-0.15-0`
