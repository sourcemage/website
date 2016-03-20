title: Stable-0.14 released
author: sandalle
category: news
date: 2007-10-17
tags: [grimoire]
---
Stable grimoire version 0.14 has been released!

As usual, users of stable merely need to run `sorcery system-update`. Spells listed on the [0.14 release page](/Grimoire/stable/0.14) were tested and qualified to have no known defects of "gating" severity at the time of this release.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.14.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.14.tar.bz2.asc>.

I would like to thank Jaka Kranjc (lynx), Martin Spitzbarth (mar_s), and Mathieu Lonjaret (lejatorn) for helping test spells.

In case anyone is interested, here's the shortlog between 0.13 and 0.14[0]:

```
Alexander Tsamutali (24):
      devel/ghc: updated to 6.6.1
      new section: haskell
      haskell/haskell-mtl: new spell, monad transformer library
      haskell/haskell-x11: new spell, a binding to the X11 graphics library
      haskell/haskell-x11-extras: new spell, missing Haskell bindings to                                 the X11 graphics library
      windowmanagers/xmonad: new spell, a lightweight X11 window manager
      wm-addons/xmobar: new spell, a minimalistic text based status bar
      protected, volatiles: Added ghc's package.conf
      haskell/FUNCTIONS: Modified default_install to install *.cabal files     haskell/HASKELL_{POST_REMOVE,PRE_RESURRECT,POST_RESURRECT}:     Added to fix many possible problems.
      devel/ghc: Added PRE_RESURRECT, POST_RESURRECT to protect package.conf
      haskell/haskell-mtl:       POST_REMOVE: Added to unregister package with ghc-pkg       PRE_RESURRECT, POST_RESURRECT: Added to protect package.conf and       also register package with ghc-pkg
      haskell/haskell-x11:       POST_REMOVE: Added to unregister package with ghc-pkg       PRE_RESURRECT, POST_RESURRECT: Added to protect package.conf and       also register package with ghc-pkg
      haskell/haskell-x11-extras:       POST_REMOVE: Added to unregister package with ghc-pkg       PRE_RESURRECT, POST_RESURRECT: Added to protect package.conf and       also register package with ghc-pkg
      haskell/haskell-quickcheck: a library for automatic testing of Haskell programs
      haskell/haskell-html: new spell, a Haskell HTML combinator library
      devel/darcs: updated to 1.0.9, added some missing dependencies
      python-devel/django: added option to install bash completion
      python-devel/django: remade installation of bash completion
      haskell/haskell-x11-extras: updated to 0.3
      windowmanagers/xmonad: updated to 0.3
      x11-toolkits/kiwi: updated to 1.9.16
      gnome2-apps/gazpacho: updated to 0.7.2
      python-devel/python-markdown: new spell, a Python implementation of Markdown
      shell-term-fm/sakura: updated to 1.2.1

Andraž Levstik (42):
      dovecot: update to 1.0.3, MANAGESIEVE update
      dovecot: forgot the SECURITY_PATCH
      exim: use _list not _multi
      exim: update to 4.67
      mailx: update to 12.3
      dzen2: version update
      tor: version update and SECURITY update
      libetpan: version update 0.51
      dzen2: update to 0.8.0
      tor: update dev to 0.2.0.4-alpha, SECURITY_PATCH++
      dropbear: version update 0.50
      dosemu: just some minor fixups and adding disable_pic
      net/dnrd: new spell, a very usefull dns proxy and server
      gxmms2: made it work
      pan: version update 0.132
      dovecot: updated MANAGESIEVE patch
      dzen2: version update 0.8.5
      dzen2: added svn version
      Merge
      backup-manager: update to 0.7.6
      fusepod: new spell fuse FS for iPod access
      fusepod: minor fixups
      ffmpeg-svn: sync the DEPENDS file with regular ffmpeg spell
      gnash: update to 0.8.1, upstream gpg, other fixups/revamping
      video/ffmpeg-svn: forgot some stuff tnx Jaka
      pilot-link: upstream sigs, various cleanups and revamps, tcl option     doesn't build so disabled it for now
      tor: version updates for both devel and stable
      agg: new spell, a graphics library
      gnupod: version update 0.99.3
      mesalib: minor depends fixups to make it build properly
      security/skey: new spell, skey lib and utilities
      security/pam_skey: new spell, pam otp module
      dspam: added installation of pref.h
      dovecot: always install dev headers
      slim: added pam support and use our CFLAGS
      science/viking: new spell, a google/terraserv/openstreetmap map viewer
      science/viking: new spell, a google/terraserv/openstreetmap map viewer
      gnash: minor bugfixes, thanks to Bearcat
      gnupod: version update
      gnash: minor fixup
      http/kazehakase: version update
      mesalib: minor fixup for depends

Arjan Bouter (16):
      gxmms2: added git version
      golem: version bump to 0.0.6 , fixed depends and fixed building
      grdesktop: removed unneeded dep
      thunderbird: missing dep on gnome-panel
      soundtracker: re-enabled alsa
      enthrall: version 0.6, added jwm support
      squirrelmail-notes: fixed install
      jwm: separated the menu from the config and added session files for the     login-managers
      grep: made texinfo optional
      postgres: added optional dep on openldap
      amsn: version bumped to 0.97RC1
      dovecot: create a dovecot account for the default config
      i wonder why this was left out of my prev commit...
      soundtracker: version 0.6.8 and added explanation for alsa
      gnucash: made texinfo an optional dep
      soundtracker: removed the now standard BUILD

Arwed von Merkatz (46):
      sudo: updated to 1.6.9p3
      libgnomekbd: remove -Werror from Makefiles
      rxvt-unicode: optional_depend on libxft with xorg-modular
      lesstif: don't install stuff to /usr/LessTif
      ghostscript: default to dispelling espgs
      swfdec: updated to 0.5.2
      swfdec-mozilla: updated to 0.5.2
      brasero: updated to 0.6.1
      udev: only run coldplugging if udev is used
      gtk+2: compile with cups 1.3
      pkgconfig: removed our pc-path hacks, upstream works fine
      vala: updated to 0.1.3
      net-tools: patch so it works with vanilla kernel headers
      evince: updated to 2.19.92
      tracker: updated to 0.6.2
      tracker: support xdg-open
      wxgtk: updated to 2.8.5, added bugfix for 2.6.4
      mplayer: only support dvdnav in release version
      transcode: updated to 1.0.4
      gnumeric: don't chain persistent_read with && or the spell fails if gnumeric2 vars aren't set
      init.d: made telinit work if a script exists in more than one runlevel
      osmo: new spell
      faad2: conflict with self
      netpbm: fixed build with xorg modular
      Revert "libsigc++: updated to 2.1.1"
      gnome-sharp: hardcode gtkhtml pkgconfig name again
      courier: removed obsolete options
      mozilla: const correctness fixes for changed freetype2 api
      libgphoto2: unbreak hal support if no camera is selected
      pango: fix check for xorg-modular
      e17: fixed xorg-modular check
      transfig: fixed xorg-modular check
      gdm2: fixed xorg-modular check
      freewrl: fixed xorg-modular check
      imagemagick: fixed xorg-modular check
      tgif: fixed xorg-modular check
      xulrunner: fixed xorg-modular check
      ami: fixed xorg-modular check
      iiimf-canna: fixed xorg-modular check
      scim: fixed xorg-modular check
      xaw3d: fixed xorg-modular check
      tightvnc: fixed xorg-modular check
      xfwm4: fixed xorg-modular check
      sensors-applet: fixed xorg-modular check and added missing CONFIGURE
      xawtv: fixed to work with xorg-modular, bug 13014
      goggles: updated to 0.9.1

Bearcat M. Sandor (8):
      MythTV: Updated CONFIGURE and BUILD to add DVB functionality
      Updated to version .20.2. This will allow use of the Schedules Direct grabber which replaces DataDirect.
      Updated mythweb to 0.20.2
      Updated Mythmusic to 0.20.2
      Updated qloud to 0.22
      Updated espeak to 1.29
      New Spell! Myththemes version 0.20.2
      According to the website for Virtualbox bin86 and dev86 work equally well, so i changed the "dev86" to LD86.

David Kowis (30):
      Adding spell shorewall-common
      Adding spell shorewall-shell
      Adding spell shorewall-perl
      Adding spell shorewall-docs-html
      Adding spell shorewall-docs-xml
      Adding spell shorewall-lite
      shorewall-shell: heh, don't need to depend on all this.
      shorewall-perl: only needs to depend on perl
      shorewall-perl: fixed the download URLs
      shorewall-common: fixing SOURCE_URLs
      shorewall-shell: fixing download URLs
      shorewall-docs-html: fixing download URLs
      shorewall-docs-xml: Fixing download URLs
      shorewall-lite: fixing download URLs
      shorewall-lite: DOH! fixing RELEASE value so it can download
      shorewall-shell: fixing RELEASE variable
      shorewall-perl: fixing RELEASE variable
      shorewall-docs-xml: Fixing RELEASE variable
      shorewall-common: fixing RELEASE variable
      shorewall-docs-html: fixing RELEASE variable
      shorewall-lite: adding a conflicts with shorewall-common
      shorewall-lite: dOH! needs to be executable
      shorewall-common: making it conflict with shorewall-lite
      shorewall: Transforming the spell into a profile spell     Makes casting shorewall still work, and will still work for upgrades
      shorewall-common: Moved the docs depends to the shorewall spell
      Adding prepare
      shorewall: Had the wrong syntax for the PREPARE stuff
      shorewall: Fixed PREPARE for reals this time
      iptables: update grsec patch to 1.3.5, it also applies to 1.3.8 with a small hax     Added the small hax ;)
      Changelog entry for the new shorewall suite

David Michael Leo Brown Jr (89):
      linux updated mm patches
      linux updated pre 2.6 patches
      util-linux updated ng to rc3
      linux updated maintenance patches
      linux updated mm patches
      linux updated mm patches again"
      linux updated pre 2.6 kernel patch
      linux updated maintenance patches
      cups fixed treeve's syntax errors
      kvm updated to version 35
      linux updated latest mm patches
      removed across BUILD/INSTALL push and pop directory operations. sorcery guarantee's the pwd across build/install but not the directory stack hasn't been this way for a long time.
      linux updated pre 2.6 patches
      util-linux updated testing version to 2.13, not sure if this is considered testing anymore... :\
      linux updated latest mm patches
      linux updated latest pre 2.6 kernel
      net-tools added BRIDGE_PORTS variable so that bridges can be created around interfaces
      netconf added BRIDGE_PORTS variable to netconf
      Revert "netconf added BRIDGE_PORTS variable to netconf"
      netconf added BRIDGE_PORTS variable
      net-tools updated patchlevel from previous commit
      linux-initramfs updated mkinitrd to use cpio instead of gen_init_cpio from the kernel
      gtkmm2 updated to work with newer gnome2 beta version
      glibmm updated for latest gnome beta to work
      gnome-system-monitor added depends on gtkmm2
      kvm updated to version 37
      linux-initramfs forgot to quiet the pushd/popd's and remove the cpio root
      linux updated pre 2.6 kernel patches
      xrdp updated to 0.4.0
      xrdp added some depends that's needed
      kvm updated to 38
      audit new spell for linux auditing system
      util-linux enabled selinux for ng stuff and added a little patch for when LC_ALL doesn't seem to be defined
      coreutils added selinux patch
      coreutils fixed name of selinux patch in PRE_BUILD oopse
      coreutils fixed selinux patch didn't apply cleanly against hostname patch
      fixed selinux patch again... *sigh*
      coreutils added selinux option to the configure command
      coreutils added glibc 2.6.1 fix for futimens function
      forgot about the default n placement in the function arguments
      selinux/pam don't seem to like useradd/groupadd commands being run with LD_PRELOAD on so back it up and execute the command
      coreutils fixed PRE_BUILD check for enableing the patch or not
      coreutils fixed more selinux stuff from last night... need to stop coding like mad when its too late
      simpleinit-msb added selinux patch for loading selinux policies
      perl-fuse updated bindings for fuse in perl
      fuse-python updated to version 0.2
      fuse-python fixed hash sum for source
      seedit new spell for editing selinux policies
      cpio added glibc 2.6.1 futimens patch so it will compile with glibc 2.6.1
      gzip added internalization of futimens patch for glibc 2.6.1 compatability to gzip
      gzip should have been the gzip patch not the cpio one
      gedit updated to new 2.19.92 along with the rest of gnome beta
      firefox patch for updated cairo
      seedit updated to make it work hopefully
      seedit fixe python install to use python2.5 instead of python2.4
      kvm updated to version 40
      linux updated latest mm patches
      firefox some of the lines in DETAILS were left commented, uncommented them
      Oopse probably should reexport LD_PRELOAD for installwatch
      linux updated pre 2.6 kernel patches
      kvm updated to 41
      kvm updated to 42
      linux-initramfs swapped out symlinks for hard links and removed some of the symlinked dirs... no more /sbin or /usr/sbin just /bin and /usr/bin
      linux updated maintenance patches
      cryptsetup-luks added building static cryptsetup for use in initrd's
      kvm updated to 44
      mkinitrd added support for cryptsetup additions for root crypto support
      linux-initramfs fixed some goof ups and added some more comments with the optional depends
      linux-initramfs wrapped copy parts in the variables it should have been to begin with
      Revert "glibc: Fix Bug #14004 (fails to find acceptable grep)"
      merged the big update of 2.6.1 into test
      merged in tests from lynx commit (I think)
      merged arwed's fixes for GLIBC_ARCH variable
      glibc removed GLIBC_ARCH altogether its only getting set and not used anywhere
      glibc fixes syntax errors as a result of removing GLIBC_ARCH
      glibc minor fixes of old bugfix patches already applied in newer versions
      glibc more iffy merges from 2.6.1 update not needed patches
      linux updated mm patches
      linux updated latest pre 2.6. kernel patch
      updated mm patches
      linux updated maintenance patches
      anjuta updated stable to 2.2.1
      linux updated maintenance patches
      init.d mountall.sh added luks encrypted partition opening to mountall.sh
      linux updated mm patches
      cobbler and koan new nifty packages for managing repositories kickstarts preseeds networking pxeboot dhcping all of it
      linux-initramfs removed redundant dm-mod addition, dm-crypt depends on dm-mod
      elfutils fixed file offset bits problem in linux-kernel-modules.c undef __USE_FILE_OFFSET64 makes it work
      elfutils fixed patch location of files didn't work right

Elisamuel Resto (22):
      gurus.gpg: Added myself (0x18615F19) to the gurus.gpg keyring
      libs/elfutils: update to 0.128, fix bug #13767, fix upgrade error, update sigs
      libs/elfutils: fixed a typo in SOURCE2_URL[1]
      chat-im/pidgin: updated to version 2.1.0
      chat-im/pidgin: forgot to remove old signature
      libs/libstroke: fix for bug #13146 (no detection for x64)
      xfce/xfce4-toys: deprecation cycle target release reached, removing. (Bug #13674)
      ChangeLog: forgot to state the xfce4-toys removal in the ChangeLog
      utils/pfqueue: new spell, console-based tool for managing MTA queued messages
      ChangeLog, net/sfllaw.gpg, net/wlach.gpg: upstream maintainer change (replaced keyrings)
      net/wvstreams: updated version to 4.4, changed SOURCE_URL and SOURCE2_URL to match upstream, changed gpg keyring name
      net/wvdial: updated version to 1.60, changed SOURCE_URL to match upstream, changed gpg keyring name
      graphics/inkscape: added PyXML (Bug #13291) and numPy as optional dependencies
      gnome2-libs/java-access-bridge: fixed broken check for X11-LIBS in DEPENDS
      libs/lrmi: install vbetest utility that comes with lrmi
      doc/evince: upstream wants specifically 0.5.9, we have 0.5.91 and no versioned spells, so sedit the requirement and it worked fine.
      audio-players/audacious: removed audacious-plugins dependency (Bug #13958)
      net/samba: fix python bindings failing to cast (Bug #13967)
      disk/parted: fixed compile error when warnings were treated as errors
      crypto/opencdk: Old SOURCE_URL was no longer valid
      Revert "crypto/opencdk: Old SOURCE_URL was no longer valid"
      mail/ssmtp: created, added openssl as a optional dep for SSL/TLS support

Eric Sandall (95):
      VERSION: 0.14-test
      l2a: Added a simple LaTeX->ASCII conversion tool
      eclipse: Updated to 3.3
      eclipse-cdt: Updated to 4.0.0 for eclipse 3.3
      eclipse-cdt-sdk: Now part of eclipse-cdt
      evas: Added optional dependency on glew
      nfs-utils: Allow for specifying the ports these services start on (for NFS through a firewall)
      cdemu-daemon: Depends on sysfsutils
      git: Updated to 1.5.2.5
      git: Fix a typo in the date
      sudo: Updated to 1.6.9p4
      kcpufreq: A KDE CPUfreq applet
      polyester: Updated to 1.0.2
      qtcurve-kde3: New widget style for QT/KDE3
      Add forgotten polyester GPG signature and fix ChangeLog entry for kcpufreq
      counter-linux: Added an installer for the Counter Linux.org script
      mdadm: Updated to 2.6.3
      tomcat: Missing dependency on z-rejected for some packages
      jakarta-regexp: Fix missing parameters for grimoire dependency
      jakarta-log4j: Fix missing parameters for grimoire dependency
      bochs: Updated to 2.3.5
      mpich2: Updated to 1.0.6
      wpa_supplicant: Also work for non-associated off/any ESSIDs
      glibc: Fix Bug #14004 (fails to find acceptable grep)
      ppp: Requires group ppp to exist
      xml-libxml: Fails to install with multiple make jobs
      xml-libxml: HISTORY date fix
      galago-sharp: Depends on xml-libxml and dbus-mono
      kdebase-workspace4: X11-SERVER dependency is redundant (see KDE_DEPENDS)
      xfce4-mixer: Fails to compile with multiple make jobs
      pidgin: Fails to compile with multiple make jobs
      kdebase-workspace4: Make sure /usr/share/xsessions is a directory before copying
      e_modules: e_module-devian no longer exists
      e_dbus: Depends on ecore
      gimp: That's ASCII, not Ascii ;)
      e-emotion: Optionally depends on gst-ffmpeg
      gimp: Uses gimp-print, not gutenprint, for printing support
      gst-plugins-good: It's ASCII, not ascii ;)
      e-emotion, gst-plugins-good: e-emotion may optionally use gst-plugins-good built with libcdio for CDDA support
      915resolution: Clear out 386 prebuilt 915resolution.o before compiling
      xaw3d: Fails with multiple make jobs
      evolution: Depends on libxml2 built with python support (sub_depends already there for it :))
      trm: Remove incorrect Metadata:: qualification (gcc 4.1+ now errors on this)
      gst-plugins: Added optional dependency on x264
      java-access-bridge: Need to source /etc/profile.d/java.sh before building
      elfutils: Updated to 0.129. Include portability patch to avoid issues in the future
      alsa-driver, alsa-lib: Updated to 1.0.15rc2 (fixes suspend/resume on my hda-intel)
      nss: Fails with multiple make jobs
      xml-sax-expat: Fails to install with multiple jobs
      meanwhile: Added Lotus IM/Sametime protocol library
      pidgin: Optionally depends on meanwhile for Lotus IM/Sametime protocol
      uml_utilities: Depends on fuse
      net-snmp: Fails to compile with multiple make jobs
      kpowersave: Now hosted with powersave, website and all
      wlassistant: Updated to 0.5.7
      kwlaninfo: Updated to 0.9.5, depends on arts, and use KDE_* generic scripts
      kpowersave: Fails with multiple make jobs, fix website
      Revert "texinfo: Updated to version 4.11"
      binutils: Adding texinfo as a dependency (See Bug #14015)
      ifplugd: Fix compilation on x86_64 with glibc 2.6
      reiserfsprogs: Updated to 3.6.20
      blender: Updated to 2.45
      net/isc.gpg: Added Internet Systems Consortium GPG key 0x1BC91E6C (VERIFIED_KEY)
      bind-tools: Updated to 4.4.1-P1 (use upstream GPG key)
      bind: Updated to 9.4.1-P1
      gnome2-profile: Optionally depend on gnome-power-manager
      evolution: Removed deprecated services file
      gnome2-{apps,libs}, gnome2-*/*: Fix Bug #14014 (packages with G_SCHEMAS defined should *not* fail if the schema cannot be removed during pre_remove)
      horde: Updated to 3.1.4
      imp: Updated to 4.1.4
      chora: Updated to 2.0.2
      gollem: Updated to 1.0.3
      kronolith: Updated to 2.1.5
      ingo: Updated to 1.1.3
      nag: Updated to 2.1.3
      turba: Updated to 2.1.4
      passwd: Updated to 3.0.1
      ant: Ant requires Java, so make sure it can find it
      java/java-functions: Remove extra whitespaces (cosmetic)
      java/java-functions: Use the provided profile.d scripts for setting JAVA_HOME and ANT_HOME
      j2ssh: Added a Java SSH tools suite
      java/java-functions: Force symlink creation
      jeta: Added HORDE Java SSH plugin
      ifplugd: Treat ifplugd.action as a configuration file as well
      maxima: Updated to 5.13.0
      Revert "glibc more iffy merges from 2.6.1 update not needed patches"
      Revert "glibc minor fixes of old bugfix patches already applied in newer versions"
      Revert "glibc fixes syntax errors as a result of removing GLIBC_ARCH"
      Revert "glibc removed GLIBC_ARCH altogether its only getting set and not used anywhere"
      Revert "merged arwed's fixes for GLIBC_ARCH variable"
      Revert "merged in tests from lynx commit (I think)"
      Revert "merged the big update of 2.6.1 into test"
      Revert "Revert "glibc: Fix Bug #14004 (fails to find acceptable grep)""
      VERSION: 0.14-rc
      VERSION: 0.14-0

Ethan Grammatikidis (7):
      libs/libixp:	rewrote long desc for clarity
      libtelepathy: more delinting
      btsco, decibel, flite, ilbc-rfc3951, kdeaccessibility, libjingle-tapioca:     	DETAILS: delinting long desc
      bubblemon-dockapp: DETAILS delint
      yiff: DETAILS: delinting
      w3m: CONFIGURE question clarified.
      firefox: firefox script: removed obsolete xfeDoCommand code

Florian Franzmann (19):
      wm-addons/wmnd: updated to latest version
      latex/unicode: added VERSION and SOURCE_HASH to DETAILS
      latex/europecv: added VERSION and SOURCE_HASH to DETAILS
      disk/hdparm: added init script
      utils/sunbird: corrected source url
      wm-addons/wmgtemp: updated to 0.8
      wm-addons/wmforkplop: new spell
      perl-cpan/file-tail: updated to 0.99.3
      graphics-libs/ogre: fixed BUILD
      devel/graphviz: updated to 2.14.1
      latex/pgf: updated to 1.18
      utils/gnuplot: added optional support for a lua terminal
      utils/gnuplot: fixed installation of lua terminal
      editors/xfig: updated to 3.2.5
      editors/transfig: updated to 3.2.5
      utils/bochs: updated to 2.3
      utils/helpdeco: new spell
      collab/subversion: updated to 1.4.5
      graphics/blender: fixed install process so scripts can actually be used,     added optional dependency on ffmpeg

George Sherwood (110):
      ufraw: Updated to version 0.12.1
      imagemagick: Updated to version 6.3.5-6
      gtk-sharp-2: Downgraded to version 2.10.0.  That is the version that is     listed as stable on mono's website and 2.10.1 caused at least     Bug 13900.
      xfce4-places-plugin: Updated to version 0.9.991
      seamonkey: Updated to version 1.1.4.  SECURITY_PATCH++
      php: Added option for multibyte support.  Bug 13943.
      f-spot: Updated to version 0.4.0
      liferea: Updated stable to version 1.2.21
      xfree86: Updated to version 4.7.0.  PRE_BUILD removed unneeded patches.
      snort: Updated to version 2.7.0.1
      spamassassin: Updated to version 3.2.3
      webmin: Updated to version 1.360
      lyx: Updated to version 1.5.1.  NOw uses qt4 for qt frontend.     Updated DEPENDS and BUILD.
      icewm: Updated to version 1.2.31
      banshee: Updated to version 0.13.0
      icewm: Updated to version 1.2.32
      liferea: Uppdated stable to version 1.2.22
      gnucash: Updated to version 2.2.1. No upstream sig for this versions.     Switched to hash.
      pidgin: Updated to version 2.1.1
      samba: Updated to version 3.0.25c
      ayttm: Updated to version 0.5.0-6. Adjusted DEPENDS, BUILD
      phpmyadmin: Updated to version 2.11.0
      lftp: Updated to version 3.5.13
      tea: Updated to version 17.2.0
      banshee: Updated to version 0.13.1
      bash: Updated to current upstream patches.  PATCHLEVEL++
      pdf-api2: Updated to version 0.62
      imagemagick: Added optional depends for perl
      pdf-api2: Added depends compress-zlib
      compress-zlib: Added depends compress-raw-zlib, io-compress-zlib
      perl-gtk2-simple-list: Added new spell.
      gscan2pdf: Added new spell
      readline: Updated with latest upstream patches.
      unpaper: added new spell
      gscan2pdf: Cleaned up DEPENDS and added missing
      libidn: Fix for bug 13857.
      loudmouth: Updated to version 1.2.3
      gossip: Updated to version 0.27
      loudmouth: forgot HISTORY entery for added depends libidn
      beagle: Updated to version 0.2.18
      libidn: Use sedit vice patch file.  Appears file can be created     correctly on some systems.  Suspect with newer glibc it is     created correctly.
      lighttpd: Updated to version 1.4.17
      mono: Updated to version 1.2.5
      ayttm: Updated to version 0.5.0-10.  Removed workaournd in     BUILD
      liferea: Updated devel to version 1.4.0 and stable to 1.2.23
      squid: Updated to version 2.6.STABLE15
      netatalk: Updated to version 2.0.3.  Fixed compiles problems with     newer version of db. Bug #11524.  Added patches from gentoo for     this problem.  Cleaned up DETAILS and fixed bug that spell was     using variable OPTS in CONFIGURE.
      ktorrent: Updated to version 2.2.2
      lftp: Updated to version 3.5.14
      imagemagick: Updated to version 6.3.5-7
      afterstep: Update to version 2.2.7
      amsn: Fix problems introducted with abouter's commit.
      git: Updated to version 1.5.3
      postgresql: updated broken pgcluster patch.  Something that needs to     be check on version updates.
      openldap: Updated to version 2.3.38.  Removed non-working SOURCE_URL's.
      bitlbee: Updated to version 1.0.4
      libotr: Updated to version 3.1.0
      pidgin-otr: Updated to version 3.1.0.  Updated SOURCE_URL
      madwifi: Added SOURCE_HINTS to get svn version working again
      libssh2:  Revert "libssh2 0.17".  Bug #13963.  Will update to 0.17 once     curl 7.17 is released.
      seamonkey: Use check_if_xorg_modular_libs to ensure all cases     are covered.  Bug #13976
      sqlite: Updated to version 3.5.0
      imagemagick: Updated to version 6.3.5-8
      tea: Updated to version 17.2.1
      liferea: Updated devel to version 1.4.1
      sqlite: My error this should not have been updated.     Revert "sqlite: Updated to version 3.5.0"
      openssh: Updated to version 4.7p1
      libgsf: Updated to version 1.14.6
      goffice-dev: Updated to version 0.4.3
      goffice-dev: Fix HISTORY typo
      abiword: Updated devel version to 2.5.2
      goffice-dev: Updated to version 0.5.0. Required for devel version of     gnumeric. 0.4.x doesn't work.
      goffice-dev: Revert "goffice-dev: Updated to version 0.5.0."  This     version does not work with gnucash 2.2.1 and hopefully gnumeric devel     will be updated to work with goffice-dev 0.4.x
      squid: Updated to versin 2.6.STABLE16
      gnome-build: Updated to version 0.2.0
      weechat: Updated to version 0.2.6
      lighttpd: Updated to version 1.4.18.  SECURITY_PATCH++
      pidgin: Updated to version 2.2.0
      cups: Updated to version 1.3.1
      gtk+2: Updated to stable version 2.12.0
      centerim: Updated to version 20070625
      gedit: Added depends pygtksourceview if optional_depends python
      liferea: Updated stable to version 1.4.1.  Now always depends sqlite     Fixed build when chossing xulrunner for GECKO.
      liferea: Forgot to remove old sig file
      imagemagick: Updated to verison 6.3.5-9. SECURITY_PATCH++
      pwlib: Updated to version 1.10.10.  Updated SOURCE_URL's.
      opal: Updated to version 2.2.11. Fixed SOURCE_URL
      ekiga: Updated to version 2.0.11. Fixed SOURCE_URL
      firefox: Updated to version 2.0.0.7. SECURITY_PATCH++.  New sig     not part of firefox.gpg.  Added missing && in PRE_BUILD
      liferea: Updated to version 1.4.2b
      Revert "firefox some of the lines in DETAILS were left commented, uncommented     them". Reverting this and fixing the one left uncommented.
      firefox: Hopefully at least now have a working firefox spell.  Still     need to find the missing sig for firefox.gpg
      phpmyadmin: Updated to version 2.11.1
      imagemagick: Updated to version 6.3.5-10
      mono: Updated to version 1.2.5.1
      firefox: Updated to use UPSTREAM_KEY again. Bug 14006
      git: Updated to version 1.5.3.2
      webmin: Updated to version 1.370
      texinfo: Updated to version 4.11
      tcl: Updated to version 8.4.16
      tk: Updated to version 8.4.16
      planner: Updated to version 0.14.2
      liferea: Updated to version 1.4.3
      liferea: Updated to version 1.4.3b
      pidgin: Updated to version 2.2.1. SECURITY_PATCH++
      qgit4: Updated to version 2.0
      epic4: Updated to version 2.8
      epic5: Updated to version 0.3.5
      elfutils: Adjusted patch to move unset's to just before #include fts.h.     Good troubleshooting by dmlb200. :)
      liferea: Updated to version 1.4.4

Jaka Kranjc (38):
      init.d: fix my workaround for #13363     thanks Arwed
      guile: added libtool dependency #13933
      added jwm #13931
      added yaf-splash
      jwm: space cleanup
      util-linux: fix #13926 for good
      sorcery-pubkeys: added my key
      rp-pppoe: fixed url and gpgised
      pear-xml_serializer: fixed known bugs
      uds: fixed #11737
      uds: fixed source url
      uds: forgot the dep
      mp3-tag: added missing deps, fixes #11810
      compress-raw-zlib 2.005
      io-compress-base 2.005
      io-compress-zlib 2.005
      perl-cpan: terminally deleted old sigs
      confuse: fixed #13956
      ginac: 1.3.7
      octave-forge: fix #12395
      octave: updated to 2.9.13
      octave-devel: synced from octave
      octave-forge: updated to match octave
      octave: forgot to include a fix
      octave-forge: temporary commit, it is still as broken as before     looks like we'll have to install these using the octave pkg managment
      libtunepimp: updated UP_TRIGGERS, last version change is also a breaker
      kst: 1.4.0
      amarok: TRIGGERS: added flac
      lilypond: 2.10.29
      net-tools: fixed typo #13970
      samba: added python_install target, the final nail for #13967
      k9copy: 1.1.3, patch from Julien "KaZe" ROZO #13971
      samba: run python_install only when python was chosen, a mistake from the previous commit
      gnokii: 0.6.18 #13979
      gnokii: needs make_single
      strigi: fix a query
      quill: 0.2.8
      gimp-lqr-plugin: 0.2.0

Julien ROZO (1):
      kdebluetooth : updated version to 1.0-beta3, corrected WEB_SITE

Juuso Alasuutari (28):
      Phasex 0.11.1
      New spell: fwknop, a port knocking and single packet authorization server/client. Fwknop has its own perl install script, which makes     writing a proper spell difficult. Here are some known bugs in this first commit:     - won't use $INSTALL_ROOT     - will attempt to kill an existing fwknopd daemon on updates (and might fail, making the cast break)     - will do its own config file merging     Proceed with caution and please, please improve this spell if you can.
      rsbac-admin 1.3.5
      ardour2: New spell, professional Digital Audio Workstation.
      nekobee 0.1.6
      rosegarden: Added svn version.
      rosegarden: Moved SOURCE_HASH to inside the VCS conditional.
      specimen: Added SVN option.
      jackdmp 0.65
      jackdmp: forgot HISTORY
      qjackctl 0.3.1a
      qsynth 0.3.1
      jack-cvs: Deleted PROVIDES because this spell is deprecated.
      libgnomecanvas: Added depends pango & gail, that's what ./configure says
      gail: Removed depends libgnomecanvas because it depends on gail, not vice-versa.
      qjackctl: Re-added PRE_BUILD; we need to sed the configure script because it detects the     Qt3 qmake/moc/uic executables instead of the Qt4 ones, so that the build will fail if both     libraries are installed.
      qsynth: Added PRE_BUILD; need to sed the configure script so that it will find Qt4's     qmake/moc/uic executables instead of Qt3's equivalent ones when both libraries are     installed.
      jackdmp: Added install of headers and pkgconfig file to enable building packages against jackdmp.
      boost-jam: Fix bjam segfault with gcc 4.2 which caused boost compile to fail
      valgrind: fix build with glibc 2.6
      specimen: moved ./bootstrap for SVN version from BUILD to PRE_BUILD
      qjackctl: replace sed hack for configuring correct Qt4 bin path with patch from cvs
      boost-jam: bumped PATCHLEVEL to push the gcc 4.2 fix to users in time
      ndiswrapper 1.48
      jackdmp 0.66
      ardour2: Moved FFT analysis window option from CONFIGURE to DEPENDS as it depends on fftw.
      ardour2: Added depends soundtouch for when using system libraries.
      ardour2 2.1

Ladislav Hagara (135):
      thunderbird 2.0.0.6
      libafterimage 1.15
      rxvt-unicode 8.3
      iso-codes 1.3
      m2crypto 0.18
      net-snmp 5.4.1
      libpcap 0.9.7
      emelfm2 0.3.5
      aterm 1.0.1
      strace 4.5.16
      ecryptfs-utils 20
      phppgadmin 4.1.3
      lshw B.02.11.01
      udev 114
      ucview 0.11
      unicap 0.2.13
      video/camorama: new spell, a utility to view, alter and save images from a webcam
      ChangeLog: added new spell video/camorama
      libssh2 0.17
      pycurl 7.16.4
      tea 17.1.4
      mesalib 7.0.1
      mesademos 7.0.1
      libgksu 2.0.5
      dejavu-ttf 2.19
      thunderbird, enigmail 0.95.3
      getmail 4.7.6
      whois 4.7.22
      utils/lsvpd: new spell     a utility to list device Vital Product Data (VPD) information
      hdparm 7.7
      libs/libsexymm: new spell, a set of C++ bindings around libsexy
      bmpx 0.40.0
      shared-mime-info 0.22
      parted 1.8.8
      e16 0.16.8.9
      gsasl 0.2.20
      bmpx 0.40.1
      man-pages 2.64
      seahorse 2.19.90
      gamin 0.1.9
      testdisk 6.8
      stardict 3.0.0
      cryptsetup-luks 1.0.5
      workrave 1.8.4-2
      gimp 2.4.0-rc1
      gnupg-exp 2.0.6
      dirmngr 1.0.1
      links-twibright 2.1pre30, SECURITY_PATCH=1
      linux 2.6.22.4
      linux 2.6.22.5
      mrxvt 0.5.3
      udev 115
      xfe 1.00
      fox: added optional_depends libxft (xfe 1.00 needs it)
      libassuan 1.0.3
      jfsutils 1.1.12
      fox: optional_depends libxft only if xorg-modular
      lvm 2.02.28
      device-mapper 1.02.22
      squirrelmail-gpg 2.1
      smgl-ledger 0.07, IP address has been changed
      openct 0.6.13
      subversion 1.4.5     fixed security issue on Microsoft Windows clients     on linux no security problems     http://subversion.tigris.org/servlets/ReadMsg?list=users&msgNo=69413
      pan: fixed svn SOURCE_DIRECTORY     i tested new version of subversion and found out this bug
      ruby-evas: moved from subversion to git
      ruby-ecore: moved from subversion to git
      ruby-edje: moved from subversion to git
      ruby-esmart: moved form subversion to git
      euphoria: moved from cvs to git
      libtasn1 0.3.10
      binutils 2.18
      samba: added some && to fail properly [Bug 13967]
      php 5.2.4, SECURITY_PATCH=5
      pdfedit 0.3.2     From Cahnelog:     Fixed bug when doxygen would overwrite /dev/null device if run under root
      iso-codes 1.4
      sylpheed 2.4.5, SECURITY_PATCH=1, SA26550
      linux 2.6.22.6
      seahorse 2.19.91
      opencdk: added backup SOURCE_URLs [Bug 13972]
      ipsec-tools 0.7
      claws-mail 3.0.0
      claws-mail-extra-plugins 3.0.0
      virtualbox-module 1.5.0
      virtualbox 1.5.0
      sysstat 8.0.0
      gnutls: added support for new stable 2.0 branch (2.0.0)     it wants some testing before it can be default, for now it looks OK
      libtasn1 1.1     removed UP_TRIGGERS because it wants to rebuild almost all system     version number change from 0.3.10 to 1.1 but libraries are compatible     libtasn1.so.3.0.10 versus libtasn1.so.3.0.12
      opencdk: added support for new 0.6 branch (0.6.4)     new gnutls 2.0.0 needs 0.6     old gnutls 1.6.3 needs 0.5
      libxml2 2.6.30
      man-pages-cs 0.17.20070905
      apache22 2.2.6, SECURITY_PATCH=2
      openct 0.6.14
      opensc 0.11.4
      apache 1.3.39, SECURITY_PATCH=2
      apache2 2.0.61, SECURITY_PATCH=2
      apache-mod_ssl 2.8.29-1.3.39, SECURITY_PATCH=1
      gnupg-exp 2.0.7
      xfsprogs 2.9.4
      acl 2.2.45
      attr 2.4.39
      xfsdump 2.2.46
      samba 3.0.26a, SECURITY_PATCH=4
      apache-mod_ssl 2.8.30-1.3.39
      xfe 1.04
      krb5: SECURITY_PATCH=5, CVE-2007-3999, CVE-2007-4000
      moc 2.4.3
      bmpx 0.40.4
      curl 7.17.0
      Now we have curl 7.17.
      dejavu-ttf 2.20
      bmpx 0.40.7
      pcsc-lite 1.4.4
      e/ecore: added possibility to build Ecore_Desktop module
      claws-mail 3.0.1
      claws-mail-extra-plugins 3.0.1
      postgresql 8.2.5
      seahorse 2.20
      sylpheed 2.4.6
      man-pages 2.65
      tea 17.2.5
      pgpdump 0.26
      pcre 7.4
      gnutls 2.0.1
      bmpx 0.40.8
      cryptopp 552     doesn't work with my CXXFLAGS, commented out
      tcpdump 3.9.8
      libpcap 0.9.8
      units 1.87
      seahorse 2.20.0
      whois 4.7.23
      libntlm 0.4.0
      libnids 1.22
      gsasl 0.2.21
      git 1.5.3.3
      bmpx 0.40.10

Lalo Martins (5):
      a2ps dependency on tex is optional
      a2ps dependency on tex is optional
      a2ps dependency on tex is optional
      updating mplayerplug-in to 3.45
      oops, fixing incorrect optional_depends line

Martin Spitzbarth (17):
      asterisk: updated to 1.4.10, SECURITY_PATCH++
      asterisk: fixed download url and mirrors
      asterisk-addons: fixed download url and mirrors
      openbox: updated to 3.4.4
      iksemel: new spell, multiversion 1.3 and svn
      asterisk: added iksemel as optional dependency
      asterisk.gpg: Added two upstream keys to the keyring.
      asterisk: updated to 1.4.11 and applied upstream patch. SECURITY_PATCH++
      zaptel: updated to 1.4.5.1, rework of DETAILS, BUILD and INSTALL
      asterisk: added zaptel as optional_depends
      gurus.gpg: Added my key (0x6B750C1F)
      amanda: Added missing guru signature file
      star: Updated to 1.15a84, SECURITY_PATCH++, Bug 13957
      tar: added upstream patch, SECURITY_PATCH++, bug 13957
      rsnapshot: New spell, a filesystem snapshot utility
      asterisk: forgot to remove a patch file from the grimoire
      asterisk: Updated to 1.4.13, SECURITY_PATCH++, Bug 14035

Mathieu Lonjaret (21):
      libtorrent: 0.11.6
      rtorrent: 0.7.6
      dmenu: 3.2
      dwm: 4.3
      drawterm: 20070724
      plan9port: 20070726
      octave-devel: 2.9.13 bump
      libextractor: 0.5.18
      gnunet: update to 0.7.2b, reworked deps
      gnunet-gtk: new spell
      libmatroska: 0.8.1
      mvktoolnix: 2.0.2
      pcre: g++ subdepends for mkvtoolnix
      mkvtoolnix: pcre depends with g++ subdep
      libmatroska: corrected typo in HISTORY
      libtorrent: 0.11.7
      rtorrent: 0.7.7
      gpac: new video spell
      gpac: new spell
      libtorrent: 0.11.8
      rtorrent: 0.7.8

Philippe Caseiro (7):
      Adding clutter new spell
      Adding clutter-cairo new spell
      Updating Changelog
      Adding lignomecanvas to gtkpod DEPENDS
      Updating Tree spell to version 1.5.1.1
      Now INSTALL_ROOT setting affects tree spell (bug #13623)
      Fixing an little mistake

Pol Vinogradov (57):
      graphics-libs/rmagick:
      kernels/linux:
      kernels/linux/HISTORY: quick fix of formatting issue
      perl-cpan/parrot:
      python-devel/tagpy:
      libs/boost:
      graphics-libs/rmagick:
      graphics-libs/rmagick:
      spelling/stardict:
      spelling/stardict:
      chat-im/gajim:
      graphics/gimp:
      xfce/thunar:
      xfce/xfce4-session:
      xfce/xfce-utils:
      python-devel/django: new spell, a high-level Python Web framework
      audio-creation/espeak:
      spelling/stardict:
      devel/jruby:
      devel/jruby:
      audio-drivers/alsa-driver:
      audio-drivers/alsa-firmware:
      audio-drivers/alsa-lib:
      audio-drivers/alsa-plugins:
      audio-drivers/alsa-utils:
      audio-drivers/pyalsa:
      audio-drivers/alsa-lib:
      disk/hdparm:
      video-libs/libdvdread:
      video-libs/libdvdnav:
      database/pgadmin3:
      x11-toolkits/wxgtk:
      database/pgadmin3:
      x11-toolkits/wxgtk:
      kernels/deskopt: new spell, utility to tune kernel schedulers
      kernels/deskopt:
      database/pgadmin3:
      x11-toolkits/wxgtk:
      database/pgadmin3:
      x11-toolkits/wxgtk/SUB_DEPENDS: quick fix of needless spaces
      graphics/gimp-lqr-plugin: new spell, GIMP Liquid rescale plugin
      python-devel/soappy:
      libs/ode:
      audio-players/sonata:
      graphics-libs/poppler:
      spelling/stardict:
      disk/cdrdao:
      graphics-libs/poppler:
      graphics-libs/rmagick:
      http/seamonkey:
      chat-im/gajim:
      gnome2-libs/pygobject:
      chat-im/gajim:
      utils/memtest86:
      audio-libs/libdca: new spell, free library for decoding     DTS Coherent Acoustics streams, replacement for libdts
      audio-libs/libdts:
      audio-libs/libdca/DETAILS: quick fix of SOURCE_DIRECTORY

Remko van der Vossen (11):
      audio-players/ncmpc bumped to 0.11.1, applied wide char patch
      kde-apps/kid3: version 0.9
      audio-soft/eyeD3: new spell, Python id3(v2) tag program/library
      i18n/scim: fixed SOURCE_HASh
      audio-soft/eyeD3: renamed (deprecated) spell to eyed3
      devel/slang: version 2.1.2
      ftp/ncftp: Fixed SOURCE_HASH     	Verified source by comparing with an older release
      i18n/im-ja: Fixed XIM configure switch (bug# 13896)
      libs/libidn: versions 1.1 (bug# 13857)
      audio-soft/shntool: version 3.0.4
      audio-soft/cuetools: New spell, cue/toc file utilities

Robin Cook (219):
      libiodbc: added make_single
      glib2: updated to 2.14.0
      libxml++: updated to 2.18.2
      gtkmm2: updated to 2.10.11
      vte: updated to 0.16.8
      gdm2: updated to 2.18.4
      libglade2: updated to 2.6.2
      intltool: updated to 0.36.0
      gstreamer: 0.10.14
      gst-plugins-base: updated to 0.10.14
      libgomeprint: updated to 2.18.1
      sound-juicer: updated to 2.19.3
      totem: updated to 2.19.90
      pango: updated to 1.18.1
      gtk+2: updated to 2.11.6
      atk: updated to 1.19.6
      gail: updated to 1.19.6
      at-spi: updated to 1.19.5
      gconf2: updated to 2.19.1
      gnome-vfs2: updated to 2.19.91
      libbonobo: updated ot 2.19.6
      libgnome: updated to 2.19.1
      libgnomecanvas: updated to 2.19.2
      libbonoboui: updated to 2.19.6
      libgnomeui: updated to 2.19.1
      control-center2: depricated as renamed to gnome-control-center
      libgtop2: updated to 2.19.92
      libwnck: updated to 2.19.92
      dasher: updated to 4.5.2
      evolution-data-server: updated to 1.11.92
      gnome-keyring: updated to 2.19.91
      evolution-webcal: updated to 2.11.91
      gconf-editor: updated to 2.18.2
      gnome-doc-utils: updated to 0.11.2
      librsvg2: updated to 2.18.2
      gdm2: updated to 2.19.7
      libxklavier: updated to 3.3
      gnome-desktop: updated to 2.19.92
      gnome-menus: updated to 2.19.92
      gnome-panel: updated to 2.19.92
      gnome-applets2: updated to 2.19.91
      metacity: update to 2.19.55
      eel2: updated to 2.19.90
      gtk-engines2: updated to 2.11.7
      gnome-icon-theme: update to 2.19.91
      gnome-themes: updated to 2.19.92
      libgnomekbd: updated to 2.19.91
      nautilus2: updated to 2.19.91
      gnome-control-center: renamed and updated to 2.19.92
      gtksourceview: updated to 1.90.4
      nautilus-cd-burner: updated to 2.19.6
      gnome-python-desktop: updated to 2.19.2
      gnome-games2: updated to 2.19.92
      libgail-gnome: updated to 1.19.5
      gtkhtml2: updated to 3.15.92
      gnome-mag: updated to 0.14.8
      gnome-nettool: updated to 2.19.90
      gnome-screensaver: updated to 2.19.7
      gnome-screensaver: forgot to add the DEPENDS change to HISTORY
      gnome-session: update to 2.19.92
      gnome-system-monitor: updated to 2.19.91.1
      gnome-utils2: updated to 2.19.91
      vino: updated to 2.19.92
      scrollkeeper: deprecated - replaced by rarian
      rarian: new spell replaces scrollkeeper
      yelp: updated to 2.19.90
      ChangeLog: fix conflict
      pygtksourceview: really add new spell
      poppler-data: new spell
      poppler: updated to 0.6
      glib2: updated to 2.14.1
      pango: updated to 1.18.2
      libxslt: updated to 1.1.22
      libidl: updated to 0.8.9
      orbit2: updated to 2.14.9
      gconf2: updated to 2.20.0
      intltool: updated to 0.36.2
      atk: updated to 1.20.0
      at-spi: updated to 1.20.0
      gail: updated to 1.20.0
      gnome-vfs2: updated to 2.20.0
      gnome-common2: updated to 2.20.0
      libbonobo: updated to 2.20.0
      libgnome: updated to 2.20.0
      libgnomecanvas: updated to 2.20.0
      libbonoboui: updated to 2.20.0
      devhelp: updated to 0.16
      libgnomeui: updated to 2.20.0
      rarian: updated to 0.6.0
      startup-notification: updated to 0.9
      libwnck: updated to 2.20.0
      dasher: updated to 4.6.0
      evolution-data-server: updated to 1.12.0
      gnome-keyring: updated to 2.20.0
      evolution-webcal: updated to 2.12.0
      gnome-doc-utils: updated to 0.12.0
      gnome-doc-utils: correct added blank line
      gnome-desktop: updated to 2.20.0
      pygtk2: updated to 2.12.0
      gnome-menus: updated to 2.20.0
      eel2: updated to 2.20.0
      gnome-panel: updated to 2.20.0.1
      gnome-panel: forgot DEPENDS change
      fast-user-switch-applet: updated to 2.20.0
      gconf-editor: updated to 2.20.0
      gdm2: updated to 2.20.0
      gnome-applets2: updated to 2.20.0
      gnome-applets2: removed blank line
      gnome-backgrounds: updated to 2.20.0
      gtk-engines2: updated to 2.12.0
      gnome-themes: updated to 2.20.0
      icon-naming-utils: updated to 0.8.6
      gnome-icon-theme: updated to 2.20.0
      nautilus2: updated to 2.20.0
      metacity: updated to 2.20.0
      libgnomekbd: updated to 2.20.0
      gnome-control-center: updated to 2.20.0
      gnome-python2: updated to 2.20.0
      nautilus-cd-burner: updated to 2.20.0
      libgtop2: updated to 2.20.0
      gtksourceview: updated to 2.0.0
      gnome-media2: updated to 2.20.0
      gnome-python-desktop: updated to 2.20.0
      gnome-games2: updated to 2.20.0.1
      gnome-mag: updated to 0.14.10
      gnome-nettool: updated to 2.20.0
      gnome-screensaver: updated te 2.20.0
      gnome-session: updated to 2.20.0
      gnome-system-monitor: updated to 2.20.0
      vte: updated to 0.16.9
      gnome-terminal: updated to 2.18.2
      gnome2-user-docs: updated to 2.20.0
      gtkhtml2: updated to 3.16.0
      libgail-gnome: updated to 1.20.0
      pygtksourceview: updated to 2.0.0
      vino: updated to 2.20.0
      yelp: updated to 2.20.0
      zenity: updated to 2.20.0
      bug-buddy2: updated to 2.20.0
      deskbar-applet: updated to 2.20.0
      eog2: updated to 2.20.0
      eog2: remove blank line in HISTORY
      epiphany: updated to 2.20.0
      epiphany-extensions: updated to 2.20.0
      evince: updated to 2.20.0
      evolution: updated to 2.12.0
      evolution-exchange: updated to 2.12.0
      evolution: remove blank line
      file-roller: updated to 2.20.0
      file-roller: removed blank line
      gcalctool: upadated to 5.20.0
      gedit: updated to 2.20.0
      gnome-keyring-manager
      gnome-power-manager: updated to 2.20.0
      system-tools-backends: updated to 2.4.0
      liboobs: updated to 2.20.0
      gnome-system-tools: updated to 2.20.0
      gok: updated to 1.3.4
      gucharmap: updated to 1.10.1
      orca: updated to 2.20.0
      gtk-sharp-2: updated to 2.10.2
      tomboy: updated to 0.8.0
      sound-juicer: updated to 2.20.0
      totem: updated to 2.20.0
      libgnomeprint: updated to 2.18.2
      libgnomeprintui: updated to 2.18.1
      gnome-media2: updated to 2.20.1
      gtk-engines2: updated to 2.12.1
      libgsf: updated to 1.14.7
      gnumeric: updated to 1.7.12
      goffice-0.5: New spell for gnumeric devel version
      glade3: updated to 3.4.0
      gnome-devel-docs: New Spell
      gnome-python-extras: updated to 2.19.1
      New Spell: gnome2-apps/accerciser
      pessulus: New Spell
      sabayon: New Spell
      libxml++: updated to 2.20.0
      libsigc++: updated to 2.1.1
      glibmm: updated to 2.14.0
      gtkmm2: updated to 2.12.0
      libgnomemm: updated to 2.20.0
      libgnomecanvasmm: updated to 2.20.0
      libgnomeuimm: updated to 2.20.0
      gnome-vfsmm: updated to 2.20.0
      evolution-sharp: updated to 0.14.0.1
      gnome-games-extra-data: updated to 2.20.0
      gnome-themes-extras: updated to 2.20
      natuilus-sendto: updated to 0.12
      rhythmbox: updated to 0.11.2
      goobox: updated to 1.9.2
      xdg-user-dirs: updated to 0.9
      sabayon: updated to 2.20.1 and fixed depends
      anjuta: changed scrollkeeper to rarian
      gnucash-docs: changed scrollkeeper to rarian
      bless: changed scrollkeeper to rarian
      gdm: changed scrollkeeper to rarian
      gnome-core: changed scrollkeeper to rarian
      gnome-media: changed scrollkeeper to rarian
      gnome-user-docs: changed scrollkeeper to rarian
      libgda: changed scrollkeeper to rarian
      nautilus: changed scrollkeeper to rarian
      balsa: changed scrollkeeper to rarian
      gedit-plugins: changed scrollkeeper to rarian
      ggv: changed scrollkeeper to rarian
      glabels2: changed scrollkeeper to rarian
      glade2: changed scrollkeeper to rarian
      gramps: changed scrollkeeper to rarian
      gthumb2: changed scrollkeeper to rarian
      gnome-utils2: changed scrollkeeper to rarian
      galeon: changed scrollkeeper to rarian
      qalculate-gtk: changed scrollkeeper to rarian
      multi-gnome-terminal: changed scrollkeeper to rarian
      ghex: updated to 2.20.0
      gnome-control-center: updated to 2.20.0.1
      gedit: updated to 2.20.1
      java-access-bridge: updated to 1.20.0
      tracker: updated to 0.6.3
      gedit-plugins: updated to 2.20.0

Thomas Orgis (14):
      mpg123: update to version 0.67
      mpg123: adding the forgotten HISTORY note.
      epiphany: fix gnome-python2 sub dep
      bash: add option for NON_INTERACTIVE_LOGIN_SHELLS
      mpg123: fix message color reset to default in CONFIGURE
      bash: the CONFIGURE file for the non-interactive shell option...
      mpg123: HISTORY entry from last change
      guilib: really remove patches and BUILD now, also not needed for alpha
      guilib: REALLY removing BUILD
      kqemu: make it work with linux-2.6.22 (trivial patch)
      bash: needs autoconf
      madwifi: bump to 0.9.3.2; making it build with linux-2.6.22
      unsermake: switch to a mirrored tarball; SVN is dead
      kdenlive: Fix the install by using the 0.5-1 source tarball; now depends on unsermake.

Tommy Boatman (2):
      quagga: Updated to 0.99.8
      zebra: update to version 0.95a

Treeve Jelbert (291):
      mpop-1.0.11
      libevent-1.3c
      sptk-3.5.4
      kdegraphics - fix CVE-2007-3387
      koffice - fix CVE-2007-3387
      berkeleydb-0.32
      text-balanced-v2.0.0
      version-0.7203
      text-balance  update DEPENDS
      mail-clamav-0.20
      paste-1.4
      qgit - add conflicts qgit4
      qgit4-2.0rc2
      kde4*3.92.0
      ghostscript-8.60
      deprecate printer/gs-afpl [replaced by ghostscript]
      strigi-0.5.4
      qgit4 - fix install location
      telepathy-sofiasip-0.3.26.1
      telepathy-mission-control-4.31
      hplip-2.7.7
      deprecate printer/hpoj [replaced by hplip]
      deprecate printer/hpijs [replaced by hplip]
      poppler - change depends
      db-4.6.18
      qt-x11   - CVE-2007-3388
      grep-2.5.3
      cups - fix bug #13308
      cups -fix bug #13105
      glibc - fix bug #13925
      glibc - fix typo
      dejavu-ttf-2.19
      fltk-2.0.x-r5940
      mlt-0.2.4
      ntp-4.2.4p3
      flex - apply upstream patch
      bisonc++-2.0.0
      libtunepimp-0.5.3
      libofa-0.9.3
      strigi-0.5.5
      strigi - extra depends
      util-linux  - fix bug #13926
      strongswan - 4.1.5 /2.8.6
      util-linux - fix typo
      qt4-4.3.1
      telepathy-mission-control-4.33
      cmake-2.4.7
      cups - updated description
      aria2-0.11.2
      gutenprint - update description
      wine-0.9.43
      qt4 - update snapshot
      ntfs-3g-1.810
      kdenlive-0.5
      partimage-0.6.6
      mlt++ - add TRGGERS
      amarok-1.4.7
      newt-0.52.7-2.fc8
      libedit-20070813-2.10
      sqlite-3.4.2
      cups-1.3.0
      gambas2-1.9.50
      gambas-1.0.19
      libosip2-3.0.3
      libexosip2-3.0.3
      sqlalchemy-0.4.0beta2
      firebird - remove support for v1.5
      libcap-1.97
      libgphoto2 - fix install
      dhcpcd-3.1.4
      deprecate printer/espgs [replaced by ghostscript]
      kde4 - update dpends
      strigi - add a profile
      freevo-1.7.3
      sqlalchemy-0.4.0beta3
      itools-0.16.6
      cherrypy-3.0.2
      qt4pas-V1.46_Qt4.3.0
      ghostscript - deprecate gs-afpl
      deprecate printer/cups-drivers [replaced by ghostscript]
      kde4/kdeedu4-3.92.0
      kde4/kdetoys4-3.92.0
      libpng-1.2.19
      rubygems-0.9.4
      rake-0.7.3
      libcap - use get_kernel_version
      cherokee-0.6.0b863
      ed-0.8
      lirc-0.8.2
      numpy-1.0.3.1
      clucene-0.9.20
      clamav-0.91.2
      firebird-2.0.2.12964-RC1-0
      x264-20070821-2245
      ibgpod-0.5.2
      gtkpod-0.99.10
      delete obsolete signature
      kdelibs - security fix 13950
      kdebase - security fix 13950
      sqlalchemy-0.4.0beta4
      poppler-0.5.91
      cairomm-1.4.4
      liboil-0.3.12
      lwp-5.808
      qt4pas-V1.47_Qt4.3.1
      kmplayer - update depends
      re2c-0.13.1
      wine-0.9.44
      cimg-1.2.3
      dar-2.3.5
      lame-3.97
      lame - extra depends
      perl-gtk2-1.146
      ntfs-3g-1.826
      firebird  2.0.2.12964-0
      heyu2-2.1.0
      newt-0.52.7-3.fc8
      qca2-2.0.0-test1
      kino-1.1.1
      /xine-lib-1.1.8
      dazuko-2.3.4-pre1
      popt-1.12
      fontforge-20070808
      dialog-1.1-20070704
      pcre-7.3
      nasm-0.99.01
      opencdk-0.5.13
      dbi-1.59
      intltool-0.36.1
      libgphoto2 - update camera list
      Revert "nasm-0.99.01"     which broke lame     This reverts commit 0f1e739e1df35b4dc8499164e7fb1b719c9d2f15.
      libedit-20070831-2.10
      ksquirrel-libs-0.7.1
      ksquirrel-0.7.1
      gtklp-1.2.5
      p7zip-4.53
      dazuko-2.3.4-pre2
      tesseract-2.01
      sqlalchemy-0.4.0beta5
      tesseract - apply upstream patch
      strongswan-4.1.6
      ksquirrel-libs-0.7.1try2
      ksquirrel-0.7.1try2
      xaralx-0.7r1780
      git-1.5.3.1
      firebird-2.0.3.12981-0
      zziplib-0.13.49
      sdl_net-1.2.7
      kdelibs4-3.93.0
      kdepimlibs4-3.93.0
      kdebase-workspace4-3.93.0
      qimageblitz-0.0.706674
      kdetoys4-3.93.0
      kdeadmin4-3.93.0
      kde4 - update depends
      kdebase-workspace4 - updated depends
      kdeutils4-3.93.0
      kdebase4-3.93.0
      kdemultimedia4-3.93.0
      kde4-profile-4-3.93.0
      kdenetwork4-3.93.0
      kdegames4-3.93.0
      kdegraphics4-3.93.0
      kdesdk4-3.93.0
      qimageblitz - fix typo
      kdebase4 - fix typo
      kdebase4 - install fixed
      kde4 - move stuff between kdebase4  and kdebase-workspace4, and adjust dependencies
      openbabel-2.1.1
      kdeedu4-3.93.0
      kdebase-workspace4 - fix typo
      kdebase4 - update dpends
      kdepim4 - 3.93.0
      kde4 - adjust depends
      itools-0.16.8
      libpng-1.2.20
      clamav - fix bug #13983
      ix bug #13987
      fix bug #13987
      fix bug #13987
      koffice2  1.9.93
      glpk-4.21
      libgnomeui -extra depends
      t4pas-V1.48_Qt4.3.1
      glpk - make gmp optional
      kdegames4 -add optional ggz-client-libs
      aria2-0.11.3
      kde4-l10n-3.93.0
      fpcsrc-2.2.0
      fpc-2.2.0
      man-pages-fr-2.40.0
      graphicsmagick-1.1.8
      pstoedit-3.45
      imagemagick - minor change
      ksquirrel-0.7.1try3
      dvgrab-3.0
      tagua: new spell
      myodbc-3.51.16r494
      telepathy.gpg - add extra key
      libtelepathy-0.0.57
      telepathy-glib-0.5.14
      telepathy-mission-control-4.37
      telepathy-sofiasip-0.3.29
      qt4pas - add trigger
      qca2-2.0.0-test4
      ntfs-3g-1.910-RC
      bisonc++-2.2.0
      xapian-core-1.0.2
      ntfs-3g-1.913
      turbokid-1.0.3
      pastescript-1.3.6
      paste-1.4.2
      qt4pas-V1.49_Qt4.3.1
      Revert "xapian-core-1.0.2"
      xapian-core-1.0.2
      turbogears-1.0.4b1
      wine-0.9.45
      p7zip-4.55
      ksquirrel-0.7.1try4
      gwenview-1.4.2
      libgda3-3.1.1
      libgnomedb3-3.1.1
      ragel-5.24
      partimage-0.6.7_beta1
      kdelibs4 - fix install
      icu-3.8
      kipi-plugins - add trigger
      libkexiv2-0.1.6
      digikam - fix build with latest lcms
      ntp-4.2.4p4
      tora-1.3.22
      pxlib-0.6.2
      cups-1.3.2
      qt4pas-V1.50_Qt4.3.1
      photoprint - changed depends
      ace-5.6.1
      graphicsmagick-1.1.10
      kde4/kdeaccessibility4: new spell
      kde4/kdeaddons4 - new spell
      powertop-1.8
      telepathy-sofiasip-0.3.30
      git-1.5.3.2
      fontforge-20070917
      kdelibs - security fix
      kdebase - security fix
      pcre-7.4
      tellico-1.2.14
      ruby-1.8.6-p110
      soprano-1.90.0-beta1
      hal-0.5.9.1
      ksquirrel-libs-0.7.1try3
      ksquirrel-0.7.1try5
      hal - add back selinux stuff
      qt4pas-V1.51_Qt4.3.1
      libevent-1.3e
      syslinux-3.52
      soprano-0.9.0
      kde4 - updatesection depends
      kdelibs4 - update depnds
      kdenetwork4 - updated depends
      kde4/kdebindings4
      libtelepathy-0.0.58
      gimp-2.4.0-rc3
      cimg-1.2.4
      firebird-2.0.3.12981-1
      libtheora-1.0beta1
      sqlalchemy-0.4.0beta6
      sptk-3.5.5-r1
      flac-1.2.1
      sptk - update depnds
      wxgtk-2.8.6
      sptk - eliminate for loop
      itools-0.16.9
      perl-glib-1.160
      perl-gtk2-1.160
      wxpython-2.8.6.0
      wine-0.9.46
      sip-4.7.1
      cups-1.3.3
      hplip-2.7.9
      pyqt4-4.3.1
      xapian-core-1.0.3
      dar-2.3.6
      cupsddk-1.2.1
      qgit4-2.0
      kbarcode-2.0.6
      boost-jam-3.1.15
      raptor-1.4.16
      wireless_tools-29
      pxlib-0.6.3
      xmltv-0.5.49

root (1):
      gurus.gpg: added new key for Robin Cook
```

[0] Generated with: `git shortlog --no-merges stable-0.13-6..stable-0.14-0`
