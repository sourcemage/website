title: Stable-0.62 released
author: stealth
category: news
date: 2015-03-01
tags: [grimoire]
---
Stable grimoire version 0.62 has been released!

As usual, users of stable merely need to run `sorcery system-update`. Spells listed on the [0.62 release page](/Grimoire/stable/0.62) were tested and qualified to have no known defects of "gating" severity at the time of this release. The tarballs have been signed and uploaded to our server and will be propogating out to the mirrors within six hours.

To download the grimoire manually, get <http://codex.sourcemage.org/stable.tar.bz2> or specifically <http://codex.sourcemage.org/stable-0.62.tar.bz2>.

GPG signatures are available at <http://codex.sourcemage.org/stable.tar.bz2.asc> or <http://codex.sourcemage.org/stable-0.62.tar.bz2.asc>.

I would like to thank Thomas Orgis (sobukus) for helping test spells on x86_64 arch.

In case anyone is interested, here's the shortlog between 0.61 and 0.62[0]:


```
Andraž Levstik (6):
      ibpp: use the right char for (r)
      intercal: bad encoding in DETAILS
      libftdi: updated and fixed as per |_emming
      phpmyadmin: cleaned up weird chars
      qt-creator: fixed screwy (r)
      scribus4: removed oddly encoded unicode stuff

Arjan Bouter (16):
      pygobjec: added missing optional dep on libffi
      tzdata: use ln instead of zic so the spell works if /etc and /usr are on     different partitions. Note that the SA still has to clean     /usr/share/zoneinfo or the spell will fail.
      loudmouth: fixed glib2 includes
      abiword: fixed glib includes, only glib.h can be included.
      goffice: pcre_info is replaced by pcre_fullinfo, I added a fix from     opensuse so we can build spells that depend on goffice again.     see http://lists.opensuse.org/archive/opensuse-commit/2012-02/msg01190.html     for more info
      qt4: added a fix for icu, so webkit support can be enabled again.
      procmeter: version 3.6, converted to upstream keys, now installs to /usr and     added gtk+3 support
      procmeter: 3, I mean 3! ;)
      glib2: added sub dependency info for python and fixed patching
      gcr: added dependency info
      labyrinth: added missing deps on gnome-desktop and gnome-python2,     corrected website url
      minidlna: added a patch to make it build against ffmpeg 0.11
      libplist: version 1.8 and corrected source url
      sox: added patch from arch to fix building against ffmpeg 0.11
      awesome: version 3.4.13
      cssutils: version 0.9.10b1 and corrected urls

Bor Kraljič (3):
      pdfgrep: updated spell to 1.3.0
      qtcurve-gtk2: updated spell to 1.8.15
      qtcurve-kde4: updated spell to 1.8.14

David Haley (15):
      Spell Updated: syslog-ng
      Spell Update: mdadm 3.1.5 -> 3.2.1
      Spell Update: feh - Dependency Added
      Spell Update: subversion
      Spell Update: thc-hydra 5.4 -> 7.5
      Spell Update: ntop 3.3.9 -> 5.0.1
      New Spell: amap, an application protocol tool.
      Spell Deprecation: amap
      Spell Update: thc-amap 5.2 -> 5.4
      Spell Deprecation: amap (cont.)
      New Spell: gnupg2
      Spell Update: iasl 20121220 -> 20130823
      Spell (nss) Dependancies Removed: sqlite & zip
      Spell Updated: syslog-ng 3.4.5 -> 3.5.1
      Spell Update: eventlog 2.12 -> 2.20

David Kowis (5):
      Adding a libyaml spell for ruby
      Fixing DETAILSwq
      Updating squashfs-tools to the latest version
      nagios: set it to the sf.net specific URL
      nagios: set it to the sf.net specific URL

Eric Sandall (449):
      git: Updated devel to 1.5.4
      wine: Updated devel to 1.5.5
      vim: fix compilation with perl 5.16     After perl 5.16 my vim fails to compile with this error:     https://groups.google.com/forum/#!msg/vim_dev/3KD82kZJwgo/4yM1ZaEUFZIJ
      gnome-python-desktop: Fix compilation with metacity 2.34.2+
      wine: Updated devel to 1.5.6
      babl: Fix compilation with gobject-introspection     * babl-0.1.10-gir-build-fix.patch: Fix compilation with gobject-introspection.       See https://bugs.gentoo.org/show_bug.cgi?id=413663     * babl-introspection.patch: Fix .gir and .typelib       See https://bugs.gentoo.org/show_bug.cgi?id=413663#c3     * Broken with vala, disable       See https://bugs.gentoo.org/show_bug.cgi?id=413663#c20
      mysql: Fix MySQL NDB disable
      mysql: Fix plugin configure flags
      mysql: ndbcluster requires ndb-test for API     Some plugins fail with -Wl,--as-needed (e.g. ndbcluster)
      mysql: Cleanup MSQL_ENGINES
      wine: Updated devel to 1.5.8
      nautilus-dropbox: Depends on docutils
      docutils: Updated to 0.9.1
      nautilus2: Suggest gvfs for Connect to Server funcionality
      nautilus-dropbox: Updated to 1.4.0     Suggest pygpgme to verify binary signatures
      handbrake: Updated to 0.9.6, matches upstream MD5
      wine: Updated devel to 1.5.10
      wine: Updated devel to 1.5.11
      wine: Updated devel to 1.5.12
      wine: Updated devel to 1.5.13
      libgsf: Remove stale GPG signature
      libgsf: Updated to 1.4.24     ./configure does not understand --with-gnome-vfs, --with-bonobo, nor --with-gnome-vfs     GNOME VFS swapped to GIO libraries a while ago     Added optional dependency on gdk-pixbuf2     Incorrect sub-dependency on poppler -> gio (should have been gnome-vfs2)
      libgsf: Added optional dependency on gobject-introspection
      goffice: Updated to 0.9.6     SOURCE matches upstream posted SHA256     .bz2 -> .xz
      vips: Updated to 7.30.2 (required for nips 7.30.x)     ./configure doesn't know --with-openexr, --without-cimg, --with-liboil, nor --with-lcms2 anymore     *-openexr -> *-OpenEXR     Removed cimg optional dependency     Removed liboil optional dependency     Removed lcms optional dependency (only supports lcms2 now)
      nip2: Updated to 7.30.1     Apply yyleng.patch to fix compilation with newer bison/flex     Fixes for 7.26.x as well
      Revert "goffice: Updated to 0.9.6"
      gnumeric: Depends on libglade2, intltool
      gnumeric: Disable GNOME support (see Bug #444)
      handbrake: Optionally depend on LIBAVCODEC for ffmpeg support
      advancecomp: Added a collection of recompression utilities
      advancecomp: Remove broken bzip2 optional dependency
      wine: Updated devel to 1.5.14
      cifs-utils: Depends on keyutils regardless of features, now
      grub2: Fix compilation with glibc 2.16+     gets removed from GNU libc, see     http://permalink.gmane.org/gmane.comp.lib.gnulib.bugs/30292)
      wine: Updated devel to 1.5.15
      mx: Depends on xcb-util
      pidgin: endif -> fi
      strace: Patch to fix compilation against newer glibc
      guile: Updated to 2.0.6
      libtasn1: Updated to 2.14
      libvirt: Updated to 0.10.2, depends on yajl
      virt-viewer: Updated to 0.5.4
      virtinst: Updated to 0.600.3
      gtk-vnc: Updated to 0.5.1     SOURCE matches upstream SHA256     SOURCE uses .xz instead of .bz2     Optionally depends on gettext, pulseaudio, and     gobject-introspection
      virt-manager: Updated to 0.9.4
      linux-pam: Updated to 1.1.6     Upstream MD5/SHA1 not posted for 1.1.6
      strigi: Apply strigi-0.7.7-ffmpeg-0.11.patch for ffmpeg 1.0+ as well
      strigi: Cleanup formatting
      linux-pam: Cleanup formatting
      pykde4: Updated to 4.9.2
      pykde4: Apply sip-4.14.patch     Fix compilation with sip 4.14+ (affects pykde4 4.9.1 as well).
      libgweather: Updated to 3.6.1 (for evolution-data-server 3.6.1)     SOURCE .bz2 -> .xz     SOURCE matches upstream SHA256
      evolution-data-server: Updated to 3.6.1     No more optional calendar, just weather calendar     No more '--*-ssl' option for nss     No more optional gnome-keyring support     Optionally depends on gettext
      gtkhtml2: Updated to 4.6.0 (for evolution 4.6.1)     SOURCE matches upstream posted SHA256     No more --disable-deprecated-warning-flags     Removed, supports parallel make now
      evolution: Updated to 3.6.1     mono, rarian, python, and gnome-pilot-conduits are no longer used     --disable-contacts-map is not available (default=no)     --disable-nm no longer exists
      evolution-exchange: Updated to 3.5.2     SOURCE matches upstream posted SHA256
      Revert "evolution-exchange: Updated to 3.5.2"
      gnome-settings-daemon: Updated to 3.6.1     SOURCE matches upstream posted SHA256
      glib2: Updated to 2.34.1 (for gnome-desktop3 3.6.0.1)     SOURCE matches upstream posted SHA256
      gnome-desktop3: Updated to 3.6.0.1 (for gnome-settings-daemon 3.6.1)     SOURCE matches upstream posted SHA256
      gsettings-desktop-schemas: Updated to 3.6.0 (for gnome-settings-daemon 3.6.1)     SOURCE matches upstream posted SHA256
      ibus: Updated to 1.4.99.20121006 (for gnome-settings-daemon 3.6.1)     Nothing else currently uses ibus
      gnome-settings-daemon: Depends on ibus
      ibus-anthy: Updated to 1.2.7
      ibus-pinyin: Updated to 1.4.0     boost is optional     Optionally depends on LUA     Disable -Wl,--as-needed in LDFLAGS, breaks linking lua
      gobject-introspection: Updated to 1.34.0 (works with glib2 2.34.1)     SOURCE matches upstream posted SHA256
      ecore: Depends on eobj
      e_dbus: Depends on eobj
      efreet: Depends on eobj
      geoclue: Updated to 0.12.99 (works with glib2 2.34.1)     Removed geoclue-gcc46.patch included in release
      orbit: Fix compilation with newer make
      Revert "gsettings-desktop-schemas: Updated to 3.6.0 (for gnome-settings-daemon 3.6.1)"
      Revert "gnome-desktop3: Updated to 3.6.0.1 (for gnome-settings-daemon 3.6.1)"
      Revert "glib2: Updated to 2.34.1 (for gnome-desktop3 3.6.0.1)"
      Revert "gnome-settings-daemon: Depends on ibus"
      Revert "gnome-settings-daemon: Updated to 3.6.1"
      Revert "libgweather: Updated to 3.6.1 (for evolution-data-server 3.6.1)"
      Revert "evolution-data-server: Updated to 3.6.1"
      Revert "evolution: Updated to 3.6.1"
      wine: Updated devel to 1.5.16
      nautilus2: Depends on tracker
      wine: Updated devel to 1.5.17
      wine: Updated devel to 1.5.18
      wine: Updated devel to 1.5.19
      efl: Depends on fribidi >= 0.19.2
      efl: Depends on libxp
      wine: Updated to 1.5.20
      wine: Updated devel to 1.5.21
      efl: Depends on valgrind
      efl: Depends on bullet
      efl: Cleanup formatting
      efl: bullet is optional, not required
      efl: More optional depends     fontconfig, sdl, pixman, curl tslib, pulseaudio, and util-linux
      efl: Fails with multiple make jobs, use make_single
      efl: Optionally depend on giflib and tiff for image loaders.
      efl: Spell physics correctly :p
      efl: Sort CONFLICTS for easier checking what's missing
      ephysics: typo efs -> efl
      eet: Conflicts with efl
      eina: Conflicts with efl
      embryo: Conflicts with efl
      eobj: Conflicts with efl
      evas: Conflicts with efl
      efl: Optionally depends on libwebp
      eina: Updated stable to 1.7.4     Remove SVN option, this code is now in the efl package     Remove posix and coverage configure options     configure: WARNING: unrecognized options: --enable-posix-threads,     --disable-coverage
      gnutls: Apply gets.patch/x509.patch for DEFAULT/2.12 branch (Bug #493)     * gets.patch: Fix gets() removal from glibc 2.16 (Bug #493)     * x509.patch: Fix x509 compilation (found after Bug #493 fixed)
      eet: Updated stable to 1.7.4     Removed svn option, included in efl package
      ecore: Updated stable to 1.7.4     Removed svn support, included in efl package     Stable version does not depend on efl (conflicts!)     Optionally depends on libxcomposite and libxp     Add '--enable*' options for other optional dependencies     Replace 'xorg-libs' optional dependency with libx11
      evas: Updated stable to 1.7.4     Removed svn version, included in efl package     Expand pixman flags     Optionally depends on doxygen
      evas: Cleanup formatting
      ecore: Cleanup formatting
      ecore: Optionally depends on evas (auto-detect what evas supports)
      embryo: Updated stable to 1.7.4     Removed svn version, included in efl package     Optionally depends on doxygen
      edje: Updated stable to 1.7.4     SCM branch only depends on efl package     SCM branch conflicts with ecore (provided by required efl)     Stable depends on ecore embryo     Optionally depends on doxygen, LIBAVCODEC, and alsa-lib     Stable branch only conflicts with efl package
      efreet: Stable version updated to 1.7.4     Removed svn version, included in efl package     Removed efl dependency (not for stable)     Does not depend on edbus nor e_dbus     Depends on eet and eina
      ecore: Depends on eina
      eeze: Stable version updated to 1.7.4     Removed svn version, included in efl package     Depends on eet     Optionally depends on doxygen
      ecore: Allow forcing using evas
      edje: Depends on ecore built with evas support (ecore-evas)
      e_dbus: Updated stable branch to 1.7.4     Stable branch does not use efl, only SCM branch
      e_dbus: Cleanup formatting
      eio: Removed SCM option, included in efl     Updated stable to 1.7.4     Conflicts with efl     Optionally depends on doxygen
      e17: dd stable 0.17.0 branch     SCM depends on efl, subversion, and edbus; stable does not     exchange and bluez are no longer options     Stable depends on e_dbus ecore edje efreet eina eio evas     xcb-util-keysyms     Stable optionally depends on eeze     Only install e17update for SCM version
      emotion: Updated stable to 1.7.4     Optionally depends on doxygen     VLC is now under "generic" (--enable-generic-vlc)
      e_dbus: Fix ./configure flags for connman and eofono
      eio: Depends on eet and eina
      elementary: Added stable 1.7.4 release     Only SCM branch depends on subversion     Stable branch depends on eio edje
      e17: Optionally depends on gettext, elementary, and emotion
      eio: Cleanup formatting
      e17: Cleanup formatting
      e17: Fix trailing &&
      e17: Switch SOURCE from .gz -> .bz2
      e_dbus: Switch SOURCE from .gz -> .bz2
      ecore: Switch SOURCE from .gz -> .bz2
      edje: Switch SOURCE from .gz -> .bz2
      eeze: Switch SOURCE from .gz -> .bz2
      efreet: Switch SOURCE from .gz -> .bz2
      eina: Switch SOURCE from .gz -> .bz2
      embryo: Switch SOURCE from .gz -> .bz2
      evas: Switch SOURCE from .gz -> .bz2
      elementary: EDJE_BRANCH -> ELEMENTARY_BRANCH
      expedite: Add stable 1.7.4 branch     Only SCM branch depends on subversion
      exquisite: Add stable 1.0.0 branch     Only SCM branch depends on efl and subversion
      edje: Depends on eet and eina
      ethumb: Add stable 1.7.4 branch     Only SCM branch depends on efl and subversion     e_dbus for stable and edbus for SCM     Optionally depends on doxygen
      ethumb: Cleanup formatting
      evas_generic_loaders: Added stable 1.7.4 branch     SCM version depends on subversion
      evas: --disable-images-loader-eet -> --disable-image-loader-eet
      evas: eet is required, not optional
      ecore: Add all evas flags for evas optional dependency
      e17: Depends on ecore built with evas support
      evas: X11 and XCB are mutually exclusive
      ecore: Add all evas flags for evas optional dependency to SUB_DEPENDS
      terminology: Add stable branch 0.2.0     Only SCM branch depends on efl     SCM branch depends on subversion     Stable branch depends on edje, eet, efreet, and eina
      eet: Updated stable branch to 1.7.5
      eina: Updated stable branch to 1.7.5
      evas: Updated stable branch to 1.7.5
      ecore: Updated stable branch to 1.7.5
      embryo: Updated stable branch to 1.7.5
      edje: Updated stable branch to 1.7.5
      efreet: Updated stable branch to 1.7.5
      e_dbus: Updated stable branch to 1.7.5
      eeze: Updated stable branch to 1.7.5
      expedite: Updated stable branch to 1.7.5
      evas_generic_loaders: Updated stable branch to 1.7.5
      eio: Updated stable branch to 1.7.5
      emotion: Updated stable branch to 1.7.5
      ethumb: Updated stable branch to 1.7.5
      elementary: Updated stable branch to 1.7.5
      webkitgtk: Depends on ruby
      neon: Allow requiring SSL support
      subversion: Fix subversion SSL support
      neon: Reset color to default at the end of message
      ruby-1.8: Fix glibc 2.14+ compilation     From http://bugs.ruby-lang.org/issues/5108
      ruby-1.8: Cleanup formatting
      webkitgtk: Depends on RUBY (tested ruby-1.9 and ruby-1.8)
      libvirt: Updated to 1.0.1     Optionally depends on fuse
      gnome-media2: Depends on gnome-doc-utils
      wine: Updated devel to 1.5.22
      gnutls: Fix typo for "2.12" -> "x2.12" (part of Bug #509)
      gnutls: Removed patches, no longer needed for 2.12.23 (Bug #509)
      openssl: Remove TLSEXT option (See Bug #511)
      gnome-media2: Depends on unique, not libunique
      gnome-media2: Cleanup formatting
      gst-plugins-bad: Optionally depends on openal-soft (cannot use openal)
      wine: Updated devel to 1.5.24
      mysql: Add -fpermissive in CXXFLAGS with 5.1.67 (!$OLD)     Add -fpermissive in CXXFLAGS with 5.1.67 (!$OLD)     for extra/yassl/taocrypt/src/Makefile.in
      wine: Updated devel to 1.5.28     OpenSSL no longer used, it's all GNUTLS baby.
      gnome-media2: Depends on unique, not libunique
      gnome-media2: Cleanup formatting
      gst-plugins-bad: Optionally depends on openal-soft (cannot use openal)
      wine: Updated devel to 1.5.24
      mysql: Add -fpermissive in CXXFLAGS with 5.1.67 (!$OLD)     Add -fpermissive in CXXFLAGS with 5.1.67 (!$OLD)     for extra/yassl/taocrypt/src/Makefile.in
      curl: Fix -DPIC from CFLAGS -> CPPFLAGS (Bug #537)
      openjpeg: PATCHLEVEL++ for Bug #540 (Javier Vasquez's fix)     Adding "default_install" and the removal of broken symlink and the     creation of the correct one.
      qemu: Updated to 1.4.1     Removed branches, they no longer (even 1.1) compile without     work.     Query for enabling VNC     Optionally depends on libcap-ng     Move VNC-specific optional dependencies into a VNC enabled     check     Pass $QEMU_VNC to ./configure     PRE_BUILD, cflags.patch, archs-0.15: Removed     Updated architecture list to 1.4.1
      automake: Depends on LZMA for uncompressing SOURCE (Bug #542)
      linux: Linux 3.9.0+ depends on bc
      linux: smgl-logo-0.2-for-2.6.31.patch works for 3.1-3.9
      pinentry: libx11 is optional (and the GUI toolkits are optional based on this).     Need to explicitly disable X11 (and all the toolkits) to not fail     when libx11 is not installed.
      mesalib: GLUT functionality depends on libxmu and libxi (plus libx11)
      wine: Updated devel to 1.5.31
      perl-error: Updated to 0.17020 (0.17018 file missing)
      lightdm: Updated to 1.7.0 (1.8 branch)     1.5.1 no longer seems to compile.     Added optional dependency on gettext.
      orbit2: Fix linc2 compilation using deprecated glib2 symbols     Included linc2 fails to compile due to usage of deprecated glib2     symbols.     ORBit2 is dead.     Long live ORBit2.
      systemd: +x DETAILS
      perl-tk: Updated to 804.031     Fixes compilation issue 'invalid use of void expression'
      perl-tk: Change xorg-server -> libx11, freetype2, JPEG, libpng
      clusterssh: Suggest xterm or cssh won't work     without defining an alternate terminal emulator.
      mdm: Added Mint Display Manager (git version)
      subversion: Requires ruby-1.8, does not work with 1.9+
      smgl-mirrors: Updated to 0.7     Updated SOURCEFORGE to new mirrors     SOURCEFORGE default is now "Auto Select"
      libbonobo: Fix compilation against new glib2
      gnome-vfs2: Fix compilation with newer glib2
      libgnome: Fix compilation with newer glib2
      gnome-panel: Depends on gnome-desktop in addition to gnome-desktop3
      gnome-panel: Fix compilation against gnome-desktop 3.8+     0001-panel-Fix-launcher-icon-animation-ending-with-black.patch,     0002-fix-build-error-due-to-missing-gweather-xml.h.patch,     0003-na-apply-style-after-realize.patch,     0004-drop-support-for-commandline-based-calendar-tasks-ap.patch,     0005-panel-run-dialog-resurrect-function-gnome_desktop_pr.patch,     0006-panel-run-dialog-rename-helper-function.patch,     0007-notification_area-Use-the-generic-marshaller.patch: Added     from http://git.pld-linux.org/gitweb.cgi/packages/gnome-panel.git/commitdiff/fd33e2e0d0dd96ab56e3ee8b297e7de83556c0e0
      gnome-panel: Updated to 3.6.2
      gnome-desktop3: Updated to 3.8.3 (various memory leak fixes)
      gsettings-desktop-schemas: Updated to 3.8.2     Match upstream posted SHA256
      libgnome-keyring: Updated to 3.4.1     SOURCE matches upstream SHA256
      gnome-keyring: Updated to 3.6.3     SOURCE matches upstream SHA256
      libgweather: Updated to 3.6.2     SOURCE matches upstream posted SHA256
      tango-icon-theme: Fix compilation against librsvg2 2.35+     Depends on autoconf for autoreconf     rsvg-2.35.2.patch added from     https://build.opensuse.org/package/view_file?expand=1&file=tango-icon-theme-rsvg-2_35_2.patch&package=tango-icon-theme&project=openSUSE%3AFactory
      tango-icon-theme-extras: Fix compilation against librsvg2 2.35+     Depends on autoconf for autoreconf     rsvg-2.35.2.patch added from     https://build.opensuse.org/package/view_file?expand=1&file=tango-icon-theme-extras-rsvg-2_35_2.patch&package=tango-icon-theme&project=openSUSE%3AFactory
      firefox: firefox.desktop icon moved under icons/browser directory     PATCHLEVEL++
      thunderbird: thunderbird.desktop mozicon50.xpm is no longer available,     PATCHLEVEL++     desktop icon to use /usr/lib/thunderbird/chrome/icons/default/default256.png
      sysstat: Setup sar to actually have data     PATCHLEVEL++     Query about installing cron jobs.     Default is 'y' otherwise sar is pretty useless.     Depend on CRON if using cron jobs     cron.daily/sa2: Add (optional) cron jobs to update stats     cron.hourly/sa1: Add (optional) cron jobs to update stats     init.d/sysstat: Add boot sysstat init script to set stats
      clusterssh: Fix desktop file to use a valid icon: clusterssh-48x48.png     PATCHLEVEL++
      libxfce4util: Updated to 4.10.1     SOURCE matches upstream posted SHA1
      garcon: Updated to 0.2.1     SOURCE matches upstream posted SHA1
      thunar: Updated to 1.6.3     SOURCE matches upstream posted SHA1
      tumbler: Updated to 0.1.29     SOURCE matches upstream posted SHA1
      xfce4-appfinder: Updated to 4.10.1     SOURCE matches upstream posted SHA1
      xfce4-panel: Updated to 4.10.1     SOURCE matches upstream posted SHA1
      xfce4-session: Updated to 4.10.1     SOURCE matches upstream posted SHA1
      xfce4-settings: Updated to 4.10.1     SOURCE matches upstream posted SHA1
      xfwm4: Updated to 4.10.1     SOURCE matches upstream posted SHA1
      xdg-utils: Runtime depends on xprop
      parole: Updated to 0.5.1     SOURCE matches upstream posted SHA1     Update libnotify flags
      thunar-thumbnailers: Updated to 0.4.1     SOURCE matches upstream posted SHA1     SOURCE_URL and SOURCE_DIRECTORY updated
      xfce4-dict: Updated to 0.7.0     SOURCE matches upstream posted SHA1
      xfce4-mixer: Updated to 4.10.0     SOURCE matches upstream posted SHA1
      xfce4-notifyd: Updated to 0.2.4     SOURCE matches upstream posted SHA1
      xfce4-screenshooter-plugin: Updated to 1.8.1     SOURCE matches upstream posted SHA1     Updated SOURCE_URL
      terminal renamed to xfce4-terminal; updated to 0.6.2
      xfwm4-themes: Updated to 4.10.0     SOURCE matches upstream posted SHA1
      xfce4-battery-plugin: Updated to 1.0.5     SOURCE matches upstream posted SHA1
      xfce4-cpufreq-plugin: Updated to 1.0.0     SOURCE matches upstrea posted SHA1     Updated SOURCE_URL     SOURCE is now .bz2     SOURCE_DIRECTORY now uses SPELL
      xfce4-datetime-plugin: Updated to 0.6.2     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-diskperf-plugin: Updated to 2.5.4     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-eyes-plugin: Updated to 4.4.2     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-fsguard-plugin: Updated to 1.0.1     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-genmon-plugin: Updated to 3.4.0     SOURCE matches upstream posted SHA1     SOURCE_URL updated     SOURCE_DIRECTORY uses short VERSION
      xfce4-mount-plugin: Updated to 0.6.4     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-mpc-plugin: Updated to 0.4.4     SOURCE matches upstream posted SHA1     SOURCE_URL updated     SOURCE is now .bz2
      xfce4-netload-plugin: Updated to 1.2.0     SOURCE matches upstream posted SHA1     SOURCE_URL updated     bug2782-asneeded.patch: Removed, now applied
      xfce4-places-plugin: Updated to 1.5.0     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-quicklauncher-plugin: Updated to 1.9.4     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-systemload-plugin: Updated to 1.1.1     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-wavelan-plugin: Updated to 0.5.9     SOURCE matches upstream posted SHA1     SOURCE is now .bz2     SOURCE_URL updated
      xfce4-weather-plugin: Updated to 0.8.3     SOURCE matches upstream posted SHA1     SOURCE_URL updated
      xfce4-xkb-plugin: Updated to 0.7.0     SOURCE matches upstream posted SHA1
      thunar-archive-plugin: Updated to 0.3.1     SOURCE matches upstream posted SHA1
      thunar-media-tags-plugin: Updated to 0.2.1     SOURCE matches upstream posted SHA1
      thunar-vcs-plugin: Added Subversion and Git context menus for Thunar
      wine: Updated devel to 1.6-rc2
      wine: Updated devel to 1.6-rc3
      nautilus2: Fix compilation with gnome-desktop3 3.8+ and libgnome API 3.8     Apply 000-gnome-desktop-3.8.patch,     001-do-not-use-NautilusDesktopBackground.patch,     002-add_receive_dropped_background_image.patch, and     003-remove_gnome_bg_set_draw_background.patch.     gnome-desktop-3.8.patch borrowed from     http://git.pld-linux.org/gitweb.cgi/packages/gnome-panel.git/commitdiff/fd33e2e0d0dd96ab56e3ee8b297e7de83556c0e0
      nautilus2: Updated to 3.6.3     SOURCE matches upstream posted SHA256
      nautilus-dropbox: Depends on pygtk2
      nautilus-dropbox: Updated to 1.6.0
      firefox: Remove gnome-vfs2 support (broken)     See https://bugzilla.mozilla.org/show_bug.cgi?id=799458, gnome-vfs     support is disabled by default. They say it works, but the last few     firefox releases it has not worked for me.
      pango: Add REPAIR file for prior PRE_SUB_DEPENDS missing GI
      wine: Updated devel to 1.6-rc4
      linux: smgl-logo-0.2-for-2.6.31.patch works with 3.10
      gtkmm2: Updated to 2.24.4 (fixes bugged 2.24.3 release)     See https://bugs.launchpad.net/inkscape/+bug/1171147     Fixes libglademm (and probably others) compilation.
      kmix: alsa-libs -> alsa-lib
      kde4/KDE_DEPENDS: kdebase4-runtime depends on kdepimlibs4
      pykde4: Depends on phonon
      akonadi: Fix compilation with boost 1.53+     See http://comments.gmane.org/gmane.linux.lfs.beyond.support/46883
      KDE_DEPENDS: kdepim4-runtime depends on phonon
      audiocd-kio: Depends on cdparanoia
      kde4/KDE_DEPENDS,kdepimlibs4: Add kdepimlibs4 depends case     Default KDE_DEPENDS case causes circular dependency with kdebase4-runtime     and optional circular dependency with kdebase-workspace4.
      gwenview4: Depends on kdebase4     http://forums.fedoraforum.org/showthread.php?t=226155
      qt4: Fix some compilation with boost 1.52+ for dependent spells.     e.g. akonadi and kdepim4     See https://bugreports.qt-project.org/browse/QTBUG-22829     PATCHLEVEL++
      qt4: Use message instead of echo
      Revert "akonadi: Fix compilation with boost 1.53+"
      digikam4: Depends on sane-backends     Also builds its own libksane instead of using the package.
      wine: Updated devel to 1.6-rc5
      wine: sc2-login.diff updated to apply cleanly to 1.6
      matplotlib: Depend on a provider of PYTHON for default_build()     Depend on a provider of PYTHON so that python-pypi's     default_build() calls the correct python.
      tmux: Updated to 1.8
      eina: Updated to 1.7.8
      ecore: Updated to 1.7.8
      eet: Updated to 1.7.8
      eio: Updated to 1.7.8
      embryo: Updated to 1.7.8
      evas: Updated to 1.7.8
      edje: Updated to 1.7.8
      expedite: Updated to 1.7.7
      e_dbus: Updated to 1.7.8
      expedite: Remove older 1.7.5 sig
      expedite: Updated to 1.7.8
      evas_generic_loaders: Updated to 1.7.8
      emotion: Updated to 1.7.8
      ethumb: Updated to 1.7.8
      elementary: Updated to 1.7.8     SCM optionally uses edbus, stable optionally uses e_dbus
      efreet: Updated to 1.7.8
      eeze: Updated to 1.7.8
      e17: Updated to 0.17.4
      terminology: Updated to 0.3.0
      e17/etrophy: Added a library to manage scores, trophies, and unlockables
      e17/echievements: Added an achievements module for Enlightenment 17
      prelink: Updated to 20130503
      wine: Updated devel to 1.7.0     1.7.0+ optionally uses lcms2 instead of lcms     1.6 and 1.7 optionally depend on openal-soft (not openal)
      terminator: Updated to 0.97     SOURCE/VERSION separator changed from "_" to "-"
      terminator: Depends on vte built with python (pygtk2) bindings
      kvm: Optionally depends on texlive for documentation
      virtinst: Depend on a provider of PYTHON for default_build()     Depend on a provider of PYTHON so that python-pypi's     default_build() calls the correct python.
      libvirt: Updated to 1.1.1
      virtinst: Updated to 0.600.4
      libvirt: --*-libssh2 -> --*-ssh2
      libs/libvirt-glib: Added a glib wrapper for libvirt.
      virt-viewer: Updated to 0.5.7
      graphite: Depend on a provider of PYTHON for default_build()     Depend on a provider of PYTHON so that python-pypi's     default_build() calls the correct python.
      qemu: Optionally depends on texinfo for documentation     Apply docs-Fix-generating-qemu-doc.html-with-texinfo-5.patch     from https://bugs.launchpad.net/qemu/+bug/1130533
      spice-protocol: Updated to 0.12.6
      spice: Updated to 0.12.4     Depends on pyparsing
      utils/spice-gtk: Added a GTK client and libraries for SPICE.
      hal: Fixes compilation against glibc 2.17+     Apply glibc-2.17.patch from     http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=701432
      qemu: Updated to 1.5.2     sb16, cs4231a, adlib, and gus sound cards removed     Query for Trusted Platform Module (TPM) support     Optionally depends on vte, libaio, libusbx, and spice     --audio-card-list= removed, modify default-configs/pci.mak (for     PCI) and default-configs/sound.mak (for ISA)     Pass QEMU_TPM to configure
      gcc: Updated to 4.6.4     Fixes compilation against texinfo 5.0+     Removed glibc216.patch, fix included in 4.6.4
      mdm: Depends on automake-1.9     Doesn't work with automake 1.14 (1.13 is the latest supported)
      python-pypi/ipaddr: Added Google's IP address manipulation library
      vte3: Depends on intltool
      vte: Depends on intltool
      vte3: Updated to 0.34.7
      vte3: Allow requesting deprecated GLib/Pango/ATK/GDK/GTK+ features
      vte3: Optionally depend on gobject-introspection     Allow forcing gobject-introspection dependency
      vte3: Does not use pygtk2 for python bindings     Uses gobject-introspection instead
      pygobject: Disable introspection support     See https://bugzilla.gnome.org/show_bug.cgi?id=657054 and     https://bugzilla.redhat.com/show_bug.cgi?id=719791
      python: Trigger check_self on pygobject3
      virt-manager: Updated to 0.10.0     Runtime depends on libvirt-glib     Depends on gtk+3, urlgrabber, x11-ssh-askpass     Depends on spice-gtk built against gtk+3     Requires gtk-vnc built against gtk+3     virtinst is now included; conflict     Use python-pypi default_build (copied)     Use python-pypi default_install (copied)
      accounts,groups,policykit: Add polkitd for policykit
      policykit-gnome: Install xdg autostart file for "other" WM/DE     polkit-gnome-authentication-agent-1.desktop autostart file     modified from http://code.google.com/p/max-repo/source/browse/trunk/x121e/etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop?spec=svn622&r=622
      nmap: Fails to build with -Wl,--as-needed in LDFLAGS
      libmad: Use --add-missing with automake
      wine: Updated devel to 1.7.1
      qemu: Optionally depends on nss     *SUB_DEPENDS: Allow forcing dependency on nss
      spice: Depends on qemu built with nss support
      spice: Optionally depends on LIBSASL
      spice: OPENGL optional dependency is for the spice client
      spice: Optionally depends on libxinerama
      spice: Optionally depends on qemu with nss
      spice-gtk: Suggest virt-viewer for a better spice client     See http://spice-space.org/download.html     Make sure virt-viewer uses spice and the same GTK as spice-gtk
      spice-gtk: Optionally depend on qemu with nss for smart cards
      gtk-vnc: Suggest virt-viewer with appropriate gtk
      gtk-vnc: Allow for building gtk-vnc without an external entity enforcing gtk+2|3
      virt-viewer: Allow for selecting spice-gtk or gtk-vnc, these are exclusive options
      e17: Replace xorg-libs with libx11, libxau, libxdmcp, and libxext
      x11-protocol: Replace xorg-libs with libx11, libxau, and libxext     as runtime dependencies     Per README, doesn't require an X11-SERVER on the current machine
      evas: Replaced xorg-libs with libsm and libx11
      xscreensaver: Replaced xorg-libs
      xscreensaver: Updated to 5.22
      xfce4-profile: Replaced runtime dependency on xorg-libs with X11-SERVER
      sdl: Replaced xorg-libs with libx11
      pulseaudio: Replaced xorg-libs with libx11, libice, libsm, libxext, libxtst
      pulseaudio: gtk+2 support also needs libxxf86vm
      cegui: Replaced xorg-libs with libx11 and libxxf86vm
      linux: smgl-logo-0.2-for-2.6.31.patch works with 3.11
      linux: ifenslave.c was removed in 3.11-rc1
      wine: Updated devel to 1.7.2
      nfs-utils: Fix SOURCE_URL for duplicate '/' causing 404
      redhat.gpg: redhat.gpg: Add E1B768A0 for libguestfs and supermin from Red Hat
      supermin: Added Tool for building supermin appliances
      libguestfs: Set of tools for virtual machine disk images
      davmail: Added a POP/IMAP/SMTP/Caldav/Carddav/LDAP exchange gateway
      mozilla.gpg: Added 15A0A4BC for latest Mozilla releases
      thunderbird: Updated to 24.0
      minidlna:  Updated to 1.1.0
      tevent: Removed PRE_BUILD, I do not even know, but it does not work; no files
      samba4: tevent: Removed PRE_BUILD, I do not even know, but it does not work; no files
      smartmontools: Updated to 6.2
      ipmitool:  Updated to 1.8.13
      linux: smgl-logo-0.2-for-2.6.31.patch works with 3.12.x
      nfs-utils: NFSv4 support requires sqlite
      minidlna: Updated to 1.1.2
      nettle: Optionally depends on nettle for NTLM authentication
      ffmpeg: SSL flag is --enable-openssl not --enable-SSL
      ffmpeg: Fix HISTORY formatting
      minidlna: Updated to 1.1.4
      wine: Updated 1.7.32 (devel)     * PREPARE, sc2-login.diff: Removed, no longer applies cleanly and fails to compile when cleaned up.     * CONFIGURE: Remove WINE_SC2_LOGIN persistent variable
      glibc: Updated kernel headers to 3.17.4     The prior 2.6.38 headers are getting too old (e.g. libcap requires newer,     see https://bugs.launchpad.net/ubuntu/+source/libcap-ng/+bug/684969)     * PRE_BUILD: Remove 2.6.x kernel code for non-sanitized headers
      glibc: Cleanup HISTORY formatting
      virtinst: SOURCE_URL moved to https://fedorahosted.org/...
      libxft: Fix to compile against freetype2 2.5.0+
      socat: fix compilation with linux errqueue.h
      socat: Cleanup whitespace
      supermin: Updated to 5.1.11
      augeas: Updated to 1.3.0
      libguestfs:  Updated to 1.28.2
      facter: Updated to 2.3.0
      hiera: Added
      puppet: Updated to 3.7.3, depends on hiera
      libvirt: Updated to 1.2.9     Python is still optional, but ./configure no longer has flags
      qemu: Updated to 2.1.2     qemu.gpg: Add F108B584 (see https://lists.nongnu.org/archive/html/qemu-devel/2014-04/msg03559.html)     Unused, removed docs-Fix-generating-qemu-doc.html-with-texinfo-5.patch
      nmap: Remove libdnet, add option for nc symlink, update CONFLICTS
      libvirt: requires nmap version of ncat and symlink as nc
      Added some Netfilter table user-space programs and libraries.
      ebtables: Install to /sbin not /usr/sbin
      libvirt: Uses ebtables for firewall/NAT
      gzip: Don't use own compression for a compression utility
      Fixes Bug #185, Bug #186, and Bug #187
      harfbuzz: --with-freetype2 -> --with-freetype
      harfbuzz: Allow forcing freetype2 dependency
      freetype2: harfbuzz is optional and requires freetype2 already installed
      dialog: Updated to 1.2-20140911
      lacheck: Updated SOURCE_URL to valid CTAN mirror forwarder
      ghostscript: lcms2 is no longer optional, but required
      texlive: Fixes Bug #630. Fix finding the path for freetype2 headers
      openssl: Work-around for Bug #556 no longer needed
      openssl:  Parallel jobs on install work, re-enable with make_normal
      mesalib: Depends on g++ (CXX in gcc) from IRC
      cpufreqd: Fix status() calling the correct variable. PATCHLEVEL++
      tevent: Fix WEB_SITE
      samba: samba.org is on https://
      samba.gpg Add 2014 and 2015 upstream GPG keys
      tevent: Updated to 0.9.22
      talloc: Updated to 2.1.1
      sgi.gpg: Added F475FA1D key
      xfsdump: Updated to 3.1.4
      xfsprogs: Updated to 3.2.2
      libaio: Updated to 0.3.110
      tdb: Updated to 1.3.4
      samba4: Update to latest stable 4.0 to 4.0.23
      libxext:  Depends on kbproto
      libxfixes: Depends on kbproto
      libxrender:  Depends on kbproto
      libxfce4menu: Depends on a provider of GTK2
      gnome-desktop3: Depends on iso-codes and xkeyboard-config
      gnome-desktop3: Depends on itstool
      x11-ssh-askpass: Depends on imake, libice, libsm, libxt, and libx11
      pygobject3: Depends on pycairo
      swig: Updated to 3.0.3
      network-manager:  Updated to 0.9.6.4     --with-ck -> --with-session-tracking=ck     Don't error on warnings, such fail
      libffi: Recast dependees on x.y version changes in x.y.z updates
      harfbuzz: Fix syntax error in PRE_SUB_DEPENDS and in REPAIR file     (cherry picked from commit 3d9db975980b525e2501b50555741c285ee98adb)

Florian Franzmann (1462):
      science/gpsbabel: new spell, a tool for converting gps data between different formats
      science/qlandkarte-gt: added suggested dependency on gpsbabel
      science/babel: fixed description
      science/gpsbabel: added optional dependencies on qt4 and perl
      science/gpsbabel: add support for the scm version
      science/gpsbabel: add patch from gentoo to prevent downloading in BUILD
      science/proj: version 4.8.0
      haskell/haskell-syb: version 0.3.6.1
      haskell/haskell-transformers: version 0.3.0.0
      haskell/haskell-mtl: version 2.1.1
      haskell/haskell-x11: version 1.6.0
      haskell/haskell-text: version 0.11.2.1
      haskell/haskell-polyparse: new spell, a variety of alternative parser combinator libraries
      haskell/haskell-haxml: new spell, utilities for manipulating XML documents
      devel/qwtplot3d: fix compile error with qt 4.8
      Revert "haskell/haskell-x11: version 1.6.0"
      libs/libxml2: fixed CVE-2011-0216, CVE-2011-1944, CVE-2011-2834, CVE-2011-3102, CVE-2011-3905 and CVE-2011-3919
      libs/libxml2: fix CVE-2011-3102
      utils/extrautils: version 1.18
      python-pypi/python-cliapp: version 0.29
      python-pypi/python-tracing: version 0.6
      python-pypi/ttystatus: version 0.18
      python-pypi/larch: version 0.31
      python-pypi/genbackupdata: new spell, a tool for generating test data for backup programs
      python-pypi/seivot: new spell, a tool for benchmarking backup programs
      python-pypi/obnam: version 1.0
      libs/pyusb: new spell, USB support for python
      python-pypi/msgpack-python: new spell, a binary-based efficient object serialization library
      python-pypi/pyserial: version 2.6
      python-pypi/pyserial: depend on PYTHON instead of python
      libs/python-ant: new spell, a library for communicating with ANT+ devices
      libs/cdk: version 5.0-20120323
      libs/python-ant: pull directly from git
      python-pypi/python-sphinx: new spell, a documentation generator for python
      doc/docutils: version 0.9
      python-pypi/python-sphinx: add dependency on docutils
      graphics/darktable: version 1.0.4
      smgl/castfs: add -lpthread to LDFLAGS to prevent linker error
      graphics/recoverjpeg: new spell, a tool for recovering jpeg files
      science/maxima: add dependency on perl
      science/maxima: version 5.27.0
      science/wxmaxima: version 12.04.0
      science/gdal: version 1.9.1
      science/qlandkarte-gt: version 1.4.2
      devel/meld: version 1.6.0
      video/mplayer: remove obsolete switch --disable-faad-internal from DEPENDS
      editors/emacs: version 24.1
      devel/ghc: version 7.4.2
      devel/qt-creator: version 2.5.0
      chat-im/licq: version 1.6.1
      haskell/haskell-syb: version 0.3.6.2
      utils/minimodem: new spell, command-line program which generates (or decodes) audio modem tones
      shell-term-fm/rdesktop: add dependency on libx11
      science/proj: downgrade to 4.7.0, 4.8.0 is incompatible with ogdi
      add missing dependencies and suggest dependencies
      graphics/lensfun: version 0.2.6
      science/qlandkarte-gt: version 1.5.0
      graphics/darktable: version 1.0.5
      devel/qt-creator: version 2.5.1
      science/mkgmap: version 2311
      shell-term-fm/rxvt-unicode: perform check_self if perl is cast
      video-libs/live: version 2012.08.17
      devel/cppcheck: version 1.55
      graphics/imagemagick: version 6.7.9-0
      perl-cpan/perlmagick: version 6.77
      shell-term-fm/zsh: version 5.0.0
      graphics/jhead: version 2.96
      net/libnet: version 1.1.6
      latex/latex-mk: new spell, a build system for latex documents
      utils/sudo: fixed SOURCE_URL
      kde4-support/phonon-backend-mplayer: new spell, mplayer phonon backend
      kde4-support/phonon-backend-gstreamer: provide PHONON_BACKEND
      kde4-support/phonon-backend-mplayer: provide PHONON_BACKEND
      kde4-support/phonon-backend-vlc: provide PHONON_BACKEND
      kde4-support/phonon-backend-xine: provide PHONON_BACKEND
      video/minitube: depend on PHONON_BACKEND
      video/mjpegtools: add -fpermissive to CFLAGS and CXXFLAGS
      utils/sudo: re-add source urls
      video-libs/gst-plugins-bad: add option for building experimental plugins
      video-libs/gst-plugins-ugly: add option for experimental plugins
      video-libs/gst-plugins-good: add option for experimental plugins
      graphics/gphoto2: version 2.5.0
      ftp/lftp: version 4.3.8
      science/mkgmap: version r2316
      video/ffmpeg: offer sub depencency on legacy/stable release
      libs/openscenegraph: add dependency on legacy release of ffmpeg
      video/ffmpeg: change sub dependency names to upper case
      libs/openscenegraph: change ffmpeg sub dependency name to LEGACY
      libs/openscenegraph: add depency on gcc with CXX, change dependency on freetype1 to freetype2, add dependency on openexr
      audio-creation/audacity: version 2.0.2
      perl-cpan/file-next: version 1.10
      perl-cpan/devel-modlist: version 0.8
      perl-cpan/http-negotiate: new spell, negotiate http requests
      perl-cpan/lwp-mediatypes: new spell, guess media type for a file or a URL
      perl-cpan/net-http: new spell, low-level HTTP connection (client)
      perl-cpan/www-robotrules: new spell, database of robots.txt-derived permissions
      perl-cpan/www-mechanize: new spell, handy web browsing in a Perl object
      perl-cpan/perl-libnet: version 1.22_01
      perl-cpan/http-message: new spell, HTTP style message (base class)
      perl-cpan/http-date: new spell, date conversion routines
      perl-cpan/http-cookies: new spell, HTTP cookie jars
      perl-cpan/html-form: new spell, class that represents an HTML form element
      perl-cpan/encode-locale: new spell, determine the locale encoding
      perl-cpan/cpan-distnameinfo: new spell, extract distribution name and version from a distribution filename
      perl-cpan/lwp: add missing dependencies
      perl-cpan/app-cpanoutdated: new spell, detect outdated CPAN modules in your environment
      perl-cpan/dbd-odbc: version 1.39
      perl-cpan/perl-graphviz: version 2.10
      perl-cpan/devel-modlist: version 0.801
      perl-cpan/mime-base64: version 3.13
      perl-cpan/xml-sax-base: base class SAX Drivers and Filters
      perl-cpan/xml-sax: version 0.99
      perl-cpan/xml-simple: version 2.20
      graphics-libs/glew: version 1.9.0
      audio-drivers/alsa-driver: version 1.0.25
      audio-drivers/alsa-utils: version 1.0.26
      audio-drivers/alsa-lib: version 1.0.26
      audio-drivers/alsa-tools: version 1.0.26.1
      audio-drivers/alsa-firmware: version 1.0.25
      audio-drivers/alsa-plugins: version 1.0.26
      audio-drivers/alsa-oss: version 1.0.25
      audio-drivers/pyalsa: version 1.0.26
      audio-drivers/alsa-driver: enable dynamic minor device ids
      science/garmindev: fixed dependency on libusb
      devel/coq: version 8.4
      x11-toolkits/qt4: version 4.8.3
      editors/texworks: new spell, an IDE for LaTeX
      devel/ghc: version 7.6.1
      haskell/haskell-text: version 0.11.2.3
      haskell/haskell-mtl: version 2.1.2
      haskell/haskell-extensible-exceptions: new spell, extensible exceptions
      windowmanagers/xmonad: add dependency on haskell-extensible-exceptions
      haskell/haskell-syb: version 0.3.7
      haskell/haskell-deepseq: version 1.3.0.1
      editors/texworks: add dependency on texlive
      devel/qt-creator: devel version 2.6.0-beta, stable version 2.5.2
      latex/texlive: version 20120701
      latex/texlive-texmf: version 20120701
      latex/texlive-texmf: add bugfixes from debian
      science/qlandkarte-gt: version 1.5.1
      graphics/imagemagick: version 6.7.9-7
      video/lives: version 1.6.3
      video/minitube: version 1.9
      science/splitter: new spell, a splitter for openstreetmap data
      science/grass: version 6.4.2
      x11-toolkits/qscintilla: version 2.6.2
      libs/sip: version 4.14
      libs/pyqt4: version 4.9.5
      libs/libspatialindex: new spell, a framework for spatial indexing
      libs/freexl: new spell, a library for reading excel files
      libs/libspatialite: new spell, spatial SQL support for sqlite
      science/qgis: version 1.8.0
      gnome2-libs/gnome-colors: new spell, icon themes for gnome
      gnome2-libs/shiki-colors: new spell, a set of themes for gtk2
      graphics/darktable: fix source url for scm version
      graphics/darktable: add patch to prevent compile error
      graphics/rawtherapee: new spell, a RAW image developer
      chat-im/licq: version 1.7.0
      devel/git: version 1.8.0
      graphics-libs/ftgl: add dependency on texlive
      graphics-libs/ftgl: fix build error
      graphics/cinepaint: version 1.3
      graphics-libs/ftgl: add dependencies on bzip2, zlib, libxext
      kernels/linux: set 3.6.1 as default version
      graphics/openexr: version 1.7.0
      graphics-libs/ilmbase: version 1.0.2
      graphics/autopano-sift-c: version 2.5.1
      perl-cpan/image-exiftool: version 9.03
      graphics/enblend: add missing library to LIBS
      graphics/hugin: version 2011.4.0
      http/firefox: version 16.0.2
      audio-players/moc: add unstable version 2.5.0-beta1 to selectable versions
      video-libs/live: version 2012.10.24
      python-pypi/scipy: version 0.11.0
      graphics/geeqie: add dependencies on atk, cairo, fontconfig, freetype2, gdk-pixbuf2, glib2, JPEG, pango and tiff
      graphics-libs/libopenraw: new spell, a RAW decoder
      gnome2-libs/exempi: version 2.2.0
      graphics/gthumb: new spell, an image viewer based on gqview
      gnome2-apps/gthumb2: version 3.0.2
      libs/elektra: version 0.7.0
      libs/yajl: version 2.0.4
      graphics-libs/libxcm: new spell, a reference implementation of the X Color Management specification
      utils/oyranos: version 0.9.0
      chat-libs/libotr: version 3.2.1
      chat-im/centerim: add patch to fix compile error
      graphics/dcraw: version 9.16
      graphics/dcraw: add missing changes for fb1bf7421561cfdc9e05fecfd2744a95d591e444
      graphics/argyllcms: new spell, software for creating color profiles for devices
      doc/gl-presenter: new spell, a dual-screen pdf presenter
      audio-drivers/alsa-tools: add dependency on gtk+2
      audio-drivers/alsa-tools: correct date of history entry
      utils/colordiff: version 1.0.13
      graphics/darktable: version 1.1
      rename graphics/qtpfsgui to luminance-hdr, version -> 2.2.1
      x11-toolkits/qt4: version 4.8.4
      libs/enet: version 1.3.5
      x11/xscreensaver: version 5.20
      libs/libircclient: new spell, a library for developing IRC clients
      libs/libircclient: fix messed up fields in DETAILS
      libs/miniupnpc: new spell, client library for upnp
      libs/libircclient: build static and shared library, install both
      graphics/darktable: version 1.1.1
      devel/bison: version 2.7
      disk/physfs: version 2.0.3
      science/qlandkarte-gt
      kernels/linux: version 3.7.1
      libs/libvformat: new spell, an interface to vcard files
      mail/lbdb: new spell, the little brother's database
      audio-libs/openal-soft: version 1.15.1
      editors/sed: version 4.2.2
      disk/eject: fix SOURCE_URL and WEB_SITE
      video-libs/smpeg: fix WEB_SITE
      lua-forge/lgi: new spell, gobject-introspection for lua
      crypto/openssl: version 1.0.1c
      crypto/gnutls update WEB_SITE
      audio-libs/libmusicbrainz: change dependency on ctypes to python
      audio-players/listen: change dependency on ctypes to dependency on python
      python-pypi/ctypes: deprecated in favour of python
      utils/procinfo: version 2.0.304
      xorg-apps/xconsole: version 1.0.4
      xorg-apps/xfontsel: version 1.0.4
      doc/t1utils: version 1.37
      doc/dvi2tty: version 5.3.4
      doc/dvipdfmx: version 20110311
      doc/lcdf-typetools: version 2.97
      latex/lacheck: fix WEB_SITE
      perl-cpan/ps2eps: version 1.68
      video/mkvtoolnix: version 5.9.0
      utils/linuxconsoletools: new spell, tools for testing and configuring joysticks
      utils/joystick: deprecated in favour of utils/linuxconsoletools
      doc/enca: version 1.14
      devel/cscope: version 15.8a
      latex/glosstex: fix WEB_SITE
      audio-libs/wavpack: version 4.60.1
      x11/xcompmgr: version 1.1.6
      science/units: version 2.01
      utils/atop: version 2.0.2
      lxde/menu-cache: version 0.4.1
      net/iputils-tracepath: version 20101006-3
      graphics-libs/libwmf: correct WEB_SITE
      devel/dev86: version 0.16.19
      doc/help2man: version 1.40.9
      utils/iotop: version 0.4.4
      apache.gpg: update keys, add key 9E49284A
      libs/apr: version 1.4.6
      xorg-extras/xterm: version 287
      python-pypi/pydot: version 1.0.28
      graphics/netpbm: version 10.35.87
      libs/findlib: version 1.3.3
      disk/gphotofs: version 0.5.0
      graphics/feh: version 2.8
      net/iproute2: version 3.7.0
      net/whois: version 5.0.20
      audio-creation/espeak: version 1.46.02
      crypto/libksba: version 1.3.0
      database/unixodbc: version 2.3.1
      utils/lshw: version B.02.16
      fonts-x11/terminus-font: version 4.38
      e/imlib2: update WEB_SITE
      libs/openmpi: version 1.6.3
      database/db: version 5.3.21
      doc/miscfiles: version 1.5
      utils/kbd: version 1.15.5
      audio-soft/id3: version 0.15
      x11/xearth: fix WEB_SITE and LICENSE
      utils/dmenu: version 4.5
      libs/libffi: version 3.0.11
      editors/nano: version 2.3.1
      video-libs/libdvdcss: version 1.2.12
      audio-libs/soundtouch: version 1.7.0
      graphics-libs/freeimage: version 3154
      gnome2-libs/atk: add dependencies on pcre and libffi
      gnome2-libs/at-spi2-atk: add dependencies on libffi, libice, libsm,     libxau, libxcb, libxdmcp, pcre and util-linux
      gnome2-libs/at-spi2-core: add dependencies on libffi, libice, libsm,     libxau, libxcb, libxdmcp, libxext, pcre, util-linux and zlib
      mail/claws-mail: add dependencies on atk, bzip2, cairo, curl, db,     dbus-glib, expat, fontconfig, freetype2, gdk-pixbuf2, glib2,     harfbuzz, libassuan, libffi, libgpg-error, libice, libidn,     libpng, libsm, libssh2, libx11, libxau, libxcb, libxdmcp,     libxext, libxrender, OPENGL, openssl, pango, pcre, pixman     and zlib
      utils/consolekit: add dependencies on dbus, glib2, libffi, libxau, libxcb, libxdmcp, pcre, zlib
      audio-soft/easytag: add dependencies on atk, bzip2, cairo, expat, fontconfig,     freetype2, gcc, gdk-pixbuf2, harfbuzz, libffi, libid3tag, libogg, libpng,     libx11, libxau, libxcb, libxdmcp, libxext, libxrender, pango, pcre,     pixman, zlib
      utils/eggdbus: add dependencies on libffi, pcre and zlib
      doc/evince: add dependencies on atk, at-spi2-atk, at-spi2-core, bzip2,     dbus, expat, fontconfig, freetype2, gdk-pixbuf2, harfbuzz,     libffi, libice, libpng, libsm, libx11, libxau, libxcb,     libxcomposite, libxcursor, libxdamage, libxdmcp, libxext,     libxfixes, libxi, libxinerama, libxrandr, libxrender, pango, pcre,     pixman, util-linux, zlib
      xfce/exo: add dependencies on atk, bzip2, cairo, expat, fontconfig,     freetype2, gdk-pixbuf2, glib2, harfbuzz, libffi, libice,     libpng, libsm, libx11, libxau, libxcb, libxdmcp, libxext,     libxrender, pango, pcre, pixman, util-linux, zlib
      gnome2-libs/gdk-pixbuf2: add dependencies on libffi, libxau, libxcb,     libxdmcp, pcre and LZMA
      gnome2-libs/glib2: add dependencies on zlib and FAM
      gnome2-libs/glib-networking: add dependencies on libffi, libgpg-error, libproxy, libtasn1, pcre and zlib
      gnome2-libs/gnome-python2: add dependencies on atk, bzip2, cairo, dbus, dbus-glib, expat,     fontconfig, freetype2, gdk-pixbuf2, glib2, gtk+2, harfbuzz, icu,     libart_lgpl, libffi, libgcrypt, libgnome-keyring, libgpg-error, libice,     libpng, libsm, libx11, libxau, libxcb, libxcomposite, libxcursor,     libxdamage, libxdmcp, libxext, libxfixes, libxinerama, libxml2,     libxrandr, libxrender, openssl, orbit2, pango, pcre, pixman, popt,     python, util-linux, LZMA and zlib
      gnome2-libs/gnome-vfs2: add dependencies on attr, bzip2, dbus, FAM,       glib2, icu, libffi, libxml2, orbit2, pcre, LZMA
      video-libs/gst-ffmpeg: add dependencies on LZMA, bzip2, glib2, icu,     libffi, libxml2, orc, pcre, zlib
      devel/graphviz: add dependencies on atk, bzip2, gdk-pixbuf2,     harfbuzz, icu, ilmbase, jasper, lcms, libcroco, libffi,     libice, libmng, librsvg2, libsm, libx11, libxau, libxcb,     libxdmcp, libxext, libxml2, libxmu, libxpm, libxrender,     libxt, openexr, pcre, pixman, tiff, util-linux, LZMA
      mail/claws-mail: make the dependency on openssl unconditional
      remove dependency on FAM, PATCH_LEVEL -> PATCHLEVEL
      xfce/exo: PATCH_LEVEL -> PATCHLEVEL
      http/lynx: PATCH_LEVEL -> PATCHLEVEL
      doc/evince: PATCH_LEVEL -> PATCHLEVEL
      gnome2-libs/atk: PATCH_LEVEL -> PATCHLEVEL
      gnome2-libs/gnome-vfs2: PATCH_LEVEL -> PATCHLEVEL
      gnome2-libs/gdk-pixbuf2: PATCH_LEVEL -> PATCHLEVEL
      gnome2-libs/at-spi2-core: PATCH_LEVEL -> PATCHLEVEL
      gnome2-libs/glib-networking: PATCH_LEVEL -> PATCHLEVEL
      gnome2-libs/at-spi2-atk: PATCH_LEVEL -> PATCHLEVEL
      utils/consolekit: PATCH_LEVEL -> PATCHLEVEL
      utils/eggdbus: PATCH_LEVEL -> PATCHLEVEL
      audio-creation/stops: PATCH_LEVEL -> PATCHLEVEL
      audio-soft/easytag: PATCH_LEVEL -> PATCHLEVEL
      devel/graphviz: PATCH_LEVEL -> PATCHLEVEL
      video-libs/gst-ffmpeg: PATCH_LEVEL -> PATCHLEVEL
      libs/pyusb: version 1.0.0a3
      add dependencies on dbus, libffi, libxext, pcre
      http/webkitgtk: add dependencies on atk, fontconfig, gdk-pixbuf2,     glib2, gstreamer, libffi, libx11, libxml2, libxrender, pcre
      gnome2-libs/vte: add dependencies on cairo, expat, gdk-pixbuf2,     harfbuzz, libffi, libpng, libxau, libxcb, libxdmcp, libxext,     libxrender, pcre, pixman
      disk/udev: add dependencies on libffi and pcre
      graphics/imagemagick: version 6.8.1-3
      devel/vala: add dependencies on libffi and pcre
      xfce/thunar: add dependencies on atk, cairo, dbus, expat, fontconfig,     freetype2, gdk-pixbuf2, glib2, gtk+2, harfbuzz, libffi, libice, libpng,     libsm, libx11, libxau, libxcb, libxdmcp, libxext, libxrender, pango,     pixman, xfconf
      ruby-raa/ruby-1.9: add dependencies on libffi, libx11, tcl
      devel/python3: add dependencies on gettext, libx11, openssl and tcl
      devel/python: add dependencies on gettext, libx11 and tcl
      gnome2-libs/pygobject: add dependency on pcre
      gnome2-libs/policykit: add dependencies on pcre, libffi and glib2
      gnome2-libs/pango: add dependencies on expat, freetype2, libffi,     libpng, libxcb, libxext, pcre, pixman
      gnome2-libs/orbit2: add dependencies on glib2, libffi and pcre
      video/mjpegtools: fixed switches for optional dependencies, added optional     dependency on libxxf86dga, added dependencies on aalib, atk,     cairo, expat, fontconfig, freetype2, gdk-pixbuf2, harfbuzz,     libffi, libggi, libgii, libx11, libxau, libxcb, libxdmcp,     libxext, libxrender, libxxf86vm, pango, pcre, pixman, slang
      gnome2-libs/libxklavier: add dependencies on glib2, icu, libffi,       libxau, libxcb, libxdmcp, libxext, libxi, pcre
      xfce/libxfce4ui: add dependencies on atk, cairo, dbus, dbus-glib, expat,     fontconfig, freetype2, gdk-pixbuf2, harfbuzz, libffi, libice, libpng,     libsm, libx11, libxau, libxcb, libxdmcp, libxext, libxfce4ui, libxrender,     pango, pcre, pixman
      video/lives: added dependencies on aalib, alsa-lib, atk, cairo, expat,     ffmpeg, fftw, fontconfig, freetype2, gdk-pixbuf2, glib2, harfbuzz, libdv,     libffi, libggi, libgii, libogg, libpng, libtheora, libx11, libxau,     libxcb, libxdmcp, libxext, libxrender, libxxf86dga, libxxf86vm,     orc, pango, pcre, pixman, schroedinger, slang
      devel/llvm: add dependency on libffi
      utils/libnotify: add dependencies on gdk-pixbuf2, glib2, libffi,     libpng, pcre
      gnome2-libs/libsoup: add dependencies on dbus, icu, libffi, libgcrypt, pcre
      gnome2-libs/librsvg2: add dependencies on added dependencies on atk, expat,     gdk-pixbuf2, gtk+2, gtk+3, harfbuzz, libffi, libpng, libxau, libxcb, libxdmcp,     libxext, libxrender, pcre, pixman
      gnome2-libs/libgnome-keyring: add dependencies on libffi, libgpg-error and pcre
      gnome2-libs/libgee: add dependencies on libffi and pcre
      libs/libfm: add dependencies on fontconfig, freetype2, gdk-pixbuf2,     libexif, libffi, pcre
      gnome2-libs/libgnome: add dependencies on dbus, dbus-glib, icu, libffi,     openssl, orbit2, pcre
      http/webkitgtk: fix syntax error in DEPENDS
      gnome2-libs/libcanberra: add dependencies on atk, cairo, fontconfig, freetype2,     gdk-pixbuf2, glib2, harfbuzz, libogg, libpng, libtool, libx11,     pango, pixman
      gnome2-libs/libgnomecanvas: add dependencies on atk, gdk-pixbuf2, glib2, libpng,     pixman
      gnome2-libs/libbonobo: add dependencies on glib2
      devel/llvm: make dependency on libffi optional
      fonts-x11/gohufont: new spell, a fixed-width bitmap font
      devel/git: version 1.8.0.3
      collab/subversion: version 1.7.8
      graphics/imagemagick: version 6.8.1-5
      http/webkitgtk: add configuration options for selecting     the acceleration backend and the unicode backend, remove     dependencies on gstreamer, libffi, libxrender and pcre
      gnome2-libs/libgnome: remove dependencies on dbus, dbus-glib, icu, libffi, openssl, pcre
      libs/libfm: make dependency on libexif optional, remove dependencies on libffi and pcre
      Revert "gnome2-libs/libgee: add dependencies on libffi and pcre"
      gnome2-libs/libgnome-keyring: remove dependencies on libffi and pcre
      gnome2-libs/librsvg2: make dependencies on vala and gdk-pixbuf2 optional, remove dependencies on libxau, libxcb, libxdmcp, libxext, libxrender and pcre
      remove dependencies on icu, libffi and pcre, add optional dependency on gobject-introspection
      utils/libnotify: remove dependencies on libffi and pcre, add optional dependency on gobject-introspection
      video/lives: remove dependencies on expat, libggi, libgii, libpng,     libxau, libxcb, libxdmcp, libxext, libxrender, libxxf86dga,     libxxf86vm, orc, pcre and slang, add optional dependencies on     ffmpeg, libpng, ladspa, libunicap and liboil
      libs/openscenegraph: fix compile error with recent versions of xine-lib
      libs/openscenegraph: remove dependency on openthreads
      libs/openproducer: change dependency on openthreads to openscenegraph
      libs/openproducer: version 1.1-1
      libs/openthreads: deprecated in favour of openscenegraph
      xfce/libxfce4ui: remove dependencies on expat, libffi, libice,     libxau, libxcb, libxdmcp, libxext, libxrender and pcre
      remove dependencies on icu, libffi, libxau, libxcb, libxdmcp, libxext and pcre
      video/mjpegtools: remove dependencies on aalib, expat, libffi, libggi,     libgii, libxau, libxcb, libxdmcp, libxext, libxrender, libxxf86vm,     pcre and slang; make dependencies on atk, cairo, fontconfig,     freetype2 gdk-pixbuf2, harfbuzz, glib2, libx11, pango and glib2     dependent on the optional dependency on gtk+2
      gnome2-libs/libcanberra: remove dependencies on libxau, libxcb, libxdmcp, libxext,     libxrender, expat, libffi and pcre
      gnome2-libs/orbit2: remove dependencies on libffi and pcre
      gnome2-libs/pango: remove dependencies on libxcb, libxext, expat, libffi, pcre
      gnome2-libs/policykit: remove dependencies on libffi and pcre
      Revert "gnome2-libs/pygobject: add dependency on pcre"
      xfce/thunar: remove dependencies on expat, libffi, libxau, libxcb, libxdmcp, libxext, libxrender
      Revert "devel/vala: add dependencies on libffi and pcre"
      Revert "disk/udev: add dependencies on libffi and pcre"
      gnome2-libs/vte: remove dependencies on expat, libffi, libxau, libxcb, libxdmcp, libxrender and pcre
      xfce/xfconf: remove dependencies on libffi, libxext and pcre
      fonts-x11/uw-ttyp0: new spell, a fixed-width font
      doc/miscfiles: remove SOURCE2
      devel/git: version 1.8.1
      graphics/imagemagick: version 6.8.1-7
      mail/claws-mail: added optional dependency on bogofilter and     network-manager, removed dependencies on libffi, bzip2, libxau,     libxcb, libxdmcp, libxext, libxrender, libssh2, pcre and zlib,     made the dependency on libassuan dependent on the dependency on gpgme
      devel/graphviz: removed dependencies on bzip2, icu, ilmbase, lcms,     libcroco, libffi, libmng, libxau, libxcb, libxdmcp, libxext,     openexr, pcre, tiff, util-linux
      video-libs/gst-ffmpeg: remove dependencies icu, libffi and pcre
      gnome2-libs/gnome-vfs2: remove dependencies on icu, libffi, orbit2, pcre
      devel/scala: version 2.10.0
      crypto/nss: add 3.14 branch
      http/firefox: version 18.0
      haskell/haskell-x11: version 1.6.0.2
      windowmanagers/xmonad: version 0.11
      wm-addons/xmonad-contrib: version 0.11
      http/firefox: change dependency on JPEG to libjpeg-turbo
      shell-term-fm/terminator: version 0.96
      mail/thunderbird: version 17.0.2
      chat-im/centerim: add option for installing the beta branch
      chat-irc/weechat: devel version 0.4.0-rc2
      graphics-libs/field3d: new spell, a library for representing voxel data
      graphics-libs/openimageio: new spell, a library for reading and writing images
      graphics-libs/opencolorio: new spell, a complete color management solution
      libs/libspnav: new spell, a replacement of the magellan library
      devel/tcl: version 8.6.0, add sub dependency on stable/devel branch
      devel/tk: version 8.6.0, add sub dependencies on stable/devel branch, force corresponding branch in tcl
      devel/itcl: new spell, object orientation for tcl
      graphics/gl2ps: new spell, an OpenGL to postscript printer
      libs/yaml-cpp: new spell, a YAML parser and emitter in C++
      devel/python: add check_self on tk and tcl cast
      devel/python3: add check_self on tk and tcl cast
      devel/ocaml: add check_self on cast binutils, tk, tcl
      devel/alt-ergo: version 0.95
      devel/why3: new spell, a rich library of proof task transformations
      devel/cppcheck: version 1.58
      utils/wyrd: new spell, a curses based front-end to remind
      graphics/dcraw: version 9.17
      graphics/darktable: version 1.1.2
      graphics/imagemagick: version 6.8.1-10
      audio-libs/faad2: remove obsolete macro from configure.in
      libs/libvdpau: version 0.6
      devel/oprofile: version 0.9.8
      science/maxima: version 5.29.1
      science/wxmaxima: version 12.09.0
      video/minitube: version 2.0
      http/firefox: version 18.0.1
      video/minitube: fix hashsum
      http/firefox: version 18.0.2
      fonts-x11/ttf-roboto: new spell, a family of sans-serif fonts
      graphics/darktable: version 1.1.3
      devel/git-cola: new spell, a GUI for git
      libs/gmp: version 5.1.1 (devel)
      add key 28C67298
      utils/coreutils: version 8.21
      audio-libs/liblrdf: version 0.5.0
      x11/conky: add optional support for hdd temperature, per task IO stats and IPv4 port monitoring
      x11/conky: add optional dependencies on ncurses and moc
      shell-term-fm/zsh: version 5.0.2
      audio-libs/libmad: fix obsolete macro in configure.ac
      mail/thunderbird: version 17.0.3, security update
      x11-libs/unity-greeter: remove obsolete patch
      x11-libs/unity-greeter: include libX11 in LIBS in BUILD
      fonts-x11/ttf-roboto: install to /usr/share/fonts/X11/TTF
      fonts-x11/gohufont: install to /usr/share/fonts/X11/misc
      fonts-x11/terminus-font: install to /usr/share/fonts/X11/misc
      windowmanagers/xmonad: install manpage
      http/webkitgtk3: add dependencies on perl, PYTHON and RUBY
      http/firefox: disable avx when using gcc 4.7
      x11-toolkits/fltk: provide sub dependency on OPENGL
      audio-players/alsaplayer: fix SOURCE_URL[0]
      graphics/darktable: remove dependency on fop
      devel/wdiff: version 1.1.2
      science/gpsbabel: version 1.4.4
      graphics-libs/babl: pass -fi to autoreconf
      science/qlandkarte-gt: add sub dependency on OPENGL for qt4
      libs/libfm: version 1.1.0
      shell-term-fm/pcmanfm: version 1.1.0
      gnu/gcc: use new version of the ada bootstrap compiler
      gnu/gcc: cleanup for moving gcc 4.7.2 into test grimoire
      gnu/gcc: remove redundant libffi
      gnu/gcc: fix -ffast-math
      gnu/gcc: fix header generation for libgo
      x11-toolkits/gtk+2: version 2.24.16
      shell-term-fm/zsh: fix SOURCE_URL[0]
      x11/lightdm: add dependency on itstool
      chat-im/licq: version 1.7.1
      x11-libs/unity-greeter: version 13.04.1
      devel/qt-creator: version 2.6.2 and 2.7.0-beta
      kernels/nct6775: new spell, driver for NCT6775F, NCT6776F and NCT6779D
      x11-toolkits/gtk+2: fix SOURCE_HASH
      graphics/imagemagick: version 6.8.3-5
      x11/lightdm: set pam files executable
      wm-addons/i3status: add dependency on yajl, make the dependency on wireless_tools mandatory
      utils/cpuburn: fix compile error on x86_64
      utils/powertop: version 2.2
      windowmanagers/fvwm: version 2.6.5
      wm-addons/bbpager: version 0.4.7
      graphics/nitrogen: version 1.5.2
      x11/xdotool: new spell, lets you programmatically simulate keyboard and mouse activity
      devel/ghc: version 7.6.2
      haskell/haskell-x11: remove BUILD
      haskell/haskell-x11: add dependencies on libx11, libxext, libxrandr
      haskell/HASKELL_POST_REMOVE: forcefully unregister packages
      devel/darcs: move to haskell/darcs
      haskell/haskell-bytestring: deprecated in favour of ghc
      haskell/haskell-network: remove dependency on haskell-bytestring
      haskell/haskell-parsec: remove dependency on haskell-bytestring
      haskell/haskell-quickcheck: version 2.5.1.1
      haskell/haskell-dlist: new spell, a list-like type supporting O(1) append
      haskell/haskell-data-default: new spell, a class for types with a default value
      haskell/haskell-x11: version 1.6.1.1
      haskell/haskell-zlib: new spell, zlib bindings for haskell
      haskell/haskell-primitive: new spell, primitive memory-related operations
      haskell/haskell-vector: new spell, efficient arrays
      haskell/haskell-tar: new spell, reading, writing and manipulating tar archive files
      haskell/haskell-mmap: new spell, memory mapped files for POSIX and Windows
      haskell/haskell-haskeline: new spell, a command-line interface for user input, written in Haskell
      haskell/haskell-dataenc: new spell, data encoding library
      haskell/haskell-regex-posix: version 0.95.2
      haskell/haskell-hashed-storage: new spell, hashed file storage support code
      haskell/darcs: version 2.8.4
      wm-addons/xmonad-contrib: fix compile error
      haskell/haskell-deepseq: deprecated in favour of ghc
      kernels/linux: version 3.8.2
      update latest.defaults, fixup for f1c9d131914f15bdd193de12df57ce81dfbaa371
      haskell/happy: version 1.18.10
      graphics/imagemagick: version 6.8.3-7
      devel/qt-creator: devel 2.7.0-rc
      utils/gnuplot: version 4.6.1
      http/firefox: version 19.0.2, security update
      mail/thunderbird: version 17.0.4esr, security update
      audio-players/ncmpcpp: version 0.5.10
      disk/cdrtools: version 3.01a13
      graphics-libs/ogre: version 1-8-1
      devel/git-cola: version 1.8.2
      devel/florist: version 2012
      graphics-libs/libwacom: version 0.7
      x11/lightdm: fix typo in init script
      x11/lightdm: reformat description
      x11-libs/unity-greeter: add dependency on gnome-settings-daemon
      xorg-app/xdm: version 1.1.11
      xorg-app/xdm: use X's default authentication mechanism
      graphics/darktable: version 1.1.4
      science/yacas: new spell, a computer algebra system
      graphics/xli: new spell, a command line driven image viewer
      graphics/xli: add dependencies on JPEG, libpng, libxext and zlib
      haskell/haskell-x11-rm: new spell, Xrm bindings for haskell
      graphics/imagemagick: version 6.8.3-10
      utils/powertop: version 2.3
      science/qlandkarte-gt: version 1.7.0
      graphics/xli: version 1.17.0
      devel/qt-creator: version 2.7.0
      editors/texmaker: version 4.0.1
      graphics/darktable: remove -Werror from FLAGS
      graphics/djvulibre: version 3.5.25.3
      http/firefox: disable avx for all gcc versions >= 4.6
      fix build error due to qt4 missin from $PATH and incompatible system zlib
      devel/bin86: version 0.16.19
      libs/glibc: TMPFS=off
      graphics-libs/harfbuzz: version 0.9.14
      utils/installwatch: fix function signatures
      video-libs/live: version 2013.03.23
      e-17/evas: fix glib include paths
      devel/binutils: version 2.23.2
      kernels/linux: version 3.8.5
      graphics/imagemagick: version 6.8.4-3
      graphics/imagemagick: add sub dependency for HDRI
      graphics-libs/pythonmagick: add dependency on imagemagick with HDRI enabled
      python-pypi/python-futures: new spell, backport of concurrent.futures to python2
      python-pypi/urlwatch: new spell, a tool for monitoring webpages for updates
      libs/sip: version 4.14.5
      libs/pyqt4: version 4.10
      x11-toolkits/qscintilla: version 2.7.1
      python-pypi/mechanize: version 0.2.5
      python-pypi/clientform: deprecated, is part of mechanize now
      python-pypi/lxml: version 3.1.1
      disk/libmtp: version 1.1.6
      python-pypi/beautifulsoup: version 3.2.1
      python-pypi/python-netifaces: new spell, portable network interface information
      python-pypi/python-cssselect: new spell, a parser for CSS3 selectors
      libs/podofo: change dep on lua51 to lua, make it mandatory
      python-pypi/calibre: version 0.9.25
      x11-toolkits/qt4-private-headers: new spell, private headers for qt4
      python-pypi/calibre: add dependency on qt4-private-headers
      python-pypi/calibre: remove obsolete patch
      python-pypi/calibre: add SOURCE_HASH
      gnome3-libs/libsecret: version 0.15
      libs/nspr: version 4.9.6
      crypto/nss: version 3.14.3
      http/firefox: version 20.0
      fixup for 8ffe1be7f82f556c74b4d1fac110a68617d031ac
      science/qlandkarte-gt: add sub dependency on OPENGL for qt4
      utils/littleutils: version 1.0.27
      science/stellarium: fix SOURCE_URL[0]
      fixup 40047660d2b05120389957ffb1586a6a729cf85c
      devel/ghc: use default_build_make
      shell-term-fm/eaglemode: add missing dependencies, fix SOURCE_URL[0]
      utils/latencytop: add dependencies on ncurses and gtk+2
      fixup 044deee59562ee70dbc2b1b0a4d77f38cbd1d273
      add dependencies on gcc with CXX, qt4 with SQLITE
      graphics/imagemagick: version 6.8.4-6
      gnome2-libs/glib2: version 2.36.0
      gnome2-libs/atk: version 2.8.0
      gnome2-libs/gdk-pixbuf2: version 2.28.0
      x11-toolkits/gtk+3: version 3.8.0
      shell-term-fm/shared-mime-info: version 1.1
      doc/evince: version 3.8.0
      mail/thunderbird: version 17.0.5, security update
      kernels/linux: version 3.8.6
      graphics/graphicsmagick: version 1.3.18
      graphics/darktable: version 1.2
      graphics/darktable: make dependency on kwallet a suggested one
      x11/nxcomp: version 3.5.0-2
      graphics/imagemagick: version 6.8.4-8
      devel/git: version 1.8.2.1
      x11/nxcomp: enforce CXXFLAGS
      x11/nxproxy: new spell, NX proxy library
      x11/x2goclient: new spell, Qt client for the x2go remote desktop
      http/firefox: version 20.0.1
      kernels/linux: version 3.8.7
      graphics/darktable: version 1.1.3
      devel/git-cola: new spell, a GUI for git
      libs/gmp: version 5.1.1 (devel)
      add key 28C67298
      utils/coreutils: version 8.21
      audio-libs/liblrdf: version 0.5.0
      x11/conky: add optional support for hdd temperature, per task IO stats and IPv4 port monitoring
      x11/conky: add optional dependencies on ncurses and moc
      shell-term-fm/zsh: version 5.0.2
      audio-libs/libmad: fix obsolete macro in configure.ac
      mail/thunderbird: version 17.0.3, security update
      x11-libs/unity-greeter: remove obsolete patch
      x11-libs/unity-greeter: include libX11 in LIBS in BUILD
      fonts-x11/ttf-roboto: install to /usr/share/fonts/X11/TTF
      fonts-x11/gohufont: install to /usr/share/fonts/X11/misc
      fonts-x11/terminus-font: install to /usr/share/fonts/X11/misc
      windowmanagers/xmonad: install manpage
      http/webkitgtk3: add dependencies on perl, PYTHON and RUBY
      http/firefox: disable avx when using gcc 4.7
      x11-toolkits/fltk: provide sub dependency on OPENGL
      audio-players/alsaplayer: fix SOURCE_URL[0]
      graphics/darktable: remove dependency on fop
      devel/wdiff: version 1.1.2
      science/gpsbabel: version 1.4.4
      graphics-libs/babl: pass -fi to autoreconf
      science/qlandkarte-gt: add sub dependency on OPENGL for qt4
      libs/libfm: version 1.1.0
      shell-term-fm/pcmanfm: version 1.1.0
      gnu/gcc: use new version of the ada bootstrap compiler
      gnu/gcc: cleanup for moving gcc 4.7.2 into test grimoire
      gnu/gcc: remove redundant libffi
      gnu/gcc: fix -ffast-math
      gnu/gcc: fix header generation for libgo
      x11-toolkits/gtk+2: version 2.24.16
      shell-term-fm/zsh: fix SOURCE_URL[0]
      x11/lightdm: add dependency on itstool
      chat-im/licq: version 1.7.1
      x11-libs/unity-greeter: version 13.04.1
      devel/qt-creator: version 2.6.2 and 2.7.0-beta
      kernels/nct6775: new spell, driver for NCT6775F, NCT6776F and NCT6779D
      x11-toolkits/gtk+2: fix SOURCE_HASH
      graphics/imagemagick: version 6.8.3-5
      x11/lightdm: set pam files executable
      wm-addons/i3status: add dependency on yajl, make the dependency on wireless_tools mandatory
      utils/cpuburn: fix compile error on x86_64
      utils/powertop: version 2.2
      windowmanagers/fvwm: version 2.6.5
      wm-addons/bbpager: version 0.4.7
      graphics/nitrogen: version 1.5.2
      x11/xdotool: new spell, lets you programmatically simulate keyboard and mouse activity
      devel/ghc: version 7.6.2
      haskell/haskell-x11: remove BUILD
      haskell/haskell-x11: add dependencies on libx11, libxext, libxrandr
      haskell/HASKELL_POST_REMOVE: forcefully unregister packages
      devel/darcs: move to haskell/darcs
      haskell/haskell-bytestring: deprecated in favour of ghc
      haskell/haskell-network: remove dependency on haskell-bytestring
      haskell/haskell-parsec: remove dependency on haskell-bytestring
      haskell/haskell-quickcheck: version 2.5.1.1
      haskell/haskell-dlist: new spell, a list-like type supporting O(1) append
      haskell/haskell-data-default: new spell, a class for types with a default value
      haskell/haskell-x11: version 1.6.1.1
      haskell/haskell-zlib: new spell, zlib bindings for haskell
      haskell/haskell-primitive: new spell, primitive memory-related operations
      haskell/haskell-vector: new spell, efficient arrays
      haskell/haskell-tar: new spell, reading, writing and manipulating tar archive files
      haskell/haskell-mmap: new spell, memory mapped files for POSIX and Windows
      haskell/haskell-haskeline: new spell, a command-line interface for user input, written in Haskell
      haskell/haskell-dataenc: new spell, data encoding library
      haskell/haskell-regex-posix: version 0.95.2
      haskell/haskell-hashed-storage: new spell, hashed file storage support code
      haskell/darcs: version 2.8.4
      wm-addons/xmonad-contrib: fix compile error
      haskell/haskell-deepseq: deprecated in favour of ghc
      kernels/linux: version 3.8.2
      update latest.defaults, fixup for f1c9d131914f15bdd193de12df57ce81dfbaa371
      haskell/happy: version 1.18.10
      graphics/imagemagick: version 6.8.3-7
      devel/qt-creator: devel 2.7.0-rc
      utils/gnuplot: version 4.6.1
      http/firefox: version 19.0.2, security update
      mail/thunderbird: version 17.0.4esr, security update
      audio-players/ncmpcpp: version 0.5.10
      disk/cdrtools: version 3.01a13
      graphics-libs/ogre: version 1-8-1
      devel/git-cola: version 1.8.2
      devel/florist: version 2012
      graphics-libs/libwacom: version 0.7
      x11/lightdm: fix typo in init script
      x11/lightdm: reformat description
      x11-libs/unity-greeter: add dependency on gnome-settings-daemon
      xorg-app/xdm: version 1.1.11
      xorg-app/xdm: use X's default authentication mechanism
      graphics/darktable: version 1.1.4
      science/yacas: new spell, a computer algebra system
      graphics/xli: new spell, a command line driven image viewer
      graphics/xli: add dependencies on JPEG, libpng, libxext and zlib
      haskell/haskell-x11-rm: new spell, Xrm bindings for haskell
      graphics/imagemagick: version 6.8.3-10
      utils/powertop: version 2.3
      science/qlandkarte-gt: version 1.7.0
      graphics/xli: version 1.17.0
      devel/qt-creator: version 2.7.0
      editors/texmaker: version 4.0.1
      graphics/darktable: remove -Werror from FLAGS
      graphics/djvulibre: version 3.5.25.3
      http/firefox: disable avx for all gcc versions >= 4.6
      fix build error due to qt4 missin from $PATH and incompatible system zlib
      devel/bin86: version 0.16.19
      libs/glibc: TMPFS=off
      graphics-libs/harfbuzz: version 0.9.14
      utils/installwatch: fix function signatures
      video-libs/live: version 2013.03.23
      e-17/evas: fix glib include paths
      devel/binutils: version 2.23.2
      kernels/linux: version 3.8.5
      graphics/imagemagick: version 6.8.4-3
      graphics/imagemagick: add sub dependency for HDRI
      graphics-libs/pythonmagick: add dependency on imagemagick with HDRI enabled
      python-pypi/python-futures: new spell, backport of concurrent.futures to python2
      python-pypi/urlwatch: new spell, a tool for monitoring webpages for updates
      libs/sip: version 4.14.5
      libs/pyqt4: version 4.10
      x11-toolkits/qscintilla: version 2.7.1
      python-pypi/mechanize: version 0.2.5
      python-pypi/clientform: deprecated, is part of mechanize now
      python-pypi/lxml: version 3.1.1
      disk/libmtp: version 1.1.6
      python-pypi/beautifulsoup: version 3.2.1
      python-pypi/python-netifaces: new spell, portable network interface information
      python-pypi/python-cssselect: new spell, a parser for CSS3 selectors
      libs/podofo: change dep on lua51 to lua, make it mandatory
      python-pypi/calibre: version 0.9.25
      x11-toolkits/qt4-private-headers: new spell, private headers for qt4
      python-pypi/calibre: add dependency on qt4-private-headers
      python-pypi/calibre: remove obsolete patch
      python-pypi/calibre: add SOURCE_HASH
      gnome3-libs/libsecret: version 0.15
      libs/nspr: version 4.9.6
      crypto/nss: version 3.14.3
      http/firefox: version 20.0
      fixup for 8ffe1be7f82f556c74b4d1fac110a68617d031ac
      science/qlandkarte-gt: add sub dependency on OPENGL for qt4
      utils/littleutils: version 1.0.27
      science/stellarium: fix SOURCE_URL[0]
      fixup 40047660d2b05120389957ffb1586a6a729cf85c
      devel/ghc: use default_build_make
      shell-term-fm/eaglemode: add missing dependencies, fix SOURCE_URL[0]
      utils/latencytop: add dependencies on ncurses and gtk+2
      fixup 044deee59562ee70dbc2b1b0a4d77f38cbd1d273
      add dependencies on gcc with CXX, qt4 with SQLITE
      graphics/imagemagick: version 6.8.4-6
      gnome2-libs/glib2: version 2.36.0
      gnome2-libs/atk: version 2.8.0
      gnome2-libs/gdk-pixbuf2: version 2.28.0
      x11-toolkits/gtk+3: version 3.8.0
      shell-term-fm/shared-mime-info: version 1.1
      doc/evince: version 3.8.0
      mail/thunderbird: version 17.0.5, security update
      kernels/linux: version 3.8.6
      graphics/graphicsmagick: version 1.3.18
      graphics/darktable: version 1.2
      graphics/darktable: make dependency on kwallet a suggested one
      x11/nxcomp: version 3.5.0-2
      graphics/imagemagick: version 6.8.4-8
      devel/git: version 1.8.2.1
      x11/nxcomp: enforce CXXFLAGS
      x11/nxproxy: new spell, NX proxy library
      x11/x2goclient: new spell, Qt client for the x2go remote desktop
      http/firefox: version 20.0.1
      graphics/imagemagick: version 6.8.4-9
      audio-soft/rockbox-utility: version 1.3.1
      audio-players/ripperx: fix SOURCE_URL[0], add -lm to LIBS
      utils/pciutils: version 3.2.0
      kernels/kmod: version 5
      disk/udev: version 182
      audio-players/cdparanoia: install /usr/bin/cdparanoia executable for non-root users
      disk/cdrtools: version 3.01a14
      perl-cpan/webservice-musicbrainz: new spell, Interface to MusicBrainz web services
      audio-soft/abcde: version 2.5.4
      gnustep-apps/gnustep-oolite: fix WEB_SITE
      gnustep-libs/gnustep-make: version 2.6.4
      gnustep-libs/gnustep-back: version 0.23.0
      Revert "portaudio: => v19_20111121"
      audio-creation/espeak: version 1.47.07
      kernels/linux: version 3.8.9
      disk/udev: install udevadm to /sbin
      graphics/darktable: add -fpermissive to CXXFLAGS
      devel/git: version 1.8.2.2
      graphics/imagemagick: version 6.8.5-3
      python-pypi/mercurial: version 2.6
      devel/cppcheck: version 1.59
      utils/remind: version 03.01.13
      utils/wyrd: version 1.4.6
      x11/merkaartor: version 0.18.1
      kernels/linux: version 3.9.1
      collab/subversion: version 1.7.9
      perl-cpan/geo-gpx: new spell, create and parse gpx files
      perl-cpan/try-tiny: new spell, minimal try/catch with proper localization of $@
      perl-cpan/test-fatal: new spell, an alternative to the popular Test::Exception
      perl-cpan/test-requires: new spell, checks to see if the module can be loaded
      perl-cpan/module-runtime: new spell, runtime module handling
      perl-cpan/module-implementation: new spell, loads one of several alternate underlying implementations for a module
      perl-cpan/params-validate: version 1.07
      perl-cpan/datetime-locale: version 0.45
      perl-cpan/list-moreutils: version 0.33
      perl-cpan/class-load: new spell, a working (require "Class::Name") and more
      perl-cpan/params-util: new spell, simple, compact and correct param-checking functions
      perl-cpan/sub-install: new spell,  install subroutines into packages easily
      perl-cpan/sub-exporter: new spell, a sophisticated exporter for custom-built routines
      perl-cpan/test-tester: new spell, Ease testing test modules built with Test::Builder
      perl-cpan/test-output: new spell, Utilities to test STDOUT and STDERR messages
      perl-cpan/data-optlist: new spell, parse and validate simple name/value option pairs
      perl-cpan/datetime-timezone: version 1.59
      perl-cpan/test-differences: version 0.61
      perl-cpan/xml-tokeparser: new spell, Simplified interface to XML::Parser
      perl-cpan/xml-descent: new spell, Recursive descent XML parsing
      perl-cpan/datetime: version 1.03
      shell-term-fm/bash: add patches 38-45
      perl-cpan/datetime-format-builder: new spell, Create DateTime parser classes and objects
      perl-cpan/file-find-rule: new spell, Alternative interface to File::Find
      perl-cpan/datetime-format-iso8601: new spell, Parses ISO8601 formats
      perl-cpan/test-simple: version 0.98_05
      perl-cpan/class-load-xs: new spell, XS implementation parts of Class::Load
      perl-cpan/class-factory-util: new spell, provide utility methods for factory classes
      perl-cpan/datetime-format-builder: add dependency on class-factory-util
      perl-cpan/geo-gpx: add dependency on class-load-xs
      Revert "perl-cpan/class-load-xs: new spell, XS implementation parts of Class::Load"
      perl-cpan/class-load-xs: new spell, XS implementation parts of Class::Load
      gnu.gpg: refresh keys
      gnu.gpg: add 937EC0D2
      editors/gawk: version 4.1.0
      kernels/linux: version 3.9.2
      x11/blueman: version 1.23
      utils/bluez-hcidump: version 2.5
      http/firefox: version 21.0
      devel/git-cola: version 1.8.3
      devel/git: version 1.8.2.3
      devel/perl: version 5.18.0, security update
      kernels/linux: version 3.9.3
      x11-toolkits/gtk+2: version 2.24.18
      gnome3-libs/gnome-icon-theme-symbolic: version 3.6.2
      utils/desktop-file-utils: version 0.21
      x11/merkaartor: add missing dependencies
      devel/gdb: disable_pic
      Revert "devel/perl: version 5.18.0, security update"
      science/ltl2ba: new spell, fast translation from LTL formulae to Büchi automata
      shell-term-fm/rxvt-unicode: version 9.18
      kernels/linux: version 3.9.4
      wm-addons/procmeter: install manpages
      wm-addons/procmeter: fix modules Makefile
      xorg-app/xclock: version 1.0.6
      devel/ocamlgraph: version 1.8.3
      devel/zarith: new spell, arbitrary precision integers for ocaml
      devel/camlp5: version 6.09
      devel/coq: add dependency on zarith
      devel/frama-c: version Fluorine-20130501
      devel/why: new spell, a software verification platform
      ftp/wget: fix bug #546
      video/ffmpeg: version 1.2.1
      shell-term-fm/rxvt-unicode: add patch to fix bug #551
      Revert "Revert "devel/perl: version 5.18.0, security update""
      python-pypi/mercurial: version 2.6.1
      devel/git: version 1.8.3
      devel/oclint: new spell, a static analyzer for C/C++/Objective C code
      graphics/darktable: version 1.2.1
      audio-players/qmpdclient: add libX11 to LIBS
      audio-libs/libid3tag: add patches from gentoo to fix buffer overflow and other bugs
      devel/ghc: version 7.6.3
      libs/sqlite3-ocaml: new spell, sqlite3 bindings for ocaml
      devel/why3: add optional dependency on sqlite3-ocaml
      devel/why3: version 0.81
      devel/why: fix incompatibility with frama-c Fluorine-20130501
      devel/alt-ergo: version 0.95.1
      audio-players/cantata: new spell, a front-end for mpd
      libs/c-ares: move -DPIC to CPPFLAGS to avoid failure in configure
      crypto/keepassx: patch in missing includes
      libs/findlib: fix WEB_SITE
      fixup 3e4ed16a7f33fcc65582374a7e18f377961d1b45
      devel/why3: use make_single in INSTALL
      devel/graphviz: version 2.30.1
      libs/fftw: fix issue with texinfo-5
      utils/ocaml-csv: new spell, a library and cli tool for csv processing
      perl-cpan/data-dumper-concise: new spell, a concise data dumper for perl
      utils/gnuplot: version 4.6.3
      kernels/linux: version 3.9.5
      disk/lilo: version 24.0
      perl-cpan/test-nowarnings: new spell, make sure your perl tests do not emit warnings
      perl-cpan/test-deep: new spell, extremely flexible deep comparison
      perl-cpan/extutils-cbuilder: version 0.280205
      perl-cpan/sub-exporter-progressive: only use Sub::Exporter if you need it
      perl-cpan/scalar-util: new spell, a selection of general-utility scalar subroutines
      perl-cpan/devel-globaldestruction: new spell, eases global destruction in perl
      perl-cpan/sys-syslog: deprecated in favour of perl
      net/snmptt: remove dependency on sys-syslog
      perl-cpan/log-report: new spell, error message dispatcher with translation
      perl-cpan/xml-libxml-simple: new spell, a rewrite of XML::Simple
      perl-cpan/xml-compile-tester: new spell, xml-compile related regression testing
      perl-cpan/xml-compile: new spell, compilation based xml processing
      perl-cpan/xml-compile-cache: new spell, cache compiled xml translators
      perl-cpan/data-peek: new spell, collection of low-level debug facilities
      perl-cpan/geo-kml: new spell, produce GoogleEarth KML/KMZ files
      windowmanagers/herbstluftwm: new spell, a manual tiling windowmanager
      utils/ncdu: version 1.10
      python-pypi/pykml: new spell, a python package for generating and parsing kml
      kernels/linux: version 3.9.6
      devel/qgrit: new spell, a GUI for git rebase -i
      devel/gitg: version 0.2.7
      python-pypi/git-review: new spell, a git command for submitting branches to gerrit
      devel/git: version 1.8.3.1
      collab/subversion: version 1.8.0
      kernels/linux: version 3.9.7
      collab/subversion: depends on apr/apr-util instead of APR/APU, fixes bug #558
      perl-cpan/strictures: new spell, make all warnings fatal
      graphics/gimp: version 2.8.6
      mail/claws-mail: version 3.9.2
      graphics/darktable: version 1.2.2
      python-pypi/jinja2: version 2.7
      python-pypi/feedgenerator: new spell, Django\'s feed generator
      doc/docutils: version 0.10
      python-pypi/pytz: version 2013b
      python-pypi/blinker: new spell, fast & simple object-to-object and broadcast signaling
      python-pypi/unidecode: new spell, ASCII transliterations of Unicode text
      python-pypi/typogrify: new spell, A set of Django template filters to make caring about typography on the web a bit easier
      python-pypi/markdown: new spell, markdown support for python
      python-pypi/pelican: new spell, a tool to generate a static blog from reStructuredText or Markdown input files
      python-pypi/pelican: add dependency on six
      python-pypi/smartypants: new spell, a smart-quotes plugin
      python-pypi/pelican: add dependency on smartypants
      python-pypi/staticgallery: new spell, a script for generating static galleries
      graphics/gexiv2: version 0.6.1
      python-pypi/genshi: version 0.7
      graphics/pyexiv2: new spell, exiv2 bindings for python
      http/lazygal: new spell, a static gallery generator
      doc/docbook-xsl: fix SOURCE_URL
      graphics/imagemagick: version 6.8.6-3
      http/cssed: new spell, a css editor
      haskell/haskell-bloomfilter: new spell, pure and impure bloom filters
      haskell/haskell-edit-distance: new spell, Levenshtein and restricted Damerau-Levenshtein algorithms
      haskell/haskell-network: version 2.4.1.2
      haskell/haskell-hslogger: new spell, a logging framework
      haskell/haskell-http: new spell, client-side http support
      haskell/haskell-ifelse: new spell, anaphoric and miscellaneous useful control-flow
      haskell/haskell-json: new spell, JSON support
      haskell/haskell-hunit: new spell, unit testing for haskell
      haskell/haskell-missingh: new spell, a library of utility functions
      haskell/haskell-base-unicode-symbols: new spell, unicode symbols for some functions
      haskell/haskell-transformers-base: new spell, lift computations from the bottom of a transformer stack
      haskell/haskell-monad-control: new spell, lift control operations
      haskell/haskell-monadcatchio-transformers: new spell, functions for throwing and catching exceptions
      haskell/haskell-safesemaphore: new spell, safer semaphore
      haskell/haskell-sha: new spell, SHA message digest
      haskell/haskell-unix-compat: new spell, portable implementation of the unix package
      haskell/haskell-byteable: new spell, abstract class to manipulate sequence of bytes
      haskell/haskell-cryptohash: new spell, collection of crypto hashes
      haskell/haskell-maccatcher: new spell, obtain the MAC address on *NIX and Windows
      haskell/haskell-uuid: new spell, uuids for haskell
      haskell/haskell-git-annex: new spell, managing files with git without checking them into git
      haskell/haskell-git-annex: version 4.20130709
      kernels/linux: version 3.10.1
      graphics/enblend: version 4.1.1
      x11-toolkits/wxgtk: version 2.8.12.1
      graphics/imagemagick: version 6.8.6-5
      graphics/argyllcms: version 1.5.1
      kernels/linux: version 3.10.2
      fixup for fcb2b347190c17d7ecc4e6677c8aecd03de5788a
      utils/xicc: new spell, a tool for setting the X server's _ICC_PROFILE property
      haskell/haskell-git-annex: version 4.20130723
      kernels/linux: version 3.10.3
      graphics/darktable: add support for nx100 liliput plus
      science/qlandkarte-gt: version 1.7.1
      crypto/mosh: version 1.2.4
      libs/protobuf: version 2.5.0
      perl-cpan/io-tty: version 1.10
      haskell/haskell-git-annex: version 4.20130802
      graphics/exiv2: add patches from upstream to fix a memory leak, add support for recent cameras/lenses, fix use after delete
      graphics-libs/ftgl: fix linker error
      utils/nocache: new spell, tool for excluding processes from the buffer cache
      utils/nocache: fix path in nocache executable
      editors/vim: version 7.4
      python-pypi/pelican: depend on python-markdown instead of markdown
      python-pypi/clint: new spell, Python Command-line Application Tools
      python-pypi/argh: new spell, an unobtrusive argparse wrapper with natural syntax
      python-pypi/pilkit: new spell, a collection of utilities and processors for the Python Imaging Libary
      python-pypi/sigal: new spell, a simple static gallery generator
      python-pypi/markdown: deprecated in favor of python-pypi/markdown
      graphics/rawtherapee: version 4.0.11
      python-pypi/pillow: new spell, a fork of pil that is maintained actively
      python-pypi/pil: deprecated in favour of pillow
      graphics/mcomix: changed dep on pil to pillow
      graphics/uniconvertor: changed dep on pil to pillow
      graphics/comix: changed dep on pil to pillow
      graphics/keyjnote: changed dep on pil to pillow
      graphics/skencil: changed dep on pil to pillow
      editors/scribus4: changed dep on pil to pillow
      audio-players/ccx2: changed dep on pil to pillow
      audio-players/exaile: changed dep on pil to pillow
      http/lazygal: change dep on pil to pillow
      http/webcleander: change dep on pil to pillow
      ftp/tucan: change dep on pil to pillow
      python-pypi/pyicqt: change dep on pil to pillow
      python-pypi/hatta: depend on pillow instead of pil
      python-pypi/pymsnt: depend on pillow instead of pil
      python-pypi/staticgallery: depend on pillow instead of pil
      python-pypi/soya: depend on pillow instead of pil
      python-pypi/grecipe-manager: depend on pillow instead of pil
      python-pypi/pilkit: depend on pillow instead of pil
      python-pypi/calibre: depend on pillow instead of pil
      python-pypi/itools: depend on pillow instead of pil
      python-pypi/reportlab: depend on pillow instead of pil
      haskell/haskell-git-annex: version 4.20130815
      graphics/gphoto2: version 2.5.2
      graphics/pktriggercord: new spell, remote control software for Pentax DSLRs
      graphics/lensfun: version 0.2.7
      chat-im/licq: version 1.8.0
      http/newsbeuter: version 2.7
      devel/qt-creator: version 2.8.1
      haskell/haskell-attoparsec: new spell, a fast parser combinator library
      haskell/haskell-blaze-builder: new spell, an abstraction of buffered output of byte streams
      haskell/haskell-hashable: new spell, a class for values that can be converted to a hash value
      haskell/haskell-unordered-containers: new spell, efficient hashing-based container types
      haskell/haskell-text: version 0.11.3.1
      haskell/haskell-aeson: new spell, a JSON parsing and encoding library
      haskell/haskell-git-annex: version 4.20130827
      graphics/ufraw: version 0.19.2
      kernels/linux: version 3.10.10
      perl-cpan/image-exiftool: version 9.27
      graphics/dcraw: version 9.19
      audio-players/mpd: fix library search path
      graphics/fbida: version 2.09
      wm-addons/xmonad-contrib: version 0.11.2
      kernels/linux: version 3.11
      http/firefox: fix WEB_SITE
      science/qlandkarte-gt: version 1.7.3
      haskell/haskell-parsec: version 3.1.3
      haskell/haskell-hslogger: version 1.2.3
      haskell/haskell-missingh: version 1.2.0.2
      haskell/haskell-unordered-containers: version 0.2.3.2
      haskell/haskell-aeson: version 0.6.2.0
      haskell/haskell-uuid: version 1.2.14
      haskell/haskell-git-annex: version 4.20130909
      graphics/darktable: version 1.2.3
      kernels/linux: version 3.11.1
      net/nfs-utils: version 1.2.8
      net/iptraf-ng: version 1.1.4
      libs/libtirpc: fix SOURCE_URL[0]
      utils/input-utils: new spell, small suite of tools for debugging input layer problems
      http/firefox: version 24.0
      science/qlandkarte-gt: version 1.7.4
      devel/git: version 1.8.4.1
      haskell/haskell-git-annex: version 4.20131002
      kernels/linux: version 3.11.4
      chat-irc/weechat: stable 0.4.2, unstable 0.4.3-dev
      devel/make: version 4.0
      video-libs/live: version 2013.10.11
      graphics-libs/opencv: version 2.4.6.2
      video/ffmpeg: legacy version 0.7.16
      kernels/linux: version 3.11.6
      haskell/haskell-network: version 2.4.2.0
      devel/git-cola: version 1.9.1
      video/vlc: depend on stable branch of ffmpeg
      devel/qt-creator: devel version 3.0.0
      devel/cppcheck: version 1.62
      science-libs/eigen3: version 3.2.0
      haskell/haskell-git-annex: version 4.20131106
      libs/icu: force using gcc instead of clang++
      graphics/imagemagick: version 6.8.7-5
      science/qlandkarte-gt: version 1.7.5
      x11/merkaartor: add bug fixes from upstream
      science/gdal: version 1.9.2
      lxde/menu-cache: version 0.5.1
      libs/libfm: version 1.1.2.2
      shell-term-fm/pcmanfm: version 1.1.2
      libs/nspr: version 4.10.2
      http/firefox: version 25.0.1
      kernels/linux: version 3.12.1
      kernels/linux: version 3.12.2
      devel/qt-creator: version 3.0.0-rc1
      hasekll/haskell-git-annex: version 5.20131130
      devel/qt-creator: ensure installation to /usr
      crypto/nss: version 3.12.3
      http/firefox: version 26.0
      devel/git-cola: version 1.9.3
      devel/qt-creator: stable version 3.0.0
      devel/git: version 1.8.5.1
      mail/thunderbird: version 24.2.0
      mail/thunderbird: remove version number from thunberbird's installation path
      haskell/haskell-git-annex: version 5.20131213
      utils/i7z: version 0.27.2
      kernels/linux: version 3.12.6
      gnome2-libs/librsvg2: version 2.40.1
      x11/x2goclient: version 4.0.1.2
      haskell/haskell-git-annex: version 5.20131221
      devel/git: version 1.8.5.2
      x11-toolkits/gtk+3: version 3.8.8
      libs/fribidi: version 0.19.6
      video/minitube: version 2.1.5
      shell-term-fm/shared-mime-info: version 1.2
      graphics-libs/libwebp: version 0.3.1
      graphics/darktable: version 1.4
      haskell/haskell-stm: version 2.4.2
      haskell/haskell-async: version 2.0.1.5
      haskell/haskell-git-annex: version 5.20131230
      audio-players/cantata: version 1.2.1
      gnustep-libs/gnustep-base: version 1.24.6
      gnustep-libs/gnustep-make: version 2.6.6
      gnustep-libs/gnustep-gui: version 0.24.0
      gnustep-libs/gnustep-make: add script for invoking gnustep-make
      chat-libs/loudmouth: prevent build error due to use of deprecated symbols
      chat-im/mcabber: fix build with libotr >= 4.0.0
      chat-im/mcabber: give credit to Debian for patch
      audio-players/mpc: version 0.24
      audio-libs/libmpdclient: version 2.9
      libs/openscenegraph: version 3.2.0
      audio-players/mpd: version 0.18.6
      libs/libcdio: version 0.92
      video/mpv: version 0.3.1
      kernels/nct6775: deprecated, part of mainline linux now
      haskell/haskell-git-annex: version 5.20140107
      libs/muparser: fix SOURCE_URL
      x11-toolkits/qwt5: fix SOURCE_URL
      devel/cppcheck: version 1.63
      devel/cppcheck: install cfg files
      kernels/linux: add support for xz compressed files
      kernels/linux: version 3.12.7
      security/wireshark: version 1.10.5
      utils/zeroxml: new spell, a lightweight abstraction layer for xml
      devel/valgrind: version 3.9.0
      devel/valgrind: use empty CFLAGS to prevent segfault
      libs/libuv: new spell, a multi-platform support library with a focus on asynchronous I/O
      video/mpv: version 0.3.2
      kernels/linux: version 3.12.8
      utils/taskwarrior: version 2.3.0
      libs/openscenegraph: add dep on gdal and optional dep on qt4
      science/geos: version 3.4.2
      libs/libnoise: new spell, a coherent noise generator in C++
      libs/osgearth: new spell, a 3D mapping SDK for openscenegraph applications
      kernels/linux: add support for xz compressed kernels
      kernels/linux: version 3.13
      science-libs/netcdf: version 4.3.1
      libs/cfitsio: version 3360
      video/mpv: version 0.3.3
      libs/asio: version 1.10.1
      libs/openscenegraph: add deps on jasper, asio, pass location of freetype2 headers to cmake
      libs/openscenegraph: select mesa for opengl
      haskell/haskell-git-annex: version 5.20140116
      shell-term-fm/mc: fix incompatibility with ncurses
      kernels/linux: version 3.13.1
      haskell/haskell-git-annex: version 5.20140129
      devel/git-cola: version 1.9.4
      gnome2-libs/gtkhtml2: version 4.6.6
      cluster/lapack: version 3.5.0
      libs/findlib: version 1.4
      utils/ocaml-csv: version 1.3.2
      devel/ocaml: version 4.01.0
      devel/coq: fix detection of make during configure
      security/rkhunter: version 1.4.0
      video/mpv: version 0.3.4
      devel/qt-creator: version 3.0.1
      devel/gdb: version 7.7
      kernels/linux: version 3.12.2
      char-irc/weechat: stable 0.4.3, unstable 0.4.4-dev
      haskell/haskell-git-annex: version 5.20140210
      devel/ninja-build-system: new spell, a small build system with a focus on speed
      kernels/linux: version 3.13.3
      video/mpv: version 0.3.5
      devel/git: version 1.9.0
      shell-term-fm/zsh: version 5.0.5
      graphics-libs/harfbuzz: version 0.9.26
      graphics/darktable: version 1.4.1
      kernels/linux: version 3.13.4
      haskell/haskell-git-annex: version 5.20140221
      editors/vim: apply patches 7.4.001 to 7.4.183
      haskell/haskell-syb: version 0.4.1
      haskell/haskell-dlist: version 0.6.0.1
      haskell/haskell-data-default-class: new spell, a class for types with a default value
      haskell/haskell-data-default-instances-base: new spell, a class for types with a default value
      haskell/haskell-data-default-instances-containers: new spell, a class for types with a default value
      haskell/haskell-data-default-instances-dlist: new spell, a class for types with a default value
      haskell/haskell-data-default-instances-old-locale: new spell, a class for types with a default value
      haskell/haskell-data-default: version 0.5.3
      haskell/haskell-scientific: new spell, scientific numbers for haskell
      haskell/haskell-attoparsec: version 0.11.1.0
      haskell/haskell-unordered-containers: version 0.2.3.3
      haskell/haskell-sha: version 1.6.4
      haskell/haskell-safesemaphore: version 0.10.0
      haskell/haskell-quickcheck: version 2.6
      haskell/haskell-primitive: version 0.5.2.1
      haskell/haskell-parsec: version 3.1.5
      haskell/haskell-network: version 2.4.2.2
      haskell/haskell-monad-control: version 0.3.2.3
      haskell/haskell-http: version 4000.2.11
      haskell/haskell-hashable: version 1.2.1.0
      haskell/haskell-cryptohash: version 0.11.2
      haskell/haskell-blaze-builder: version 0.3.3.2
      haskell/haskell-network-info: new spell, a library for accessing a local computer's network info
      haskell/haskell-uuid: version 1.3.3
      haskell/haskell-aeson: version 0.7.0.1
      haskell/haskell-monads-tf: new spell, monad classes using type families
      haskell/haskell-monadcatchio-transformers: version 0.3.1.0
      haskell/haskell-vector: version 0.10.9.1
      wm-addons/alltray: fix linking, fix SOURCE_URL
      devel/stlink: new spell, tools for interacting with ST's ARM developer boards
      devel/git-cola: version 2.0.0
      haskell-case-insensitive: new spell, case insensitive string comparison for haskell
      audio-players/mpd: version 0.18.8
      audio-players/cantata: version 1.3.0.1
      crypto/gnutls: versions 3.2.12 and 3.1.22, fixes CVE-2014-0092 and CVE-2014-1959
      crypto/gnutls: remove unmaintained branches
      crypto/nss: version 3.15.5
      haskell/haskell-git-annex: version 5.20140306
      http/lynx: version 2.8.8rel1
      kernels/linux: version 3.13.6
      crypto/libssh: version 0.6.3
      mail/ssmtp: fix build errors
      perl-cpan/mime-base64: version 3.14
      python-pypi/markupsafe: version 0.19
      python-pypi/smartypants: version 1.8.3
      python-pypi/typogrify: version 2.0.4
      perl-cpan/xml-twig: version 3.46
      doc/docutils: version 0.11
      python-pypi/blinker: version 1.3
      python-pypi/pelican: version 3.3.0
      libs/libquvi-scripts: version 0.4.21
      libs/libquvi: fix SOURCE_URL
      audio-drivers/mudita24: new spell, a mixer GUI for ice1712 based sound cards
      graphics/vym: fix SOURCE_URL[0]
      spelling/goldendict: new spell, a meta-dictionary
      graphics/imagemagick: version 6.8.8-8
      video/mpv: version 0.3.6
      audio-plugins/swh-plugins: add missing patch
      science/qlandkarte-gt: version 1.7.6
      http/firefox: version 28.0
      smgl/firefox-smglwiki: fix install path
      audio-plugins/blop: fix SOURCE_URL[0]
      audio-plugins/cmt: honour our CFLAGS/CXXFLAGS
      audio-drivers/jack2: fix build error due to incompatibility with waf_build
      audio-soft/qjackctl: version 0.3.11
      audio-drivers/jack2: add dependency on dbus-python
      gnome2-libs/gsettings-desktop-schemas: version 3.11.5
      dave_robillard.gpg: add key 29727060
      audio-soft/alsa-patch-bay: fix build errors
      devel/git-cola: version 2.0.1
      audio-plugins/rt-plugins: new spell, a set of LADSPA plugins for crossover and equalization in active speakers
      audio-drivers/ngjackspa: new spell, a set of tools for using LADSPA plugins from jack
      haskell/haskell-git-annex: version 5.20140320
      audio-plugins/vlevel: new spell, a compressor with lookahead for LADSPA
      ftp/lftp: version 4.4.15
      kernels/schedtool: version 1.3.0
      audio-plugins/fil-plugins: version 0.3.0
      audio-plugins/mcp-plugins: fix SOURCE_URL and WEB_SITE
      audio-plugins/tap-plugins: version 0.7.2
      audio-plugins/vco-plugins: fix SOURCE_URL and WEB_SITE
      audio-plugins/rev-plugins: version 0.7.1
      audio-plugins/amb-plugins: version 0.8.1
      audio-libs/zita-resampler: new spell, a library for high-quality resampling
      audio-libs/zita-alsa-pcmi: new spell, a C++ wrapper around ALSA PCM devices
      audio-plugins/zita-ajbridge: new spell, a zita-alsa-pcmi based bridge between ALSA and jack
      audio-plugins/caps-plugins: version 0.9.23
      utils/rtirq: version 20130909
      audio-drivers/jack: version 0.124.1
      kernels/linux: version 3.13.7
      video/ffmpeg: version 2.2
      audio-plugins/calf-plugins: new spell, professional-grade audio plugins for jack
      audio-creation/lmms: version 1.0.0
      audio-creation/ecasound: version 2.9.1
      audio-libs/stk: new spell, the synthesis toolkit in C++
      audio-creation/lmms: add optional dependency on stk
      audio-libs/liblo: version 0.28
      libs/raptor: version 2.0.13
      remove options from waf that aren't common to all users of waf
      audio-libs/aubio: version 0.4.1
      audio-creation/ardour3: version 3.5.357
      audio-players/mpd: version 0.18.9
      audio-players/cantata: version 1.3.3
      audio-drivers/ngjackspa: install manpage
      audio-creation/jack-rack: fix linking, fix SOURCE_URL
      libs/gmp: version 6.0.0a
      video/mpv: version 0.3.7
      haskell-git-annex: version 5.20140403
      kernels/linux: version 3.13.9
      net/bmon: version 3.2
      shell-term-fm/spacefm: depend on UDEV instead of udev
      libs/libusb: depend on UDEV instead of udev
      utils/hal: depend on UDEV instead of udev
      x11/unclutter: depend on libx11, libxext and imake
      video-libs/gst-plugins-base: depend on libxdmcp
      video/mpv: depend on lua instead of LUA
      haskell/haskell-git-annex: version 5.20140406
      audio-soft/meterbridge: fix error when link with as-needed
      audio-plugins/rt-plugins: use cmake as build system
      python-pypi/pillow: version 2.4.0
      archive/upx: version 3.91
      libs/libtcod: new spell, a library for developing roguelike games
      libs/newt: version 0.52.17
      libs/cdk: version 5.0-20140118
      crypto/openssl: version 1.0.1g, fixes CVE-2014-0160
      devel/qt-creator: version 3.1.0
      python-pypi/python-ecdsa: version 0.11
      python-pypi/paramiko: version 0.13.0
      kernels/linux: version 3.14.2
      devel/git-cola: version 2.0.2
      libs/gflags: version 2.1.1
      libs/vsqlite++: new spell, C++ bindings for sqlite3
      haskell/haskell-mtl: version 2.1.3.1
      haskell/haskell-dataenc: version 0.14.0.7
      libs/gflags: pull source from github
      crypto/nss: versions 3.14.5, 3.16, remove obsolete branches
      http/firefox: version 29.0
      graphics/darktable: version 1.4.2
      haskell/haskell-haskeline: version 0.7.1.2
      haskell/haskell-hashed-storage: version 0.5.11
      video/mpv: version 0.3.9
      editors/emacs: versions 24.3
      haskell/haskell-stm: version 2.4.3
      haskell/haskell-async: add dependency on haskell-stm
      haskell/haskell-text: version 1.1.1.1
      haskell/haskell-scientific: version 0.2.0.2
      haskell/haskell-unordered-containers: version 0.2.4.0
      haskell/haskell-attoparsec: version 0.11.3.0
      haskell/haskell-aeson: version 0.7.0.3
      wm-addons/xmonad-contrib: version 0.11.3
      haskell/haskell-missingh: version 1.2.1.0
      haskell/haskell-bloomfilter: fix compile error with ghc 7.8.2
      libs/ncurses: add libtinfo symlink
      devel/ghc: version 7.8.2
      haskell/happy: version 1.19.3
      haskell/haskell-case-insensitive: version 1.2.0.0
      haskell/haskell-cryptohash: version 0.11.4
      haskell/haskell-dlist: version 0.7.0.1
      haskell/haskell-polyparse: version 1.9
      haskell-haxml: version 1.24.1
      haskell/haskell-hslogger: version 1.2.4
      haskell/haskell-http: version 4000.2.14
      haskell/haskell-mmap: version 0.5.9
      haskell/haskell-monads-tf: version 0.1.0.2
      haskell/haskell-transformers: version 0.4.0.0
      haskell/haskell-mtl: version 2.2.0.1
      haskell/haskell-network: version 2.5.0.0
      haskell/haskell-tf-random: new spell, a high-quality splittable pseudorandom number generator
      haskell/haskell-quickcheck: version 2.7.3
      haskell/haskell-safesemaphore: version 0.10.1
      haskell/haskell-uuid: fix WEB_SITE
      devel/cppcheck: version 1.64
      editors/vim: apply patches up to 7.4.282
      windowmanagers/amiwm: make_single
      windowmanagers/herbstluftwm: version 0.6.2
      windowmanagers/openbox: version 3.5.2
      windowmanagers/xmonad: moved to haskell/haskell-xmonad
      wm-addons/xmonad-contrib: moved to haskell/haskell-xmonad-contrib
      shell-term-fm/rxvt-unicode: version 9.20
      devel/cppcheck: version 1.65
      kernels/linux: 3.14.4
      devel/cgdb: version 0.6.7
      doc/source-highlight: version 3.1.7
      doc/man-pages: version 3.66
      crypto/gnutls: fix SOURCE_DIRECTORY
      xorg-app/xfd: add dependencies on libxrender and libxmu
      fonts-x11/ttf-mensch: new spell, a console font based on Menlo
      video-libs/smpeg: fix SOURCE_URL
      python-pypi/numpy: version 1.8.1
      devel/git: version 1.9.3
      collab/subversion: version 1.8.9
      libs/libedit: version 20140213-3.1
      devel/ctags: fix SOURCE_URL
      utils/powertop: version 2.6.1
      make sure our udev.conf gets installed so /dev/shm gets created
      haskell/haskell-hasktags: new spell, ctags for haskell
      haskell/haskell-utf8-string: version 0.3.8
      devel/splint: fix dependency in Makefile.in
      python-pypi/msgpack-python: version 0.4.2
      python-pypi/python-llfuse: new spell, bindings for the fuse low-level API
      python-pypi/attic: new spell, a backup tool
      python-pypi/pyopenssl: version 0.14
      python-pypi/attic: depend on pyopenssl
      libs/glibc: add bug fixes from arch linux
      libs/glibc: add bug fixes from gentoo
      doc/man-pages-posix: version 2013-a
      doc/man-pages: version 3.68
      audio-players/cantata: version 1.3.4
      devel/git: version 2.0.0
      devel/git-cola: version 2.0.3
      shell-term-fm/zsh: add optional dependency on gdbm
      kernels/linux: version 3.14.5
      crypto/gnutls: version 3.1.25 and 3.2.15, fixes CVE-2014-3466
      chat-im/licq: version 1.8.2
      haskell/haskell-ghc-syb-utils: new spell, boilerplate reduction for the GHC API
      fonts-x11/ttf-monofur: new spell, a monospace font
      shell-term-fm/rxvt-unicode: make features configurable
      kernels/linux: version 3.14.6, fixes CVE-2014-3153
      x11/xclip: fix SOURCE_URL[0]
      kernels/linux: version 3.15
      x11/conky: fix SOURCE_URL[0]
      x11/conky: add bug fixes from gentoo
      devel/gdb: version 7.7.1
      doc/man-pages: version 3.69
      kernels/linux: version 3.15.1
      archive/p7zip: fix source url
      video/mpv: version 0.3.11
      utils/schroot: version 1.6.10
      devel/android-tools: new spell, tools for debugging android-based devices
      audio-soft/gmtp: new spell, a GUI for communicating with mtp-capable devices
      devel/android-tools: set device permissions in udev rule file if systemd is not installed
      http/firefox: add --enable-profile-guided-optimization
      archive/lz4: new spell, a very fast lossless compression algorithm
      archive-libs/lzo: version 2.07, fixes CVE-2014-4607
      kernels/linux: version 3.15.2, fixes CVE-2014-4611 and CVE-2014-4608
      video/ffmpeg: version 2.2.4, fixes CVE-2014-4610
      gnome2-libs/glib2: version 2.41.1
      x11-toolkits/gtk+3: version 3.13.3
      kernels/linux: version 3.15.4
      science/qlandkarte-gt: version 1.7.7
      kernels/linux: version 3.15.5
      devel/git-cola: version 2.0.4
      devel/git: version 2.0.1
      mail/cone: version 0.90
      video/mpv: version 0.4.1
      mail/claws-mail: version 3.10.1
      doc/man-pages: version 3.70
      kernels/linux: version 3.15.6
      net/tsocks: fix SOURCE_URL[0]
      net/tor: versions 0.2.4.22 and 0.2.5.5
      net/tor.gpg: add 63FEE659
      net/vidalia: version 0.2.21
      shell-term-fm/busybox: version 1.22.1
      utils/gnuplot: version 4.6.5
      http/firefox: add option for profiled build
      devel/ninja-build-system: version 1.5.1
      xorg-app/xdpyinfo: version 1.3.1
      graphics/argyllcms: version 1.6.3
      kernels/linux: version 3.15.7
      devel/libgc: fix urls
      graphics/inkscape: version 0.48.5
      graphics/lensfun: version 0.2.8
      graphics/graphicsmagick: version 1.3.19
      video-libs/xine-lib: version 1.2.6
      video/xine-ui: version 0.99.8
      devel/git: version 2.1.0
      disk/attr: fix library permissions
      graphics-libs/glew: version 1.11.0
      x11-toolkits/wxgtk-new: version 3.0.1
      net/tor: version 0.2.5.6
      kernels/linux: version 3.16.2
      graphics/gimp: version 2.8.14
      graphics-libs/ftgl: make dependency on texlive optional
      graphics/cinepaint: version 1.0-4
      graphics/gexiv2: version 0.10.1
      image-exiftool: version 9.70
      utils/chrpath: version 0.16
      graphics/dcraw: version 9.22
      http/firefox: version 32.0.1
      graphics-libs/libpano13: version 2.9.19
      graphics-libs/vigra: version 1.10.0
      x11-toolkits/wxgtk-new: fix link error in dependent spells
      libs/libiptcdata: fix SOURCE_URL[0]
      graphics/nitrogen: add support for building the scm version
      shell-term-fm/bash: version 4.3 patchlevel 25
      crypto/nss: version 3.16.5, security update
      http/firefox: version 3.16.5, security update
      shell-term-fm/bash: fix CVE 2014 7169
      shell-term-fm/bash: replace unofficial patch for CVE 2014 7169 with the upstream patch
      shell-term-fm/bash: another patch against the ShellShock issues, security update
      disk/lvm: version 2.02.111
      archive/dpkg: version 1.17.13
      archive/cdebootstrap: version 0.6.3
      archive/debian-archive-keyring: version 2014.1
      kernels/virtualbox-module: version 4.3.16
      utils/virtualbox: version 4.3.16
      crypto/openssl: versions 0.9.8zc and 1.0.1j, fixes CVE-2014-3513, CVE-2014-3567, CVE-2014-3568
      graphics/lensfun: version 0.3.0
      libs/openscenegraph: version 3.2.1
      disk/ddrescue: version 1.19
      video/mpv: version 0.6.2
      kernels/linux: version 3.17.2
      http/firefox: remove -s from LDFLAGS     (cherry picked from commit 77fabf78d0c9c77f9cfb08683e649b3c4082e7af)
      python-pypi/pelican: fix SOURCE_URL     (cherry picked from commit 648112bac94d5fba94826b5508f9a064db48cb2d)

Ismael Luceno (591):
      ffmpeg-svn: Add optional dependency on libvpx
      flashrom: update spell to 0.9.5.2
      xfce4-clipman-plugin: Update spell to version 1.2.3
      qemu: Cut $QEMU_VER at the last dot
      qemu: Add branch 1.1, and rename 1.00 to 1.0
      qemu: Fix branch 1.1 VERSION and SOURCE
      qjackctl: update spell to 0.3.9
      vala: update spell to 0.17.0
      btrfs-progs: Add scm branch
      btrfs-progs: Add dependency on e2fsprogs
      btrfs-progs: Fix compilation
      wikipediafs: new spell, Virtual filesystem for Wikipedia
      git: update spell to 1.7.11
      speedcrunch: new spell, Desktop calculator
      libusbx: Improve description
      quvi: depends on lua51
      firefox: Avoid buggy GCC 4.6 AVX code generation
      seahorse: depends on gcr
      ario: depends on libmpdclient
      dropbear: Remove conflict with openssh
      pidgin: explicitly link against libX11
      schroot: Fix OPTS
      heimdall: new spell, Tool to flash Samsung Galaxy S devices
      oprofileui: Depends on xml-parser
      java-gcj-compat: new spell, Java SDK compatibility for GCJ
      heimdall: update spell to 1.4.1RC2
      libconfig: update spell to 1.4.9
      dmg2img: new spell, Converts DMG to standard (hfs+) disk image
      fill-column-indicator: Fix typo in DETAILS
      emacs-lisp: FUNCTIONS: Enable to specify the source directories
      emacs-goodies-el: new spell, Various functions for Emacs
      Fix ChangeLog entry added by cc5c415 (dmg2img)
      .gitignore: Add .#*
      windowmaker 0.95.4
      tabbed 0.4.1
      solo6x10: new spell, Bluecherry Video4Linux2 driver
      xf86-video-ati: Fix call to autogen.sh
      emacs: Fix update-subdirs script permissions
      seahorse: depends on libsecret
      python-fastimport: new spell, Fastimport parser in Python
      bzr-fastimport: new spell, Bazaar Fast Import Plugin
      ChangeLog: Add entry for kde4-look/gtk-qt-engine
      raccess: Fix long description
      .mailmap: Add new mappings and sort
      ledger 2.6.3
      bzr-fastimport: Add missing spell files
      pil: Add TK sub-dependency
      flake: new spell, FLAC audio encoder
      libconfig: update spell to 1.4.9
      dmg2img: new spell, Converts DMG to standard (hfs+) disk image
      fill-column-indicator: Fix typo in DETAILS
      emacs-lisp: FUNCTIONS: Enable to specify the source directories
      emacs-goodies-el: new spell, Various functions for Emacs
      Fix ChangeLog entry added by cc5c415 (dmg2img)
      .gitignore: Add .#*
      windowmaker 0.95.4
      tabbed 0.4.1
      solo6x10: new spell, Bluecherry Video4Linux2 driver
      xf86-video-ati: Fix call to autogen.sh
      emacs: Fix update-subdirs script permissions
      seahorse: depends on libsecret
      python-fastimport: new spell, Fastimport parser in Python
      bzr-fastimport: new spell, Bazaar Fast Import Plugin
      ChangeLog: Add entry for kde4-look/gtk-qt-engine
      raccess: Fix long description
      .mailmap: Add new mappings and sort
      ledger 2.6.3
      bzr-fastimport: Add missing spell files
      pil: Add TK sub-dependency
      flake: new spell, FLAC audio encoder
      fpc 2.6.2
      dpkg: depends on timedate (for dpkg-parsechangelog)
      solo6x10 2.4.7
      dissy: new spell, Graphical frontend to the objdump disassembler
      iptraf-ng 1.1.3.1
      gdk-pixbuf2: Add optional dependency on jasper
      dissy: Add dependency on gdk-pixbuf2 and librsvg2 (for loading the icon)
      tcl: Fix building of bundled sqlite3
      debian-archive-keyring: Update spell to 2012.4
      debian-archive-keyring: Cleanup
      ubuntu-keyring: new spell, GnuPG keys of the Ubuntu archive
      ubuntu-keyring: Add optional dependency on ubuntu-keyring
      cdebootstrap 0.5.10
      dosfstools: Fix SOURCE
      wine: Update devel to 1.5.30
      pango: Add GI subdepedency
      pango: Add dependency on pango with GI
      vim-gnupg: new spell, transparently edit gpg-encrypted files
      quill: Add support for make-based install
      guile: does not compile with -ffast-math
      hplip 3.13.5
      libusbx 1.0.16-rc1
      ircii 20111115
      epic5 1.1.5
      youtube-dl 2013.07.12
      youtube-dl: Remove irrelevant text from long description
      youtube-dl 2013.07.18
      emacs: Update optional dependencies
      emacs: Fix typo
      john 1.8.0
      john: Reformat long description
      html2ps: new spell, an HTML to PostScript converter
      qpdf 5.0.0
      grub: Allow to select the target platform
      comparator: new spell, find common code segments in large source trees
      pil: Fix indentation on DETAILS
      parcellite 1.1.6
      po4a 0.45
      mcomix 1.00
      youtube-dl 2013.09.24.2
      Revert "mutter 3.8.1"
      wxgtk-new 2.9.5
      smake: new spell, highly portable make program with automake features
      sshpass: new spell, Non-interactive ssh password auth
      st: Add missing dependencies
      libx11: Disable i18n option, breaks XIM + UTF-8
      libx11 1.4.3
      xkeyboard-config 2.3
      xkbcomp 1.2.4
      xkeyboard-config 2.10.1
      cpuminer 2.3.2, pooler's fork
      cgminer: new spell, multi-threaded multi-pool FPGA and ASIC miner for bitcoin
      dmenu: Add patch for Xft fonts support
      xdelta3: new spell, Diff program that works on binaries.
      pspshrink: new spell, ISO Compressor for PSP games
      imagemagick 6.8.7-8
      minidlna 1.1.1
      ssocks: Fix LIBS, -lssl requires -lcrypto
      ssocks 0.0.14
      openssh: Remove conflict with dropbear
      indent 2.2.10
      openglut: spell deprecated [Development ceased in May 2005]
      lyx 2.0.6
      oss (stable) v4.2-build2008
      grace 5.1.23
      sshfs-fuse 2.5
      aria2 1.18.3
      phoronix-test-suite 4.8.6
      maxima 5.32.1
      statifier 1.7.3
      nicstat: new spell, Network traffic statics utility for Solaris and Linux
      sparse 0.5.0
      gnutls 3.2.12.1 + URL fix
      ca-certificates 20140223
      youtube-dl 2014.03.18.1
      vimoutliner: new spell, Outline processor for lightning fast authoring
      qemu: Pass down ARFLAGS=rv, to workaround buildsystem bug
      fpc 2.6.4
      dpkg 1.17.6
      parse-debcontrol: new spell, Easy OO parsing of debian control-like files
      file-desktopentry: depends on file-basedir
      devscripts: new spell, Debian developer scripts
      imagemagick 6.8.9-0
      laptop-mode-tools 1.64
      texmaker 4.1.1
      cdrtools 3.01a23
      imapsync 1.584
      date-manip 6.43
      mail-imapclient 3.35
      file-copy-recursive: new spell, Perl extension for recursively copying files and directories
      isync: new spell, IMAP and MailDir mailbox synchronizer
      fetchmail 6.3.26
      getmail 4.46.0
      imapsync: Depends on file-copy-recursive
      xf86-video-ati: SCM branch depends on glamor
      xf86-video-ati: Use prepare_select_branch
      lxlauncher: depends on menu-cache
      cups-filters: Use make_single
      btrfs-progs: Upstream fixed manpage's Makefile
      btrfs-progs: Fetch releases from git too
      btrfs-progs 3.14.2
      xlsclient 1.1.3
      auctex 11.87
      xdvi 22.86
      auctex: Move to the emacs-lisp section
      shotwell 0.18.0
      btrfs-progs: Fix installation paths
      lzo: Install libraries to the root directory
      lzo 2.08
      FUNCTIONS: Add get_scm_version function
      FUNCTIONS: Fix get_up_spell_name to handle the dot and plus symbols
      Make several spells to use get_scm_version
      dbus-c++: Use prepare_select_branch and get_scm_version
      pppd-chldap: Use prepare_select branch
      Add missing includes to ppd-chldap and dbus-c++
      libfreenect: Use prepare_select_branch
      openni-sensor: Use prepare_select_branch
      openni-sensorkinect: Use prepare_select_branch
      openni: Use prepare_select_branch
      gitosis: Use prepare_select_branch
      dbus-mono: Use prepare_select_branch
      obvious: Use prepare_select_branch
      wicked: Use prepare_select_branch
      gnusim8085: new spell, Graphical simulator, assembler and debugger for the Intel 8085 microprocessor
      xen-tools: Fix heredoc
      bin86 0.16.21
      dev86 0.16.21
      xen 4.4.0
      xen: Run the configure script, it runs subdirs in turn
      traceroute 2.0.20
      autopair: new spell, Automagically pair braces and quotes
      visual-regexp: new spell, A regexp/replace command for Emacs with interactive visual feedback
      whois 5.1.4
      gtk-led-askpass 0.11
      st 0.5
      p11-kit 0.20.3
      gcr 3.12.2
      st: Add patch to hide X cursor when typing
      emacs: Depedency for SVG support is on librsvg2
      brasero 3.11.3
      abiword: Fix typo in DEPENDS
      youtube-dl 2014.07.25.1
      appres 1.0.4
      arandr 0.1.7.1
      zarfy: new spell, A gui to libxrandr
      libssh2: Allow the use of libressl
      wpa_supplicant: Allow the use of libressl
      wpa_supplicant: nl80211 support requires libnl
      mawk: new spell, Interpreter for the AWK Programming Language
      sdcc: new spell, Small Device C Compiler
      meld 1.8.6
      subversion: Fix dependency on serf (without the flag, it may be skipped)
      *awk: provide AWK, make other spells depend on it
      stunnel 5.03
      *awk: Update HISTORY
      *awk: Let the user choose the primary AWK implementation
      python-magic: new spell, File type identification using libmagic
      bmake: new spell, Portable version of NetBSD make
      bmake: Fix system search path
      mk-configure: new spell, Lightweight replacement for autotools
      runawk: new spell, Wrapper for AWK providing modules
      crosstool-ng 1.20.0
      gocr 0.50
      binwalk 2.0.1
      squashfs-tools3: new spell, squashfs-tools 3.x
      mono 2.11.4
      dvtm 0.12
      ChangeLog: Fix last entry date
      abduco: new spell, session {at,de}tach support
      byobu: new spell, text based window manager and terminal multiplexer
      byobu: Optionally depends on newt for byobu-config
      newt: Update website
      newt: Clarify the python's module name
      cobra: new spell, Cobra Programming Language
      vim-csapprox: new spell, Make gvim-only colorschemes work in terminal
      latex-beamer 3.33
      texworks 0.4.5-r1281
      texmaker 4.3
      lyx 2.1.1
      elfkickers: new spell, Kickers of ELF
      corkscrew: new spell, tool for tunneling SSH through HTTP proxies
      isl: new spell, Integer Set Library
      flashrom 0.9.7
      make: Install gmake symlink
      vbindiff: new spell, Visual Binary Diff
      lxc: new spell, Userspace tools for the Linux kernel containers
      Changelog: Remove accidentally added superflous spaces
      dcmtk: new spell, DICOM Toolkit
      vtk 6.1.0
      itk: new spell, toolkit for performing registration and segmentation
      FUNCTIONS: cmake_build: Allow spaces in INSTALL_ROOT and SOURCE_DIRECTORY
      FUNCTIONS: cmake_build: Pass down CFLAGS and CXXFLAGS
      vtk: Replace custom code by cmake_build
      vtk: Add missing dependencies
      icecream 1.0.1
      distcc 3.2rc1
      gnutls: Simplify branch version handling
      gnutls: Update stable branch to 3.2.18
      byobu: Fix SOURCE
      firefox: Clean up dependencies
      yacas 1.3.4
      rkhunter 1.4.2
      ibus 1.5.5
      uim 1.8.6
      kmod 18
      pciutils: Add optional dependency on kmod
      pciutils 3.2.1
      epm 4.2
      iotop: Do not abort build on unmet kernel config dep
      claws-mail: Remove dependency on SSL, not used anymore
      claws-mail: Remove dependency on aspell, not used anymore
      sylpheed.gpg: Add new verified key from Paul Mangan
      claws-mail 3.11.1
      Revert unintentional changes in "pciutils: Add optional dependency on kmod"
      Revert "kmod 18"
      etpan-ng 0.7.1
      libetpan 1.5
      ttf-roboto: Install to /usr/share/fonts/TTF
      python 2.7.8
      python3 3.4.2
      pcc: new spell, Portable C Compiler
      box2d: new spell, 2D physics library for Python
      pyflakes: new spell, passive checker of Python programs
      vtun 3.0.3
      tor 0.2.5.10 / 0.2.6.1-alpha
      pkcs11-helper 1.11
      dconf: Use disable_pic function to fix CFLAGS
      kexec-tools: Use disable_pic function to fix CFLAGS
      gimp: Fix SOURCE_URL[0], seems ftp is not available anymore
      cmockery: new spell, Lightweight Unit Test library for C
      ghc 7.8.3
      signify: new spell, OpenBSD cryptographic signing tool
      nas 1.9.4
      clamav 0.98.5
      nas: Add proper branch selection, and replace dev version with scm
      torsocks: new spell, use socks-friendly applications with tor
      grsync 1.2.5
      file-rename-utils 1.7.3
      renameutils: new spell, File renaming utilities
      Remove file accidentally added by 98fbac9
      mikmod 3.2.6
      libmikmod 3.3.7
      mpd 0.19.4
      emacs: Allow selecting the X toolkit to use
      emacs: Switch to Git SCM
      emacs: depends bzr => git
      polarssl 1.3.9
      polarssl: Add scm branch
      mawk 1.3.4-20141027
      mawk: Nextfile statement implementation fix
      parcellite 1.1.9
      jwasm: new spell, Masm-compatible assembler
      diffuse 0.4.8
      cvsps 3.13
      reposurgeon: new spell, A tool for editing version-control repository history
      cvs-fast-export: new spell, Export an RCS or CVS history as a fast-import stream
      git-imerge: new spell, Incremental merge and rebase for git
      haskell-http 4000.2.18
      haskell-monadcatchio-transformers 0.3.1.2
      haskell-transformers-base 0.4.3
      haskell-monad-control 0.3.3.0
      atom-tools: Fix description, remove changelog and versions
      cmdparse: Fix description, remove changelog and versions
      color-tools: Fix description, remove changelog and versions
      daemonize: Fix description, remove changelog and versions
      daemons: Fix description, remove changelog and versions
      date2: Fix description, remove changelog and versions
      deplate: Fix description, remove changelog and versions
      erubis: Fix description, remove changelog and versions
      facets: Fix description, remove changelog and versions
      fastercsv: Fix description, remove changelog and versions
      fastri: Fix description, remove changelog and versions
      float-formats: Fix description, remove changelog and versions
      hyogen: Fix description, remove changelog and versions
      image_size: Fix description, remove changelog and versions
      mailparser: Fix description, remove changelog and versions
      mb-ruby: Fix description, remove changelog and versions
      needle: Fix description, remove changelog and versions
      net-ssh: Fix description, remove changelog and versions
      nio: Fix description, remove changelog and versions
      quickcert: Fix description, remove changelog and versions
      ruby-dbus: Fix description, remove changelog and versions
      ruby-dict: Fix description, remove changelog and versions
      ruby-graphviz: Fix description, remove changelog and versions
      ruby-inotify: Fix description, remove changelog and versions
      ruby-password: Fix description, remove changelog and versions
      ruby-termios: Fix description, remove changelog and versions
      ruby-xattr: Fix description, remove changelog and versions
      ruby-xslt: Fix description, remove changelog and versions
      rubygame: Fix description, remove changelog and versions
      rubymail: Fix description, remove changelog and versions
      text-format: Fix description, remove changelog and versions
      trans-simple: Fix description, remove changelog and versions
      vpim: Fix description, remove changelog and versions
      sshpass: Fix typo in description (activly -> actively)
      swatch: Fix typo in description (activly -> actively)
      pear-gtk_mdb_designer: Fix typo in description (activily -> actively)
      pear-gtk_mdb_designer: Fix description formatting
      ipc: Fix typo in description (additionaly -> additionally)
      mawk 1.3.4-20141206
      mawk: Remove nextfile-fix.patch, applied by upstream
      radare2: Replace "bit" suffix with "-bit" in description
      evas: Replace "bit" suffix with "-bit" in description
      luminance-hdr: Replace "bit" suffix with "-bit" in description
      rawstudio: Replace "bit" suffix with "-bit" in description
      cwtext: Replace "bit" suffix with "-bit" in description
      darkroom: Replace "bit" suffix with "-bit" in description
      mcelog: Replace "bit" suffix with "-bit" in description
      barry: Replace "bit" suffix with "-bit" in description
      iscsitarget: Replace "bit" suffix with "-bit" in description
      egenix-mx-base: Replace "bit" suffix with "-bit" in description
      xf86-video-impact: Replace "bit" suffix with "-bit" in description
      xf86-video-newport: Replace "bit" suffix with "-bit" in description
      firefox: Add dependency on cairo's tee backend
      lilv-0: Normalize SPELL field
      sratom-0: Normalize SPELL field
      suil-0: Normalize SPELL field
      calf-plugins: Normalize SPELL field
      lilv-util: Normalize SPELL field
      trac-graphvizplugin: Normalize SPELL field
      gtk-systrace: Normalize SPELL field
      jakarta-commons-beanutils: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-collections: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-daemon: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-dbcp: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-digester: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-fileupload: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-lang: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-logging: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-modeler: Normalize SPELL field and remove PKG_* variables
      jakarta-commons-pool: Normalize SPELL field and remove PKG_* variables
      jakarta-log4j: Normalize SPELL field and remove PKG_* variables
      jakarta-regexp: Normalize SPELL field and remove PKG_* variables
      jakarta-struts-bin: Normalize SPELL field and remove PKG_* variables
      jakarta-velocity: Normalize SPELL field and remove PKG_* variables
      crimson-apache: Normalize SPELL field and remove PKG_* variables
      msmtp 1.6.0rc2
      gsasl 1.8.0
      msmtp 1.6.0rc3
      td_lib: new spell, Thomas Dickey's library
      ded: new spell, directory editor
      qemu: Depends on python 2.x
      qemu 2.2.0
      haskell-mode: new spell, Emacs mode for Haskell
      libgit2: Fix SOURCE to make it a proper tarball name
      opencv: Fix SOURCE to make it a proper tarball name
      puppet: Fix SOURCE to make it a proper tarball name
      db: Fix OPTS, $TESTS -> $DB_TESTS
      db 5.3.28
      emacs-lisp/FUNCTIONS: Replace loops
      emacs-lisp/FUNCTIONS: Update site-lisp's loaddefs.el
      emacs-lisp/FUNCTIONS: Install gzipped emacs-lisp files
      emacs-lisp/FUNCTIONS: Fix production of info files
      Update ChangeLog regrading emacs-lisp/FUNCTIONS
      pcc 1.1.0 / 20141228
      ranger: new spell, File manager with an ncurses frontend written in Python
      cbp2make: new spell, Makefile generation tool for Code::Blocks IDE
      oss v4.2-build2010
      cproto: new spell, Generate function prototypes from C source code
      protobuf: Remove -ffast-math from CXXFLAGS, does not compile with it
      protobuf 2.6.0
      vimrc-mode: new spell, Emacs major mode for vimrc files
      ragel 6.9
      goffice 0.10.18
      gnumeric 1.12.18
      swig: Fix SOURCE_URL[0]
      talloc: Fix bundled waf, force it to run with python2
      e2fsprogs: Fix SOURCE_URL[0]
      libgphoto2: Fix SOURCE_URL[0]
      boost: Fix SOURCE_URL[0]
      libebml 1.3.0
      libmatroska 1.4.0
      wget: Make pcre optional
      mawk: Check for the patches directory existence
      wxgtk: Improve pcre dependency description
      wxgtk-new: Improve pcre dependency description
      db48: new spell, Berkeley DB 4.8
      bitcoin 0.9.3
      db48: Install symlinks to /usr/lib
      xca 1.1.0
      isomaster 1.3.13
      lvm 2.02.114
      libwbxml 0.11.2
      virtuoso: SSL and libxml2 are hard dependencies
      tinyxml: Fix VERSION
      nickle: new spell, Nickle prototyping environment
      emacs-lisp/FUNCTIONS: Search for .txi files too
      w3: Move to emacs-lisp section
      w3 4.0.49
      dart-mode: new spell, Dart-mode for emacs
      xdvi 22.87
      xdvik 22.87
      dillo 3.0.4.1
      wbar 2.3.4
      asio 1.10.2
      file-spec 3.47
      lftp 4.6.1
      netpipe 3.7.2
      python-gnupg 0.3.7
      duplicity 0.6.25
      libexplain: new spell, Explain errno values returned by libc functions
      aegis 4.25
      tardy: new spell, tar post-processor
      dar 2.4.15
      emacs 24.4
      wxgtk-new 3.0.2
      torsocks 2.0.0
      i3 4.8
      cgminer 4.9.0
      pangomm 2.34.0
      cogl 1.18.2
      qoauth: Depends on qca2
      qca2: Fix typo
      botan 1.10.9
      cssc 1.4.0
      qca2: Fix sed script to patch properly in any line
      radvd 2.9
      stow 2.2.0
      nasm 2.11.06
      kdelibs4: Fix last HISTORY entry
      box2d: Scacrifice python comments to compile
      {->py}box2d: renamed spell
      lftp: Fixed dependency on xz-utils
      pbzip2 1.1.12
      whohas 0.29
      pwgen 2.07
      libpng 1.2.51
      musl: new spell, musl libc
      aria2 1.18.8
      aria2: Patch sources for GCC 4.9
      mpg123: Fix depends: openal -> OPENAL
      sfml 2.2
      gtk+2 2.24.25
      tabbed 0.6
      ii: new spell, Minimalist filesystem-based IRC client
      lsw: new spell, List windows titles
      lsx: new spell, List executables
      abiword 3.0.1
      slock 1.2
      sic: new spell, simple irc client
      surf 0.6
      libpng: Fix APNG patch checksum
      abiword: Add missing HISTORY entry
      abiword: Patch includes of missing headers
      abiword: Add gnome-vfs2 to include paths and LDFLAGS
      abiword: Removed Emacs and Vi keybindings options, not available anymore
      abiword: Build goffice-bits2 first, build system is broken
      windowmaker 0.95.6
      alien 8.93
      tcsh 6.18.01
      xosview 1.16
      wdiff 1.2.2
      darkice 1.2
      eyed3 0.7.5
      xfce4-power-manager 1.4.2
      libshout-idjc: new spell, libshout plus some extensions for IDJC
      idjc 0.8.14
      ubase: new spell, suckless linux base utils
      sbase: new spell, suckless unix tools
      nwcc: new spell, Nils Weller's C Compiler
      apulse: new spell, PulseAudio emulation for ALSA
      sbase: Fix missing inclusion of $GRIMOIRE/FUNCTIONS
      claws-mail-extra-plugins: Fix the deprecation
      xtermcontrol 3.2
      sgrep 1.94a
      kismet 2013-03-R1b
      dropbear 2014.66
      dvtm 0.13
      bip: new spell, Sexy IRC proxy
      axel: PATCHLEVEL++; Allow larger number of redirects, like wget
      lyx 2.1.2.2
      porg: new spell, Source Code Package Organizer
      paco: Deprecate in favor of porg
      ghc 7.8.4
      texmacs 1.99.2
      cproto 4.7l
      freeimage: Fix CXXFLAGS, must prepend a space
      gforth 0.7.3
      sbc 1.3
      redis 2.8.19
      nginx: Update stable to 1.6.2 and devel to 1.7.9
      dmc: new spell, dynamic mail client
      dmc: Fix missing include for $GRIMOIRE/FUNCTIONS
      haskell-regex-base: Add dependency on haskell-mtl
      dzen: new spell, general purpose messaging, notification and menuing program for X11
      dzen: Fix typos
      Merge dzen into dzen2
      heimdall 1.4.1
      dzen2: Fix SOURCE_URL[0]
      apl: new spell, interpreter for the programming language APL
      ucl: Rework description
      axel: SECURITY_PATCH++; security and build flags fixes
      octave: depends on LAPACK
      scons 2.3.4
      scons: Fix scons script to explicitly use python2
      asciidoc: Fix scripts to use python2 explicitly
      asl 142-bld97
      gtkmm3 3.11.10
      seahorse 3.14.0
      ipv6calc 0.97.4
      nmap: Specify to use python2 explicitly
      btrfs-progs: Depends on xmlto & docbook-xsl for manpages
      ipv6calc: Add missing HISTORY entry
      ired: new spell, minimalistic hexadecimal editor
      acr 0.9.9
      lives 2.2.7
      sdcc: Fix build with GCC 4.9.x, adding -Wno-unused to CFLAGS
      lirc 0.9.2
      lirc: Fix building with python 3 as system default
      bzr-fastimport: Depend on python explicitly
      phonon: Add proper to enable/disable pulseaudio
      nepomuk-core: Depends on soprano's virtuoso backend
      gvfs 1.23.4
      x264: Last snapshot is 20141218
      mypaint Fix SOURCE_URL
      telepathy-glib 0.24.1
      sup: new spell, minimalistic sudo replacement
      gpgme 1.5.3
      gpa 0.9.7
      bind: 9.10.1-P1
      bind-tools 9.10.1-P1

Javier Vasquez (4):
      zenity: => 3.6.0
      gcc: fixed patching for non-Go installations
      dconf: Updating to 0.14.1 (Bug #450)     Removing CFLAGS -fPIC and -DPIC prior to default     build to prevent compilation error:     dbus.c:(.text.startup+0x2a): undefined reference to `dconf_engine_dbus_init_for_testing' /usr/lib/gcc/x86_64-pc-linux-gnu/4.6.3/../../../../x86_64-pc-linux-gnu/bin/ld: gdbus-thread: hidden symbol `dconf_engine_dbus_init_for_testing' isn't     defined
      texlive: Fixes Bug #471

Jeremy Blosser (40):
      chat-libs/libotr, chat-im/pidgin-otr: version 4.0.0
      wm-addons/batterymon-clone: new spell, updated clone of batterymon
      kernels/mtdev: 1.1.4
      libs/libva: new spell, Video Acceleration (VA) API for Linux
      libs/libva-intel-driver: new spell, HW video decode support for Intel integrated graphics
      Revert "wm-addons/batterymon-clone: new spell, updated clone of batterymon"
      python-pypi/batterymon-clone: new spell, updated clone of batterymon
      pidgin: dbus optional dependency actually requires dbus-glib
      purple-plugin-pack: build requires PYTHON in ./configure
      notify-osd: libwnck needs to be >= libwnck3
      xfce4-notifyd: DEPENDS libxfce4ui
      libstrophe: new spell, XMPP library in C
      profanity: new spell, console based XMPP client
      sword: 1.7.0
      bibletime4: version 1.7.0, add scm branch (needed to build against current sword release)
      lualdap: new spell, LDAP library for lua
      prosody: version 0.9.1, optional lualdap support
      Revert "lualdap: new spell, LDAP library for lua"
      lualdap: new spell, LDAP library for lua
      sdl: add upstream patch to build against recent libx11
      tinyxml: allow building with STL support
      xbmc: 12.2
      Revert "sdl: add upstream patch to build against recent libx11"
      sdl: add upstream patch to build against recent libx11 (include HISTORY file in commit this time)
      viridian: new spell, ampache client in python
      viridian: depends on pysqlite, gst-plugins-good, libsoup
      openssh: update LPK patch
      snappy: 1.1.2 and add git version
      snappy: fix malformed DETAILS
      leveldb: new spell, fast key-value storage library by Google
      irrlicht: new spell, high performance realtime 3D engine
      irrlicht: move to games grimoire
      cairo: add a patch for --disable-lto option and a query for it; upstream     appears to have accepted this patch some time ago, but the commit isn't in the     repo. https://bugs.freedesktop.org/show_bug.cgi?id=60852
      xautolock: depends gccmakedep
      editors/jq: new spell, stream editor/filter for JSON data
      python-pypi/botocore: new spell, low-level aws interface library
      python-pypi/bcdoc: new spell, tools to help document botocore-based projects
      python-pypi/jmespath: new spell, module to extract elements from a JSON document
      python-pypi/colorama: new spell, cross-platform colored terminal text
      python-pypi/aws-cli: new spell, unified command line interface to aws

Julien ROZO (23):
      mdnsresponder: updated version to 333.10, no longer fails to build with     multiple make jobs
      dfc: new spell, a df replacement with graphs and colors
      oxygen-gtk2: updated version to 1.2.4
      oxygen-gtk3: updated version to 1.0.4
      live: updated version to 2012.07.14
      oxygen-gtk2: updated version to 1.2.5
      oxygen-gtk3: updated version to 1.0.5
      oxygen-gtk2: updated version to 1.3.0
      oxygen-gtk3: updated version to 1.1.0
      kdesvn4: updated version to 1.6.0, PATCHLEVEL=0
      live: updated version to 2012.08.20
      kdiff4: updated version to 0.9.97
      oxygen-gtk2: updated version to 1.3.2.1
      oxygen-gtk3: updated version to 1.1.2
      oxygen-gtk2: updated version to 1.3.2.1
      oxygen-gtk3: updated version to 1.1.2
      live: updated version to 2013.09.27
      oxygen-gtk2: updated version to 1.4.0
      oxygen-gtk3: updated version to 1.2.0
      oxygen-gtk2: updated version to 1.4.3
      unetbootin: updated version to 585
      filezilla : updated version to 3.7.4.1
      openvpn : updated version to 2.3.2, using new upstream signing key     linux-pam is now a mandatory dependency

Justin Boffemmyer (19):
      utils/teapot: new spell, advanced spreadsheet
      crypto/mosh: update to 1.2.2, fix dependencies
      crypto/mosh: direct depends on gcc with CXX
      audio-soft/alsaequal: new - alsa equalizer plugin
      security/shadow: add missing dependencies
      security/shadow: correct date in HISTORY
      chat-irc/bitlbee: update to 3.0.5
      chat-irc/bitlbee: remove commented dependency
      crypto/mosh: suggest_depends openssh
      chat-irc/bitlbee: add missing space
      crypto/mosh: update to 1.2.3
      lua-forge/luajit: new spell
      net/wpa_supplicant: updated to 1.1
      audio-players/cmus: update to 2.5.0
      audio-players/cmus: update to 2.5.0
      audio-players/cmus: really remove CONFIGURE
      shell-term-fm/tmux: update to 1.9a
      chat-im/prosody: updated to 0.9.4
      lua-forge/luajit: update to 2.0.3

Ladislav Hagara (1478):
      linux 3.3.6
      gtk+3 3.4.3
      gpa 0.9.2
      midori 0.4.6
      glib2 2.32.3
      gthumb2 2.14.4
      gvfs 1.12.3
      glib-networking 2.32.3
      dhex 0.67
      lftp 4.3.6
      tcpflow 1.2.6
      linux 3.4
      linux LATEST_3=3.4
      soprano 2.7.6
      nmap 6.00
      wireshark 1.6.8, SECURITY_PATCH=36
      qt4 4.8.2
      libvpx 1.1.0
      virtualbox 4.1.16
      virtualbox-module 4.1.16
      util-linux 2.21.2
      c-ares 1.8.0
      wdiff 1.1.1
      curl 7.26.0
      curl: set SECURITY_PATCH back to 8
      libidn 1.25
      libdbusmenu-qt 0.9.2
      gedit 3.4.2
      gedit-plugins 3.4.0
      poppler 0.20.0
      girara 0.1.2
      zathura 0.1.2
      zathura-pdf-poppler 0.1.1
      uzbl 2012.05.14 / 228bc38
      shell-term-fm/spacefm: new spell, multi-panel tabbed file manager
      clutter 1.10.6
      iptables 1.4.14
      lftp 4.3.7
      libwpd 0.9.4
      libwps 0.2.7
      mono-addins 0.6.2
      banshee 2.4.1
      banshee-community-extensions 2.4.0
      mlt 0.7.8
      kdenlive4 0.9.2
      automake 1.12.1
      tea 33.1.0
      media-player-info 17
      figlet 2.2.5
      libevent 2.0.19
      libnl 3.2.9
      libnl: libnl-3.pc removed
      iw 3.4
      http/xombrero: new spell, minimalists web browser
      libbsd 0.4.1
      vifm 0.7.3
      linux 3.4.1
      gdata 2.0.17
      digikam4 2.6.0
      miro 5.0.1
      pango 1.30.1
      nspr 4.9.1
      nss 3.13.5
      firefox 13.0, SECURITY_PATCH=49
      gnutls 3.0.20
      cryptsetup-luks 1.4.3
      libnl 3.2.10
      psmisc 22.17
      python-pypi/arandr: new spell, Another XRandR GUI
      guvcview 1.6.0
      pgadmin3 1.14.3
      libxfce4util: UP_TRIGGERS fixed
      linux 3.4.2
      lvm 2.02.96
      mplayer 1.1
      mpg123: HISTORY fixed
      eaglemode 0.84.0
      libpcap 1.3.0, patch is still needed
      tcpdump 4.3.0
      e2fsprogs 1.42.4
      vamp-plugin-sdk 2.2.1
      rubberband 1.7.0
      audio-players/stretchplayer: new spell, audio player with time stretch     and pitch shift
      freetype2 2.4.10
      php 5.3.14, SECURITY_PATCH=18
      poppler 0.20.1
      girara 0.1.3
      zathura 0.2.0
      zathura-pdf-poppler 0.2.0
      nmap 6.01
      firefox 13.0.1, SECURITY_PATCH=50
      linux 3.4.3
      stellarium 0.11.3
      wine 1.4.1
      spacefm 0.7.8
      gavl 1.4.0
      gmerlin 1.2.0
      gmerlin-avdecoder 1.2.0
      gmerlin-encoders 1.2.0
      krb5-appl: system-et patch removed, not needed
      gzip 1.5
      net/dnstop: new spell, various tables of DNS traffic
      vym 2.2.0
      virtualbox 4.1.18
      virtualbox-module 4.1.18
      xz-utils 5.0.4
      linux 3.4.4
      c-ares 1.9.1
      wireshark 1.8.0
      bino 1.4.0
      tiff 4.0.2, SECURITY_PATCH=4, CVE-2012-1173, CVE-2012-2113
      system-config-printer 1.3.9
      pycups 1.9.61
      hplip 3.12.6
      psmisc 22.19
      traceroute 2.0.18
      live 2012.06.23
      rb-libtorrent 0.16.1
      devel/bff: new spell, brainfuck interpreter
      bluefish 2.2.3
      samba 3.6.6
      cifs-utils 5.5
      claws-mail 3.8.1
      claws-mail-extra-plugins 3.8.1
      minitube 1.8
      vlc 2.0.2, SECURITY_PATCH=24
      shadow 4.1.5.1
      linux-firmware 20120615
      glibc 2.16.0
      whois 5.0.17
      clutter 1.10.8
      clutter-gst 1.6.0
      libjpeg-turbo 1.2.1
      sip 4.13.3
      pyqt4 4.9.4
      iw 3.5
      libbsd 0.4.2
      xombrero 1.1.0
      pidgin 2.10.5, SECURITY_PATCH=15
      qmmp 0.6.0
      graphics/mutiara: new spell, motif designer
      usbutils 006
      pidgin 2.10.6
      nilfs-utils 2.1.4
      xournal 0.4.7
      upower 0.9.17
      digikam4 2.7.0
      dbus 1.6.2
      dbus-glib 0.100
      dbus-python 1.1.1
      colordiff 1.0.10
      gnutls 2.12.20 & 3.0.21
      ethtool 3.4.1
      automake 1.12.2, SECURITY_PATCH=1, CVE-2012-3386
      xombrero 1.1.1
      gpgme 1.3.2
      poppler 0.20.2
      opencv 2.4.2
      evas configure options sdl updated
      e-17/ephysics: new spell, EFL wrapper for physics engine
      e-17/terminology: new spell, EFL terminal emulator
      gparted 0.13.0
      phonon-backend-gstreamer 4.6.1
      gtk+3 3.4.4
      eog2 3.4.3
      gtk+2 2.24.11
      ecryptfs-utils 99
      qtfm 5.5
      spacefm 0.7.9
      linux 3.4.5
      xombrero 1.2.0
      seamonkey 2.11, SECURITY_PATCH=44
      iso-codes 3.37
      git 1.7.11.2
      cogl 1.10.4
      mc 4.8.1.4
      xlockmore 5.40
      vlc 2.0.3
      linux 3.4.6
      p11-kit 0.13
      x11/xteddy: new spell, cuddly teddy bear for your X
      libpng 1.2.50, SECURITY_PATCH=9, CVE-2012-3386
      scite 3.2.1
      doxygen 1.8.1.2
      rekonq 1.0
      bison 2.6
      linux 3.5
      wireshark 1.8.1, SECURITY_PATCH=37
      dbus 1.6.4
      utils/ponysay: new spell, cowsay wrapper with ponies
      whois 5.0.18
      video/kamerka: new spell, webcam app
      xombrero 1.2.2
      curl 7.27.0
      vimpager 1.7.1
      tea 33.2.0
      liberation-fonts-ttf 2.00.0
      iptables 1.4.15
      cryptsetup-luks 1.5.0
      qmmp 0.6.2
      bison 2.6.2
      flex 2.5.37
      webkitgtk 1.8.2, SECURITY_PATCH=6
      webkitgtk3 1.8.2, SECURITY_PATCH=2
      e2fsprogs 1.42.5
      miro 5.0.2
      python-pypi/keepnote: new spell, note taking application
      vym 2.2.4
      nspr 4.9.2
      gmic 1.5.1.7
      graphicsmagick 1.3.16
      cimg 1.5.0
      pycups 1.9.62
      system-config-printer 1.3.11
      gpa 0.9.3
      npth 0.91
      linux 3.5.1
      wget 1.14
      gparted 0.13.1
      libs/libverto: new spell, event loop abstraction interface
      krb5 1.10.3, SECURITY_PATCH=10, CVE-2012-1014, CVE-2012-1015
      krb5: optional_depends libverto added
      libspectre 0.2.7
      e-17/evas_generic_loaders: new spell, additional generic loaders for     evas
      libs/glm: new spell, openGL Mathematics library
      gource 0.38
      coreutils 8.18
      gdk-pixbuf2 2.26.2
      libgee 0.6.5
      ethtool 3.5
      libfm 1.0
      pcmanfm 1.0
      phonon-backend-gstreamer 4.6.2
      phonon-backend-vlc 0.6.0
      geeqie 1.1
      samba 3.6.7
      cifs-utils 5.6
      kdelibs4 4.9.0
      kdebase4 4.9.0
      kdebase4-runtime 4.9.0
      shared-desktop-ontologies 0.10.0
      soprano 2.8.0
      akonadi 1.8.0
      nepomuk-core: new spell
      kdepimlibs4 4.9.0
      linux 3.5.2
      wireshark 1.8.2, SECURITY_PATCH=38
      digikam4 2.8.0
      kamera 4.9.0
      konsole 4.9.0
      kdenetwork4 4.9.0
      marble 4.9.0
      kwallet 4.9.0
      okular 4.9.0
      gwenview4 4.9.0
      kde-wallpapers 4.9.0
      kdewebdev4 4.9.0
      kgpg 4.9.0
      kdesdk4 4.9.0
      libkdeedu 4.9.0
      pykde4 4.9.0
      oxygen-icons 4.9.0
      svgpart 4.9.0
      libkipi4 4.9.0
      sweeper 4.9.0
      php 5.3.16, SECURITY_PATCH=19
      utils/gti: new spell, silly git launcher
      kcolorchooser 4.9.0
      ksaneplugin 4.9.0
      kgamma 4.9.0
      libksane 4.9.0
      ksnaphost 4.9.0
      superkaramba 4.9.0
      kdeplasmoids4 4.9.0
      kdebase4-runtime needs nepomuk-core
      nepomuk-core info updated
      kdegames4 sha512 fixed
      nss 3.13.6
      sudo 1.8.5p3
      automake 1.12.3
      iso-codes 3.38
      spacefm 0.7.11
      doxygen 1.8.2
      ponysay 2.0
      guvcview 1.6.1
      gdb 7.5
      coreutils 8.19
      nepomuk-core: new spell mentioned in ChangeLog
      ponysay 2.2
      powertop 2.1
      libvisio 0.0.19
      gimp 2.8.2
      ponysay 2.4
      qmmp 0.6.3
      xosview 1.9.4
      linux 3.5.3
      firefox 15.0, SECURITY_PATCH=52
      xombrero 1.3.0
      openssh 6.1p1
      seamonkey 2.12, SECURITY_PATCH=45
      gdk-pixbuf2 2.26.3
      gtk+2 2.24.12
      Revert "usb-modeswitch - change depends libusb -> LIBUSB"
      usb-modeswitch 1.2.4
      usb-modeswitch-data 20120815
      iw 3.6
      video/eviacam: new spell, webcam based mouse emulator
      xscreensaver 5.19
      p11-kit 0.14
      libs/gfreenect: new spell, wrapper for libfreenect
      libs/skeltrack: new spell, skeleton tracking library
      mc 4.8.1.5
      ponysay 2.6
      mc 4.8.1.6
      linux 3.5.4
      spacefm 0.8.0
      firefox 15.0.1, SECURITY_PATCH=53
      xombrero 1.3.1
      lsof 4.86
      feh 2.6.1
      librsvg2 2.36.3
      webkitgtk 1.8.3, SECURITY_PATCH=7
      webkitgtk3 1.8.3, SECURITY_PATCH=3
      samba 3.6.8
      pgadmin3 1.16.0
      dhex 0.68
      php 5.3.17
      xfce4-settings needs garcon
      parole 0.3.0.3
      ffmpeg 0.11.2
      midori 0.4.7
      virtualbox 4.2.0
      virtualbox-module 4.2.0
      libfm 1.0.1
      pcmanfm 1.0.1
      smplayer 0.8.1
      gdk-pixbuf2 2.26.4
      stellarium 0.11.4
      automake 1.12.4
      gnome-common2 3.4.0.1
      network-manager 0.9.6.0
      gnome-menus 3.4.2
      metacity 2.34.8
      network-manager-applet 0.9.6.2
      gnome-panel 3.4.2.1
      whois 5.0.19
      e2fsprogs 1.42.6
      gtksourceview3 3.4.2
      pyatspi2 2.4.0
      pyxdg 0.23
      pygobject3 3.2.2
      gtk+2 2.24.13
      dbus 1.6.8, SECURITY_PATCH=8
      patch 2.7.1
      feh 2.6.3
      ffmpeg 1.0
      lftp 4.4.0
      clutter 1.12.0
      vala 0.18.0
      gobject-introspection 1.34.0
      pygobject3 3.4.0
      gjs 1.34.0
      gnome-js-common 0.1.2
      gstreamer-1.0: new spell, version 1.0.0
      linux 3.6
      openshot 1.4.3
      wireshark 1.8.3, SECURITY_PATCH=39
      gst-plugins-base-1.0: new spell, based on gst-plugins-base
      gst-plugins-good-1.0: new spell, based on gst-plugins-good
      gst-plugins-bad-1.0: new spell, based on gst-plugins-bad
      gst-plugins-ugly-1.0: new spell, based on gst-plugins-ugly
      gst-libav-1.0: new spell, based on gst-ffmpeg
      gstreamer 1.0 spells mentioned in ChangeLog
      clutter-gst 1.9.92
      clutter-gtk 1.3.2
      mutter 3.6.0
      dconf 0.14.0
      libgweather 3.6.0
      libsoup 2.40.0
      evolution-data-server 3.6.0
      gnome-panel 3.6.0
      gnome-menus 3.6.0
      gsettings-desktop-schemas 3.6.0
      gnome-desktop3 3.6.0.1
      gnome-shell 3.6.0
      libwnck3 3.4.3
      libwacom 0.6
      gnome-settings-daemon 3.6.0
      gnome-terminal 3.6.0
      gcr 3.6.0
      gnome-session 3.6.0
      e16 1.0.11
      epplet-base 0.14
      linux 3.6.1
      harfbuzz 0.9.4
      pango 1.32.1
      evince 3.6.0
      glib-networking 2.34.0
      accountsservice 0.6.25
      gdm2 3.6.0
      firefox 16.0, SECURITY_PATCH=54
      seamonkey 2.13, SECURITY_PATCH=47
      cairo 1.12.4
      firefox 16.0.1, SECURITY_PATCH=55
      Revert "Revert "grep 2.11""
      Revert "Revert "grep: => 2.12""
      grep 2.14
      poppler 0.20.5
      linux 3.6.2
      razor-qt 0.5.0
      e-17/eobj: new spell, EFL's generic object system library
      nodejs 0.8.12
      bino 1.4.1
      tig 1.1
      man-pages 3.43
      flann 1.7.1
      graphics/meshlab: new spell, advanced mesh processing system
      vtk 5.10.0
      vtk-data 5.10.0
      pcl 1.6.0
      glib2 2.34.1
      gtk+3 3.6.1
      gnome2-libs/pangox-compat: new spell, pangox compatibility library
      vlc 2.0.4
      ncurses: PATCHLEVEL=1, --enable-pc-files added
      qhull 2012.1
      poppler-data 0.4.6
      linux 3.6.3
      librsvg2 2.36.4
      bash: SECURITY_PATCH=1, CVE-2012-3410
      gnome-online-accounts 3.6.1
      security-libs/libpwquality: new spell, password quality checking library
      gnome-control-center 3.6.2
      seahorse 3.6.2
      cairo 1.12.6
      clutter 1.12.2
      clutter-gtk 1.4.0
      gnome-session 3.6.1
      gnome-settings-daemon 3.6.1
      mutter 3.6.1
      gnome-shell 3.6.1
      usbview 2.0
      science-libs/mrpt: new spell, Mobile Robot Programming Toolkit
      razor-qt 0.5.1
      gnome-desktop3 3.6.1
      telepathy-glib 0.20.0
      xapian-core 1.2.12
      gnome3-libs/zeitgeist: new spell, log activities and present to other     apps
      gnome3-libs/libzeitgeist: new spell, zeitgeist client library
      folks 0.8.0
      json-glib 0.15.2
      upower 0.9.18
      gobject-introspection 1.34.1.1
      pygobject3 3.4.1.1
      libpeas 1.6.1
      gnome-keyring 3.6.1
      gnome-themes-standard 3.6.1
      cheese 3.6.1
      gstreamer-1.0 1.0.2
      gst-plugins-base-1.0 1.0.2
      gst-plugins-good-1.0 1.0.2
      gst-plugins-ugly-1.0 1.0.2
      gst-plugins-bad-1.0 1.0.2
      gst-libav-1.0 1.0.2
      evolution-data-server 3.6.1
      gtkhtml2 4.6.0
      evolution 3.6.1
      skeltrack 0.1.10
      gnome-power-manager 3.6.0
      libsoup 2.40.1
      gnome-backgrounds 3.6.1
      metacity 2.34.13
      exempi 2.2.0
      tracker 0.14.3
      nautilus2 3.6.1
      gnome-icon-theme 3.6.0
      gnome-icon-theme-symbolic 3.6.0
      Revert "gnome2-libs/exempi: version 2.2.0"
      Revert "graphics/gthumb: new spell, an image viewer based on gqview"
      Revert "gobject-introspection: Updated to 1.34.0 (works with glib2 2.34.1)"
      Revert "gtkhtml2 4.6.0"
      libzeitgeist: HISTORY fixed
      seamonkey 2.13.2, SECURITY_PATCH=49
      terminology needs elementary
      installwatch fixed to work with glibc 2.15 and 2.16
      matplotlib 1.1.1
      clutter-gst needs gst-plugins-base-1.0
      gfreenect needs gobject-introspection and gtk-doc
      linux-firmware converted to git version
      connman 1.9
      efreet needs edbus now
      e-17/edbus: new spell, access to D-Bus from EFL applications
      xvkbd 3.3
      linux 3.6.6
      htop 1.0.2
      bison 2.6.5
      man-pages 3.44
      libvirt 1.0.0
      virtualbox 4.2.4
      virtualbox-module 4.2.4
      fltk 1.3.1
      deadbeef 0.5.6
      glib2 2.34.2
      gtk+3 3.6.2
      gdk-pixbuf2 2.26.5
      ltrace 0.7.0
      filezilla 3.6.0
      colordiff 1.0.12
      e-17/efl: new spell, collection of libraries
      e17 now needs efl
      eviacam 1.6.0
      linux 3.6.7
      ldns 1.6.16
      filezilla 3.6.0.1
      firefox 17.0, SECURITY_PATCH=57
      medit 1.1.1
      nspr 4.9.4
      linux 3.6.8
      nmap 6.25
      wireshark 1.8.4, SECURITY_PATCH=40
      libssh2 1.4.3
      ltrace 0.7.1
      xombrero 1.4.0
      firefox 17.0.1
      ed 1.7
      efl contains ecore now
      linux 3.6.9
      ffmpeg 1.0.1
      util-linux 2.22.1
      libxp: sig file updated, upstream sources changes
      glib2 2.34.3
      gtk+2 2.24.14
      harfbuzz 0.9.9
      pango 1.32.4
      xosview 1.12
      automake 1.12.5
      ltrace 0.7.2
      sip 4.14.2
      pyqt4 4.9.6
      smplayer 0.8.2
      samba 3.6.10
      pgadmin3 1.16.1
      linux 3.6.10
      webkitgtk 1.10.2, SECURITY_PATCH=8
      webkitgtk3 1.10.2, SECURITY_PATCH=4
      fraqtive 0.4.6
      vlc 2.0.5
      efl contains eio now
      utils/binwalk: new spell, firmware analysis tool
      inkscape 0.48.4, SECURITY_PATCH=2
      gnupg 1.4.13
      cracklib 2.8.22
      automake 1.12.6
      pulseaudio 3.0
      mc 4.8.1.7
      rxvt-unicode 9.16
      smplayer 0.8.3
      fonts-x11/open-dyslexic: new spell, font for readers with dyslexia
      efl contains efreet and edbus now
      kdelibs4 4.9.5
      kdebase4 4.9.5
      nepomuk-core 4.9.5
      kactivities 4.9.5
      attica 0.4.1
      kdebase4-runtime 4.9.5
      konsole 4.9.5
      kdebase-workspace4 4.9.5
      kdenetwork4 4.9.5
      libkipi4 4.9.5
      oxygen-icons 4.9.5
      akonadi 1.8.1
      kdepimlibs4 4.9.5
      kdepim4-runtime 4.9.5
      kdepim4-runtime: sha512 fixed, it was from kdepim4, sorry
      kdepim4 4.9.5
      kdewebdev4 4.9.5
      okular 4.9.5
      gwenview4 4.9.5
      kamera 4.9.5
      pykde4 4.9.5
      kate 4.9.5
      kdeartwork4 4.9.5
      kdegames4 4.9.5
      kdetoys4 4.9.5
      kwallet 4.9.5
      analitza 4.9.5
      ark 4.9.5
      libkcddb 4.9.5
      libkcompactdisc 4.9.5
      audiocd-kio 4.9.5
      kmix 4.9.5
      marble 4.9.5
      pairs 4.9.5
      parley 4.9.5
      kalgebra 4.9.5
      kstars 4.9.5
      blinken 4.9.5
      cantor 4.9.5
      kalzium 4.9.5
      avogadro 1.1.0
      filelight 4.9.5
      jovie 4.9.5
      kaccessible 4.9.5
      kcalc 4.9.5
      kcharselect 4.9.5
      kde4-l10n 4.9.5
      kdeadmin4 4.9.5
      kdeplasmoids4 4.9.5
      kdf 4.9.5
      kfloppy 4.9.5
      kgpg 4.9.5
      kmag 4.9.5
      kmousetool 4.9.5
      kmouth 4.9.5
      kremotecontrol 4.9.5
      ktimer 4.9.5
      printer-applet 4.9.5
      superkaramba 4.9.5
      sweeper 4.9.5
      kdesdk4 4.9.5
      qyoto 4.9.5
      perlkde 4.9.5
      perlqt4 4.9.5
      smokegen 4.9.5
      smokeqt 4.9.5
      smokekde 4.9.5
      check 0.9.9
      efl contains edje, emotion and ethumb
      qtruby 4.9.5
      kross-interpreters 4.9.5
      libkdeedu 4.9.5
      kgeography 4.9.5
      kanagram 4.9.5
      kbruch 4.9.5
      khangman 4.9.5
      kig 4.9.5
      kiten 4.9.5
      klettres 4.9.5
      kmplot 4.9.5
      ktouch 4.9.5
      kturtle 4.9.5
      kwordquiz 4.9.5
      rocs 4.9.5
      step 4.9.5
      kcolorchooser 4.9.5
      libksane 4.9.5
      libkexiv24 4.9.5
      svgpart 4.9.5
      libkdcraw4 4.9.5
      ksnapshot 4.9.5
      kdegraphics-strigi-analyzer 4.9.5
      kdegraphics-thumbnailers 4.9.5
      kgamma 4.9.5
      kolourpaint 4.9.5
      kruler 4.9.5
      ksaneplugin 4.9.5
      mobipocket 4.9.5
      dragon 4.9.5
      ffmpegthumbs 4.9.5
      juk 4.9.5
      kscd 4.9.5
      mplayerthumbs 4.9.5
      rekonq 2.0
      scribus4 1.4.2
      video/v4l2ucp: new spell, universal control panel for V4L2 devices
      video/v4l2ucp added into ChangeLog
      linux 3.7.4
      ffmpeg 1.0.3
      calligra 2.5.5
      glibc 2.17
      glibc.gpg permission fixed
      zathura 0.2.2
      zathura-pdf-poppler 0.2.1
      girara 0.1.5
      clutter-gst 2.0.0
      clutter-gtk 1.4.2
      rekonq 2.1
      linux 3.7.5
      linux: BUILD: -I/usr/src/linux/include removed from ifenslave
      efl conflicts also with eeze and ephysics
      bino 1.4.2
      wireshark 1.8.5, SECURITY_PATCH=41
      ucview 0.33
      libucil 0.9.10
      phonon-backend-gstreamer 4.6.3
      linux 3.7.6
      iotop 0.5
      nspr 4.9.5
      nss 3.14.2
      graphics/evolvotron: new spell, interactive generative art software
      calligra 2.6.0
      openssl 0.9.8y, 1.0.0k, SECURITY_PATCH=20
      midori 0.4.8
      gnutls 3.1.7, 3.0.28 and 2.12.23, SECURITY_PATCH=8
      kdelibs4 4.10.0
      kdebase4 4.10.0
      soprano 2.9.0
      nepomuk-core 4.10.0
      kactivities 4.10.0
      kdebase4-runtime 4.10.0
      konsole 4.10.0
      akonadi 1.9.0
      kdepimlibs4 4.10.0
      kdeartwork4 4.10.0
      kde4/nepomuk-widgets: new spell, library with the nepomuk widgets
      kdepim4-runtime 4.10.0
      kwallet 4.10.0
      libkexiv24 4.10.0
      libkipi4 4.10.0
      kdeplasmoids4 4.10.0
      libkdcraw4 4.10.0
      okular 4.10.0
      superkaramba 4.10.0
      kgpg 4.10.0
      kate 4.10.0
      kdesdk4 4.10.0
      kdewebdev4 4.10.0
      oxygen-icons 4.10.0
      libkdeedu 4.10.0
      marble 4.10.0
      gimp 2.8.4
      shell-term-fm/st: new spell, simple terminal
      ark 4.10.0
      grantlee 0.3.0
      ffmpeg 1.0.4, SECURITY_PATCH=14
      gtk+2 2.24.15
      xfe 1.34
      freerdp 1.0.2
      linux 3.7.7
      kdenetwork4 4.10.0
      kdeadmin4 4.10.0
      kdetoys4 4.10.0
      filelight 4.10.0
      jovie 4.10.0
      kaccessible 4.10.0
      kcalc 4.10.0
      kcharselect 4.10.0
      kmousetool 4.10.0
      sweeper 4.10.0
      pidgin 2.10.7, SECURITY_PATCH=16
      linux 3.7.8
      linux 3.7.9
      feh 2.9.1
      phonon-backend-vlc 0.6.2
      v4l-utils 0.9.3
      e2fsprogs 1.42.7
      util-linux 2.22.2
      linux 3.8
      firefox 19.0, SECURITY_PATCH=61
      potrace 1.11
      seamonkey 2.16, SECURITY_PATCH=52
      linux 3.8.1
      rekonq 2.2
      efl: subversion -> git
      e17: subversion -> git
      elementary: subversion -> git
      terminology: subversion -> git
      kdebase-workspace4 4.10.0
      libqrencode 3.4.2
      guvcview 1.7.0
      strigi 0.7.8
      kdebase-workspace4 4.10.1
      kdelibs4 4.10.1
      kdebase4 4.10.1
      nepomuk-core 4.10.1
      kactivities 4.10.1
      kdebase4-runtime 4.10.1
      konsole 4.10.1
      kdepimlibs4 4.10.1
      kdeartwork4 4.10.1
      nepomuk-widgets 4.10.1
      kdepim4-runtime 4.10.1
      kwallet 4.10.1
      libkexiv24 4.10.1
      libkipi4 4.10.1
      kdeplasmoids4 4.10.1
      libkdcraw4 4.10.1
      okular 4.10.1
      superkaramba 4.10.1
      kgpg 4.10.1
      kate 4.10.1
      kdesdk4 4.10.1
      kdewebdev4 4.10.1
      oxygen-icons 4.10.1
      libkdeedu 4.10.1
      lsof 4.87
      marble 4.10.1
      ark 4.10.1
      kdenetwork4 4.10.1
      kdeadmin4 4.10.1
      kdetoys4 4.10.1
      filelight 4.10.1
      jovie 4.10.1
      kaccessible 4.10.1
      kcalc 4.10.1
      kcharselect 4.10.1
      kmousetool 4.10.1
      sweeper 4.10.1
      wireshark 1.8.6, SECURITY_PATCH=42
      libs/libfaketime: new spell, reports faked system time to programs
      midori 0.4.9
      rekonq 2.2.1
      kdepim4 4.10.1
      kdf 4.10.1
      kfloppy 4.10.1
      kmag 4.10.1
      kmouth 4.10.1
      ktimer 4.10.1
      kremotecontrol 4.10.1
      gwenview4 4.10.1
      kamera 4.10.1
      kcolorchooser 4.10.1
      kdegraphics-strigi-analyzer 4.10.1
      kdegraphics-thumbnailers 4.10.1
      kgamma 4.10.1
      kolourpaint 4.10.1
      kruler 4.10.1
      ksaneplugin 4.10.1
      ksnapshot 4.10.1
      libksane 4.10.1
      mobipocket 4.10.1
      svgpart 4.10.1
      audiocd-kio 4.10.1
      dragon 4.10.1
      ffmpegthumbs 4.10.1
      juk 4.10.1
      kmix 4.10.1
      kscd 4.10.1
      libkcddb 4.10.1
      libkcompactdisc 4.10.1
      mplayerthumbs 4.10.1
      akonadi 1.9.1
      ffmpeg 1.0.5
      calligra 2.6.2
      linux 3.8.3
      digikam4 3.1.0
      libgcrypt 1.5.1
      gexiv2 0.6.0
      shotwell 0.14.0
      samba 3.6.13
      linux 3.8.4
      git 1.8.2
      openssh 6.2p1
      file 5.14
      poppler 0.22.2
      gparted 0.15.0
      e17: updated to better work with git version
      evas_generic_loaders: scm version - subversion -> git
      live 2013.04.01
      mmidori 0.5.0
      lua 5.2.2
      miro 6.0
      shotwell 0.14.1
      evince depends on libsecret
      gnutls 3.1.10 and 3.0.29
      libvirt 1.0.4
      glibc 2.17
      glibc.gpg permission fixed
      kdelibs4 4.10.0
      kdebase4 4.10.0
      soprano 2.9.0
      nepomuk-core 4.10.0
      kactivities 4.10.0
      kdebase4-runtime 4.10.0
      konsole 4.10.0
      akonadi 1.9.0
      kdepimlibs4 4.10.0
      kdeartwork4 4.10.0
      kde4/nepomuk-widgets: new spell, library with the nepomuk widgets
      kdepim4-runtime 4.10.0
      kwallet 4.10.0
      libkexiv24 4.10.0
      libkipi4 4.10.0
      kdeplasmoids4 4.10.0
      libkdcraw4 4.10.0
      okular 4.10.0
      superkaramba 4.10.0
      kgpg 4.10.0
      kate 4.10.0
      kdesdk4 4.10.0
      kdewebdev4 4.10.0
      oxygen-icons 4.10.0
      libkdeedu 4.10.0
      marble 4.10.0
      ark 4.10.0
      grantlee 0.3.0
      kdenetwork4 4.10.0
      kdeadmin4 4.10.0
      kdetoys4 4.10.0
      filelight 4.10.0
      jovie 4.10.0
      kaccessible 4.10.0
      kcalc 4.10.0
      kcharselect 4.10.0
      kmousetool 4.10.0
      sweeper 4.10.0
      pidgin 2.10.7, SECURITY_PATCH=16
      linux 3.7.8
      linux 3.7.9
      feh 2.9.1
      phonon-backend-vlc 0.6.2
      v4l-utils 0.9.3
      e2fsprogs 1.42.7
      util-linux 2.22.2
      linux 3.8
      firefox 19.0, SECURITY_PATCH=61
      potrace 1.11
      seamonkey 2.16, SECURITY_PATCH=52
      linux 3.8.1
      rekonq 2.2
      efl: subversion -> git
      e17: subversion -> git
      elementary: subversion -> git
      terminology: subversion -> git
      kdebase-workspace4 4.10.0
      libqrencode 3.4.2
      guvcview 1.7.0
      strigi 0.7.8
      kdebase-workspace4 4.10.1
      kdelibs4 4.10.1
      kdebase4 4.10.1
      nepomuk-core 4.10.1
      kactivities 4.10.1
      kdebase4-runtime 4.10.1
      konsole 4.10.1
      kdepimlibs4 4.10.1
      kdeartwork4 4.10.1
      nepomuk-widgets 4.10.1
      kdepim4-runtime 4.10.1
      kwallet 4.10.1
      libkexiv24 4.10.1
      libkipi4 4.10.1
      kdeplasmoids4 4.10.1
      libkdcraw4 4.10.1
      okular 4.10.1
      superkaramba 4.10.1
      kgpg 4.10.1
      kate 4.10.1
      kdesdk4 4.10.1
      kdewebdev4 4.10.1
      oxygen-icons 4.10.1
      libkdeedu 4.10.1
      lsof 4.87
      marble 4.10.1
      ark 4.10.1
      kdenetwork4 4.10.1
      kdeadmin4 4.10.1
      kdetoys4 4.10.1
      filelight 4.10.1
      jovie 4.10.1
      kaccessible 4.10.1
      kcalc 4.10.1
      kcharselect 4.10.1
      kmousetool 4.10.1
      sweeper 4.10.1
      wireshark 1.8.6, SECURITY_PATCH=42
      libs/libfaketime: new spell, reports faked system time to programs
      midori 0.4.9
      rekonq 2.2.1
      kdepim4 4.10.1
      kdf 4.10.1
      kfloppy 4.10.1
      kmag 4.10.1
      kmouth 4.10.1
      ktimer 4.10.1
      kremotecontrol 4.10.1
      gwenview4 4.10.1
      kamera 4.10.1
      kcolorchooser 4.10.1
      kdegraphics-strigi-analyzer 4.10.1
      kdegraphics-thumbnailers 4.10.1
      kgamma 4.10.1
      kolourpaint 4.10.1
      kruler 4.10.1
      ksaneplugin 4.10.1
      ksnapshot 4.10.1
      libksane 4.10.1
      mobipocket 4.10.1
      svgpart 4.10.1
      audiocd-kio 4.10.1
      dragon 4.10.1
      ffmpegthumbs 4.10.1
      juk 4.10.1
      kmix 4.10.1
      kscd 4.10.1
      libkcddb 4.10.1
      libkcompactdisc 4.10.1
      mplayerthumbs 4.10.1
      akonadi 1.9.1
      ffmpeg 1.0.5
      calligra 2.6.2
      linux 3.8.3
      digikam4 3.1.0
      libgcrypt 1.5.1
      gexiv2 0.6.0
      shotwell 0.14.0
      samba 3.6.13
      linux 3.8.4
      git 1.8.2
      openssh 6.2p1
      file 5.14
      poppler 0.22.2
      gparted 0.15.0
      e17: updated to better work with git version
      evas_generic_loaders: scm version - subversion -> git
      live 2013.04.01
      mmidori 0.5.0
      lua 5.2.2
      miro 6.0
      shotwell 0.14.1
      evince depends on libsecret
      gnutls 3.1.10 and 3.0.29
      libvirt 1.0.4
      seamonkey 2.17.1, SECURITY_PATCH=53
      linux 3.8.8
      e16 1.0.13
      poppler 0.22.3
      ilmbase 2.0.0
      openexr 2.0.0
      gmic 1.5.5.2
      whois 5.0.24
      man-pages 3.51
      glib2 2.36.1
      gtk+3 3.8.1
      less 458
      ed 1.8
      linux 3.8.10
      dmidecode 2.12
      p11-kit 0.18.1
      gstreamer-1.0 1.0.7
      gst-plugins-base-1.0 1.0.7
      gst-plugins-good-1.0 1.0.7
      gst-plugins-ugly-1.0 1.0.7
      gst-plugins-bad-1.0 1.0.7
      gst-libav-1.0 1.0.7
      linux 3.9
      gpgme 1.4.1
      gpa 0.9.4
      libgcrypt 1.5.2
      gpg-crypter 0.4.1
      gparted 0.16.1
      util-linux 2.23
      dhcpcd 5.6.8
      gjs 1.36.1
      gobject-introspection 1.36.0
      gsettings-desktop-schemas 3.8.0
      cogl 1.14.0
      clutter 1.14.2
      clutter-gst 2.0.2
      clutter-gtk 1.4.4
      mutter 3.8.1
      dconf 0.16.0
      vala 0.20.1
      accountsservice 0.6.31
      libxslt 1.1.28
      libgee 0.10.1
      caribou 0.4.10
      gnome-desktop3 3.8.1
      gnome-session 3.8.1
      gnome-settings-daemon 3.8.1
      gnome-menus 3.8.0
      zenity 3.8.0
      dbus-glib 0.100.2
      gcr 3.8.2
      devel/spidermonkey17: spell created, new stable version of spidermonkey
      libwnck3 3.4.5
      libcroco 0.6.8
      libsoup 2.42.2
      gnome-online-accounts 3.8.1
      evolution-data-server 3.8.1
      gnome-shell 3.8.1
      gconf2 3.2.6
      gvfs 1.16.1
      gdm2 3.8.1.1
      mplayer 1.1.1, SECURITY_PATCH=4
      gnupg-exp 2.0.20
      at-spi2-core 2.8.0
      at-spi2-atk 2.8.1
      baobab 3.8.1
      cantarell-fonts 0.0.12
      libpeas 1.8.0
      eog2 3.8.0
      eog-plugins 3.8.0
      gdk-pixbuf2 2.28.1
      libgsf 1.14.26
      c-ares 1.10.0
      openssh 6.2p2
      xombrero 1.5.0
      midori 0.5.2
      wireshark 1.8.7, SECURITY_PATCH=43
      python 2.7.5
      st 0.4.1
      vlc 2.0.7
      devel/rust: new spell, a safe, concurrent, practical language
      strace 4.8
      wireshark 1.10.0
      sg3_utils 1.36
      eviacam 1.7.0
      gthumb2 3.2.2
      gzip 1.6
      xombrero 1.6.0
      v4l-utils 0.9.5
      usbutils 007
      claws-mail conflicts with claws-mail-extra-plugins, part of claws-mail     since 3.9.1
      claws-mail-extra-plugins deprecated, part of claws-mail now
      feh 2.9.3
      xombrero 1.6.1
      linux 3.9.8
      linux 3.10
      xz-utils 5.0.5
      rekonq 2.3.2
      libgpg-error 1.12
      multitail 5.2.13
      libs/libbinio: new spell, binary I/O stream class library
      audacious 3.4
      audacious-plugins 3.4
      audacious-plugins needs libbinio
      cmake 2.8.11.2
      qt4 4.8.5, SECURITY_PATCH=5
      kamerka 0.8.5
      smplayer 0.8.5
      gtk-doc 1.19
      gettext 0.18.3
      evince 3.8.3
      gtk+2 2.24.20
      mc 4.8.9
      xombrero 1.6.3
      automake 1.13.2
      glib2 2.36.3
      audio-soft/sphinxbase: new spell, shared components for Sphinx speech     recognition
      audio-soft/pocketsphinx: new spell, lightweight speech recognition     system
      wine 1.6
      seamonkey 2.19, SECURITY_PATCH=54
      guvcview 1.7.1
      git 1.8.3.4
      gnupg 1.4.14, SECURITY_PATCH=8
      libgcrypt 1.5.3, SECURITY_PATCH=1
      wireshark 1.10.1, SECURITY_PATCH=44
      hplip 3.13.7
      system-config-printer 1.4.1
      linux 3.10.4
      nmap 6.40
      linux 3.10.5
      mc 4.8.10
      lshw B.02.17
      nspr 4.10
      digikam4 3.3.0
      libkdcraw4 4.10.5
      libkexiv24 4.10.5
      libkipi4 4.10.5
      tcpdump 4.4.0
      kdelibs4 4.10.5
      kdebase4 4.10.5
      kdebase4-runtime 4.10.5
      kdepimlibs4 4.10.5
      kdepim4 4.10.5
      kdepim4-runtime 4.10.5
      kdenetwork4 4.10.5
      nepomuk-core 4.10.5
      nepomuk-widgets 4.10.5
      kdeplasmoids4 4.10.5
      oxygen-icons 4.10.5
      ark 4.10.5
      filelight 4.10.5
      jovie 4.10.5
      kaccessible 4.10.5
      kactivities 4.10.5
      kate 4.10.5
      kcalc 4.10.5
      kcharselect 4.10.5
      kdeadmin4 4.10.5
      kdeartwork4 4.10.5
      kdebase-workspace4 4.10.5
      kdetoys4 4.10.5
      kwallet 4.10.5
      sweeper 4.10.5
      superkaramba 4.10.5
      ktimer 4.10.5
      kdewebdev4 4.10.5
      kdesdk4 4.10.5
      okular 4.10.5
      testdisk 6.14
      kdf 4.10.5
      kfloppy 4.10.5
      kgpg 4.10.5
      kmag 4.10.5
      kmousetool 4.10.5
      kmouth 4.10.5
      konsole 4.10.5
      kremotecontrol 4.10.5
      dragon 4.10.5
      tig 1.2
      iproute2 3.10.0
      nasm 2.10.09
      ethtool 3.10
      whois 5.0.26
      linux 3.10.6
      curl 7.32.0
      analitza 4.10.5
      audiocd-kio 4.10.5
      blinken 4.10.5
      cantor 4.10.5
      ffmpegthumbs 4.10.5
      gwenview4 4.10.5
      juk 4.10.5
      kalgebra 4.10.5
      kalzium 4.10.5
      kamera 4.10.5
      kanagram 4.10.5
      kcolorchooser 4.10.5
      kdegraphics-strigi-analyzer 4.10.5
      kdegraphics-thumbnailers 4.10.5
      kmix 4.10.5
      pykde4 4.10.5
      svgpart 4.10.5
      akonadi 1.10.2
      attica 0.4.2
      shared-desktop-ontologies 0.11.0
      soprano 2.9.3
      stellarium 0.12.2
      linux 3.10.7
      qlandkarte-gt: fault removed
      samba 3.6.18, SECURITY_PATCH=20, CVE-2013-4124
      darkstat 3.0.717
      midori 0.5.5
      gpgme 1.4.3
      qtscriptgenerator 0.2.0
      glib2 2.36.4
      dhcpcd 6.0.5
      gettext 0.18.3.1
      lvm 2.02.100
      linux 3.10.8
      gnupg-exp 2.0.21
      linux 3.10.9
      nss: fixed for DEFAULT branch
      seamonkey 2.20, SECURITY_PATCH=55
      openssh 6.3p1
      wireshark 1.10.2, SECURITY_PATCH=45
      e2fsprogs 1.42.8
      libidn 1.28
      gtk+3 3.8.4
      ltrace 0.7.3
      seamonkey 2.21, SECURITY_PATCH=56
      gparted 0.16.2
      links-twibright 2.8
      linux 3.11.3
      texinfo 5.2
      gnupg 1.4.15, SECURITY_PATCH=9, CVE-2013-4402
      libassuan 2.1.1
      gnupg-exp 2.0.22, SECURITY_PATCH=7, CVE-2013-4402
      Revert "New Spell: gnupg2"
      v4l-utils 1.0.0
      girara 0.1.7
      zathura 0.2.4
      zathura-pdf-poppler 0.2.3
      python-pypi/pexpect: new spell, pure Python expect-like module
      linux 3.11.5
      fping 3.6
      kde4-apps/clementine: new spell, music player and library organizer
      erlang R16B02
      sg3_utils 1.37
      git 1.8.4.2
      glib2 2.38.1
      libemf 1.0.7
      gpicview 0.2.4
      firefox 25.0, SECURITY_PATCH=68
      fluidsynth/HISTORY fixed
      wireshark 1.10.3, SECURITY_PATCH=46
      linux 3.12
      rxvt-unicode 9.19
      gimp 2.8.8
      graphviz 2.34.0
      perl 5.18.1
      imagemagick 6.8.7-4
      gobject-introspection 1.38.0
      gsettings-desktop-schemas 3.10.1
      librsvg2 2.40.0
      openssh 6.4p1, SECURITY_PATCH=7
      vlc 2.1.1
      bino 1.4.3
      xaos 3.6
      python3 3.3.3
      midori 0.5.6
      rekonq 2.4.0
      rdesktop 1.8.1
      wine 1.6.1
      wine 1.7.7
      clementine 1.2.1
      libpcap 1.5.1
      tcpdump 4.5.1
      iptables 1.4.21
      gimp 2.8.10
      mc 4.8.11
      e-17/emotion_generic_players: new spell, Emotion Generic Players
      ChangeLog: e-17/emotion_generic_players added
      poppler 0.22.4
      linux 3.12.3
      linux 3.12.4
      freetype2 2.5.2
      python-pypi/python-efl: new spell, python bindings for EFL
      python-efl mentioned in ChangeLog
      guvcview 1.7.2
      vlc 2.1.2
      file 5.16
      linux 3.12.5
      samba 3.6.22, SECURITY_PATCH=21, CVE-2013-4408 and CVE-2012-6150
      ffmpeg 2.1.1
      wireshark 1.10.4, SECURITY_PATCH=47
      coreutils 8.22
      gnupg 1.4.16, SECURITY_PATCH=10, CVE-2013-4576
      gstreamer-1.0 1.2.2
      gst-plugins-base-1.0 1.2.2
      gst-plugins-good-1.0 1.2.2
      gst-plugins-ugly-1.0 1.2.2
      gst-plugins-bad-1.0 1.2.2
      gst-libav-1.0 1.2.2
      openssl 1.0.0l, SECURITY_PATCH=21
      multitail 6.0
      pulseaudio 4.0
      ffmpeg 2.1.2
      whois 5.1.1
      rpm2targz 9.0.0.5g
      midori 0.5.7
      http/qupzilla: new spell, web browser based on qtwebkit
      rekonq 2.4.2
      libusb 1.0.18
      libusb-compat 0.1.5
      openssh 6.5p1
      djm.gpg: 0x6D920D30 added, Damien Miller <djm@mindrot.org>
      nss 3.15.4, SECURITY_PATCH=4, CVE-2013-1740
      nspr 4.10.3
      firefox 27.0, SECURITY_PATCH=71
      qupzilla 1.6.1
      vlc 2.1.3
      v4l-utils 1.0.1
      bino 1.4.4
      ffmpeg 2.1.3
      firefox 27.0.1, SECURITY_PATCH=72
      portaudio19 stable_v19_20140130
      libpng 1.2.51
      multitail 6.2.1
      libfm 1.2.0
      pcmanfm 1.2.0
      gparted 0.18.0
      ffmpeg 2.1.4
      clementine 1.2.2
      linux 3.13.5
      openssh 6.6p1
      nspr 4.10.4
      midori 0.5.8
      libjpeg-turbo 1.3.1
      linux 3.14
      linux 3.14.1
      nmap 6.46
      wireshark 1.10.7, SECURITY_PATCH=48
      htop 1.0.3
      linux 3.14.3
      tig 2.0.1
      gnupg-exp 2.0.23
      ffmpeg 2.2.3
      gnupg 1.4.17, SECURITY_PATCH=11
      samba 3.6.24, SECURITY_PATCH=23, CVE-2014-0244 and CVE-2014-3493
      gnupg-exp 2.0.24, SECURITY_PATCH=8
      gnupg 1.4.18
      gnupg-exp 2.0.25
      dbus 1.8.6, SECURITY_PATCH=11
      libpcap 1.6.1
      tcpdump 4.6.1
      v4l-utils 1.2.1
      ffmpeg 2.3
      nss 3.16.3
      firefox 31.0
      gtk+2 2.24.24
      opencv 2.4.9
      opencv: patch from Arch added
      graphics/nomacs: new spell, image viewer
      minitube 2.2
      qt4 4.8.6, SECURITY_PATCH=6
      vlc 2.1.5
      wireshark 1.12.0
      nomacs 2.0.2
      linux 3.15.8
      git 2.0.4
      linux 3.16
      ffmpeg 2.3.1
      phonon 4.7.2
      phonon-backend-gstreamer 4.7.2
      phonon-backend-vlc 0.7.2
      digikam4 4.2.0
      qmmp 0.8.0
      qmmp 0.8.1
      qmmp-plugin-pack: new plugin, set of extra plugins for qmmp
      ChangeLog: qmmp-plugin-pack added
      deadbeef 0.6.2
      ffmpeg 2.3.2
      linux 3.16.1
      libgcrypt 1.6.2
      gnutls 3.2.17 and 3.1.26
      libassuan 2.1.2
      libgpg-error 1.13
      nss 3.16.4
      firefox 32.0, SECURITY_PATCH=75
      libpcap 1.6.2
      tcpdump 4.6.2
      tig 2.0.3
      mc 4.8.13
      nmap 6.47
      utils/direvent: new spell, directory event monitoring daemon
      man-pages 3.72
      libvpx 1.3.0
      seamonkey 2.29, SECURITY_PATCH=57
      phonon 4.8.0
      phonon-backend-gstreamer 4.8.0
      phonon-backend-vlc 0.8.0
      linux 3.16.3
      wireshark 1.12.1
      libcaca 0.99.beta19
      mpv 0.6.0
      openal-soft 1.16.0
      bino 1.6.0
      gtk-doc 1.21
      atk 2.14.0
      gobject-introspection 1.42.0
      gtk+3 3.14.1
      poppler 0.26.5
      poppler-data 0.4.7
      libsecret 0.18
      whois 5.2.0
      bash 4.3.30, SECURITY_PATCH=8
      guvcview 2.0.1
      openssh 6.7p1
      linux 3.17
      shotwell 0.20.1
      gexiv2 0.10.2
      ChangeLog: fixed
      linux 3.17.1
      tea 38.0.0
      wireshark 1.12.2, SECURITY_PATCH=50
      midori 0.5.9
      linux 3.17.3
      traceroute 2.0.21
      linux 3.17.4
      libksba 1.3.2, SECURITY_PATCH=1
      pciutils 3.3.0
      git 2.2.0
      gpa 0.9.6
      lsscsi 0.28
      linux 3.18
      wget 1.16.1
      file 5.21
      net/libpsl: new spell, C library to handle the Public Suffix List
      linux 3.18.1
      links-twibright 2.9
      file 5.22
      openssl 0.9.8zd, 1.0.1k, SECURITY_PATCH++
      linux 3.18.2
      wireshark 1.12.3, SECURITY_PATCH=51
      gettext 0.19.4
      git 2.2.2
      openssl 0.9.8ze, 1.0.1l
      linux 3.18.3
      libmtp 1.1.8
      dbus 1.8.14, SECURITY_PATCH=14
      nettle needs -L/lib to find gmp
      guile needs -L/lib to find gmp
      linux 3.18.4
      patch 2.7.3, SECURITY_PATCH=2, CVE-2015-1196
      gnu.gpg: added 5D1B36D7, Andreas Gruenbacher <agruen@gnu.org>
      linux 3.18.5
      linux 3.18.6
      gti 1.2.0
      linux 3.19
      feh 2.12
      dbus 1.8.16, SECURITY_PATCH=15
      doxygen 1.8.9.1
      glibmm 2.42.0
      exif 0.6.21
      imagemagick 6.9.0-5

Mark Bainter (1):
      Adding missing dependency on glib2

Pavel Vinogradov (20):
      gurus.gpg: added my new uids
      mail/mutt: updated devel version to 1.5.23
      mail/mutt: added new subkey to mutt.gpg keyring
      http/firefox: version 35.0.1
      science-libs/mdds: new spell, multi-dimensional data index algorithm
      science-libs/mdds: added scm branch and its sub_dependency
      libs/ixion: new spell, a general purpose formula parser and interpreter
      libs/orcus: new spell, an import filter library for ODS, XLSX and CSV filters
      libs/orcus/REPAIR^all^PRE_SUB_DEPENDS: small fix, wrong check
      graphics-libs/libvisio: updated to 0.1.1
      graphics-libs/libvisio/libvisio-0.0.19.tar.xz.sig: deleted
      chat-im/pidgin: updated to 2.10.11, SECURITY_PATCH++
      libs/gettext: made gettextize non-interactive
      audio-drivers/alsa-utils: moved BUILD scm code to PRE_BUILD,     added gettext for scm branch as well
      graphics-libs/freetype2: version 2.5.5
      x11-libs/fontconfig: version 2.11.92
      audio-players/mpd: version 0.19.8
      devel/git: version 2.3.0
      libs/glibc: version 2.21, SECURITY_PATCH++
      doc/evince: version 3.15.4

Pol Vinogradov (157):
      disk/fuse-google-drive: new spell, a fuse filesystem wrapper for Google     Drive
      lxde/lxdm: added high CPU load fix
      lxde/lxdm/HISTORY: corrected formatting
      xfce/libxfcegui4: version 4.10.0
      collab/subversion: added ${INSTALL_ROOT} in zlib and neon in DEPENDS, need neon with DAV
      collab/subversion: version 1.7.5, changed SOURCE_URL[0], switched gpg keys
      collab/subversion: fixed DEPENDS completely
      video/mplayer2: changed git url, disabled esound and arts dependencies for scm branch
      libs/glibc: version 2.15, added some gcc fixes, renewed GnuPG key
      http/firefox: version 14.0.1
      video/mplayer2: fixed scm branch dependencies
      disk/fuse: unlock.patch now applies to stable branch only
      xfce/xfburn: apply glib232.patch to stable branch only
      wm-addons/cairo-dock: version 3.0.2
      wm-addons/cairo-dock-plugins: version 3.0.2
      ftp/lftp: added patch to build with glibc 2.16 and newer
      wm-addons/cairo-dock: version 3.1.0
      wm-addons/cairo-dock-plugins: version 3.1.0
      video/mplayer2: fixed scm branch build
      http/lightspark: version 0.7.0
      mail/claws-mail: version 3.9.0
      mail/claws-mail-extra-plugins: updated to 3.9.0
      lxde/lxinput: new spell, a small program used to configure keyboard and mouse for LXDE
      video-libs/gmtk: version 1.0.7
      video/gnome-mplayer: version 1.0.7
      video/gecko-mediaplayer: version 1.0.7
      wm-addons/cairo-dock: updated to 3.1.2
      wm-addons/cairo-dock-plugins: version 3.1.2
      http/gnash: updated to 0.8.10
      http/gnash: fixed linking with current boost
      graphics-libs/agg: fixes to build with current autotools
      http/lightspark: version 0.7.1
      gnome3-libs/vte3: updated version to 0.34.2
      doc/fbreader: switched to git for scm branch
      doc/fbreader: switched to git for scm branch
      x11/lightdm: updated to 1.4.0
      x11/lightdm-gtk-greeter: version 1.4.0
      x11/lightdm-gtk-greeter: my bad, version 1.3.1
      graphics-libs/poppler: added automake related fixes to the scm branch
      science/stellarium: version 0.12.0
      mobile/cpufreqd: updated to 2.4.2
      x11/lightdm: version 1.5.1
      x11/lightdm-gtk-greeter: version 1.5.1
      wm-addons/cairo-dock: version 3.2.0
      wm-addons/cairo-dock-plugins: version 3.2.0
      kernels/linux-fusion: switched to git
      gnome2-libs/libsoup: version 2.42.0
      http/webkitgtk: version 2.0.0
      http/webkitgtk3: version 2.0.0
      x11/lightdm: version 1.5.1
      x11/lightdm-gtk-greeter: version 1.5.1
      wm-addons/cairo-dock: version 3.2.0
      wm-addons/cairo-dock-plugins: version 3.2.0
      kernels/linux-fusion: switched to git
      gnome2-libs/libsoup: version 2.42.0
      http/webkitgtk: version 2.0.0
      http/webkitgtk3: version 2.0.0
      Revert "http/webkitgtk: version 2.0.0"
      Revert "http/webkitgtk3: version 2.0.0"
      video-libs/live: version 2013.04.30
      gnome2-libs/policykit: spidermonkey is required now
      audio-libs/flac: version 1.3.0
      http/firefox: changed mozconfig to prevent segfaults
      http/firefox: version 22.0
      ftp/transmission: version 2.80
      crypto/nettle: changed libdir
      wm-addons/cairo-dock: version 3.3.0
      wm-addons/cairo-dock-plugins: version 3.3.0
      video/xbmc: updated to 13.0_r2 Gotham
      http/webkitgtk: updated to 2.4.2
      http/webkitgtk3: updated to 2.4.2
      libs/glibc: version 2.19
      mail/claws-mail: updated to 3.10.0
      http/webkitgtk: version 2.4.3
      http/webkitgtk3: version 2.4.3
      video/xbmc: version 13.1
      gnome2-libs/gobject-introspection: version 1.40.0
      libs/nspr: version 4.10.6
      crypto/nss: version 3.16.1
      http/firefox: version 30.0
      kernels/kmod: updated to 18
      wm-addons/cairo-dock: version 3.3.2
      wm-addons/cairo-dock-plugins: version 3.3.2
      FUNCTIONS: more fixes to recent changes
      FUNCTIONS: more fixes in get_scm_version
      x11-libs/cairo: added scm branch
      http/midori: git -> bzr, converted to cmake build system completely
      http/webkitgtk: updated to 2.4.4
      http/webkitgtk3: version 2.4.4
      devel/vala: version 0.24.0
      gnome3-libs/granite: new spell, elementary Development Library
      http/midori: fixed building with gobject-introspection
      http/webkitgtk3: version 2.5.1
      utils/dialog: added option for shared library
      disk/whdd: new spell, a HDD diagnostic and recovery tool for Linux
      video/xbmc: version 13.2
      gnome3-libs/adwaita-icon-theme: new spell, Adwaita icon theme for GNOME
      doc/evince: version 3.13.92
      chat-im/pidgin: updated to 2.10.9
      chat-im/pidgin-window-merge: new spell, one window plugin for Pidgin
      http/dwb: new spell, a WebKit browser
      http/dwb: fixed a typo in grimoire's ChangeLog, replaced PREFIX with DESTDIR in INSTALL
      http/dwb/INSTALL: fixed the "fix"
      http/dwb: browser needs gnutls and json-c
      http/webkitgtk3: updated to 2.6.0
      http/webkitgtk: updated to 2.4.6
      disk/grub2: fixed binary names, gcc flag matching and building with current freetype2
      disk/grub2/BUILD: good old sed works better
      doc/evince: version 3.14.1
      gnome3-libs/adwaita-icon-theme: version 3.14.0
      http/webkitgtk: version 2.4.7
      http/webkitgtk3: version 2.6.2
      wm-addons/cairo-dock: version 3.4.0
      wm-addons/cairo-dock-plugins: version 3.4.0
      ftp/wget: version 1.16
      net/bridge-utils: added a missed header fix from Red Hat patch
      xfce/xfdesktop: version 4.10.3
      http/firefox: updated to 34.0
      crypto/nss: updated to 3.17.3
      http/firefox: updated to 34.0.5, reorganized mozconfig and DEPENDS
      graphics-libs/freetype2: version 2.5.4, SECURITY_PATCH++
      libs/glibc: version 2.20, SECURITY_PATCH++
      libs/glibc: forgot to fix init script
      archive/tar: added optional depends on acl and attr, helps to get rid of them properly
      archive/tar/DEPENDS: fixed typos/errors
      video/mpv: can be built with LIBAVCODEC, fixed previous HISTORY entry
      video/mpv: version 0.7.1 + some cleanups/fixes
      archive/xz-utils: updated to 5.2.0
      video/kodi: a new rebranded XBMC
      video/xbmc: added CONFLICTS for kodi
      video/xbmc: deprecated in favour of kodi
      python-pypi/python-crontab: new spell, Python Crontab API
      python-pypi/python-crontab: s/UPDATED/ENTERED/
      python-pypi/python-crontab: fixed DEPENDS and switched to https in DETAILS
      python-pypi/python-crontab/HISTORY: date fix
      ftp/curl: updated to 7.40.0
      graphics-libs/libjpeg-turbo: version 1.4.0
      libs/libunibreak: new spell, a liblinebreak replacement
      libs/liblinebreak: spell deprecated [in favour of libunibreak]
      doc/fbreader: now depends on libunibreak
      e-17/evas: now depends on libunibreak
      libs/libunibreak/DETAILS: removed a typo in SOURCE_URL[0]
      libs/libunibreak: now it uses Github only
      emacs-lisp/auto-complete: version 1.4.0, switched to Github
      emacs-lisp/popup-el: new spell, Visual Popup Interface Library for Emacs
      emacs-lisp/auto-complete: needs popup-el
      doc/fbreader: made use of shared libunibreak
      http/firefox: updated to 35.0
      haskell/haskell-text: updated to 1.2.0.4
      graphics-libs/harfbuzz: added FORCE_DOWNLOAD=on for scm branch
      mail/claws-mail: c-ares is not needed anymore
      video/mpv: version 0.7.2
      video/mpv: fixed getting the waf script from upstream
      video/mpv: made use of DETAILS' SOURCE2 for bootstrapping waf
      database/sqlite: updated to 3.8.8.1
      http/firefox: made profile guided optimisation fully optional, simplified some logic in DEPENDS
      database/sqlite: made use of string replacement and date utility     to compute VERSIONX and SOURCE_URL[0]

Remko van der Vossen (169):
      FUNCTIONS: have disable_pic handle multiple PIC opts
      Revert "FUNCTIONS: have disable_pic handle multiple PIC opts"
      FUNCTIONS: have disable_pic handle multiple PIC opts
      cairo: added depends xz-utils, it's not part of basesystem...
      glib2: added depends xz-utils, it's not part of basesystem...
      apache22: fix compilation for pcre8.30
      glib2: make python optional
      rxvt: depend on specific libs instead of xorg-libs
      xdm: make xdm install config files to etc
      rxvt: fix depends chaining
      w3m: fix build failure with recent glibc
      ruby-glib2: version 1.2.1
      qiv: version 2.2.4 + various dependency fixes
      grip: version 3.3.1
      iputils-tracepath: add missing source hashes
      grip: commit PRE_BUILD missing from fa9d77c8ff6503233cd6700c00e1632ac983b771
      libgpod: added a patch to make hal support work again
      nss: fix patch apply if statement
      pcb: added missing gtkglext dependency if OPENGL enabled
      modsecurity: version 2.7.2
      grip2: deprecate in favour of grip
      live: version 2013.02.11
      libusb: make docs optional
      pciutils: pci.ids is volatile
      pciutils: removed configs; pci.ids.gz was already marked volatile
      qiv: version 2.2.4 + various dependency fixes
      grip: version 3.3.1
      iputils-tracepath: add missing source hashes
      grip: commit PRE_BUILD missing from fa9d77c8ff6503233cd6700c00e1632ac983b771
      libgpod: added a patch to make hal support work again
      nss: fix patch apply if statement
      pcb: added missing gtkglext dependency if OPENGL enabled
      modsecurity: version 2.7.2
      grip2: deprecate in favour of grip
      live: version 2013.02.11
      libusb: make docs optional
      pciutils: pci.ids is volatile
      pciutils: removed configs; pci.ids.gz was already marked volatile
      qemu: version 1.4
      binutils: workaround texinfo related build failure
      curl: improve -DPIC in CFLAGS fix
      glib2: make python optional again
      busybox: version 1.20.2, fix build issue
      libdrm: version 2.4.45
      tdb: 1.2.12
      thunderbird: version 17.0.6, fix up dependencies
      firefox: fix up dependencies
      pidgin-sipe: new spell, SIPE protocol supprt for pidgin
      fdm: 1.7
      dbd-pg: 2.19.3
      openssl: workaround for bug #556
      libxslt: only trigger check_self if optional dep enabled
      libtorrent: 0.13.3
      rtorrent: 0.9.3
      iputils-traceptch: 20121221
      iputils-ping: 20121221
      xzgv: fixed compilation with --as-needed
      iputils-ping: forgotten to add PRE_BUILD
      motif: new spell, motif is released under LPGL
      imlib2: cleanup and X11 sub depends added
      qiv: Fix build for as-needed, X11 subdep on imlib2
      sudo: fix BUILD for case when no editor selected
      w3m: fix build failure with recent libgc
      iptables: 1.4.19.1
      dejavu-ttf: proper download link
      terminus-font: proper download link
      rdesktop: proper download link
      quota: 4.01
      thunderbird: build fails without OpenGL headers
      firefox: build fails without OpenGL headers
      xmag: version 1.0.5
      gnupg: replace -O3 with -O2, gnupg doesn't play nice with -O3
      blackbox: depend no specific X libs
      vnc: depend on specific X libs
      xaw3d: depend on specific X libs
      nss: branch 3.15, version 3.15.1
      thunderbird: version 17.0.8
      firefox: version 23.0.1
      texlive: do not install luatex fonts without lua
      dvipdfmx: add alternative download location
      giflib: xmlto can shove it
      libusb: optional depends udev
      firefox: optional depends gstreamer
      thunderbird: optional depends gstreamer
      grub2: don't strip binary objects
      binutils: removed temporary fix for #543, was fixed in 2.24
      python: download site ssl certificate does not verify
      lua51: shared object not properly linked to dependencies
      lua: link liblua.so with libm.so
      courier: courier_filter init script
      imagemagick: 6.8.9-7
      bitmap: add missing depends libxt
      cairo: missing libxext
      courier-authlib: depends libtool
      curl: depends gmp
      dvipng: depends gd, t1lib
      fdm: depends pcre, SSL
      firefox: added various missing dependencies
      fontconfig: added missing dependencies
      gawk: depends gmp, mpfr
      freetype2: depends glib2, harfbuzz, pcre
      gdk-pixbuf2: libpthread-stubs
      gettext: depends icu
      ghostscript: depends fontconfig
      giblib: depends freetype2, libx11, libxext
      giflib: depends libice, libsm, libx11
      graphviz: added missing dependencies
      groff: optional X11 dependencies
      gtk+2: added missing dependencies
      harfbuzz: depends glib2, libpng, pcre
      imlib2: added missing X11 dependencies
      librsvg2: added missing dependencies
      libidl: depends libidl
      libmms: depends pcre
      libx11: depends libpthread-stubs
      libxaw: added missing X11 dependencies
      libxcb: depends libxdmcp
      libxext: depends libpthread-stubs, libxcb, libxdmcp
      libxmu: added missing dependencies
      libxrender: added missing dependencies
      pango: added missing dependencies
      gtk+2: typo in DEPENDS
      gawk: typo in DEPENDS
      giblib: depends harfbuzz, libpng
      imlib2: depends glib2, harfbuzz, pcre
      libxcomposite: added missing dependencies
      libxcursor: added missing dependencies
      libxdamage: added missing dependencies
      libxfixes: added missing dependencies
      libxft: added missing dependencies
      libxi: added missing dependencies
      libxinerama: added missing dependencies
      libxkbfile: added missing dependencies
      libxpm: added missing dependencies
      libxrandr: added missing dependencies
      libxres: added missing dependencies
      libxtst: added missing dependencies
      libxv: added missing dependencies
      libxvmc: added missing dependencies
      libxxf86dga: added missing dependencies
      libxxf86misc: added missing dependencies
      libxxf86vm: added missing dependencies
      mesalib: depends libxt
      mpd: depends on libogg if libvorbis is enabled
      mplayer: added missing dependencies
      nss: depends sqlite
      mplayer: mesalib -> MESALIB
      pango: depends MESALIB
      xterm: freetype2 was both hard and optional dep
      pidgin: depends nspr
      pidgin-sipe: added missing dependencies
      python: depends gettext
      rdesktop: depends libxrandr
      ruby-2.0: depends libffi
      scrot: depends imlib2, libx11
      slock: depends libx11, libxext
      thunderbird: added missing dependencies
      wget: depends pcre
      wine: depends gettext, libxml2
      x11perf: added missing dependencies
      xdm: added missing dependencies
      xf86-video-ati: added missing dependencies
      xfontsel: added missing dependencies
      xterm: depends libxpm
      xdm: proper optional dependecy descriptions
      rxvt-unicode: clarify extended ISO 14755 modes
      mpd: fix build with --as-needed
      ruby-2.0: version 2.0.0-p576
      wget: properly migrate from openssl to SSL provider

Robin Cook (177):
      live: update to 2012.05.17
      opencv: updated to 2.4.0
      calibre: updated to 0.8.53
      alsa-plugins: updated to 1.0.25
      audacious: updated to 3.2.3 and updated source url
      audacious-plugins: updated to 3.2.3 and updated source url
      libquicktime: updated to 1.2.4
      opencv: updated to 2.4.1
      icedtea6: updated to 1.11.3
      icedtea6: added ICEDTEA to provides so icedtea-web can use either 6 or 7
      icedtea7: new spell - openjdk7
      icedtea7: forgot to add ICEDTEA to provides
      icedtea-web: updated to 1.2 and changed DEPENDS icedtea6 to ICEDTEA
      icedtea6: added icedtea7 to CONFLICTS
      gmtk: update to 1.0.6
      gnome-mplayer: updated to 1.0.6
      gecko-mediaplayer: updated to 1.0.6
      icedtea-web: updated to 1.2.1
      icedtea6: updated to 1.11.4
      gvfs: apply patch to build with gphoto 2.5
      hexchat: new spell, irc client based on xchat
      libproxy: added depends and build options
      libmtp: updated to 1.1.5
      calibre: updated to 0.8.70
      clutter: requires json-glib now
      gnote: updated to 0.8.4 and corrected DEPENDS
      pythonmagick: updated to 0.9.8
      youtube-dl: updated to 2012.02.27
      youtube-dl: updated to 2012.09.27
      evas: added eobj as scm depends
      eobj: added to depends
      libguess: new spell, high-speed character set detection library
      audacious: updated to 3.3.2
      audacious-plugins: updated to 3.3.2
      icedtea6: updated to 1.11.5
      New Spell: libwebp - library for Web-P graphics format
      edbus: change to depend on efl
      eeze: change to using efl
      eio: change to using efl
      e_dbus: change to using efl
      ecore: change to using efl
      edje: change to using efl
      e17: changed e_dbus to edbus
      efreet: changed to using efl
      ethumb: changed e_dbus and use efl
      elementary: changed e_dbus to edbus
      emap: change to using efl
      enki: change to using efl
      emprint: change to using efl
      exchange: change to using efl
      ephysics: change to using efl
      terminology: changed to using efl
      libeweather: changed to using efl
      eweather: changed to using efl
      exquisite: changed to using efl
      imlib2_loaders: changed to using efl
      icedtea7: updated to 2.3.3
      icedtea-web: updated to 1.3.1
      graphite2: updated to 1.2.0
      lua51: updated to 5.1.5
      podofo: updated to 0.9.1
      automake-1.8: added --add-missing to automake command in PRE_BUILD
      cdrdao: added patch for configure.ac so svn will build
      openjade: apply patch to build with perl 5.16 or later
      lightmediascanner: apply patch for autotool changes on scm version
      lua51: remove mistakenly added a.out file
      gwc: updated to 0.21-19
      libnice: updated to 0.1.3
      farstream: updated to 0.2.2
      telepathy-farstream: update to 0.6.0
      gkrellm2: apply gentoo patches to build with newer glib2
      dbus-c++: apply configure.ac patch
      sox: update to 14.4.1
      gst-plugins-good: apply patch to fix v4l2 changes
      clamav: fix sourceforge url
      audacious: updated to 3.3.4
      libcdio-paranoia: new spell, split from libcdio
      audacious-plugins: updated to 3.3.4
      gst-plugins-ugly: apply patch to fix cdio build
      boost: added two missing libraries to CONFIGURE
      mlt: updated to 0.8.8
      mlt: forgot to update website
      gwc: corrected where I commented out libgnomeui in depends
      icedtea6: updated to 1.12.2
      icedtea7: updated to 2.3.6
      icedtea7: updated to 2.3.7
      xf86-input-wacom: updated to 0.19.0
      rubrica: updated to 2.0.12
      libdvdcss: updated to 1.2.13
      uptimed: update to 0.3.17 and added patch for current autotools
      lua51: updated to 5.1.5
      podofo: updated to 0.9.1
      automake-1.8: added --add-missing to automake command in PRE_BUILD
      cdrdao: added patch for configure.ac so svn will build
      openjade: apply patch to build with perl 5.16 or later
      lightmediascanner: apply patch for autotool changes on scm version
      lua51: remove mistakenly added a.out file
      gwc: updated to 0.21-19
      libnice: updated to 0.1.3
      farstream: updated to 0.2.2
      telepathy-farstream: update to 0.6.0
      gkrellm2: apply gentoo patches to build with newer glib2
      dbus-c++: apply configure.ac patch
      sox: update to 14.4.1
      gst-plugins-good: apply patch to fix v4l2 changes
      clamav: fix sourceforge url
      audacious: updated to 3.3.4
      libcdio-paranoia: new spell, split from libcdio
      audacious-plugins: updated to 3.3.4
      gst-plugins-ugly: apply patch to fix cdio build
      boost: added two missing libraries to CONFIGURE
      mlt: updated to 0.8.8
      mlt: forgot to update website
      gwc: corrected where I commented out libgnomeui in depends
      icedtea6: updated to 1.12.2
      icedtea7: updated to 2.3.6
      icedtea7: updated to 2.3.7
      xf86-input-wacom: updated to 0.19.0
      rubrica: updated to 2.0.12
      libdvdcss: updated to 1.2.13
      uptimed: update to 0.3.17 and added patch for current autotools
      glibmm: updated to 2.36.2
      pavucontrol: updated to 2.0
      gtkmm2: updated to 2.24.3
      policykit: updated to 0.110
      gtkmm3: updated to 3.8.1
      gmtk: updated to 1.0.8
      gnome-mplayer: updated to 1.0.8
      claws-mail: added additional configure and optional depends
      dconf: updated to 0.16.1
      tbb: adde -f to link command
      ibus: updated to 1.5.3
      ibus-anthy: updated to 1.5.3
      gstreamer: added patch to build with bison 3
      linuxdoc-tools: updated to 0.9.69
      guile: updated to 2.0.9
      libmad: use automake 1.9 until someone wants to fix using newest automake
      libmad: didn't need automake-1.9 just needed --add-missing
      uptimed: modify PRE_BUILD for new automake and autoconf
      swh-plugins: added patch to remove set locale calls
      icedtea7: changed pre build to work with new automake
      gstreamer-1.0: updated to 1.0.10
      cdrdao: fixed to build with new automake
      cairo: updated to 1.12.16
      gst-plugins-good: another patch needed to get the v4l2 to compile
      mlt: updated to 0.9.0
      cups: force to use gcc and will use clang by default and fail
      fluidsynth: updated to 1.1.6
      sdl2: new spell, new version of SDL
      sdl2_image: new version of sdl_image
      sdl2_mixer: new version of sdl_mixer
      sdl2_net: new version of sdl_net
      sdl2_ttf: new version of sdl_ttf
      timidity: updated to 2.14.0
      smpeg2: new spell, smpeg that uses sdl2
      barcode: updated to 0.99
      iec16022: new spell, library for DataMatrix barcode
      glabels: updated to 3.2.0
      gimp: added PRE_BUILD to fix freetype2 header path
      gecko-mediaplayer: updated to 1.0.8
      easytag: updated to 2.1.9
      docbook-utils: apply patch to work with new grep
      docbook-utils: forgot PATCHLEVEL
      dvdauthor: updated to 0.7.1 and added scm build option
      transcode: added PRE_BUILD to apply gentoo patches so will build
      New Spell: x11-toolkits/goocanvas2
      libsecret: updated to 0.16
      gtksourceview3: updated to 3.8.2
      libgda5: changed gtksourceview and goocanvas and added optional depends
      gofffice: updated to 0.10.9
      gnumeric: updated to 1.12.9
      abiword: updated devel version to 2.9.4
      claws-mail: updated to 3.9.3
      xplanet: apply fix for newest giflib
      webkitgtk: updated to 2.2.4
      webkitgtk3: updated to 2.2.4
      abiword: updated to 3.0.0

Sukneet Basuta (357):
      i3status: => 2.5.1
      deadbeef: => 0.5.4
      kernel.gpg: 6092693E Greg Kroah-Hartman (Linux kernel stable release signing key)
      glibc: fix SOURCE URLS for sigs of kernel versions >=3.0     PRE_BUILD: correctly verify files with GPG for Kernel headers >=3.1 and patches >3.0.4
      tzdata: new spell, the Time Zone Database     time zone list generated by     { sed /#/d /usr/share/zoneinfo/zone.tab | cut -f 3-4 -d "    " && find /usr/share/zoneinfo/ -path '/usr/share/zoneinfo/posix' -prune -o -path '/usr/share/zoneinfo/right' -prune -o \! -name \*.\* -type f -print | sed 's:/usr/share/zoneinfo/::g' ;}| sort -k 1,1 -u | awk '{OFS=FS="\t"}{$2="\x22" $2 "\x22"}{printf "%-50s%-100s%s\n",$1,$2,"off"}
      glibc: PATCHLEVEL++, do not install timezone rules, use tzdata instead     The timezone files supplied by glibc are fairly dated, so use tzdata instead.
      mx: => 1.4.6
      totem: => 3.4.2
      totem-pl-parser: => 3.4.2
      gnome-settings-daemon: => 3.4.2
      gsettings-desktop-schemas: => 3.4.2
      orca: => 3.4.2
      gcalctool: => 6.4.2.1
      nautilus2: => 3.4.2
      gnome-control-center: => 3.4.2
      distribute: => 0.6.27
      file-roller: => 3.4.2     bz2 -> xz     I'm assuming that it is no longer necessary have a PRE_BUILD for xz files.
      libvdpau: PATCHLEVEL=1     recast to ensure new TRIGGERS are active
      tzdata: add config_query to ask if sorcery should manage /etc/localtime     - only install local timezone if requested to     - remove files that should be hard linked, in the case they are actual files and not links (should adress Arjan's issue)     * hard_linked_files: added, list of files that should be hard links     * FINAL: added, provide instructions if the SA decided to manually manage /etc/localtime
      tzdata: fix filename for hard_linked_files in INSTALL
      gnu.gpg: added 5B147849: public key "Aspell Dictionary Upload <dict-upload@aspell.net>"
      aspell-en: => 7.1-0
      tzdata: $SCRIPT_DIRECTORY -> $SPELL_DIRECTORY     fixed spelling error in INSTALL: TIme -> Time
      lua51:  if x86_64, force fPIC CFLAG
      lua: if x86_64, force fPIC CFLAG
      ChangLog: forgot to add additions to gnu.gpg and kernel.gpg     relevant commits are:     ff89247d36d1f89017f0164788bf434fec2b5c6f -     gnu.gpg: added 5B147849: public key "Aspell Dictionary Upload <dict-upload@aspell.net>"     & 7084d80b203bae09e8ba22abcd9aca746cb0eb91 -     kernel.gpg: 6092693E Greg Kroah-Hartman (Linux kernel stable release signing key)
      libcfg+: if x86_64, force fPIC CFLAG     fix website url
      printproto: re-sign source tarball, source seems to have changed     removed PRE_BUILD, no longer needed
      lua51: fix x86_64 check in PRE_BUILD
      lua: fix x86_64 check in BUILD
      a52dec: remove prefer-non-pic flag from LIBA52_CFLAGS if x86_64 so it builds on systems without -fPIC CFLAG     - PRE_BUILD: added, to apply fPIC.patch if x86_64     - fPIC.patch: added, remove prefer-non-pic flag from LIBA52_CFLAGS so it builds on systems without -fPIC
      libglade2: added depends atk
      cyrus-sasl: added sqlite optional_depends     sqlite.patch: added, removes invalid gcc flags to allow compilation with sqlite support
      libprelude: => 1.0.0     libtool.patch: added, fixes compilation with libtool 2.4     PRE_BUILD: added to apply patch     NOTE: the build still fails with gnutls 3.0 branch. I couldn't find a patch so I'll have to look into this when I can.I don't use this lib for anything so it may be a while.
      eog2: => 3.4.1
      eog-plugins: => 3.4.1
      libproxy: fix compilation with gcc 4.7     compilation with gcc 4.6 still works     unistd.patch: added, from fedora. Add unistd.h to files that need it     PRE_BUILD: added
      pulseaudio: => 2.0
      qcomicbook: => 0.9.0
      lxappearance: => 0.5.2     PRE_BUILD: added, need to remove call to g_thread_init(). It is depreciated in glib 2.31+ and does not link automatically
      qt4: add config_query to build webkit with or without HTML5 video support
      i3lock: => 2.4.1
      weechat: => 0.3.8
      ffmpeg: stable => 0.11     DEPENDS: dirac replaced by schroedinger in stable              yasm -> X86-assembler (--disable-yasm is still valid)              optional_depends libvpx added for stable
      ffmpeg-svn: remove optional_depends dirac replaced by schroedinger
      udisks: added depends udev with GUDEV subdepends
      deadbeef: => 0.5.5     gtk+3 support no longer experimental
      hspell: => 1.2     BUILD: added, build with enable-shared
      dwm: => 6.0     fixed formatting for Long description     PRE_BUILD: ensure EDITOR has a value by sourcing /etc/profile.d/editor.sh or defaulting to nano
      sandy: new spell, A tiny ncurses text editor (Closes #368)
      ffmpegthumbnailer: new spell, Thumbnailer to create thumbnails for video files.
      surf: ensure EDITOR has a value by sourcing /etc/profile.d/editor.sh or defaulting to nano
      init.d: fixed udev check for linux 3.x
      init.d:  make udev check for linux 3.x more robust
      gnuplot: apply fix for automake-1.12     patch from upstream
      pygobject: fix build with gobject-introspection
      pygobject3: added UP_TRIGGERS - cast pygobject if pygobject has gobject-introspection enabled, so it is built without it.     See https://bugzilla.gnome.org/show_bug.cgi?id=657054
      pygobject3: added UP_TRIGGERS - cast pygobject if pygobject has gobject-introspection enabled, so it is built without it.     See https://bugzilla.gnome.org/show_bug.cgi?id=657054
      ragel: apply fix for gcc 4.7     still compiles with gcc 4.6
      avahi: Do not run autoreconf as it seems to break install
      Revert "avahi: Do not run autoreconf as it seems to break install"
      avahi: Do not run autoreconf as it seems to break install     Changed qt.patch to patch configure rather than configure.ac so autoreconf does not need to be run.
      oss: stable => 4.2-build2006
      gdb: removed optional_depends tk as gdbtk is a separate project (insight) (fixes #249)
      ddd: fix compilation on gcc >= 4.4     PRE_BUILD - added to apply patch     gcc-4.4.patch - added, fixes compilation on gcc >= 4.4
      krb5: => 1.10.2     fixed SOURCE_URL[0]     BUILD: --with-krb4 no longer valid, removed.            --enable-dns-for-kdc no longer valid, removed.     * CONFIGURE: removed, no longer needed     * PRE_BUILD: Don't apply system-et.patch.                  Apply gcc-4.7.patch.     * gcc-4.7.patch: added, fix compilation with gcc 4.7, still compiles with gcc 4.6     * system-et.patch.bz2: removed, not needed --with-system-et should do this
      krb5-appl: => 1.0.3
      scim: => 1.4.13     * DEPENDS: Changed optional_Depends scim-tables to  suggest_depends.                Changed depends gtk+2 to optional_depends.                Added optional_depends gtk+3
      scim-tables: => 0.5.10
      eigen2: updated sha512 and fixed SOURCE_DIRECTORY
      atlas: if fortran is enabled, apply patch to not compile fortran libs (fixes #161)     * no_fortran.patch: added, patch to not compile fortran libs     * BUILD: Only install fortran libs if optional fortran depends is enabled
      scim: => 1.4.14     * DEPENDS: added optional_depends qt4 and clutter     * BUILD: removed, compiles fine when gtk+3 is selected as default
      llvm: fix compilation on gcc 4.7     Still compiles on gcc 4.6
      atlas: fixed HISTORY     if fortran is enabled, apply patch to not compile fortran libs -> if fortran is NOT enabled, apply patch to not compile fortran libs
      gnokii: => 0.6.31
      libmsn: fix compilation on gcc 4.7     still compiles on gcc 4.6     PRE_BUILD added
      glade3: => 3.12.1     bz2 -> xz     Fixed SOURCE_DIRECTORY, SOURCE, and SOURCE_URL
      glade3: forgot to add new sig
      graphite2: => 1.1.3
      gksu: fix compilation of nautilus plugin with glib >= 2.31
      unique: fix compilation with glib >= 2.31
      system-config-printer: added depends desktop-file-utils (for desktop file install)
      mutter: add flag to treat warnings as warnings, not errors
      cdrdao: fix compilation of stable branch by adding stat headers     * PRE_BUILD: added, to apply patch for stable branch     * stat.patch: added, add stat headers to fix compilation
      vlc: apply lua 5.2 fixes
      totem: => 3.4.3
      linux-pam: switch to optional_depends for selinux to pass proper flags
      libgnomecups: => 0.2.3     fixed WEB_SITE
      libgnomeprint: fix compilation by adding missing header
      glibc: add as_fn_executable_p() to configure            so it can detect grep. I have no idea why or how its missing though.
      ptlib: => 2.10.5            Fixed SOURCE_URL[0]            Added scm branch to go with opal            Updated licence and WEB_SITE
      opal: => 3.10.5           Fixed SOURCE_URL[0]           fixed SCM info and switched to prepare_select_branch           updated License, WEB_SITE, SHORT, and description
      libgpod: added optional_depends gtk-sharp-2 & udev              changed GTK2  to gdk-pixbuf2
      libgda3: => 3.1.5     	 fix compilation with glib >= 2.31
      openssh: updated LPK patch to 6.0p1 (fixes #404)
      pilot-link: fix compilation with perl>=5.14
      pilot-link: actually add files
      glibc: specify libdir so libs install to /usr/lib on all archs
      libfame: fix build
      xine-libs: replaced optional_depends libdts with libdca
      xbmc: changed optional_depends libdts to libdca
      libdts: spell deprecated [libdca replaced libdts a long time ago.]     PATCHLEVEL=9999
      mysql-workbench: howl -> -sub COMPAT_HOWL avahi
      pidgin: removed optional-depends howl
      carrier: removed optional-depends howl
      gnome-user-share: howl -> -sub COMPAT_HOWL avahi
      xinetd: optional_depends howl -> -sub COMPAT_HOWL avahi
      net6: => 1.3.14
      gnome-vfs2: removed optional_depends howl
      gobby: depends howl -> -sub COMPAT_HOWL avahi
      supercollider: depends howl -> -sub COMPAT_HOWL avahi
      libdts: deprecated, forgot to commit ChangeLog
      howl: spell deprecated [Replaced by avahi and no longer compiles for me.]     PATCHLEVEL=9999
      mcomix: => 0.99
      glib2: => 2.32.4
      libchamplain: => 0.12.3     PRE_BUILD removed, no longer needed
      tzdata: => 2012d     updated SOURCE_URL[1]
      vala: stable => 0.16.1           devel  => 0.17.3
      strigi: => 0.7.7     changed SOURCE_URL to debian since 0.7.7 is no longer available from official sources
      easystroke: added TRIGGERS to check_self when boost is cast
      distribute: => 0.6.28     * DEPENDS: depend on PYTHON, rather than selecting with PREPARE     * PREPARE: removed, no longer needed
      digikam4: added depends marble
      clucene: re-add stable branch (0.9.21b)            * PREPARE: added, to select branch            * DEPENDS: if branch is 2.x depend on boost and cmake            * BUILD: use default_build if stable branch, cmake_build otherwise            * SUB_DEPENDS, PRE_SUB_DEPENDS, REPAIR^ALL^PRE_SUB_DEPENDS: added, to force stable branch
      strigi: changed depends clucene to optional_depends, with sub_depends stable
      soprano: added sub_depends stable to clucene to ensure proper functionality, as 2.x of clucene is not supported     suggested_depends virtuosso -> optional_depends since it is the default backend.
      kdemultimedia4: => 4.8.4     * DEPENDS: added optional_depends pulseaudio & ffmpeg                fixed up optional_depend descriptions     * PRE_BUILD: added to apply patch if ffmpeg >= 0.11 is installed     * kdemultimedia-4.8.4-ffmpeg-0.11.patch: added, to remove deprecated functions
      mediastreamer: =>2.8.2     * PREPARE: added, to query for video support     * BUILD: added, to apply video support flags     * DEPENDS: added optional_depends pulseaudio & doxygen.                added optional_depends ffmpeg, libvpx, libtheora, libxv for when if video support is enabled.      * PRE_BUILD: apply ffpmeg patch if ffmpeg is enabled & >= 0.11      * mediastreamer-ffmpeg-0.11.patch: added, to fix compilation with ffmpeg >=0.11      * disable-v4l1.patch: removed, no longer needed
      kdemultimedia4: forgot to account for ffmpeg-svn     DEPENDS: ffmpeg -> LIBAVCODEC     PRE_BUILD: apply ffmpeg-0.11 patch for ffmpeg-svn as well
      mediastreamer: apply ffmpeg patch for ffmpeg-svn as well
      ktorrent4: => 4.2.1     * DEPENDS: added depends qca2
      libktorrent: => 1.2.1-2
      ktorrent4: removed depend qca2, it's a libktorrent depends
      kdegames4: => 4.8.4     bz2 -> xz
      kdenetwork4: => 4.8.4
      antlr: SUB_DEPENDS added to force JAVA optional_depends
      kdesdk4: => 4.8.4
      kde4*/FUNCTIONS: added prepare_cmake_flags to default_build, to allow passing cmake flags.     Added to default_build rather than each individual BUILD since all kde spells use cmake.
      kdesdk4: use % instead of @ to pass cmake flags, as prepare_cmake_flags handles this.
      kdepimlibs4: => 4.8.4     * DEPENDS: added depends boost, gpgme, shared-mime-info, shared-desktop-ontologies, soprano, libxsl
      kdepim4: => 4.8.4     * DEPENDS: added depends akonadi, zlib, strigi, libxslt.                Changed optional_depends gpgme, libassuan to depends.                Removed optional_depends qca2, libmal, gnokii.                Added optional_depends grantlee, dblatex     * PRE_BUILD: added, to apply boost patch     * kdepim-4.8.4-boost-1.48.patch: added, fixes compilation with boost >= 1.48
      pycups: apply patch to fix compatibility with cups 1.6 (fixes #417)     * pycups-1.9.61-cups-1.6.patch: from upstream git, fixes pycups for cups 1.6
      rake: => 0.9.2.2     SOURCE_URL changed to debian since upstream does not have a tarball.
      tzdata: => 2012e
      libprelude: fix build with patch     libprelude-1.0.0-ptrdiff.patch: adds missing header
      Revert "Merge branch 'master' into glibc"
      glibc: specify slibdir to force install all libs to /lib (fixes #411)
      glibc: checkout head for scm, instead of a release branch     PREPARE: scm-2.13 renamed to scm
      i3: => 4.3     DEPENDS:       added optional_depends pango
      gdb: Use make -C gdb install to install, so it does not install files that conflict with bintuils     Added INSTALL
      Revert "Revert "Merge branch 'master' into glibc""
      gvfs: run autoreconf to solve libtool version mismatch errors
      ladspa: patch for proper PIC support     PRE_BUILD: added, to apply patch.
      swh-plugins: Run autopoint and autoreconf     PRE_BUILD added, to apply patches and run autopoint and autoreconf. Autopoint is run to update gettext macros.
      glib2: => 2.34.0
      gtk+3: => 3.6.0     DEPENDS: updated versions for gdk-pixbuf2, atk, pango              added depends at-spi2-atk
      atk: => 2.6.0
      at-api2-core: => 2.6.0
      at-spi2-atk: => 2.6.0
      libsecret: new spell, A library for storing and retrieving passwords and other secrets.
      file-roller: => 3.6.0     DEPENDS: gtk+2 -> gtk+3              added optional_depends libarchive              added suggest_depends zip, rar, unrar, tar, unace, p7zip
      lua: PROVIDES lua     added PROVIDES since it looks like lua51 will be around for awhile
      lua51: PROVIDES LUA     added PROVIDES since it looks like lua51 will be around for awhile
      weechat: stable => 0.3.9, devel => 0.4.0-dev     readded devel branch info
      i3status: => 2.6
      freedesktop.gpg: added, for freedesktop software     added FA970E17 "Richard Hughes <richard@hughsie.com>"
      colord: => 0.1.22     switched to upstream GPG verification
      colord-gtk: new spell, GTK support for colord
      libcanberra: => 0.30     tar.gz -> tar.xz
      mash: new spell, a small library for using 3D models in clutter
      gnome-color-manager: => 3.6.0     DEPENDS: added depends glib2, gtk+3, gnome-desktop3, colord-gtk, libcanberra              added optional_depends clutter-gtk, mash, exiv2, libexif, vte3
      vte3: => 0.34.0
      easystroke: => 0.5.6
      cracklib: fix BUG #504     Fix from Javier Vasquez     PRE_BUILD: Replacing AM_CONFIG_HEADER by  AC_CONFIG_HEADER, since the 1st got obsolete on automake 1.13.1.
      ilmbase: fix compilation of programs dependent on ilmbase (opnexr)     patch from upstream
      pango: remove fake gtk doc check     check works fine now.
      krb5: fix build with tcl 8.6     define USE_INTERP_RESULT to fix building with tcl 8.6     * Note that this is a hack and should be removed on next update *
      mariadb: build with -with-readline     until system readline support fixed.
      soundtouch: fix build with automake 1.13     replace AM_CONFIG_HEADER with AC_CONFIG_HEADERS in configure.ac
      kde4-apps/FUNCTIONS: ensure $SORCERY_PATH is the first path (BUG #506)
      libktorrent: => 1.3.1
      ktorrent4: => 4.3.1
      passenger: PASSENGER_BRANCH=3 => 3.0.19     Passenger 2 doesn't seem to compile with the latest version of BOOST.     I couldn't find a patch and am not sure if anyone still needs it. (BUG #507)
      loudmouth: run autoconf so it links to gobject correctly
      gnome-online-accounts: added depends libsecret
      readpst: => 0.6.58     changed SOURCE_URL to official src     * CONFIGURE: added, to enable dii utility     * DEPENDS: added, added optional_depends python and boost when python is enabled     * BUILD: force building shared libs     * INSTALL, libpst.pc: removed, no longer needed
      evolution: updated configure flags     * BUILD: remove disable-nm build flag, no longer valid     * DEPENDS: removed optional_depends gnome-pilot-conduits, mono, python, rarian                added optional_depends gnome-online-accounts                updated configure flags for libchamplain
      kernel.gpg: added key 1DCF2659 "Marcel Holtmann <marcel@holtmann.org>"     for bluez
      bluez: => 4.101     gz -> xz     * PRE_BUILD: added, for gpg verification of extracted tar     * CONFIGURE: removed deprecated configure flags     * DEPENDS: removed optional_depends libcap-ng
      samba.gpg: added with keys 6568B7EA "Samba Distribution Verification Key <samba-bugs@samba.org>" and 13084025 "Samba Library Distribution Key <samba-bugs@samba.org>"     for samba and related spells
      tevent: remove git version, add stable 0.9.17     git version removed because it checks out entire samba4 and it was broken     * DEPENDS: removed depends git     * PRE_BUILD: uncompress gz to verify tarball     * BUILD, INSTALL, PREPARE: removed
      samba4: stable => 4.0.2     updated SOURCE_URLs     changed to upstream gpg verification
      i3: => 4.4
      i3: forgot to add PRE_BUILD
      sbc: new spell, Bluetooth Subband Codec (SBC) library     required by pulseaudio and gstreamer when bluez support is enabled
      bluez: if bluez enabled depend on sbc and dbus
      mediastreamer: fixed ffmpeg version check in PRE_BUILD
      pasystray: new spell, PulseAudio system tray
      padevchooser: removed, deprecated upstreams and hasn't compile in a long time     pasystray is a third party replacement
      pulseaudio: suggest_depends padevchooser->pasystray
      gnome-settings-daemon: => 3.6.4
      totem-pl-parser: => 3.4.3     * DEPENDS: gtk+2->gtk+3                added optional-depends libarchive & libgcryp
      ffmpegthumbnailer: => 2.0.8     * BUILD: build with --enable-thumbnailer to register as thumbnailer under /usr/share/thumbnailers     * PRE_BUILD, ffmpegapi_fix_r241.patch: removed, no longer needed
      tracker: => 0.14.5     * DEPENDS: added optional_depends taglib, libgxps, libcue, giflib, gdk-pixbuf2                thunderbird, firefox, rest, network-manager                removed optional_depends id3lib, libnotify                added depends libgee if search-bar is enabled                disabled optional_depends evolution, currently broken with evolution 3.6                **check if its fixed on next update**     * BUILD: updated configure flags
      qt4: PATCHLEVEL++     * PRE_BUILD, qt-everywhere-opensource-src-4.8.4-QTBUG-22829.patch: patch to fix moc for builds that depend on BOOST 1.53
      i3status: => 2.7
      i3status: added optional_depends libcap
      bug-buddy2: spell removed, deprecated in gnome 3
      gnome2-profile: removed optional_depends bug-buddy2     This spell is no longer valid, but updating anyway since there is no gnome3 profile spell yet
      gnome-python-desktop: removed optional_depends bug-buddy2
      gnome-applets2: => 3.5.92     latest dev version used because latest stable version doesn't compile with gnome 3.6
      evince: => 3.6.1
      gtkhtml2: => 4.6.4
      gtksourceview3: => 3.6.3
      gtkspell3: new spell, gtkspell v3     not API-compatible with 2.x     spell copied from gtkspell
      balse: => 2.5.0     DEPENDS: added depends gtk+3, glib2, 2.4 gmime, webkit, gtkhtml2              added optional_depends gpgme, libcanberra, gtksourceview3, gtkspell3, libnotify, network-managet, sqlite, libsecret, rubrica              removed depends libgnomeprintui, aspell
      nautilus-sendto: => 3.6.1     added optional_depends gtk-doc
      gnome-bluetooth: => 3.6.1     DEPENDS: nautilus2 -> nautilus-sendto              removed optional_depends rarian
      stunnel: => 4.55     changed SOURCE_URLs to use archive dir so source is always available
      libsecret: => 0.14
      gtk+2: => 2.4.17
      libgee: => 0.6.8     DEPENDS: added optional_depends gobject-introspection
      notify-osd: => 0.9.34     changed to upstream GPG verification     DEPENDS: gtk+2 -> gtk+3     CONFIGURE, PRE_BUILD, leolik.patch: added to optionally apply leolik's patch for a customizable notify-osd (https://launchpad.net/~leolik/+archive/leolik)
      notification-daemon: => 0.7.6
      canonical.gpg: added key 0B6AF348, Mirco Müller (MacSlow) <macslow@bangang.de>     for notify-osd
      exo-0.5, thunar-1.1: removed, should probably never been created     removed CONFLICTS in exo and thunar
      xfce4-notifyd: spell created     I assume this replaces notification-daemon-xfce, but xfce4-notifyd is already pretty old so I assume notific     ation-daemon-xfce still works.     I'll leave it up to the xfce maintainer to decide whether notification-daemon-xfce is still relavent
      notification-daemon: added conflicts xfce4-notifyd
      notification-daemon-xfce: added conflicts xfce4-notifyd
      notify-osd: added conflicts xfce4-notifyd
      date-manip: => 6.39
      xml-twig: => 3.42
      xmltv: => 0.5.63     updated WEB_SITE     DEPENDS: added depends xml-parser-expat
      portaudio: => v19_20111121     DEPENDS: added     BUILD, INSTALL: removed
      audio-drivers/libfreebob: removed, no longer compiles and is no longer relevant     also added exo-0.5 and thunar-1.1 to Changelog, which I forgot earlier
      jack: removed optional_depends libfreebob and portaudio     removed optional_depends libfreebob, spell removed, and portaudio, to prevent a cyclic dependency and is not needed on linux anyway (portaudio spell will provide necessary files)
      gstreamer-1.0: => 1.0.5
      gst-plugins-base-1.0: => 1.0.5     DEPENDS: removed optional_depends gnome-vfs2, no longer valid
      gst-plugins-good: => 1.0.5     DEPENDS: removed optional_depends hal, gconf2, libxml2, esound              gtk+2 -> gdk-pixbuf2              added optional_depends libvpx
      gst-plugins-bad: => 1.0.5
      gst-plugins-ugly: => 1.0.5
      mythtv: => 0.26.0     CONFIGURE: removed query for OSS     DEPENDS: added optional_depends yasm, libxml2, pulseaudio, libvdpau, xrandr, libxv, libass, avahi, lame, faac, x264, libvpx              removed optional_depends directfb
      cheese: => 3.6.2      DEPENDS: removed depends mx, gstreamer, gst-plugins-base, gnome-desktop               removed optional_depends rarian               added depends gstreamer-1.0, gst-plugins-base-1.0, gst-plugins-bad-1.0, pango, clutter               added optional_depends gtk-doc, gobject-introspection               changed sub-depends libcanberra to GTK3
      icedtea7: DOWNLOAD: only check if SOURCE1 exists. Always download the others. (BUG #503)     If we wish to download only on a timestamp change, we will have to use cURL or something similar.
      gnome-control-center: => 3.6.3     DEPENDS: gtk+2 -> gtk+3, gnome-desktop -> gnome-desktop3              added runtime_depends consolekit & accountsservice              removed optional_depends evolution-data-server, xscreensaver, rarian              added optional_depends ibus, cheese              added suggest_depends network-manager, gnome-bluetooth
      xcb-proto: => 1.8
      libxcb: => 1.9
      xcb-util: => 0.3.9
      xcb-util-image: => 0.3.9
      xcb-util-keysyms: => 0.3.9
      xcb-util-wm: => 0.3.9
      xpyb: => 1.3
      kdebase-workspace4: added depends strigi, xcb-util, xcb-util-image, xcb-util-renderutil     added optional_depends kdelibs4, fontconfig2, pciutils, soprano, nepomuk-core, boost, akonadi, kdepim4, qjson, OPENGL
      Revert "xpyb: => 1.3"
      Revert "xcb-util-wm: => 0.3.9"
      Revert "xcb-util-keysyms: => 0.3.9"
      Revert "xcb-util-image: => 0.3.9"
      Revert "xcb-util: => 0.3.9"
      Revert "libxcb: => 1.9"
      Revert "xcb-proto: => 1.8"
      Revert "gnu/gcc: fix header generation for libgo"
      Revert "gnu/gcc: fix -ffast-math"
      Revert "gnu/gcc: remove redundant libffi"
      Revert "gnu/gcc: cleanup for moving gcc 4.7.2 into test grimoire"
      Revert "gcc: => 4.7.2"
      Revert "gnu/gcc: use new version of the ada bootstrap compiler"
      Revert "gcc: => 4.7.1"
      Revert "gcc: => 4.7.0"
      kdepim4: added depends nepomuk-widgets              added optional_depends cyrus-sasl
      libev: => 4.15
      i3: => 4.5
      i3: => 4.5.1
      smplayer: => 0.8.4
      glibmm: => 2.34.1
      gtkmm3: => 3.6.0
      easystroke: => 0.6.0
      bluez: if bluez enabled depend on sbc and dbus
      mediastreamer: fixed ffmpeg version check in PRE_BUILD
      pasystray: new spell, PulseAudio system tray
      padevchooser: removed, deprecated upstreams and hasn't compile in a long time     pasystray is a third party replacement
      pulseaudio: suggest_depends padevchooser->pasystray
      gnome-settings-daemon: => 3.6.4
      totem-pl-parser: => 3.4.3     * DEPENDS: gtk+2->gtk+3                added optional-depends libarchive & libgcryp
      ffmpegthumbnailer: => 2.0.8     * BUILD: build with --enable-thumbnailer to register as thumbnailer under /usr/share/thumbnailers     * PRE_BUILD, ffmpegapi_fix_r241.patch: removed, no longer needed
      tracker: => 0.14.5     * DEPENDS: added optional_depends taglib, libgxps, libcue, giflib, gdk-pixbuf2                thunderbird, firefox, rest, network-manager                removed optional_depends id3lib, libnotify                added depends libgee if search-bar is enabled                disabled optional_depends evolution, currently broken with evolution 3.6                **check if its fixed on next update**     * BUILD: updated configure flags
      qt4: PATCHLEVEL++     * PRE_BUILD, qt-everywhere-opensource-src-4.8.4-QTBUG-22829.patch: patch to fix moc for builds that depend on BOOST 1.53
      i3status: => 2.7
      i3status: added optional_depends libcap
      bug-buddy2: spell removed, deprecated in gnome 3
      gnome2-profile: removed optional_depends bug-buddy2     This spell is no longer valid, but updating anyway since there is no gnome3 profile spell yet
      gnome-python-desktop: removed optional_depends bug-buddy2
      gnome-applets2: => 3.5.92     latest dev version used because latest stable version doesn't compile with gnome 3.6
      evince: => 3.6.1
      gtkhtml2: => 4.6.4
      gtksourceview3: => 3.6.3
      gtkspell3: new spell, gtkspell v3     not API-compatible with 2.x     spell copied from gtkspell
      balse: => 2.5.0     DEPENDS: added depends gtk+3, glib2, 2.4 gmime, webkit, gtkhtml2              added optional_depends gpgme, libcanberra, gtksourceview3, gtkspell3, libnotify, network-managet, sqlite, libsecret, rubrica              removed depends libgnomeprintui, aspell
      nautilus-sendto: => 3.6.1     added optional_depends gtk-doc
      gnome-bluetooth: => 3.6.1     DEPENDS: nautilus2 -> nautilus-sendto              removed optional_depends rarian
      stunnel: => 4.55     changed SOURCE_URLs to use archive dir so source is always available
      libsecret: => 0.14
      gtk+2: => 2.4.17
      libgee: => 0.6.8     DEPENDS: added optional_depends gobject-introspection
      notify-osd: => 0.9.34     changed to upstream GPG verification     DEPENDS: gtk+2 -> gtk+3     CONFIGURE, PRE_BUILD, leolik.patch: added to optionally apply leolik's patch for a customizable notify-osd (https://launchpad.net/~leolik/+archive/leolik)
      notification-daemon: => 0.7.6
      canonical.gpg: added key 0B6AF348, Mirco Müller (MacSlow) <macslow@bangang.de>     for notify-osd
      exo-0.5, thunar-1.1: removed, should probably never been created     removed CONFLICTS in exo and thunar
      xfce4-notifyd: spell created     I assume this replaces notification-daemon-xfce, but xfce4-notifyd is already pretty old so I assume notific     ation-daemon-xfce still works.     I'll leave it up to the xfce maintainer to decide whether notification-daemon-xfce is still relavent
      notification-daemon: added conflicts xfce4-notifyd
      notification-daemon-xfce: added conflicts xfce4-notifyd
      notify-osd: added conflicts xfce4-notifyd
      date-manip: => 6.39
      xml-twig: => 3.42
      xmltv: => 0.5.63     updated WEB_SITE     DEPENDS: added depends xml-parser-expat
      portaudio: => v19_20111121     DEPENDS: added     BUILD, INSTALL: removed
      audio-drivers/libfreebob: removed, no longer compiles and is no longer relevant     also added exo-0.5 and thunar-1.1 to Changelog, which I forgot earlier
      jack: removed optional_depends libfreebob and portaudio     removed optional_depends libfreebob, spell removed, and portaudio, to prevent a cyclic dependency and is not needed on linux anyway (portaudio spell will provide necessary files)
      gstreamer-1.0: => 1.0.5
      gst-plugins-base-1.0: => 1.0.5     DEPENDS: removed optional_depends gnome-vfs2, no longer valid
      gst-plugins-good: => 1.0.5     DEPENDS: removed optional_depends hal, gconf2, libxml2, esound              gtk+2 -> gdk-pixbuf2              added optional_depends libvpx
      gst-plugins-bad: => 1.0.5
      gst-plugins-ugly: => 1.0.5
      mythtv: => 0.26.0     CONFIGURE: removed query for OSS     DEPENDS: added optional_depends yasm, libxml2, pulseaudio, libvdpau, xrandr, libxv, libass, avahi, lame, faac, x264, libvpx              removed optional_depends directfb
      cheese: => 3.6.2      DEPENDS: removed depends mx, gstreamer, gst-plugins-base, gnome-desktop               removed optional_depends rarian               added depends gstreamer-1.0, gst-plugins-base-1.0, gst-plugins-bad-1.0, pango, clutter               added optional_depends gtk-doc, gobject-introspection               changed sub-depends libcanberra to GTK3
      icedtea7: DOWNLOAD: only check if SOURCE1 exists. Always download the others. (BUG #503)     If we wish to download only on a timestamp change, we will have to use cURL or something similar.
      gnome-control-center: => 3.6.3     DEPENDS: gtk+2 -> gtk+3, gnome-desktop -> gnome-desktop3              added runtime_depends consolekit & accountsservice              removed optional_depends evolution-data-server, xscreensaver, rarian              added optional_depends ibus, cheese              added suggest_depends network-manager, gnome-bluetooth
      xcb-proto: => 1.8
      libxcb: => 1.9
      xcb-util: => 0.3.9
      xcb-util-image: => 0.3.9
      xcb-util-keysyms: => 0.3.9
      xcb-util-wm: => 0.3.9
      xpyb: => 1.3
      kdebase-workspace4: added depends strigi, xcb-util, xcb-util-image, xcb-util-renderutil     added optional_depends kdelibs4, fontconfig2, pciutils, soprano, nepomuk-core, boost, akonadi, kdepim4, qjson, OPENGL
      Revert "xpyb: => 1.3"
      Revert "xcb-util-wm: => 0.3.9"
      Revert "xcb-util-keysyms: => 0.3.9"
      Revert "xcb-util-image: => 0.3.9"
      Revert "xcb-util: => 0.3.9"
      Revert "libxcb: => 1.9"
      Revert "xcb-proto: => 1.8"
      Revert "gnu/gcc: fix header generation for libgo"
      Revert "gnu/gcc: fix -ffast-math"
      Revert "gnu/gcc: remove redundant libffi"
      Revert "gnu/gcc: cleanup for moving gcc 4.7.2 into test grimoire"
      Revert "gcc: => 4.7.2"
      Revert "gnu/gcc: use new version of the ada bootstrap compiler"
      Revert "gcc: => 4.7.1"
      Revert "gcc: => 4.7.0"
      kdepim4: added depends nepomuk-widgets              added optional_depends cyrus-sasl
      libev: => 4.15
      i3: => 4.5
      i3: => 4.5.1
      smplayer: => 0.8.4
      glibmm: => 2.34.1
      gtkmm3: => 3.6.0
      easystroke: => 0.6.0
      thunderbird: => 24.5.0     DEPENDS: use nss version 3.16

Thomas Orgis (148):
      gnuplot: bump to 4.6 and fixup
      mpg123: push to 1.14.2
      mpd: docs need doxygen
      mpg123: fix integer quality choice
      mpg123: bump to 1.14.3
      module-starter: create spell
      path-class: new spell     module-starter: actually depends on the above
      pod-coverage, test-pod, test-pod-coverage: created
      devel-size: added
      devel-cover: added
      transcode: make it build again
      device-modem: update
      device-gsm: update to 1.58
      config-param: added
      config-param: now also announced in Changelog
      config-param: bump to 3.000005
      hydrogen: bump to 0.9.5
      config-param: bump to 3.000009
      clalsadrv: bump to 2.0.0
      mpg132: bump to 1.14.4
      qwt5: update tp 6.0.1
      jaaa: added
      wpa_supplicant: fix qt4/gui switch
      text-asciipipe: new spell
      live: bump to 2012.09.27 (that one is obtainable)
      devel-nytprof, json, json-any: added
      config-param: bump to 3.000010
      math-derivative: added
      math-spline: added
      calibre: fix source url
      calibre: fix source url
      liblo: bump to 0.26
      cryptsetup-luks: really build static binary
      ardour2: bump to 2.8.16, with syslibs as only remaining option
      gammu: bump to 1.32.0
      jack2: add website
      jack2: bump to 1.9.9.5
      libffado: bump to 2.1.0 (made jack2 work again for me)
      mpg123: bump to 1.15.1
      mpg123: bump to 1.15.3
      mpg123: bump to 1.15.1
      avidemux2: switch to provided build script, enabling avidemux to     actually do something since plugins are not missing
      mksh: bump to R46
      mpg123: bump to 1.15.4
      texlive: hack to install a copy of TexLive::TLUtils to make updmap work
      texlive: build gsftopk
      avidemux2: fix things to get something workable, less proper choice,     but at least with plugins to have some functionality!
      djview4: fix build for still-present old Qt
      graphicsmagic: fix DEPENDS to make it build again
      gnuplot: fix CVS build
      nco: new spell
      libao: fix license and update description
      mpg123: 1.16.0
      text-numericdata: new spell, replacing textdata
      buntstift: update to 0.61
      text-asciipipe: bump to 1.001000
      text-numericdata: bump to 2.000004
      rdflib: bump to 4.0.1
      serd: update to 0.18.2     dave_robillard.gpg: new key for serd and friends (updates follow)
      sord: update to 0.12.0
      lv2: new spell for the full package, replacing lv2core     lv2core: deprecated
      lv2: fix build (missing $SOURCE2, typo in BUILD)
      sratom: new spell
      sratom: moved to audio-libs, as it's audio plugin-specific
      lv2: license is called ISC
      lilv: new spell
      sratom-0, lilv-0, lilv-util: Trying to sort out the mess with multi-version libs and utils.
      suil-0: new spell
      liblrdf: update checksum (cannot compare what changed, though, due to lack of old source)
      xmlrpc-c: bump to 1.25.26
      ardour2: fix build with current lilv
      ardour3: created
      ardour3: ChangeLog entry
      ardour3: add phone-home option
      text-numericdata: bump to 2.001000
      mpg123: bump to 1.17.0
      mpg123: bump to 1.18.0
      mpg123: is a security fix
      glibc: Switch to .xz files for 3.x kernel headers (.bz2 files not present for recent versions).
      mpg123: bump to 1.18.1
      avidemux3: new spell
      openmpi: fix Fortran dependency
      mpg123: 1.20.0
      config-param: bump to 3.001000
      dermixd: bump to 2.0.0, adapt to new build system
      mpg123: bump to 1.20.1
      klick: bump to 0.12.2
      gtklick: bump to 0.6.4
      nss: fixup, also new PEM; spell still a mess
      libdrm: NV and NOUVEAU duality
      freeglut: fix deps for mesalib-1x
      wxgtk: depend on glu
      cairo: build fix
      net-tools: fix build by disabling obsolete hardware
      tcp_wrappers: PIC build
      gawk: reduce library usage
      lvm: 2.02.109 and hack to make static build work (again)
      screen: bump to 4.2.1
      libffado: depends on libconfig
      libconfig: needs C++ compiler
      libiec61883: hash changed
      jack2: bump to 1.9.10
      lv2: more robust installation
      slv2: fix dependency on lv2
      lilv-0: fail-safe cleanup before install
      dbus-c++: build fixup
      ecore: bump to 1.7.10
      eina: bump to 1.7.10
      garcon: more depends
      libxfce4util: more depends
      aubio03: historic version of spell for ardour2
      ardour2: keep spell working
      audacity: bump to 2.0.5 and build fix
      swh-plugins: fix with current autotools
      sox: hack for current ffmpeg
      cdrtools: bump to 3.01a24 and man path fix
      xcdroast: bump to 0.98alpha16, include patches
      lightdm: bump to 1.8.0
      xcdroast: remove old patch
      mupdf: bump to 1.4
      evince: needs symbolic icons
      xmms2: does not build without CDDA
      libdrm: final stray .orig file from committery
      subversion: bump to 1.8.10 (1.8.9 source already unavailable)
      jack2: depends on libsamplerate, also change scm option to git
      firefox: fix build with gcc-4.9 (on a core2 64 bit machine with PIC CFLAGS, if              that matters ... did not need that on an Athlon II X3 machine with              "native" archspecs)
      whois: bump to 5.1.5 (source for 5.1.4 already pulled by upstream)
      cairo: needs xextproto
      pkgconfig: Remove glib2 dependency, fixing things to version 0.28.
      glib2: hard-depends on PYTHON to avoid the situation without any glib2     when INSTALL fails after removing old one ...
      glib2: Re-add commented optional PYTHON dep at request from fellow mage, for making things optional again some time in the future.
      imagemagick: use ftp.sunet.se as backup URL
      youtube-dl: switch to versioned sources and use upstream signature
      youtube-dl: update to youtube-dl-2014.09.04.3
      youtube-dl: the missing change to INSTALL to make the versioned source work
      calligra: add vc as optional dependency
      calligra: really add vc to DEPENDS
      calligra: use non-empty value for KTINY to properly remember a "no"
      mpg123: bump to 1.21.0
      fix gcj build with freetype
      nted: version 1.10.18
      subversion: add archive URLs
      nted: build fixes
      harfbuzz: avoid cyclic dependency with cairo
      grub2: fix spelling
      cairo: update to 1.12.18 and ditch LTO stuff (update needed to fix firefox scrolling crash)
      firefox: needs libxcomposite
      cryptsetup-luks: update to 1.6.6

Tommy Boatman (201):
      giggle: added patch to address upstream bug 667350
      gtk-sharp-2: issue #407 - fix build with glib2 >= 2.31
      glances: version 1.4              BUILD/INSTALL now use python              DEPENDS require some SETUPTOOLS
      oprofile: version 0.9.7 upgrade to deal with 3.x kernels
      yelp-tools : add hard yelp-xsl dependency
      ark -> 4.9.0
      filelight -> 4.9.0
      jovie -> 4.9.0
      kaccessible -> 4.9.0
      kactivities -> 4.9.0, depends s/kdelibs/nepomuk-core
      kate -> 4.9.0
      kcalc -> 4.9.0
      kcharselect -> 4.9.0
      kde4-l10n -> 4.9.0
      kdeadmin4 -> 4.9.0
      kdeartwork -> 4.9.0, optional eigen2 depends
      kdebase-workspace4 -> 4.9.0
      kdevelop4 -> 4.3.1     kdevplatform4 -> 1.3.1
      kdf -> 4.9.0
      kmag -> 4.9.0
      kmousetool: 4.9.0, bz2 -> xz
      kmouth -> 4.9.0
      Revert "kdf -> 4.9.0"
      kdegames -> 4.9.0
      printer-applet -> 4.9.0
      ktimer -> 4.9.0, bz2 -> xz
      ksecrets -> 4.8.5
      kremotecontrol -> 4.9.0
      kmag -> 4.9.0
      kfloppy -> 4.9.0
      kdf -> 4.9.0
      kdetoys4 -> 4.9.0
      kdepim4-runtime -> 4.9.0
      kdepim4 -> 4.9.0
      analitza: 4.9.0, bz2 -> xz
      blinken: 4.9.0, bz2 -> xz
      kwordquiz:  4.9.0, bz2 -> xz
      cantor: 4.9.0, bz2 -> xz
      kalgebra: 4.9.0, bz2 -> xz
      kalzium: 4.9.0, bz2 -> xz
      kanagram: 4.9.0, bz2 -> xz
      kbruch: 4.9.0, bz2 -> xz
      kgeography: 4.9.0
      khangman: 4.9.0, bz2 -> xz
      kig: 4.9.0, bz2 -> xz
      kiten: 4.9.0, bz2 -> xz
      klettres: 4.9.0, bz2 -> xz
      kmplot: 4.9.0, bz2 -> xz
      kstars: 4.9.0, bz2 -> xz
      ktouch: 4.9.0, bz2 -> xz
      kturtle: 4.9.0, bz2 -> xz
      parley: 4.9.0, bz2 -> xz
      rocs: 4.9.0, bz2 -> xz
      step: 4.9.0, bz2 -> xz
      kimono: 4.9.0, bz2 -> xz
      smokeqt: 4.9.0, bz2 -> xz
      smokeqt: 4.9.0, bz2 -> xz, remove BUILD, add sub-depends for qwt5, add -D switches to qwt5 dependency
      qtruby: 4.9.0, bz2 -> xz, depends smokeqt with qwt5
      smokekde: 4.9.0, bz2 -> xz
      smokegen: 4.9.0, bz2 -> xz
      qyoto: 4.9.0, bz2 -> xz
      korundum: 4.9.0, bz2 -> xz, patch for ruby19
      gnome-settings-daemon:  pulseaudio subdepend glib2 - fix issue #400
      pulseaudio: subdepend glib2 for gnome (Fixes issue #400)
      digikam4: 2.9.0, remove up trigger on kdegraphics4
      sweeper: 4.9.1
      superkaramba: 4.9.1
      printer-applet: 4.9.1
      oxygen-icons: 4.9.1
      nepomuk-core: 4.9.1
      kwallet: 4.9.1
      kdetoys4: 4.9.1
      kdf: 4.9.1
      kfloppy: 4.9.1
      kmag: 4.9.1
      kmousetool: 4.9.1
      konsole: 4.9.1
      kremotecontrol: 4.9.1
      kdenetwork4: 4.9.1
      kdepim4-runtime: 4.9.1
      kdepim4: 4.9.1
      kdeplasmoids4: 4.9.1
      kdesdk4: 4.9.1
      kgpg: 4.9.1
      kmouth: 4.9.1
      kcharselect: 4.9.1
      kdeadmin4: 4.9.1
      kdeartwork4: 4.9.1
      kdebase4: 4.9.1
      kdegames4: 4.9.1
      ktimer: 4.9.1
      kdewebdev4: 4.9.1
      ark: 4.9.1
      filelight: 4.9.1
      kate: 4.9.1
      kcalc: 4.9.1
      kdelibs4: 4.9.1
      kdepimlibs4: 4.9.1
      jovie: 4.9.1
      kdebase4-runtime: 4.9.1
      kaccessible: 4.9.1
      kde4-l10n: 4.9.1
      kactivites: 4.9.1
      kdebase-workspace4: 4.9.1
      kimono: 4.9.1
      korundum: 4.9.1
      kross-interpreters: 4.9.1 - does NOT work with ruby 1.9 per upstream
      perlkde: 4.9.1
      perlqt4: 4.9.1
      pykde4: 4.9.1
      smokekde: 4.9.1
      qtruby: 4.9.1
      qyoto: 4.9.1
      smokegen: 4.9.1
      smokeqt: 4.9.1
      gwenview4: 4.9.1
      kamera: 4.9.1
      kcolorchooser: 4.9.1
      kdegraphics-strigi-analyzer: 4.9.1
      kgamma: 4.9.1
      mobipocket: 4.9.1
      kolourpaint: 4.9.1
      kdegraphics-thumbnailers: 4.9.1
      kruler: 4.9.1
      ksaneplugin: 4.9.1
      ksnapshot: 4.9.1
      libkdcraw4: 4.9.1
      libkexiv24: 4.9.1
      libkipi4: 4.9.1
      libksane: 4.9.1
      okular: 4.9.1
      svgpart: 4.9.1
      analitza: 4.9.1
      blinken: 4.9.1
      cantor: 4.9.1
      kalgebra: 4.9.1
      kalzium: 4.9.1
      kanagram: 4.9.1
      kbruch: 4.9.1
      kgeography: 4.9.1
      khangman: 4.9.1
      kig: 4.9.1
      kiten: 4.9.1
      klettres: 4.9.1
      kmplot: 4.9.1
      kstars: 4.9.1
      kturtle: 4.9.1
      kwordquiz: 4.9.1
      libkdeedu: 4.9.1
      marble: 4.9.1
      parley: 4.9.1
      ktouch: 4.9.1
      step: 4.9.1
      pairs: new spell - KDE memory game
      kdemultimedia4: deprecated (kde4-multimedia-profile)
      audiocd-kio: new spell - KDE audio CD libraries
      mplayerthumbs: new spell - KDE video thumbnailer
      libkcddb: new spell - KDE CD libraries
      dragon: new spell - Dragon media player
      kde4-multimedia-profile: replacement for kdemultimedia4
      ffmpegthumbs: new spell - KDE video thumbnail generator
      juk: new spell - KDE media player
      kmix: new spell - KDE audio mixer
      kscd: new spell - KDE CD player
      libkcompactdisc: new spell - KDE CD libraries
      kde4-multimedia: new section, include KDE functions
      kde4-profile: replace kdemultimedia4 with kde4-multimedia-profile
      ChangeLog: add entries for commits in this batch
      at-spi2-atk: remove extraneous dconf dependency
      gdb: fix libunwind dependency
      xinit: 1.3.2 - fix bug 452
      gmorgan -> 0.57 (Prometheus barfs on old version)
      b43-tools: Prometheus summon failure - changed website to git.bues.ch
      httpry: Fix bombed man page installation  (Prometheus report)
      kdebase4-runtime: kactivities required dependency
      commoncpp2: 1.8.1, sys/stat.h patch from OpenSDE (Bug #190)
      aldo: 0.7.7
      hamlib: 1.2.15.3
      traceroute: upgrade to 2.0.19
      xclock -> 1.0.7
      dash -> 0.5.7
      sharutils -> 4.14
      unrar -> 5.0.14
      pingtunnel -> 0.72
      glances: requires psutil
      gtk-doc: requires itstool
      ffmpeg: requires libcdio-paranoia
      ffmpeg: fixed typo in previous correction
      iso-codes -> 3.50
      fltk: change download URL to fltk.org
      qtbase: removed demos from BUILD to match CONFIGURE
      skrooge: 1.8.0, download URL to download.kde.org
      graphviz: 2.36.0
      db: switch depend from uudeview to UUDECODE
      freetype2: requires libpng
      giflib: depends xmlto
      udisks: needs dbus-glib and policykit
      openexr -> 2.1.0
      kdebase4: optional depends tidy
      orc: optional gtk-doc depends and typo fixes
      gtk+2: PRE_BUILD sed to fix build failure with gtk-doc

Treeve Jelbert (1998):
      Revert "Revert "libs/icu: version 49.1""
      adjust build so that users of icu build correctly     add a TESTING results file
      pylibacl: => 0.5.1
      rasqal: => 0.9.29
      cups: => 1.5.3
      libffi: => 3.0.11
      libatomic_ops: => 7.2
      libgc: => 7.2
      udisks2: => 1.97.0
      udisks2 - depends libacl
      kwave4: => 0.8.8-1
      libssh2: => 1.4.2
      policykit - adjust depends and build
      perl: => 5.16.0
      cython: => 0.16
      mako: => 0.7.0
      beaker: => 1.6.3
      file-next: => 1.08
      dbi: => 1.620
      uri: => 1.60
      html-parser: => 3.69
      lwp: => 6.04
      html-tableextract: => 2.11
      perl-error: => 0.17018
      kmod: => 5
      kmod: => 6
      kmod: => 7
      kmod - add default_final to FINAL
      kmod: => 8
      kmod provides MODTOOLS
      module-init-tools - provides MODTOOLS
      basesystem: => 0.9.6
      kmod - add FINAL
      kmod - now provides all module-init-tools funtions
      gramps: => 3.3.2
      gramps: => 3.4.0
      xapian-core: => 1.2.10
      xapian-bindings: => 1.2.10
      search-xapian: => 1.2.10.0
      gramp - update depends
      libzdb: => 2.10.3
      kyotocabinet: => 1.2.76
      libgssglue: => 0.4
      gdb: => 7.4.1
      numpy: => 1.6.2
      byacc: => 20120526
      bzr: => 2.5.1
      fdb: => 0.8.0
      calligra: => 2.4.2
      webob: => 1.2
      swig: => 2.0.7
      pyutil: => 1.9.3
      libcsv: => 3.0.2
      openfst: => 1.3.2
      alembic: => 0.3.4
      git: => 1.7.10.4
      quazip: => 0.4.4
      new spell - libmusicbrainz5 version 5.0.1
      libgphoto2 - needs libusb-compat
      gutenprint: => 5.2.8
      clamav-0.97.5 - SECURITY++
      libusb-compat - fix build with latest libusbx
      libusbx: => 1.0.12
      dbus: => 1.6.0
      psmisc: => 22.18
      ddrescue: => 1.16
      kmod: => 9
      partclone: => 0.2.49
      docbook-xsl: => 1.77.1
      bash-completion: => 2.0
      dbi: => 1.622
      new spell - six - Python 2 and 3 compatibility utilities
      fuzzyparsers: => 0.8.0
      fb-python: => 0.7.0
      libusb-compat - fix previous sed
      eigen3: => 3.1.0
      pciutils: => 3.1.10
      fdb: => 0.8.5
      raptor: => 2.0.8
      camelot: => 12.06.29
      libunicap - fix obsolete syntax in udev rules
      camelot - add misssing pyside fix
      grub2: => 2.00
      mpfr: => 3.1.1
      alembic: => 0.3.5
      nettle: => 2.5
      boost: => 1_50_0
      partclone: => 0.2.50
      pcre: => 8.31
      libgphoto2: => 2.5.0
      wxgtk-new: => 2.9.4
      wxgtk-new - libxpm is optional
      libexif: => 0.6.21
      libgphoto2 - fix instal in some cases
      acpid2: => 2.0.16
      clucene: => 2.3.3.4
      libburn: => 1.2.4
      libisofs: => 1.2.4
      libisoburn: => 1.2.4
      libmpc: => 1.0
      cups: => 1.6.0
      cups-filters-1.0.20 new spell     contains filters and backends which were previously part of CUPS
      gutenprint: => 5.2.9
      flex: => 2.5.36
      cups: => 1.6.1
      kde4-apps/KDE_DEPENDS revert an invalid change
      udisks2: => 1.99.0
      icu: => 49.1.2
      partclone: => 0.2.51
      cups-filters - add depends bc
      dhcpcd: => 5.6.1
      virtuoso: => 6.1.6
      eigen3: => 3.1.1
      mercurial: => 2.3
      cmake: => 2.8.9
      ghostscript - 9.06 -- security fixes
      perl: => 5.16.1
      schroot: => 1.6.3
      pkgconfig: => 0.27
      alembic: => 0.3.6
      git: => 1.7.12
      calligra: => 2.5.1
      qtbase-5.0.0-beta1   new spell
      qtxmlpatterns-5.0.0-beta1  - new spell
      qtscript-5.0.0-beta1  - new spell
      qtjsbackend-5.0.0-beta1  - new spell
      qt5/FUNCTIONS
      qtdeclarative-5.0.0-beta1  - new spell
      tsvg-5.0.0-beta1  - new spell
      qtquick1-5.0.0-beta1  - new spell
      qtsystems-5.0.0-beta1  - new spell
      qttools-5.0.0-beta1  - new spell
      qtgraphicaleffects-5.0.0-beta1  - new spell
      qtmultimedia-5.0.0-beta1  - new spell
      qtimageformats-5.0.0-beta1  - new spell
      qtwayland-5.0.0-beta1  - new spell
      qtpim-5.0.0-beta1  - new spell
      qt3d-5.0.0-beta1  - new spell
      qtlocation-5.0.0-beta1  - new spell
      qtwebkit-5.0.0-beta1  - moved from http section
      ChangeLog - for qt5 section
      boost - fix SUB_DEPENDS python usage
      boost: => 1_51_0
      kmod: => 10
      libmpc: => 1.0.1, fixes CVE-2012-3386
      ebook-tools: => 0.2.2
      gramps: => 3.4.1
      libatasmart: => 0.19
      python-markdown: => 2.2.0
      mako: => 0.7.2
      webob: => 1.2.2
      postgresql: => 9.2.0
      patch-2.7 - fixes CVE-2010-4651
      calligra: => 2.5.2
      lcms2: => 2.4
      qpdf-3.0.2 - new spell
      cups-filters: => 1.0.24
      geraldo: => 0.4.16
      acpid2: => 2.0.17
      clamav: => 0.97.6
      libusb-compat - remove libusbx fix
      libusbx: => 1.0.13
      tiff-4.0.3 - security - fixes CVE-2012-3401
      scons: => 2.2.0
      dbd-firebird: => 1.11
      six: => 1.2.0
      hdparm: => 9.42
      partclone: => 0.2.54
      byacc: => 20121003
      cython: => 0.17.1
      taglib: => 1.8
      syslog-ng: => 3.3.6
      alembic: => 0.4.0
      sqlalchemy: => 0.7.9
      udisks2: => 2.0.0
      fdb: => 0.9
      ctemplate: => 2.2
      fdb: => 0.9.1
      tzdata: => 2012f
      curl: => 7.28.0
      libxml2: => 2.9.0
      partclone: => 0.2.55
      subversion: => 1.7.7
      v4l-utils: => 0.9.1
      deprecate video-libs/libv4l [replaced by v4l-utils]
      vlc - change depends libv4l -> v4l-utils
      transcode - change depends libv4l -> v4l-utils
      kamerka - change depends libv4l -> v4l-utils
      guvcview - change depends libv4l -> v4l-utils
      xine-lib - change depends libv4l -> v4l-utils
      libunicap - change depends libv4l -> v4l-utils
      kdenetwork4 - change depends libv4l -> v4l-utils
      tellico2 - change depends libv4l -> v4l-utils
      opencv - change depends libv4l -> v4l-utils
      vips - change depends libv4l -> v4l-utils
      gegl - change depends libv4l -> v4l-utils
      amsn - change depends libv4l -> v4l-utils
      sg3_utils: => 1.34
      Revert "python3: https://bugs.gentoo.org/374579 added same to fix installs."
      python3: => 3.3.0
      FUNCTIONS - explicitly use python2
      cracklib: => 2.8.19
      leptonica: => 1.69
      libdvdnav: => 4.2.0
      libdvdread: => 4.2.0
      libzdb: => 2.10.6
      libusbx: => 1.0.14
      tzdata: => 2012h
      cmake: => 2.8.10
      distribute: => 0.6.30
      gramps: => 3.4.2
      mercurial: => 2.4
      tesseract: => 3.02.02
      perl: => 5.16.2
      eigen3: => 3.1.2
      lm_sensors: => 3.3.3
      firebird25: => 2.5.2.26539-0
      firebird25 - tweak init script
      cmake: => 2.8.10.1
      zint: => 2.4.2
      kwave4: => 0.8.9-1
      partclone: => 0.2.56
      libnl: => 3.2.14
      libproxy: => 0.4.10
      kmod: => 11
      icu: => 50.1
      reportlab: => 2.6
      libarchive - make link to icu explicit
      libcroco - make link to icu explicit
      librsvg2 - make link to icu explicit
      hdparm: => 9.43
      hg-git: => 0.3.4
      dulwich: => 0.8.6
      qjson: => 0.8.0
      cython: => 0.17.2
      fuse: => 2.9.2
      libcutl: => 1.7.0
      firebird25 - fixes  CVE-2012-5529
      fftw: => 3.3.3
      boost: => 1_52_0
      schroot: => 1.6.4
      lockdev - create a symlink for liblockdev.so
      qjson: => 0.8.1
      cmake  - use system libraries
      cmake: => 2.8.10.2
      fdb: => 0.9.9
      libssh: => 0.5.3  security fix
      pcre: => 8.32
      mercurial: => 2.4.1
      mako: => 0.7.3
      beaker: => 1.6.4
      python-markdown: => 2.2.1
      pyutil: => 1.9.4
      webob: => 1.2.3
      baker: => 1.3
      kmod: => 12
      alembic: => 0.4.1
      nasm: => 2.10.06
      decorator: => 3.4.0
      syslog-ng: => 3.3.7
      bogofilter: => 1.2.3    SECURTIY FIX
      iw: => 3.7
      libnl: => 3.2.16
      glib2 - remove obsolete patch
      udisks2: => 2.0.1
      odbcfb: => 2.0.1.152
      kbd - optional depends linux-pam
      icu: => 50.1.1
      libdvbpsi: => 1.0.0
      libtasn1: => 3.2
      gnutls: => 3.1.5
      libdvbpsi: => 1.0.0
      libtasn1: => 3.2
      gnutls: => 3.1.5
      tbb: => 41_20121003
      opencv: => 2.4.3
      opencv - optional depends openexr
      eigen3 - provides EIGEN
      eigen2 - provides EIGEN
      opencv - depends EIGEN
      krb5: => 1.11
      freerdp: => 1.0.1
      liblqr: => 0.4.2
      opencv - fix qt4 support
      cimg: => 1.5.2
      upower: => 0.9.19
      opencv - improve build
      ccache: => 3.1.9
      binutils: => 2.23.1
      add  key 306037D9 -P�draig Brad
      coreutils: => 8.20
      partclone: => 0.2.57
      ntfs-3g: => 2013.1.13
      automake: => 1.13.1
      polarssl: => 1.2.3
      ChangeLog - add key for Daiki Ueno
      gettext: => 0.18.2
      fontconfig: => 2.10.2
      sg3_utils: => 1.35
      libcdio: => 0.90
      curl: => 7.28.1
      curl - add support for polarssl
      curl - add krb5 (GSSAPI) support
      libssh2 - add libgcrypt support
      libssh - add libgcrypt support
      libproxy: => 0.4.11
      libburn: => 1.2.6
      libisofs: => 1.2.6
      libisoburn: => 1.2.6
      partclone: => 0.2.58
      ghostscript - update depends
      wine - fix libxxf86vm dependency
      sharutils: => 4.13.3
      libnl: => 3.2.21
      iw: => 3.8
      pstoedit: => 3.61
      syslinux: => 5.01
      schroot: => 1.6.5
      cython: => 0.18
      man-pages: => 3.46
      mercurial: => 2.5
      wine: => 1.5.23
      boost: => 1_53_0  (SECURITY fix)
      kwave4: => 0.8.10-1
      easytag - new website
      redland: => 1.0.16
      rasqal: => 0.9.30
      libssh: => 0.5.4 SECURITY fix
      ChangeLog - for qt5 section
      qtbase: => 5.0.1
      FUNCTIONS: move qt5build to global level
      qtxmlpatterns: => 5.0.1
      qtjsbackend: => 5.0.1
      qtdeclarative: => 5.0.1
      fix qt5 build with multiple versions of python
      qtscript: => 5.0.1
      qtsvg: => 5.0.1
      qtimageformats: => 5.0.1
      qtgraphicaleffects: => 5.0.1
      qtmultimedia: => 5.0.1
      /qtwebkit5-5.0.1
      Revert "qtwebkit-5.0.0-beta1  - moved from http section"
      qttools: => 5.0.1
      harfbuzz: => 0.9.12
      cimg: => 1.5.4
      xlrd: => 0.9.0
      xlwt: => 0.7.4
      chardet: => 2.1.1
      ragel: => 6.8
      syslog-ng: => 3.4.1
      openbabel: => 2.3.2
      ghostscript: => 9.07
      dbus-glib: => 0.100.1   SECURITY fix CVE-2013-0292
      nettle: => 2.6
      polarssl: => 1.2.5  SECURITY_PATCH CVE-2013-0169
      partclone: => 0.2.59
      polarssl: => 1.2.5  SECURITY fix
      gcc: => 4.7.0
      gcc: => 4.7.1
      gcc: => 4.7.2
      librsvg2 - gtk-{2,3} are optional
      podofo: => 0.9.2
      tzdata: => 2012j
      mtools: => 4.0.18
      libgphoto2: => 2.5.1
      cups - adjust build flags
      ndiswrapper: => 1.58
      iw - new url
      mercurial: => 2.5.2
      dosfstools: => 3.0.16
      geraldo: => 0.4.17
      byacc: => 20130304
      gnutls: => 3.1.9.1
      pyicu-1.5 - new spell
      sqlalchemy: => 0.8.0
      clamav: => 0.97.7
      dbi: => 1.623
      mpfr: => 3.1.2
      wine: => 1.5.26
      libtirpc: => 0.2.3
      perl: => 5.16.3 SECURITY fix CVE-2013-1667
      cups: => 1.6.2
      libburn: => 1.2.8
      libisofs: => 1.2.8
      libisoburn: => 1.2.8
      upower: => 0.9.20
      polarssl: => 1.2.6
      icu: => 51.1
      gettext - depends libxml2
      harfbuzz - fix build with icu
      firebird25: => 2.5.2.26540-0  SECURITY FIX
      binutils - extra depends
      unifdef: => 2.7
      partclone: => 0.2.60
      wine: => 1.4.1
      cppunit: => 1.12.1
      gramps: => 3.4.3
      sqlite: => 3.7.16.1
      wxgtk-new  - allow build with gtk+{3,2}
      mc: => 4.8.8
      mercurial: => 2.5.3
      diffutils: => 3.3
      cups-filters: => 1.0.33
      alembic: => 0.5.0
      orc: => 0.4.17
      opencv: => 2.4.5
      udisks2: => 2.1.0
      ruby-2.0: => 2.0.0-p0
      ruby-1.8 - conflicts ruby-2.0
      ruby-1.9 - conflicts ruby-2.0
      ruby-enterprise-edition - conflicts ruby-2.0
      openjpeg: => 1.5.1
      ghostscript - nolonger uses jasper
      qpdf: => 4.0.1
      six: => 1.3.0
      libverto: => 0.2.5
      krb5: => 1.11.1  SECURTIY PATCH - fix CVE-2013-1415
      fdb: => 1.1
      camelot: => 13.04.13
      tzdata: => 2013b
      alsa-lib: => 1.0.27
      alsa-utils: => 1.0.27
      harfbuzz: => 0.9.12
      cimg: => 1.5.4
      xlrd: => 0.9.0
      xlwt: => 0.7.4
      chardet: => 2.1.1
      ragel: => 6.8
      syslog-ng: => 3.4.1
      openbabel: => 2.3.2
      ghostscript: => 9.07
      dbus-glib: => 0.100.1   SECURITY fix CVE-2013-0292
      nettle: => 2.6
      polarssl: => 1.2.5  SECURITY_PATCH CVE-2013-0169
      partclone: => 0.2.59
      polarssl: => 1.2.5  SECURITY fix
      gcc: => 4.7.0
      gcc: => 4.7.1
      gcc: => 4.7.2
      librsvg2 - gtk-{2,3} are optional
      podofo: => 0.9.2
      tzdata: => 2012j
      mtools: => 4.0.18
      libgphoto2: => 2.5.1
      cups - adjust build flags
      ndiswrapper: => 1.58
      iw - new url
      mercurial: => 2.5.2
      dosfstools: => 3.0.16
      geraldo: => 0.4.17
      byacc: => 20130304
      gnutls: => 3.1.9.1
      pyicu-1.5 - new spell
      sqlalchemy: => 0.8.0
      clamav: => 0.97.7
      dbi: => 1.623
      mpfr: => 3.1.2
      wine: => 1.5.26
      libtirpc: => 0.2.3
      perl: => 5.16.3 SECURITY fix CVE-2013-1667
      cups: => 1.6.2
      libburn: => 1.2.8
      libisofs: => 1.2.8
      libisoburn: => 1.2.8
      upower: => 0.9.20
      polarssl: => 1.2.6
      gettext - depends libxml2
      harfbuzz - fix build with icu
      firebird25: => 2.5.2.26540-0  SECURITY FIX
      binutils - extra depends
      unifdef: => 2.7
      partclone: => 0.2.60
      wine: => 1.4.1
      cppunit: => 1.12.1
      gramps: => 3.4.3
      sqlite: => 3.7.16.1
      wxgtk-new  - allow build with gtk+{3,2}
      mc: => 4.8.8
      mercurial: => 2.5.3
      diffutils: => 3.3
      cups-filters: => 1.0.33
      alembic: => 0.5.0
      orc: => 0.4.17
      opencv: => 2.4.5
      udisks2: => 2.1.0
      ruby-2.0: => 2.0.0-p0
      ruby-1.8 - conflicts ruby-2.0
      ruby-1.9 - conflicts ruby-2.0
      ruby-enterprise-edition - conflicts ruby-2.0
      openjpeg: => 1.5.1
      ghostscript - nolonger uses jasper
      qpdf: => 4.0.1
      six: => 1.3.0
      libverto: => 0.2.5
      krb5: => 1.11.1  SECURTIY PATCH - fix CVE-2013-1415
      fdb: => 1.1
      camelot: => 13.04.13
      tzdata: => 2013b
      qtbase: => 5.0.2
      qtxmlpatterns: => 5.0.2
      qtjsbackend: => 5.0.2
      qtdeclarative: => 5.0.2
      qtscript: => 5.0.2
      qtsvg: => 5.0.2
      qtimageformats: => 5.0.2
      qtgraphicaleffects: => 5.0.2
      qtmultimedia: => 5.0.2
      qtwebkit5: => 5.0.2
      qttools: => 5.0.2
      qtquick1: => 5.0.2
      curl-7.30.0  - SECURITY FIX
      Python-3.3.1 - SECURITY fix
      lxml - depends PYTHON
      glib2 needs gettext
      deprecate python-pypi/kinterbasdb [replaced by fdb]
      sqlalchemy - use fdb for firebird support
      sqlalchemy4 - remove firebird support
      sqlobject - remove firebird support
      reportlab: => 2.7
      vlc: => 2.0.6
      fdb - fix python3 depends
      sqlalchemy - fix python3 depends
      lxml - fix python3 depends
      six - fix python3 depends
      pyicu - fix python3 depends
      xlrd: => 0.9.2
      xlwt: => 0.7.5
      pycrypto - fix python3 depends
      nose - fix python3 depends
      fb-python: => 0.7.2
      jinja2 - fix python3 depends
      mako: => 0.8.0
      beaker - fix python3 depends
      markupsafe - fix python3 depends
      numpy: => 1.7.1
      camelot - fix python3 depends
      astyle: => 2.03
      libusbx: => 1.0.15
      eigen3: => 3.1.3
      pyparsing: => 1.5.7
      python3 support
      pyfpdf-1.7
      pyparsing: => 2.0.0
      libunwind: => 1.1
      mercurial: => 2.5.4
      clamav: => 0.97.8  SECURITY FIX
      update gnu.gpg - add 30D155AD Karl Berry <karl@freefriends.org>
      texinfo: => 5.1
      patchutils: => 0.3.3
      cython: => 0.19
      cups-filters: => 1.0.34
      libarchive: => 3.1.2
      dbus: => 1.6.10
      polarssl: => 1.2.7
      raptor: => 2.0.9
      libzip: => 0.11.1
      sqlalchemy: => 0.8.1
      nettle: => 2.7
      tokyocabinet: => 1.4.48
      gdb: => 7.6
      python-dateutil - fix python3 usage
      distribute: => 0.6.36
      python-pypi/FUNCTIONS: fix usage when both python 2,3 are installed
      new spell - vc-0.7.1
      libcsv: => 3.0.3
      iw: => 3.10
      quassel: => 0.9.0
      djview4: => 4.9
      formencode: => 1.2.6
      qpdf: => 4.1.0
      libgda-5.1.2
      cheetah: => 2.4.4
      unifdef: => 2.8
      python-markdown: => 2.3.1
      new spell: pypdf2-1.15
      freetype2: => 2.4.12
      dbi: => 1.625
      tzdata: => 2013c
      libnl: => 3.2.22
      fdb: => 1.1.1
      libburn: => 1.3.0
      libisofs: => 1.3.0
      libisoburn: => 1.3.0
      ruby-2.0.0-p195 SECURITY FIX
      git - optional depends gettext, pcre
      partclone: => 0.2.61
      tbb: => 41_20130314
      gmp: => 5.1.2
      libgphoto2: => 2.5.2
      quazip: => 0.5.1
      libical: => 1.0
      pcre: => 8.33
      lm_sensors: => 3.3.4
      gramps: => 3.4.5
      libjpeg-turbo: => 1.3.0
      new spell: inflect-0.2.3
      swig: => 2.0.10
      libburn: => 1.3.0.pl01
      krb5: => 1.11.2
      gnutls: => 3.1.12
      faulthandler: => 2.2
      libassuan: => 2.1.0
      nettle: => 2.7.1
      python3: => 3.3.2
      lxml: => 3.2.1
      fdb: => 1.2
      dosfstools: => 3.0.18
      icu: => 51.2
      xapian-core: => 1.3.1
      unifdef: => 2.9
      fdb: => 1.3
      cmake: => 2.8.11.1
      wine: => 1.6-rc1
      inflect: => 0.2.4
      sqlacodegen-1.1.0
      cython: => 0.19.1
      dosfstools: => 3.0.20
      sqlacodegen: => 1.1.1
      dbus-1.6.12 SECURITY fix
      python-stdnum-0.8.1
      bash-completion: => 2.1
      openjpeg - extra depends
      cracklib: => 2.9.0
      podofo - lua is optional
      partclone: => 0.2.62
      docbook-xsl: => 1.78.1
      apr: => 1.4.8
      apr-util: => 1.5.2
      libgpg-error: => 1.11
      ack: => 2.04
      freetype2: => 2.5.0.1
      dbi: => 1.627
      ragel - new website
      bsddb3: => 6.0.0
      bash-completion - fix install
      attr: => 2.4.47
      acl: => 2.2.52
      libraw1394: => 2.1.0
      libdc1394: => 2.2.1
      fdb: => 1.4
      polarssl-1.2.8  SECURITY fix
      libdiscid: => 0.5.1
      gccxml: => git
      pybindgen-0.16.0
      dri2proto: => 2.6
      dri2proto: => 2.8
      add missing ChangeLog entry
      rfkill: => 0.5
      lcms2: => 2.5
      boost: => 1_54_0
      serf-1.2.1
      subversion - build with serf
      partclone: => 0.2.66
      kmod: => 14
      cups-filters: => 1.0.35
      mercurial: => 2.6.3
      subversion - various tweaks
      ruby-2.0.0-p247 -  SECURITY fix
      sqlalchemy: => 0.8.2
      qtbase: => 5.1.0
      qtxmlpatterns: => 5.1.0
      qtjsbackend: => 5.1.0
      qtdeclarative: => 5.1.0
      qtscript: => 5.1.0
      qtsvg: => 5.1.0
      qttools: => 5.1.0
      qtimageformats: => 5.1.0
      qtgraphicaleffects: => 5.1.0
      qtmultimedia: => 5.1.0
      qtquick1: => 5.1.0
      qtwebkit5: => 5.1.0
      qtx11extras-5.1.0
      tquickcontrols-5.1.0
      syslog-ng: => 3.4.2
      shiboken: => 1.2.0
      pyside: => qt4.8+1.2.0
      gettext - optional depends libunistring
      cups: => 1.6.3
      openmpi: => 1.6.5
      gnutls: => 3.2.2
      nettle - do not install to /usr/lib64
      fuse: => 2.9.3
      odbcfb: => 2.0.2.153
      chrony: => 1.28
      alembic: => 0.6.0
      distribute: => 0.6.49
      setuptools: => 0.9.6
      deprecate python-pypi/distribute [replaced by setuptools]
      libusbx: => 1.0.16
      opencv: => 2.4.6.1
      hdf5: => 1.8.11
      freeglut: => 2.8.1
      glew: => 1.10.0
      molequeue-0.6.1
      avogadrolibs-0.6.0
      avogadroapp-0.6.0
      openbabel - depends EIGEN
      media-player-info: => 21
      pkgconfig: => 0.28
      libxml2 - fix build with python3
      udev - provides UDEV - prepare for future eudev
      udisks2 - depends UDEV
      upower - depends UDEV
      init.d - depends UDEV
      qtbase - change depends udev  -> UDEV
      libgphoto2 - change depends udev  -> UDEV
      qtsystems - change depends udev  -> UDEV
      xorg-server - change depends udev  -> UDEV
      xf86-video-intel - change depends udev  -> UDEV
      xf86-input-wacom - change depends udev  -> UDEV
      thunar - change depends udev  -> UDEV
      thunar-volman - change depends udev  -> UDEV
      colord - change depends udev  -> UDEV
      deprecate x11-toolkits/qt-embedded
      razor-qt - change depends udev  -> UDEV
      vlc - change depends udev  -> UDEV
      kino - change depends udev  -> UDEV
      guvcview - change depends udev  -> UDEV
      xen - change depends udev  -> UDEV
      pcmciautils - change depends udev  -> UDEV
      cdemu-daemon - change depends udev  -> UDEV
      spacefm - change depends udev  -> UDEV
      system-config-printer - change depends udev  -> UDEV
      network-manager - change depends udev  -> UDEV
      connman - change depends udev  -> UDEV
      libvirt - change depends udev  -> UDEV
      libdrm - change depends udev  -> UDEV
      drm - change depends udev  -> UDEV
      deprecate gnome2-libs/devicekit-power [replaced by upower]
      pulseaudio - change depends udev  -> UDEV
      libgpod - change depends udev  -> UDEV
      media-player-info - change depends udev  -> UDEV
      drbd - change depends udev  -> UDEV
      pcsc-lite - change depends udev  -> UDEV
      gparted - change depends udev  -> UDEV
      udisks - change depends udev  -> UDEV
      e17 - change depends udev  -> UDEV
      eeze - change depends udev  -> UDEV
      devicekit - change depends udev  -> UDEV
      gvfs - change depends udev  -> UDEV
      systemd - change depends udev  -> UDEV
      deprecate database/hk_classes
      deprecate database/xbase
      deprecate database/xbase64
      deprecate database/xbsql
      deprecate database/rekall
      upower: => 0.9.21
      alsa-utils: => 1.0.27.2
      automake: => 1.14
      eudev-v1.1     eudev is a fork of udev, which is independent of the init system     it builds and runs for me on two systems.     the only poroblem that I currently have is that /dev/pts is not created,     even though /etc/init.d/runlevels/%DEV/devices runs.
      virtuoso: => 6.1.7
      gnutls: => 3.2.3
      vlc: => 2.0.8
      util-linux: => 2.23.2
      bzr: => 2.6.0
      mercurial: => 2.7
      libvdpau: => 0.7
      tcpdump.gpg - add key D9C15D0D
      libpcap: => 1.4.0
      groff: => 1.22.2
      bison: => 3.0
      subversion-1.8.1 - SECURITY fix
      eudev: => v1.2
      tbb: => 41_20130613
      libburn: => 1.3.2
      libisofs: => 1.3.2
      libisoburn: => 1.3.2
      chrony-1.29  SECURITY fix
      qwt5: => 6.1.0
      deprecate x11-toolkits/qt-embedded
      qwtplot3d - use qt4_build
      muparser: => v2_2_3
      qtiplot: => 0.9.8.9
      qtoctave: => 0.10.1
      octave: => 3.6.4
      pugixml-1.2
      eigen3: => 3.1.4
      libdiscid: => 0.5.2
      tzdata: => 2013d
      eigen3: => 3.2
      deprecate kde4-apps/koffice2 [replaced by calligra]
      cups-filters: => 1.0.36
      setuptools: => 0.9.8
      ca-certificates: => 20130610
      vc: => 0.7.2
      eudev - added extra script to create amd mount /dev/pts if needed
      eudev - depends docbook-xsl
      git: => 1.8.4
      setuptools: => 1.1
      python-pypi/PY_DEPENDS = use setuptools
      udisks2: => 2.1.1
      gnutls: => 3.2.4
      ghostscript: => 9.10
      qtbase: => 5.1.1
      qtxmlpatterns: => 5.1.1
      qtjsbackend: => 5.1.1
      qtdeclarative: => 5.1.1
      qtscript: => 5.1.1
      qtsvg: => 5.1.1
      qttools: => 5.1.1
      qtimageformats: => 5.1.1
      qtgraphicaleffects: => 5.1.1
      qtmultimedia: => 5.1.1
      qtx11extras: => 5.1.1
      qtquick1: => 5.1.1
      qtquickcontrols: => 5.1.1
      qtwebkit5: => 5.1.1
      sqlite: => 3.8.0.2
      mercurial: => 2.7.1
      libusbx: => 1.0.17
      dbus: => 1.6.14
      dbd-firebird: => 1.12
      dbi: => 1.628
      re2c: => 0.13.6
      cups-filters: => 1.0.38
      setuptools: => 1.1.4
      libcap-ng: => 0.7.3
      boost - extra libaries
      setuptools: => 1.1.6
      clamav: => 0.98
      deprecate kernels/dazuko [replaced by unmaintained]
      deprecate kernels/dazukofs [replaced by unmaintained]
      dbd-firebird: => 1.15
      fb-python: => 0.7.3
      deprecate python-pypi/kinterbasdb [replaced by fdb]
      eudev: => v1.3
      QxOrm_1.2.5
      qxorm - add qt5 support
      FUNCTIONS - fix qt5_build
      parrot - 5.7.0/5.0.0
      man-pages: => 3.54
      byacc: => 20130925
      pyopenssl-0.13.1  - SECURITY fix
      vlc: => 2.1.0
      kmod: => 15
      mercurial: => 2.7.2
      cups-filters: => 1.0.39
      tzdata: => 2013g
      libdvbpsi: => 1.1.1
      setuptools - suppport simultaneous python2/3
      dbus: => 1.6.16
      make: => 4.0
      icu: => 52.1
      upower: => 0.9.22
      boost - fix build
      fontconfig: => 2.11.0
      pango: => 1.36.0
      librsvg2-1.39.0 - SECURITY FIX
      harfbuzz: => 0.9.22
      gtk+2: => 2.24.22
      iso-codes: => 3.47
      at-spi2-core: => 2.10.0
      glib2: => 2.38.0
      gdk-pixbuf2: => 2.30.0
      udisks2 - adjust depends
      gmp: => 5.1.3
      iw: => 3.11
      polarssl: => 1.3.1
      ca-certificates: => 20130906
      curl: => 7.33.0
      cython: => 0.19.2
      tbb: => 42_20130725
      json-c: => 0.11
      orc: => 0.4.18
      nspr: => 4.10.1
      nss: => 3.15.2
      gconf2 - update depends
      dhcpcd: => 6.1.0
      cups-filters: => 1.0.40
      upower: => 0.9.23
      sqlite: => 3.8.1
      cups: => 1.6.4
      libatasmart - depends UDEV
      cups: => 1.7.0
      gnutls-3.2.5 SECURITY fix
      sqlalchemy: => 0.8.3
      fb-python: => 0.7.4
      mercurial: => 2.8
      astyle: => 2.04
      six: => 1.4.1
      setuptools: => 1.1.7
      pyparsing: => 2.0.1
      dbus: => 1.6.18
      syslog-ng: => 3.4.5
      wine: => 1.7.6
      qbs-1.1.0
      python: => 2.7.6
      libdvbpsi: => 1.1.2
      dbi: => 1.630
      libraw: => 0.15.4
      opencv: => 2.4.7
      subversion-1.8.4 SECURITY fix
      setuptools: => 1.3.2
      cups-filters: => 1.0.41
      boost: => 1_55_0
      libssh: => 0.5.5
      util-linux: => 2.24
      fix builds involving python3.3
      pyopenssl - depends PYTHON
      pybindgen - depends PYTHON
      tempita - python3 support
      webob - python3 support
      babel - python3 support
      webhelpers - python3 support
      babel: => 1.3
      pyutil: => 1.9.7
      chardet - depends PYTHON
      numpy: => 1.8.0
      libxml2 - tweak build for python3
      setuptools: => 1.4.1
      FUNCTIONS - fix python2 usage
      xlwt: => 0.8.0
      gnutls: => 3.2.7
      ndiswrapper: => 1.59
      alembic: => 0.6.1
      quassel: => 0.9.2
      tbb: => 42_20131003
      libvpx: => 1.2.0
      gramps: => 3.4.6
      binutils: => 2.24
      dosfstools: => 3.0.24
      setuptools: => 1.4.2
      FUNCTIONS - fix typo
      dbd-firebird: => 1.16
      fb-python: => 0.8.0
      cups-filters: => 1.0.42
      mercurial: => 2.8.1
      sqlite: => 3.8.2
      molequeue: => 0.7.0
      avogadrolibs: => 0.7.0
      avogadroapp: => 0.7.0
      gpart: => 0.2.1
      fb-python: => 0.8.1
      sqlalchemy: => 0.8.4
      deprecate qt5/qt3d
      deprecate qt5/qtpim
      deprecate qt5/qtsystems
      deprecate qt5/qtjsbackend
      qtbase - CONFIGURE changes
      qtbase - update patch
      qtbase - fix CVE-2013-4549
      qtbase: => 5.2.0
      qtxmlpatterns: => 5.2.0
      qtdeclarative: => 5.2.0
      qtgraphicaleffects: => 5.2.0
      qtscript: => 5.2.0
      qtdeclarative - missing file
      qtsvg: => 5.2.0
      qtquickcontrols: => 5.2.0
      qtx11extras: => 5.2.0
      qtmultimedia: => 5.2.0
      qttools: => 5.2.0
      qtquick1: => 5.2.0
      qtgraphicaleffects - missing file
      qtimageformats: => 5.2.0
      qtwebkit5: => 5.2.0
      qtserialport-5.2.0
      qtlocation: => 5.2.0
      iw: => 3.13
      libnl: => 3.2.23
      enca: => 1.15
      libburn: => 1.3.4
      libisofs: => 1.3.4
      libisoburn: => 1.3.4
      virtuoso: => 6.1.8
      pypdf2: => 1.19
      pyfpdf - fix build with python3
      pcre: => 8.34
      libtasn1: => 3.4
      ruby-2.0.0-p353 - SECURITY fix
      tzdata: => 2013h
      libzip: => 0.11.2
      partclone: => 0.2.68
      fb-python: => 0.8.2
      pstoedit: => 3.62
      pstotext: => 1.9
      cimg: => 1.5.7
      xml-parser-expat: => 2.42_01
      lwp: => 6.05
      file-next: => 1.12
      html-parser: => 3.71
      http-message: => 6.06
      net-http: => 6.06
      curl-7.34.0 0 SECURITY fix
      gnutls: => 3.2.8
      tzdata: => 2013i
      setuptools: => 2.0.1
      molequeue: => 0.7.1
      avogadrolibs: => 0.7.2
      avogadroapp: => 0.7.2
      ruby-2.1-2.1.0
      tzdata - fix install
      oxygen-icons: => 4.12.0
      cups-filters: => 1.0.43
      raptor: => 2.0.12
      rasqal: => 0.9.31
      alembic: => 0.6.2
      iproute2: => 3.12.0
      swig: => 2.0.11
      redland: => 1.0.17
      libsigc++3: => 2.2.11
      glibmm: => 2.38.1
      atk: => 2.11.4
      sqlalchemy: => 0.9.0
      cracklib: => 2.9.1
      python-stdnum: => 0.9
      neon: => 0.30.0
      isort-3.0.0
      apr: => 1.5.0
      apr-util: => 1.5.3
      subversion-1.8.5 SECURITY FIX
      mercurial: => 2.8.2
      setuptools: => 2.0.2
      sqlacodegen: => 1.1.4
      partclone: => 0.2.69
      gdk-pixbuf2: => 2.30.2
      at-spi2-core: => 2.10.2
      isort: => 3.1.0
      sqlalchemy: => 0.9.1
      dhcpcd: => 6.2.0
      unifdef: => 2.10
      libofx: => 0.9.9
      libssh: => 0.6.0
      cups: => 1.7.1
      grep: => 2.16
      giflib: => 4.2.3
      itstool: => 2.0.2
      libgda5: => 5.2.2
      exiv2: => 0.24
      valknut - is qt4 only
      FUNCTIONS - remove some obsolete functions
      udisks2: => 2.1.2
      e2fsprogs: => 1.42.9
      clamav: => 0.98.1
      git: => 1.8.5.3
      dosfstools: => 3.0.25
      dhcpcd: => 6.2.1
      par2cmdline-tbb: => 0.4-tbb-20100203
      tbb: => 42_20131118
      wget: => 1.15
      libmpc: => 1.0.2
      libraw: => 0.16.0
      dhcpcd - IPv6/4 support
      partclone: => 0.2.70
      isort: => 3.1.2
      pango: => 1.36.1
      harfbuzz: => 0.9.25
      six: => 1.5.2
      dbus: => 1.8.0
      glib2: => 2.38.2
      vc: => 0.7.3
      cmake: => 2.8.12.2
      lm_sensors: => 3.3.5
      qxmledit-0.8.9
      create a group for kde5
      cups-filters: => 1.0.44
      qtwebkit5 - fix build with icu-51.1+
      deprecate libs/libusbx [replaced by libusb]
      pyxattr: => 0.7.3
      gnutls: => 3.2.9
      ack-2.13_06 - SECRITY fix
      isort: => 3.3.0
      libgphoto2: => 2.5.3
      psi: => 0.15
      cython: => 0.20
      setuptools: => 2.1
      mpfr$ - upstream patches
      jinja2-2.7.2 - SECURITY fix
      qxmledit: => 0.8.9.1
      jinja2 - fix typo - SECURITY fix
      opencv: => 2.4.8
      chrony-1.29.1 - SECURITY fix
      tea: => 37.1.0
      gdisk: => 0.8.8
      sqlalchemy: => 0.9.2
      alembic: => 0.6.3
      gnu-efi-3.0u
      gnu-efi - tweak
      qt-creator - add qt5 support
      qupzilla - add qt5 support
      libgcrypt-1.6.1 SECURITY fix
      qbs - move to devel section
      qbs: => 1.1.1
      fb-python: => 0.8.4
      gnu-efi - tweak build
      gummiboot-43
      gummiboot - SOURCE_IGNORE=volatile
      cln: => 1.3.3
      yaz: => 5.0.12
      tellico2: => 2.3.8
      delete obsolete kde3 stuff
      deprecate kde4/ksecrets
      deprecate kde4/kdeedu4
      deprecate kde4/kdemultimedia4
      deprecate kde4/kdegraphics4
      isort: => 3.4.1
      libatomic_ops: => 7.4.0
      deprecate http/qtwebkit [replaced by qt5/qtwebkit]     1. this spell is obsolete - upstrame now uses git     2. the checkout is enormous     3. the qt4 version is part of qt4     4. there is a separate qtwebkit available for qt5
      pyqt5-5.2
      sip: => 4.15.4
      dbus-glib: => 0.102
      Python-3.3.4 - SECURITY FIX
      Revert "pyqt5-5.2"     this spell belongs on qt5-kde5 grimoire
      syslog-ng: => 3.5.3
      fuzzyparsers: => 0.9.0
      sqlalchemy: => 0.9.3
      dbus-python: => 1.2.0
      isort: => 3.6.0
      cffi-0.8.1
      pycparser-2.10
      Revert "pyxattr: => 0.7.3"
      pyxattr: => 0.5.2
      pyqt4: => 4.10.3
      fb-python: => 0.9.0
      wine: => 1.7.13
      qxorm: => 1.2.6
      eigen3: => 3.2.1
      libdbusmenu-qt: => 0.9.2
      libevdev-1.0
      setuptools: => 2.2
      cups-filters: => 1.0.46
      ruby-2.1: => 2.1.1
      mercurial: => 2.9.1
      eudev: => v1.5
      adjust cmake install locations for lib and man
      libburn: => 1.3.6
      libisofs: => 1.3.6
      libisoburn: => 1.3.6
      extra-cmake-modules-0.0.11
      isort: => 3.6.2
      setuptools: => 3.1
      tzdata: => 2014a
      cups-filters: => 1.0.48
      udisks-2.1.3 - SECURITY fix
      sip: => 4.15.5
      fftw: => 3.3.4
      python3: => 3.4.0
      pyqt4: => 4.10.4
      pybindgen: => 0.17.0
      setuptools: => 3.3
      six: => 1.6.1
      cython: => 0.20.1
      pango: => 1.36.2
      gramps: => 3.4.7
      pbzip2: => 1.1.8
      libevdev: => 1.0.1
      libisoburn: => 1.3.6.pl01
      libdbusmenu-qt: => 0.9.3
      pugixml: => 1.4
      pngcrush: => 1.7.23
      dbd-firebird: => 1.18
      sqlite: => 3.8.4.1
      RBTools-0.5.7
      eudev: => 1.5.3
      hicolor-icon-theme: => 0.13
      move hicolor-icon-theme to desktop-themes
      move oxygen-icons to desktop-themes
      adjust oxygen-icons
      fontforge: => 20120731-b
      alembic: => 0.6.4
      sqlalchemy: => 0.9.4
      cups-filters: => 1.0.50
      gummiboot: => 44
      mercurial: => 2.9.2
      grep: => 2.18
      zlib: => 1.2.8
      icu: => 53.1
      pyicu: => 1.6
      setuptools: => 3.4.1
      pcre: => 8.35
      gnu.gpg : add D7E69871: Daiki Ueno
      gettext: => 0.18.3.2
      at-spi2-core: => 2.12.0
      libverto: => 0.2.6
      mc: => 4.8.12
      bogofilter: => 1.2.4
      leptonica: => 1.70
      bsddb3: => 6.0.1
      taglib: => 1.9.1
      flex: => 2.5.39
      desktop-file-utils: => 0.22
      docx2txt: => 1.3
      lcms2: => 2.6
      git: => 1.9.1
      ca-certificates: => 20140325
      cups-filters: => 1.0.52
      xmlto: => 0.0.26
      perl-error: => 0.17022
      libdvdread: => 4.2.1
      libdvdnav: => 4.2.1
      formencode: => 1.3.0a1
      dhcpcd: => 6.3.2
      syslog-ng: => 3.5.4.1
      byacc: => 20140409
      run-parts: => 4.4
      libcap: => 2.24
      gnu.gpg -add AE05B3E9: Patrick Alken
      gsl: => 1.16
      gdbm: => 1.11
      sdl2: => 2.0.3
      libvorbis: => 1.3.4
      tbb: => 42_20140122
      subversion-1.8.8 - SECURIT fix
      file: => 5.18
      readline: => 6.3
      unifont: => 6.3.20140214
      gawk: => 4.1.1
      scons: => 2.3.1
      serf: => 1.3.4
      cffi: => 0.8.2
      mesalib - conflicts mesalib-1x
      eflwebkit - depends mesalib
      webkitgtk - depends mesalib
      webkitgtk3 - depends mesalib
      libcaca - depends mesalib
      libs/libva - depends mesalib
      libs/openscenegraph - depends mesalib
      libs/sdl2 - depends mesalib
      x11-toolkits/fltk2 - depends mesalib
      x11-toolkits/wxgtk - depends mesalib
      x11/xlockmore - depends mesalib
      xorg-app/xdriinfo - depends mesalib
      xorg-xserver/xorg-server - depends mesalib
      xf86-video-ati - depends mesalib
      xf86-video-glint - depends mesalib
      xf86-video-intel - depends mesalib
      xf86-video-mga - depends mesalib
      xf86-video-openchrome - depends mesalib
      xf86-video-r128 - depends mesalib
      xf86-video-sis - depends mesalib
      xf86-video-tdfx - depends mesalib
      xf86-video-via - depends mesalib
      fb-python: => 0.9.3
      libdvbpsi: => 1.2.0
      deprecate kde4/kdebindings4 [replaced by kde4-bindings-profile]
      json-c-0.12 SECURITY fix
      eudev: => 1.6
      glib2: => 2.40.0
      guile: => 2.0.11
      glibmm: => 2.40.0
      harfbuzz: => 0.9.27
      librsvg2: => 2.40.2
      pango: => 1.36.3
      wine: => 1.7.17
      syslog-ng - more depends
      rsync: => 3.1.0
      gdisk: => 0.8.10
      libevdev: => 1.1
      cups-filters: => 1.0.53
      partclone - add FAT support
      wine: => 1.7.18
      setuptools: => 3.5
      alembic: => 0.6.5
      gummiboot - add a splash screen
      isort: => 3.8.0
      libgphoto2: => 2.5.4
      gummiboot - add config script
      dbus: => 1.8.2
      groups: add plasma
      libyaml: => 0.1.6
      ruby-2.1: => 2.1.2
      clamav: => 0.98.3
      extra-cmake-modules: => 0.0.13
      libevdev: => 1.2
      kmod: => 17
      gummiboot: => 45
      eudev - fix typo in build
      readline - tweak install
      docx2txt: => 1.4
      wine: => 1.7.19
      perl: => 5.18.2
      gutenprint: => 5.2.10
      libdrm - fix nouveau build
      libdrm: => 2.4.46
      libdrm: => 2.4.47
      libdrm: => 2.4.48
      libdrm: => 2.4.49
      libdrm: => 2.4.50
      libdrm: => 2.4.51
      libdrm: => 2.4.53
      libdrm: => 2.4.54
      pyxattr: => 0.5.3
      gnu-efi: => 3.0v
      setuptools: => 3.6
      util-linux: => 2.24.2
      grep: => 2.19
      shared-mime-info: => 1.3
      python3: => 3.4.1
      libevdev: => 1.2.1
      perl: => 5.20.0
      dnsmasq: => 2.71
      sip: => 4.16
      freeglut - dpends cleanup
      giflib - provides GIFLIB
      fontforge - depends GIFLIB
      leptonica - depends GIFLIB
      kdelibs4 - depends GIFLIB
      giflib5 - 5.0.6
      KDE_DEPENDS - dpends GIFLIB
      directfb - change depends giflib => GIFLIB
      fbv - change depends giflib => GIFLIB
      dvipng - change depends giflib => GIFLIB
      evas - change depends giflib => GIFLIB
      xplanet - change depends giflib => GIFLIB
      wine - change depends giflib => GIFLIB
      libafterimage - change depends giflib => GIFLIB
      wdm - change depends giflib => GIFLIB
      windowmaker - change depends giflib => GIFLIB
      afterstep - change depends giflib => GIFLIB
      mplayer2 - change depends giflib => GIFLIB
      mplayer - change depends giflib => GIFLIB
      anyrename - change depends giflib => GIFLIB
      gdal - change depends giflib => GIFLIB
      driftnet - change depends giflib => GIFLIB
      spamprobe - change depends giflib => GIFLIB
      tc2-modules - change depends giflib => GIFLIB
      sdl2_image - change depends giflib => GIFLIB
      openscenegraph - change depends giflib => GIFLIB
      libgdiplus - change depends giflib => GIFLIB
      kaffe - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      - change depends giflib => GIFLIB
      qxorm: => 1.2.7
      add sddm group & user
      gpgme: => 1.5.0
      tbb: => 42_20140416
      grep: => 2.20
      gettext: => 0.19
      bison: => 3.0.2
      libtasn1: => 3.6
      extra-cmake-modules: => 0.0.14
      ntfs-3g: => 2014.2.15
      eudev: => 1.7
      atk: => 2.12.0
      at-spi2-atk: => 2.12.1
      glib2 - allow install of gdbus-codegen
      gtk+3: => 3.12.2
      pulseaudio: => 5.0
      vlc: => 2.1.4
      mdnsresponder: => 544
      cups: => 1.7.3
      cups-filters: => 1.0.54
      xdg-utils: => 1.1.0-rc1
      sip: => 4.16.1
      mtdev: => 1.1.5
      setuptools: => 4.0.1
      gettext: => 0.19.1
      cmake: => 3.0.0
      harfbuzz: => 0.9.29
      dbus-1.8.4 SECURITY fix
      wine: => 1.7.20
      lzip: => 1.15
      ddrescue: => 1.18.1
      libusb: => 1.0.19
      alsa-lib: => 1.0.28
      alsa-utils: => 1.0.28
      dhcpcd: => 6.4.0
      qxorm: => 1.2.8
      groups - add input
      eudev: => 1.8
      python: => 2.7.7
      tzdata: => 2014e
      qxmledit: => 0.8.10
      iw: => 3.15
      tbb: => 42_20140601
      dbi: => 1.631
      setuptools: => 5.0.2
      fdb: => 1.4.1
      sqlalchemy: => 0.9.6
      setuptools: => 5.2
      openjpeg-1.5.2 - SECURITY fix+++
      gdk-pixbuf2: => 2.30.8
      finance-quote: => 1.35
      wine: => 1.7.21
      libburn: => 1.3.8
      libisofs: => 1.3.8
      libisoburn: => 1.3.8
      new spell -librevenge
      new spell -libodfgen
      libwpd: => 0.10.0
      libwps: => 0.3.0
      libwpg: => 0.3.0
      extra-cmake-modules: => 1.0.0
      unifont: => 7.0.03
      libvdpau: => 0.8
      serf: => 1.3.6
      wine: => 1.7.22
      partclone: => 0.2.71
      gettext: => 0.19.2
      policykit 0.112 SECURITY FIX
      git: => 2.0.2
      coreutils: => 8.23
      xlrd: => 0.9.3
      six: => 1.7.3
      cython: => 0.20.2
      rbtools: => 0.6.2
      setuptools: => 5.4
      cffi: => 0.8.6
      pango: => 1.36.5
      nss -  fix 3.16 patching
      cups: => 1.7.4  SECURITY fix
      sqlalchemy: => 0.9.7
      chardet: => 2.2.1
      jinja2: => 2.7.3
      gnutls: => 3.2.16
      libtasn1: => 4.0
      docutils: => 0.12
      wine: => 1.7.23
      libdrm: => 2.4.55
      python-pypi/meson-0.18.0 new spell
      libdrm: => 2.4.56
      dhcpcd: => 6.4.2
      harfbuzz: => 0.9.33
      tar: => 1.28
      gdb: => 7.8
      mercurial: => 3.1
      dhcpcd: => 6.4.3
      wine: => 1.7.24
      cmake: => 3.0.1
      extra-cmake-modules: => 1.1.0
      formalchemy: => 1.5.1
      boost: => 1_56_0
      krb5: => 1.12.1
      sip: => 4.16.2
      partclone: => 0.2.72
      gnupg-exp: => 2.0.26
      glib2: => 2.41.2
      gtk+3: => 3.13.6
      pypdf2: => 1.23
      scons: => 2.3.2
      libnl: => 3.2.25
      iproute2: => 3.16.0
      harfbuzz: => 0.9.35
      pango: => 1.36.6
      openssl - provides SSL
      openssl update UP_TRIGGERS
      chntpw: depends SSL
      cyrus-sasl: depends SSL
      encfs: depends SSL
      engine_pkcs11: depends SSL
      hydan: depends SSL
      libp11: depends SSL
      lsh: depends SSL
      mosh: depends SSL
      opensc: depends SSL
      openssh: depends SSL
      pad: depends SSL
      qca-openssl: depends SSL
      ssldump: depends SSL
      unhash: depends SSL
      xca: depends SSL
      xmlsec: depends SSL
      bacula: depends SSL
      burp: depends SSL
      dar: depends SSL
      dar22: depends SSL
      libarchive: depends SSL
      centerim: depends SSL
      ejabberd: depends SSL
      gajim: depends SSL
      jabberd: depends SSL
      licq: depends SSL
      profanity: depends SSL
      prosody: depends SSL
      psi: depends SSL
      qutecom: depends SSL
      qutim: depends SSL
      tmsnc: depends SSL
      vacuum: depends SSL
      hexchat: depends SSL
      ircd-ratbox: depends SSL
      irssi: depends SSL
      xchat: depends SSL
      xchat-gnome: depends SSL
      znc: depends SSL
      gloox: depends SSL
      libmsn: depends SSL
      libstrophe: depends SSL
      loudmouth: depends SSL
      ptlib: depends SSL
      pwlib: depends SSL
      tls: depends SSL
      openca: depends SSL
      openldap: depends SSL
      rapidsvn: depends SSL
      couchdb: depends SSL
      firebird: depends SSL
      firebird25: depends SSL
      libzdb: depends SSL
      mariadb: depends SSL
      mongodb: depends SSL
      mysql: depends SSL
      mysql-workbench: depends SSL
      pgadmin3: depends SSL
      postgresql: depends SSL
      virtuoso: depends SSL
      android-tools: depends SSL
      git: depends SSL
      polyorb: depends SSL
      pyside-tools: depends SSL
      python: depends SSL
      radare2: depends SSL
      swiprolog: depends SSL
      yaz: depends SSL
      qingy: depends SSL
      avfs: depends SSL
      boxbackup: depends SSL
      dmg2img: depends SSL
      dump: depends SSL
      libewf: depends SSL
      netatalk: depends SSL
      partimage: depends SSL
      testdisk: depends SSL
      uif2iso: depends SSL
      htmldoc: depends SSL
      ecore: depends SSL
      eet: depends SSL
      openoffice: depends SSL
      aria2: depends SSL
      btpd: depends SSL
      createtorrent: depends SSL
      ctorrent: depends SSL
      curl: depends SSL
      dctc: depends SSL
      deluge: depends SSL
      gftp: depends SSL
      lftp: depends SSL
      proftpd: depends SSL
      pure-ftpd: depends SSL
      tnftp: depends SSL
      transmission: depends SSL
      vsftpd: depends SSL
      wget: depends SSL
      dclib: depends SSL
      libtorrent: depends SSL
      rb-libtorrent: depends SSL
      balsa: depends SSL
      mail-notification: depends SSL
      evolution-webcal: depends SSL
      gnome-python2: depends SSL
      gnome-vfs2: depends SSL
      libgnomecups: depends SSL
      libgda5: depends SSL
      gnustep-base: depends SSL
      apache2: depends SSL
      apache22: depends SSL
      apache-mod_ssl: depends SSL
      cadaver: depends SSL
      cherokee: depends SSL
      dillo: depends SSL
      dillo2: depends SSL
      elinks: depends SSL
      elog: depends SSL
      esehttpd: depends SSL
      gnash: depends SSL
      httpd-dev: depends SSL
      lighttpd: depends SSL
      links: depends SSL
      links-twibright: depends SSL
      lynx: depends SSL
      middleman: depends SSL
      netsurf: depends SSL
      nginx: depends SSL
      pavuk: depends SSL
      serf: depends SSL
      siege: depends SSL
      squid: depends SSL
      w3c-libwww: depends SSL
      w3m: depends SSL
      webcleaner: depends SSL
      wt: depends SSL
      xshttpd: depends SSL
      icedtea7: depends SSL
      kdelibs4: depends SSL
      asio: depends SSL
      gwenhywfar: depends SSL
      gwenhywfar2: depends SSL
      ldns: depends SSL
      libchipcard: depends SSL
      libesmtp: depends SSL
      libevent: depends SSL
      libircclient: depends SSL
      mico: depends SSL
      neon: depends SSL
      omniorb: depends SSL
      omniorbpy: depends SSL
      poco: depends SSL
      podofo: depends SSL
      redland: depends SSL
      soup: depends SSL
      tc2-modules: depends SSL
      luacrypto: depends SSL
      luasec: depends SSL
      alpine: depends SSL
      althea: depends SSL
      anubis: depends SSL
      c-client: depends SSL
      claws-mail: depends SSL
      cone: depends SSL
      courier: depends SSL
      courier-imap: depends SSL
      cyrus-imapd: depends SSL
      dk-milter: depends SSL
      dovecot: depends SSL
      exim: depends SSL
      fetchmail: depends SSL
      gotmail: depends SSL
      imap: depends SSL
      isync: depends SSL
      libetpan: depends SSL
      mailx: depends SSL
      mpop: depends SSL
      msmtp: depends SSL
      mutt: depends SSL
      nbsmtp: depends SSL
      opendkim: depends SSL
      openwebmail: depends SSL
      postfix: depends SSL
      smtpc: depends SSL
      spamassassin: depends SSL
      ssmtp: depends SSL
      sylpheed: depends SSL
      sylpheed-gtk2: depends SSL
      barry: depends SSL
      xsupplicant: depends SSL
      accel-ppp: depends SSL
      bind: depends SSL
      bind-tools: depends SSL
      bitcoin: depends SSL
      envbot: depends SSL
      flow-tools: depends SSL
      freeradius: depends SSL
      fwbuilder: depends SSL
      ipsec-tools: depends SSL
      iscsitarget: depends SSL
      monit: depends SSL
      nagios-plugins: depends SSL
      netembryo: depends SSL
      net-snmp: depends SSL
      nsd: depends SSL
      ntop: depends SSL
      openntpd: depends SSL
      openvpn: depends SSL
      openwbem: depends SSL
      ppp: depends SSL
      pppd-chldap: depends SSL
      slowhttptest: depends SSL
      socat: depends SSL
      ssocks: depends SSL
      strongswan: depends SSL
      stunnel: depends SSL
      tcpdump: depends SSL
      tinc: depends SSL
      tor: depends SSL
      unbound: depends SSL
      vtun: depends SSL
      wvstreams: depends SSL
      crypt-ssleay: depends SSL
      net-ssleay: depends SSL
      parrot: depends SSL
      php: depends SSL
      php4: depends SSL
      php-dev: depends SSL
      cups: depends SSL
      cups-old: depends SSL
      gtklp: depends SSL
      hplip: depends SSL
      pt: depends SSL
      zint: depends SSL
      attic: depends SSL
      cherrypy: depends SSL
      m2crypto: depends SSL
      papyon: depends SSL
      pyicqt: depends SSL
      pymsn: depends SSL
      pymsnt: depends SSL
      pyopenssl: depends SSL
      python-ldap: depends SSL
      roundup: depends SSL
      scrapely: depends SSL
      scrapy: depends SSL
      twisted: depends SSL
      qtbase: depends SSL
      ruby-1.8: depends SSL
      ruby-1.9: depends SSL
      ruby-2.0: depends SSL
      ruby-2.1: depends SSL
      ruby-enterprise-edition: depends SSL
      boinc: depends SSL
      cern_root: depends SSL
      ettercap: depends SSL
      fingerprint: depends SSL
      hashkill: depends SSL
      nmap: depends SSL
      pam-imap: depends SSL
      pwsafe: depends SSL
      snort: depends SSL
      thc-hydra: depends SSL
      thc-pptp-bruter: depends SSL
      tpm-tools: depends SSL
      wireshark: depends SSL
      nessus-libraries: depends SSL
      opencryptoki: depends SSL
      openssl_tpm_engine: depends SSL
      trousers: depends SSL
      c3270: depends SSL
      freerdp: depends SSL
      rdesktop: depends SSL
      tn5250: depends SSL
      x3270: depends SSL
      asterisk: depends SSL
      decibel: depends SSL
      libexosip2: depends SSL
      libjingle-tapioca: depends SSL
      ortp: depends SSL
      sofia-sip: depends SSL
      telepathy-idle: depends SSL
      telepathy-qt: depends SSL
      deltup: depends SSL
      ghasher: depends SSL
      ipmitool: depends SSL
      mnogosearch: depends SSL
      ntp: depends SSL
      openipmi: depends SSL
      spice: depends SSL
      spice-gtk: depends SSL
      strigi: depends SSL
      syslog-ng: depends SSL
      uptimec: depends SSL
      xen: depends SSL
      ffmpeg: depends SSL
      gpac: depends SSL
      mpv: depends SSL
      mythtv: depends SSL
      tcvp: depends SSL
      xbmc: depends SSL
      gkrellm2: depends SSL
      x11vnc: depends SSL
      qt4: depends SSL
      sptk: depends SSL
      xorg-server: depends SSL
      libressl-2.0.5 new spell
      openss - check for libressl
      qt4 - fix ssl gflags
      libssh - fix build with libressl
      pulseaudio - openssl => SSL
      podofo: => 0.9.3
      cupos - fix SSL
      qtbase - fix SSL
      clamav: => 0.98.4
      python3 - depends SSL
      gpgme-1.5.1 - SECURITY fix
      krb5-1.12.2 SECURITY fix
      krb5 deepnds SSL
      setuptools: => 5.7
      cups-filters: => 1.0.58
      wine: => 1.7.25
      libevent - fix typo
      libarchive - fix typo
      glpk: => 4.55
      upower: => 0.99.1
      curl - support libressl
      wget - imporve libressl detection
      tweak ssl choices
      gutenprint - fix spurious dependencies
      mnogosearch: fix bad with-SSL usage
      openipmi: fix bad with-SSL usage
      bacula: fix bad with-SSL usage
      burp: fix bad with-SSL usage
      cyrus-sasl: fix bad with-SSL usage
      mysql: fix bad with-SSL usage
      postgresql: fix bad with-SSL usage
      aria2: fix bad with-SSL usage
      lftp: fix bad with-SSL usage
      polyorb: fix bad with-SSL usage
      elinks: fix bad with-SSL usage
      lighttpd: fix bad with-SSL usage
      links: fix bad with-SSL usage
      libesmtp: fix bad with-SSL usage
      omniorb: fix bad with-SSL usage
      omniorbpy: fix bad with-SSL usage
      anubis: fix bad with-SSL usage
      cyrus-imapd: fix bad with-SSL usage
      libetpan: fix bad with-SSL usage
      bind: fix bad with-SSL usage
      bind-tools: fix bad with-SSL usage
      flow-tools: fix bad with-SSL usage
      nagios-plugins: fix bad with-SSL usage
      netembryo: fix bad with-SSL usage
      wvstreams: fix bad with-SSL usage
      php: fix bad with-SSL usage
      php4: fix bad with-SSL usage
      php-dev: fix bad with-SSL usage
      nmap: fix bad with-SSL usage
      snort: fix bad with-SSL usage
      opencryptoki: fix bad with-SSL usage
      file: => 5.19
      deprecate collab/cola [replaced by git-cola]
      libgphoto2: => 2.5.5
      byacc: => 20140715
      tzdata: => 2014g
      qxmledit: => 0.8.11
      ghostscript: => 9.14
      cups-1.7.5 - SECURITY FIX
      eudev: => 1.10
      libunistring: => 0.9.4
      cups - also uses krb5
      linux-pam: => 1.1.8
      check: => 0.9.14
      kbd: => 2.0.2
      consolekit: => 0.4.6
      wine: => 1.7.26
      libtirpc: => 0.2.5
      linux-pam - depends libtirpc
      swig: => 3.0.2
      extra-cmake-modules: => 1.2.1
      dbus-1.8.8 - SECURITY FIX
      cmake: => 3.0.2
      sip: => 4.16.3
      move xdg-user-dirs to utils
      xdg-user-dirs: => 0.15
      python-pypi/grit-i18n added
      dhcpcd: => 6.4.5
      cups-filters: => 1.0.59
      gettext -icu is only needed if libxmls2 uses it
      wine: => 1.7.27
      libdrm: => 2.4.58
      ghostscript: => 9.15
      m4: => 1.4.17
      automake: => 1.14.1
      glib2: => 2.42.0
      pango: => 1.36.8
      librsvg2: => 2.40.4
      gstreamer-1.0: => 1.4.3
      gst-plugins-base-1.0: => 1.4.3
      gst-plugins-good-1.0: => 1.4.3
      gst-plugins-bad-1.0: => 1.4.3
      gst-libav-1.0: => 1.4.3
      icu: => 54.1
      cups: => 2.0.0
      gettext - fox typo
      make: => 4.1
      extra-cmake-modules: => 1.3.0
      dhcpcd: => 6.5.0
      sparsehash-2.0.2
      cups - tweak flags
      openssl - fix permissions on CONFLICTS
      cups-filters: => 1.0.60
      libressl: => 2.1.0
      partclone: => 0.2.73
      cups-filters - add depends + trigger
      libressl: => 2.1.1
      gettext: => 0.19.3
      wine: => 1.7.29
      icu - update sha512
      gdb: => 7.8.1
      eudev: => 2.1
      setuptools: => 7.0
      dhcpcd: => 6.6.0
      wine: => 1.7.30
      git: => 2.1.3
      librsvg2: => 2.40.5
      cups-filters: => 1.0.61
      libgphoto2: => 2.5.5.1
      extra-cmake-modules: => 1.4.0
      utils/dbus-qt - delete obsolete spell
      /gnupg-exp-  add conflics, provides
      gpgme - depends GNUPG
      mdp - depends GNUPG
      update GnuPG.gpg
      libgpg-error: => 1.17
      npth: => 1.1
      gnupg-exp - fix typo
      nes spell gnupg-2.1
      scute: => 1.4.0
      gnutls: => 3.2.19
      dbus-1.8.10 SECURITY FIX
      kmod: => 19
      mdnsresponder: => 561.1.1
      curl-7.39.0 SECURITY FIX
      cups: => 2.0.1
      gnutls 3.2.20 / 3.1.28 SECURITY fix
      pcre: => 8.36
      pcre -SECURITY FIX cve-2014-8964
      glib2: => 2.42.1
      harfbuzz: => 0.9.36
      ccache: => 3.2
      grep: => 2.21
      dbus: => 1.8.12
      ruby-2.1-2.1.5  SECURITY FIX
      flac: => 1.3.1
      sip: => 4.16.4
      odbcfb: => 2.0.3.154
      six: => 1.8.0
      alembic: => 0.7.0
      libtool: => 2.4.4
      v4l-utils: => 1.6.2
      extra-cmake-modules: => 1.5.0
      openssh - nolonger depends tcp_wrappers
      openldap - optional depends icu
      librsvg2: => 2.40.6
      openldap - fix typo
      lmdb-0.9.14 - new spell
      dhcpcd: => 6.6.5
      /libgit2-0.21.2 - new spell
      libgit2 - optional depends libssh2
      libgit2: => 0.21.3
      git-2.2.1 SECURITY FIX
      udisks2: => 2.1.4
      upower: => 0.99.2
      cmake: => 3.1.0
      libwebp: => 0.4.2
      libraw - extra depends
      dos2unix: => 7.1
      libpgf-6.14.12
      cimg: => 1.5.9
      binutils: => 2.25
      isort: => 3.9.3
      libaccounts-glib-1.16
      libpgf-6.14.12 missing files
      doxygen: => 1.8.9
      astyle: => 2.05.1
      sip: => 4.16.5
      libgphoto2: => 2.5.6
      qca2: => 2.1.0
      deprecate crypto/qca-gnupg [replaced by qca2]
      deprecate crypto/qca-openssl [replaced by qca2]
      deprecate crypto/qca-pkcs11 [replaced by qca2]
      gstreamer-1.0: => 1.4.5
      gst-plugins-base-1.0: => 1.4.5
      gst-plugins-good-1.0: => 1.4.5
      gst-plugins-bad-1.0: => 1.4.5
      gst-plugins-ugly-1.0: => 1.4.5
      gst-libav-1.0: => 1.4.5
      boost: => 1_57_0
      krb5-1.13 SECURITY fix
      e2fsprogs: => 1.42.12
      util-linux: => 2.25.2
      ruby-2.2.0
      ruby-2.1 - conflicts ruby-2.2
      ruby-2.0 - conflicts ruby-2.2
      ruby-1.9 - conflicts ruby-2.2
      ruby-1.8 - conflicts ruby-2.2
      libndp-1.4
      dnsmasq: => 2.72
      dhcpcd: => 6.6.7
      network-manager: => 1.0.0
      partclone: => 0.2.75
      newt: => 0.52.18
      network-manager - fix typos, depends wpa_supplicant
      harfbuzz: => 0.9.37
      librevenge: => 0.0.2
      libodfgen: => 0.1.3
      at-spi2-core: => 2.14.1
      at-spi2-atk: => 2.14.1
      gtk+3: => 3.14.6
      libffi: => 3.2.1
      update kernel.gpg
      bluez5-5.27
      cups-filters: => 1.0.62
      libssh: => 0.6.4
      alembic: => 0.7.4
      libgit2: => 0.22.0
      pyparsing: => 2.0.3
      python-stdnum: => 1.0
      six: => 1.9.0
      setuptools: => 9.1
      libdrm: => 2.4.59
      cmake: => 3.1.1
      orc: => 0.4.23
      dhcpcd: => 6.7.1
      harfbuzz: => 0.9.38
      yaml-cpp: => 0.5.1
      yaml-cpp - build shared library
      clamav: => 0.98.6
      ccache: => 3.2.1
      gnutls: => 3.3.12
      perl: => 5.20.1
      rbtools: => 0.7
      parted: => 3.2
      cln: => 1.3.4
      wine: => 1.7.36

Vlad Glagolev (1592):
      ipset: => 6.12.1
      shntool: => 3.0.10
      taglib: => 1.7.2
      fftw: => 3.3.2
      tdb: => 1.2.10
      python-gnupg: => 0.3.0
      pytz: => 2012c
      werkzeug: => 0.8.3
      dbus-python: => 1.1.0
      django: => 1.4
      python-ssh: => 1.7.14
      fabric: => 1.4.2
      sorcery-pubkeys: => 1.6.6
      metalog: removed p7zip
      gettext: force included version of glib2
      gettext: added forgotten HISTORY entry
      gettext: corrected typo
      Revert "udev: fixed #357 (missing glib2 dep)"
      elvis: pre-release update     (cherry picked from commit 879916ce5631139c9ab637d56ac221bf161880a1)
      basesystem: => 0.9.5
      mdadm: temporarily switched back to hash-checking
      module-init-tools: fixed primary mirror
      castfs: fixed static linking against >=2.9.0 fuse
      libmpc: trigger recast to fix the extra-portability bug     (cherry picked from commit fe49f25349d2511a7f4ce0d930ab8cec1a7b5bee)
      elinks: enable verbose build mode
      elvis: corrected X dep and crashing under Fluxbox and friends
      volatiles: added /usr/share/locale/locale.alias database
      util-linux: properly handle /etc/inittab upgrade
      vifm: added missing deps
      libarchive: fixed dependencies: _all_ of them are optional; added missing
      sqlite: => 3.7.12
      Revert "fuse: => 2.9.0"
      e2fsprogs: => 1.42.3
      castfs: recast statically-linked version on fuse update
      timwaugh.gpg: moved from printer section, required by patchutils
      patchutils: => 0.3.2
      Revert "Revert "fuse: => 2.9.0""
      fuse: temporary solution for #393
      lynx: added missing options
      excluded, volatiles: renewed files
      nfs-utils: added /var/lib/nfs/xtab to volatiles
      hplip: added volatiles
      man: fixed cleanse check
      nfs-utils: actually incremented PATCHLEVEL
      sysstat: => 10.0.5
      socat: => 1.7.2.1 (security)
      util-linux: autofix /etc/inittab only on successful installation of new util-linux version
      util-linux: POST_INSTALL -> FINAL
      neon.gpg: moved from neon spell, required by cadaver
      cadaver: new spell, command-line WebDAV client for Unix
      transmission: => 2.52
      ldns: => 1.6.13
      sqlite: => 3.7.12.1
      glib-networking: added TLS subdependency
      libsoup: requires glib-networking built with TLS support
      Revert "libffi: => 3.0.11"
      uget: => 1.8.2
      neon: refreshed spell
      cadaver: use DAV subdependency from neon
      neon: don't ask twice when subdep is triggered
      davfs: renewed dependencies
      cadaver: ssl & xml options depend on bundled version of neon library
      gvfs: corrected dependency for HTTP/FTP support
      sudo: => 1.8.5p1 (security)
      libxml2: => 2.8.0
      xchat: fixed compilation with static spelling support
      net/tor.gpg: added 19F78451 public key (Roger Dingledine <arma@mit.edu>)
      tor: => 0.2.2.36 (security)
      conky: => 1.9.0
      libproxy: added missing opt deps
      ruby-1.8: => 1.8.7-p358 (security)
      xml-parser-expat: => 2.41
      Revert "gnome2-libs/intltool: added dependency on xml-parser"
      xml-parser: deprecated duplicate spell
      xml-parser-expat: conflicts with duplicate spell
      bins: corrected required dependencies
      volatiles: esc dots
      libxfce4util: properly handle upgrade process
      xfce4-panel: fixed the trigger
      orage: added missing dep
      xfce4-mixer: added missing dep
      xfce4-dict: added missing dep
      orage: PATCHLEVEL=1
      xfce4-mixer: PATCHLEVEL=1
      xfce4-dict: PATCHLEVEL=1
      pycrypto: => 2.6 (security)
      pymongo: new spell, Python driver for MongoDB
      fping: => 3.2
      lighttpd: => 1.4.31
      iasl: => 20120518
      busybox: => 1.19.4
      php: security update for legacy branch (with backported patches) to 20120526
      sudo: => 1.8.5p2
      gdisk: => 0.8.5
      mercurial: => 2.2.2
      libpcap: fixed libnl support
      sqlalchemy: => 0.7.7, fixed dep flags
      postgresql: => 9.1.4 (security)
      linux: => 3.0.33 (lts)
      linux: => 3.2.19 (lts)
      linux: => 3.3.8 (lts)
      linux: => 3.1.10 (eol)
      bison: => 2.5.1
      inotify-cxx: new spell, inotify C++ interface
      incron: new spell, inotify cron system
      python-ldap: => 2.4.10
      libevent: corrected UP_TRIGGERS
      openssl: fixed UP_TRIGGERS
      mariadb: => 5.2.12 (security)
      linux: => 3.0.34 (lts)
      xine-lib: => 1.2.2
      xine-ui: => 0.99.7
      ffmpeg: => 0.7.13 (legacy)
      seamonkey: => 2.10 (+security)
      guvcview: fixed infinite loop by adding flags for optional dependencies during the configure stage
      sqlite: => 3.7.13
      tor: => 0.2.2.37
      pciutils: renewed hash sum, diff returns nothing between contents of old and new tarballs
      libmpc: recast on mpfr upgrade/downgrade
      Revert "grep: => 2.12"
      Revert "grep 2.11"
      smgl-archspecs: => 0.8.3
      Revert "Spell Update: mdadm 3.1.5 -> 3.2.1"
      Revert "pciutils: renewed hash sum, diff returns nothing between contents of old and new tarballs"
      pciutils: switched to upstream pgp checking
      pciutils: removed forgotten hash sum
      libmpc: fixed build failure if automake less than 1.12 is found. this is required if you need to compile the basic toolchain first (for example after changing archspecs)
      lua: => 5.2.1
      pyasn1: => 0.1.3
      rsa: => 3.1
      sqlalchemy: => 0.7.8
      seamonkey: => 2.10.1
      linux: => 3.0.35 (lts)
      rsa: => 3.1.1
      geany: => 1.22
      geany-plugins: => 0.21.1
      ne: => 2.4
      ipmitool: added dependencies and other options
      klavaro: => 1.9.5
      openldap: refactured the spell
      linux: => 3.0.36 (lts)
      vifm: => 0.7.3a
      ffmpeg: => 0.11.1 (stable)
      guvcview: fixed build with kernels < 3.0 and glibc without sanitize headers
      Revert "Spell Update: feh - Dependency Added"
      links-twibright: => 2.7
      pv: => 1.3.1
      mesalib: fixed GLU[T] mess
      tiff: added libtiff.so.4 symlink for skype compat and corrected GL optional dependency
      mesalib: incremented PATCHLEVEL
      sylpheed: => 3.2.0
      arping: => 2.12
      mercurial: => 2.2.3
      nginx: added support for http_realip_module
      wol: new spell, Wake On LAN client
      libnl: => 3.2.11
      wicd: fixed setting keys for secured networks
      mpfr: fixed previous update that brakes a compiler
      dhcp: => 4.2.4
      hostapd: new spell, IEEE 802.11 AP, IEEE 802.1X/WPA/WPA2/EAP/RADIUS Authenticator
      samba: libcap becomes optional
      avfs: => 1.0.1
      samba: added more optional deps
      slim: => 1.3.4
      geany-plugins: => 1.22
      pv: => 1.3.4
      linux => 3.0.37 (lts), 3.2.23 (lts)
      isomaster: => 1.3.9
      dialog: => 1.1-20120706
      iasl: => 20120711
      python-mpd: => 0.4.3
      nsd: => 3.2.12 (security)
      xxkb: added missing imake dependency
      cairo: added glib2 subdependency
      gtk+3: fixed compilation when cairo had been installed earlier than glib2
      gtk-chtheme: fixed build with gtk+2 >= 2.24
      rdesktop: dropped broken libvncserver dependency
      bind-tools: => 9.9.1-P2 (security)
      xfburn: fixed build with recent glib2
      x11vnc: added required libxtst dependency
      linux: => 3.0.38 (lts)
      audacious-plugins: fixed broken AAC dependency
      audacious: added missing gtk+3 dependency
      audacious-plugins: fixed broken MP3 dependency
      fop: fixed source url
      dia: use system docbook-xsl instead of online to generate man pages
      nsd: => 3.2.13 (security)
      davfs: => 1.4.7
      samba: fixed longer starting/stopping (don't resolve numeric IPs and ports)
      dhcp: => 4.2.4-P1 (security)
      ristretto: => 0.6.2
      proftpd: refreshed the spell
      proftpd: redefine localstatedir to /var/run
      proftpd: corrected stop() in init script
      lxml: => 2.3.5
      lzo: build shared library
      tinc: => 1.0.19
      proftpd: => 1.3.4b
      Revert "dhcpcd: => 5.6.1"
      cups-filters: fixed build when poppler doesn't conform required options
      ferm: => 2.1.1
      samba: fixed build with cups 1.6
      fuse: => 2.9.1
      castfs: fixed TRIGGERS
      castfs: fixes crashing when running without arguments, see #395
      hplip: fixed build with cups 1.6
      openntpd: applied a patch to fix time sync on modern systems
      libxml2: security update (CVE-2012-2807)
      linux: => 3.4.8 (lts), 3.2.26 (lts), 3.0.40 (lts)
      xen: => 4.1.3 (security)
      ccache: => 3.1.8
      libyaml: moved to libs section; new spell, YAML parser and emitter written in C
      ruby-1.9: added optional depends on libyaml
      passenger: => 3.0.15
      tor: => 0.2.2.38 (security)
      tor: fixed typo in 2nd source_url
      ristretto: => 0.6.3
      linux: => 3.0.41 (lts), 3.4.9 (lts)
      openntpd: actually regenerate configure script after patching
      postgresql: => 9.1.5 (security)
      rp-pppoe: => 3.11
      xvid: actually install the symlink
      qemu: => 1.1.1-1
      gtklp: => 1.2.9
      fping: => 3.3
      cciss_vol_status: => 1.10
      memcached: => 1.4.14
      nginx: added support for http_dav_module
      nginx: added support for dav_ext module
      nasm: => 2.10.04
      php: updated backports+security patches to 20120808 for legacy (5.2) branch
      django: => 1.4.1 (security)
      valgrind: => 3.8.0
      mupdf: => 1.1
      mhwaveedit: => 1.4.22
      net-snmp: prevent linking with itself (old libs) on update
      evince: added runtime depends on gsettings-desktop-schemas
      php: updated backports+security patches to 20120826 for legacy (5.2) branch
      linux: => 3.0.42 (lts), 3.2.28 (lts), 3.4.10 (lts)
      nbd: new spell, Network Block Device (TCP version) userland
      tdb: added special options for compiling
      farstream: added missing dependencies
      gajim: => 0.15.1
      farstream: requires libnice
      gajim: added required dependencies for audio/video support
      lua: dynamically link liblua.so with libdl.so
      taskwarrior: => 2.1.1
      xml-sax-base: fixed migration xml-sax -> xml-sax-base+xml-sax
      tiff2png: new spell, TIFF to PNG converter
      sqlite: => 3.7.14
      fping: => 3.4
      less: => 451
      uget: => 1.10
      fwknop: => 2.0.3 (security)
      fwknop: fixed a bug for command type access message (introduced in 2.0.1)
      fontconfig: => 2.10.1
      memcached: => 1.4.15
      mercurial: => 2.3.1
      fribidi: => 0.19.4
      masqmail: corrected default config installation
      sphinx: => 2.0.5
      tor: => 0.2.2.39 (security)
      freeradius: => 2.2.0 (security)
      dhcp: => 4.2.4-P2 (security)
      bind-tools: => 9.9.1-P3 (security)
      bind: => 9.8.3-P3 (security)
      optipng: => 0.7.2
      sudo: => 1.8.6p1
      pkgconfig: => 0.27.1
      nasm: => 2.10.05
      optipng: => 0.7.3 (security)
      sudo: => 1.8.6p2
      seamonkey: => 2.12.1
      xorg-server: => 1.8.2 (NOTE: goes only for master branch)
      sudo: => 1.8.6p3
      xen: fixed XSA-19 (CVE-2012-4411)
      taskwarrior: => 2.1.2
      apache22: => 2.2.23 (security)
      exim: fixed urls, dropped outdated & broken
      transmission: => 2.71
      postgresql: => 9.2.1
      libxslt: => 1.1.27 (security)
      linux: => 3.5.5 (lts)
      linux: => 3.4.12 (lts)
      linux: => 3.2.30 (lts)
      linux: => 3.0.44 (lts)
      php: updated backports+security patches to 20120924 (legacy branch)
      php: fixed build with ext. pcre >=8.30 (legacy)
      gcc: fixed build with glibc 2.16
      nss-pam-ldapd: => 0.7.17
      freeradius: don't conflict with system libtool
      sqlite: => 3.7.14.1
      neon: fixed file names with spaces (http://savannah.nongnu.org/support/?107114)
      libevent: => 2.0.20
      nfs-utils: fixed client automounting for NFSv3
      util-linux: prevent triggerring from other spells for migrating process
      gettext: fixed build with glibc 2.16
      weechat: added missing required dependency
      tinyproxy: fixed install with automake 1.12
      linux: => 3.5.6 (lts)
      linux: => 3.4.13 (lts)
      linux: => 3.0.45 (lts)
      uget: => 1.10.2
      bind-tools: => 9.9.1-P4 (security)
      hostapd: fixed CVE-2012-4445 (security)
      linux: => 3.2.31 (eol)
      ruby-1.9: => 1.9.3-p286 (security)
      linux: => 3.0.46 (lts)
      linux: => 3.4.14 (lts)
      linux: => 3.5.7 (lts)
      mercurial: => 2.3.2
      metalog: => 3
      seamonkey: => 2.13.1 (security)
      hatta: => 1.5.1
      util-linux: removed senseless 2nd version check
      lxml: => 3.0.1
      seamonkey: added check for nspr <4.9.2
      seamonkey: added check for sqlite <3.7.13
      seamonkey: added check for nss <3.13.5
      elvis: corrected symlink check
      vifm: => 0.7.4
      vifm: => 0.7.4a
      linux: => 3.6.4
      linux: => 3.4.16 (lts)
      linux: => 3.2.32 (lts)
      linux: => 3.0.49 (lts)
      linux: => 3.6.5 (stable)
      linux: => 3.4.17 (lts)
      linux: => 3.2.33 (lts)
      linux: => 3.0.50 (lts)
      rubygems: => 1.8.24
      hatta: => 1.5.3
      gajim: => 0.15.2
      pytz: => 2012h
      transmission: => 2.73
      galculator: => 2.0
      seamonkey: fixed segfault for corei7-avx archspecs
      dconf: corrected dependencies
      libjpeg-turbo: added support for yasm selection
      itstool: => 1.2.0
      evince: renew dependency list
      tmux: => 1.7
      ncdc: new spell, NCurses Direct Connect client
      unico: fixed crashing on newer GTK+3
      bbswitch: new spell, kernel module to power on/off GPUs in laptops with Optimus technology
      virtualgl: new spell, OpenGL proxy with full 3D hardware acceleration
      groups: added bumblebee group required for bumblebee spell
      bumblebee: new spell, project aiming to support NVIDIA Optimus technology under Linux
      linux: => 3.4.18 (lts)
      linux: => 3.0.51 (lts)
      redis-py: new spell, Python interface to the Redis key-value store
      optipng: => 0.7.4 (security)
      redis: => 2.6.3
      sylpheed: => 3.3.0
      weechat: => 0.3.9.1 (security)
      ruby-1.9: => 1.9.3-p327 (security)
      ca-certificates: => 20121105
      nsd: => 3.2.14
      smem: => 1.2
      linux: => 3.2.34 (lts)
      roundup: => 1.4.20 (security)
      libproxy: security update
      tiff: fixed CVE-2012-4564 (security)
      xen: security update
      exim: => 4.80.1 (security)
      mailx: added missing openssl dependency
      mailx: fixed multijob build
      bbswitch: recast spell on kernel update
      masqmail: corrected permissions for maildir
      gajim: pyasn1 is required for ssl support
      chrony: fixed build without IPv6 support
      lighttpd: => 1.4.32 (security)
      loop-aes: => 3.6f
      xxkb: fixed crash in some cases (see https://bugs.gentoo.org/show_bug.cgi?id=407127)
      php: updated backports+security patches to 20121114 (legacy)
      linux: => 3.4.19 (lts)
      linux: => 3.0.52 (lts)
      weechat: => 0.3.9.2 (security)
      redis: => 2.6.5
      seamonkey: => 2.14 (security)     (cherry picked from commit c409ec226afd8a9a9eb9ed2c18cc7659c52946c6)
      gvfs: => 1.14.2
      exo: => 0.9.1
      thunar: => 1.5.2 (1.4 crashes with newer gvfs)
      libsecret: corrected dependency tree
      gnome-disk-utility: => 3.6.1
      udisks2: corrected email addr in HISTORY
      udisks2: fixed build with older kernel headers
      cronie: => 1.4.9
      sox: apply ffmpeg 0.11 patch only for ffmpeg >=0.11
      copper: new spell, experimental programming language
      code-browser: => 4.5
      libopenraw: added GNOME subdependency
      tumbler: new spell, image thumbnailer service
      ristretto: added tumbler suggest dep
      loop-aes: => 3.6g
      libqrencode: new spell, QR Code encoding library
      mksh: => R41
      seamonkey: => 2.14.1
      xine-lib: added internal and optional dependencies
      xine-lib: added optipng suggest dependency
      glibc: use 2.6.39 kernel headers instead of 2.6.39.4 due to removed upstream sources
      linux: => 3.0.53 (lts)
      linux: => 3.4.20 (lts)
      exo: => 0.10.0
      thunar: => 1.6.0
      mariadb: => 5.2.13 (security)
      redis: => 2.6.7
      gdb: => 7.5.1
      net-snmp: => 5.7.2
      smartmontools: => 6.0
      mpd: => 0.17.2
      xcache: => 3.0.0
      ccrypt: => 1.10
      libsecret: => 0.11
      samba: => 3.6.9
      dssi: added HOST subdependency
      amsynth: => 1.3.2
      postgresql: => 9.2.2
      linux: => 3.0.55 (lts)
      linux: => 3.2.35 (lts)
      linux: => 3.4.22 (lts)
      xen: security update
      xen: SECURITY_PATCH++ for real
      xen: security update
      tor: => 0.2.3.25 (security)
      bind: => 9.8.4-P1 (security)
      bind-tools: => 9.9.2-P1 (security)
      m4: fixed build with glibc >=2.15
      tar: fixed build with glibc >=2.15
      diffutils: fixed build with glibc >=2.15
      pcre: readded libpcre.so.0 symlink
      pcre: added forgotten file
      pv: => 1.4.0
      dhcpcd: => 5.6.4
      talloc: => 2.0.8
      tdb: => 1.2.11
      libsecret: => 0.12
      xlockmore: => 5.41
      libevent: => 2.0.21
      hostapd: => 1.1
      msmtp: => 1.4.30
      msmtp: added sendmail symlinks
      masqmail: added msmtp to conflicts
      sendmail: added msmtp to conflicts
      postfix: added msmtp, esmtp, courier to conflicts
      esmtp: added msmtp to conflicts
      courier: added msmtp to conflicts
      exim: added msmtp to conflicts
      xen: added gnutls optional dependency
      fwknop: => 2.0.4
      xen: corrected detection of running domUs after instant poweroff/reboot
      tdb: added FTP mirror
      sqlite: => 3.7.15
      transmission: => 2.74
      nss-pam-ldapd: => 0.7.18
      xfsprogs: => 3.1.10
      dmapi: => 2.2.12
      xfsdump: => 3.1.2
      galculator: => 2.0.1
      transmission: => 2.75
      sqlite: => 3.7.15.1
      man-pages: => 3.45
      freetype2: => 2.4.11
      iasl: => 20121220
      lxml: => 3.0.2
      ferm: => 2.1.2
      xen: => 4.1.4
      linux: => 3.0.57 (lts)
      linux: => 3.4.24 (lts)
      linux: => 3.6.11 (eol)
      exo: => 0.10.1
      tumbler: => 0.1.26
      gtk-xfce-engine: => 3.0.1
      thunar: => 1.6.1
      Revert "editors/nano: version 2.3.1"
      Revert "libs/libffi: version 3.0.11"
      iptables: => 1.4.17
      ruby-1.9: => 1.9.3-p362
      Revert "crypto/openssl: version 1.0.1c"
      Revert "devel/python: add dependencies on gettext, libx11 and tcl"
      Revert "devel/python3: add dependencies on gettext, libx11, openssl and tcl"
      Revert "ruby-raa/ruby-1.9: add dependencies on libffi, libx11, tcl"
      arping: => 2.13
      Revert "devel/python: add dependencies on gettext, libx11 and tcl"
      Revert "devel/python3: add dependencies on gettext, libx11, openssl and tcl"
      Revert "ruby-raa/ruby-1.9: add dependencies on libffi, libx11, tcl"
      arping: => 2.13
      fluxbox: => 1.3.3
      fluxbox: fixed fribidi detection, when built with glib support
      exo: => 0.10.2
      thunar: => 1.6.2
      fribidi: => 0.19.5
      Revert "devel/llvm: make dependency on libffi optional"
      Revert "devel/llvm: add dependency on libffi"
      libgnome-keyring: fixed "DEPENDS: line 13: syntax error: unexpected end of file"
      gnome-vfs2: attr and acl are optional, see configure script
      gnome-vfs2: handle dependencies for auto-linking rules in configure
      mousepad: => 0.3.0
      wpa_supplicant: fixed build for 1.1
      ircd-ratbox: => 3.0.8 (stable)
      slim: => 1.3.5
      kbd: fixed regression that breaks keymap loading
      pyasn1: => 0.1.5
      pytz: => 2012j
      bpython: => 0.12
      soundtouch: => 1.7.1
      file: => 5.12
      file: include static version of library
      mercurial: => 2.4.2
      cryptcat: new spell, standard netcat enhanced with twofish encryption
      netcat: conflicts cryptcat
      nc: conflicts cryptcat
      pyasn1: => 0.1.6
      mpd: => 0.17.3
      harfbuzz: => 0.9.10
      fabric: => 1.4.4
      python-ssh: => 1.8.0
      paramiko: => 1.9.0
      fabric: => 1.5.1
      dhcpcd: => 5.6.6
      Revert "fluxbox: fixed fribidi detection, when built with glib support"
      Revert "fluxbox: => 1.3.3"
      pango: => 1.32.5
      drbd: added kernel 3.5-3.7 support
      transmission: => 2.76
      seamonkey: => 2.15 (security)
      linux: => 3.2.36 (lts)
      sqlite: => 3.7.15.2
      dhcp: => 3.2.5
      dhcp: => 4.2.5
      httplib2: => 0.7.4
      mongo: => 1.2.12
      python-mpd: => 0.5.0
      tumbler: => 0.1.27
      xcache: => 3.0.1
      nss: corrected message about 3.14 branch
      sudo: => 1.8.6p4
      dnspython: => 1.10.0
      pyasn1-modules: new spell, collection of ASN.1-based protocols modules
      sleekxmpp: new spell, elegant Python library for XMPP
      loudmouth: => 1.5.0-20121201
      mcabber: => 0.10.2
      linux: => 3.0.58 (lts)
      linux: => 3.2.37 (lts)
      linux: => 3.4.25 (lts)
      ruby-1.9: => 1.9.3-p374
      python-gnupg: => 0.3.2
      burp: new spell, network backup and restore program
      added account data for burp
      thunderbird: SECURITY_PATCH++
      gtkam: => 0.2.0
      burp: corrected PID file path
      distribute: => 0.6.34
      virtualenv: new spell, Virtual Python Environment builder
      httplib2: => 0.7.7
      celery: new spell, Distributed Task Queue
      memcache: => 3.0.7
      python-gflags: new spell, commandline flags module for Python
      gflags: new spell, commandline flags module for C++
      libdbi-drivers: updated spell with new options and docs
      boost: => 1_52_0
      libdbi: updated spell with new options and docs
      greylist: new spell, greylist policy service for postfix
      openldap: => 2.4.33
      postfix: => 2.9.5
      Revert "boost: => 1_52_0"
      postfix: it was a security update
      postfix: made pcre support optional
      seamonkey: => 2.15.1
      file: updated hash for reuploaded tarball by upstream (resolves #499)
      dia: fixed build with recent gettext
      Revert "dia: fixed build with recent gettext"
      Revert "gettext: => 0.18.2"
      vifm: => 0.7.4b
      di: => 4.34
      weechat: => 0.4.0 (stable)
      ca-certificates: => 20130119
      samba: => 3.6.11
      drbd: recast on linux update only when kernel module is enabled
      sudo: => 1.8.6p5
      cairo: => 1.12.10
      ocfs2-tools: added scm and 1.8 branches
      uget: => 1.10.3
      greylist: corrected license array
      greylstd: new spell, simple SQLite-based greylisting daemon
      cpio: fixed build with glibc=>2.15
      django: => 1.4.3 (security)
      ircd-ratbox: this was a security update
      dosfstools: => 3.0.14
      redis: => 2.6.9 (security)
      mysql: => 5.1.66 (security)
      dovecot: => 2.0.21 (security)
      xen: security update
      linux: => 3.0.61 (lts)
      linux: => 3.4.28 (lts)
      code-browser: => 4.6
      mpt-status: new spell, tool to get RAID status out of mpt (and other) HW RAID controllers
      burp: => 1.3.24 (devel)
      mariadb: => 5.2.14 (security)
      mysql: => 5.1.67 (security)
      mysql: => 5.0.96 (old) (security)
      klavaro: => 1.9.6
      cairo: => 1.12.12
      pngquant: new spell, utility for converting 24/32-bit PNG images to 8-bit PNGs
      pngquant: disabled slow debug version
      chrony: => 1.27
      samba: fixed conflicts with tdb and talloc
      tdb: fixed conflict with samba's internal lib
      talloc: fixed conflict with samba's internal lib
      samba: handle conflicts more precisely
      trac: => 0.12.5
      samba: => 3.6.12 (security)
      postfix: => 2.9.6
      ne: => 2.5
      slowhttptest: => 1.5
      fabric: => 1.5.3
      ruby-1.9: => 1.9.3-p385 (security)
      sqlobject: => 1.3.2
      seamonkey: => 2.15.2
      audiofile: => 0.3.5
      ssocks: new spell, RFC-compilant socks5 server and client
      audiofile: added forgotten sig
      gcc: fixed build with go compiler enabled
      postgresql: => 9.2.3 (security)
      git: => 1.8.1.2
      orage: => 4.8.4
      nsd: => 3.2.15
      bluefish: => 2.2.4
      mariadb: added 5.3 branch
      mercurial: => 2.5.1
      dhcpcd: => 5.6.7
      gdisk: => 0.8.6
      gtkglext: added missing dependencies
      git: => 1.8.1.3
      glib2: fixed circular dependency with gamin
      apr: marked previous update a security one
      apache22: fixed requirement of LDAP subdependency in apr-util
      v4l-utils: fixed multijob build
      pudb: new spell, full-screen, console-based Python debugger
      gnome-common2: => 3.7.4
      libgxps: => 0.2.2
      evince: added missing libgxps dependency
      libgxps: added missing &&
      midori: rewritten dependency tree
      Revert "Revert "fluxbox: => 1.3.3""
      Revert "Revert "fluxbox: fixed fribidi detection, when built with glib support""
      fluxbox: => 1.3.4
      mksh: => R42
      fluxbox: => 1.3.5
      nss: don't overwrite OpenSSL's libssl.a static library
      burp: added ability to build and use statically linked binaries
      mksh: => R42b
      linux: => 3.2.38 (lts)
      linux: => 3.4.32 (lts)
      linux: => 3.0.65 (lts)
      xen: security update
      transmission: => 2.77
      dosfstools: => 3.0.15
      ruby-1.9: => 1.9.3-p392 (security)
      nss-pam-ldapd: security update
      django: => 1.4.4 (security)
      linux: => 3.0.66 (lts)
      linux: => 3.2.39 (lts)
      linux: => 3.4.33 (lts)
      patch: added attr optional dependency
      easytag: => 2.1.8
      siege: => 2.74
      galculator: => 2.1
      cairo: => 1.12.14
      poppler: => 0.22.1
      Revert "galculator: => 2.1"
      poppler: switched to lcms2
      cups-filters: => 1.0.29
      automake-1.9: fixed build with recent autotools
      acpid2: => 2.0.18
      file: => 5.13
      klavaro: => 1.9.7
      VERSION: 0.62-rc
      VERSION: 0.63-test
      libcdio: added trigger to recast spells that link with libcdio libraries
      libcdio-paranoia: added cdda.h header symlink (part of #501 fix)
      mpd: switched from libcdio to libcdio-paranoia
      gvfs: switched from libcdio to libcdio-paranoia
      libcdio: added trigger to recast spells that link with libcdio libraries     (cherry picked from commit 4f186d8d31e3780d6d31b03873cb229e8946e9ce)
      libcdio-paranoia: added cdda.h header symlink (part of #501 fix)     (cherry picked from commit c0e7054c60158847d19960e40a9a13f11c094d91)
      mpd: switched from libcdio to libcdio-paranoia     (cherry picked from commit c0c57a3e43edbc6e84536f0ef10558b6bfcad97f)
      gvfs: switched from libcdio to libcdio-paranoia     (cherry picked from commit 1eb826c20f48ce8bf4d891f054d10a12ff59a833)
      php: => 5.4.12 (stable), 5.3.22 (previous), 5.5.0alpha5 (alpha)
      mtr: => 0.83
      siege: => 2.75
      ncdc: => 1.15
      poppler: this was a security update
      pygments: => 1.6
      openssl: added recast on x.y -> x.z upgrades
      tinc: => 1.0.20
      openldap: => 2.4.34
      burp: => 1.3.26 (devel)
      proftpd: => 1.3.4c
      lxml: => 3.1.0
      mksh: => R44
      audiofile: => 0.3.6
      siege: => 2.77
      tcc: => 0.9.26
      minicom: => 2.6.2
      sudo: => 1.8.6p7 (security)
      mupdf: => 1.2
      redis: => 2.6.10
      pv: => 1.4.6
      rxvt-unicode: => 9.17
      mtr: => 0.84
      geany: => 1.23
      geany-plugins: => 1.23
      privoxy: => 3.0.21 (security)
      xfdesktop: => 4.10.2
      siege: => 2.78
      libdbi: => 0.9.0
      libdbi-drivers: => 0.9.0
      sqlite: => 3.7.16
      man-pages: => 3.50
      ncdc: => 1.16
      znc: => 1.0
      gajim: => 0.15.3
      added missing 'ratbox' account for ircd-ratbox spell
      roundup: added suggest dependency on native SQLite extension for Python
      distribute: => 0.6.35
      urwid: => 1.1.1
      pudb: => 2013.1
      php: => 5.3.23 (previous), 5.4.13 (stable) [security]
      php: updated backports+security patches for legacy branch to 20130320
      php: removed icu dependency for branches older than 5.3
      php: added conflicts with fileinfo for PHP >=5.3
      fileinfo: added conflicts with PHP >=5.3
      egenix-mx-base: => 3.2.5
      psutil: new spell, process and system utilities module for Python
      burp: => 1.3.28 (devel)
      mozcache: new spell, viewer and manager for cache files stored by Gecko-based browsers
      openldap: => 2.4.35
      isc.gpg: added 189CDBC5 public key (Internet Systems Consortium, Inc. (Signing key, 2013) <codesign@isc.org>)
      dhcp: => 4.2.5-P1 (security)
      postgresql: => 9.2.4 (security)
      ncdc: => 1.16.1
      python: => 2.7.4 (security)
      psycopg2: => 2.5
      lxml: => 3.1.2
      sqlite: => 3.7.16.2
      fluxbox: => 1.3.5
      nss: don't overwrite OpenSSL's libssl.a static library
      burp: added ability to build and use statically linked binaries
      mksh: => R42b
      linux: => 3.2.38 (lts)
      linux: => 3.4.32 (lts)
      linux: => 3.0.65 (lts)
      xen: security update
      transmission: => 2.77
      dosfstools: => 3.0.15
      ruby-1.9: => 1.9.3-p392 (security)
      nss-pam-ldapd: security update
      django: => 1.4.4 (security)
      linux: => 3.0.66 (lts)
      linux: => 3.2.39 (lts)
      linux: => 3.4.33 (lts)
      patch: added attr optional dependency
      easytag: => 2.1.8
      siege: => 2.74
      galculator: => 2.1
      cairo: => 1.12.14
      poppler: => 0.22.1
      Revert "galculator: => 2.1"
      poppler: switched to lcms2
      cups-filters: => 1.0.29
      automake-1.9: fixed build with recent autotools
      acpid2: => 2.0.18
      file: => 5.13
      klavaro: => 1.9.7
      VERSION: 0.63-test
      libcdio: added trigger to recast spells that link with libcdio libraries
      libcdio-paranoia: added cdda.h header symlink (part of #501 fix)
      mpd: switched from libcdio to libcdio-paranoia
      gvfs: switched from libcdio to libcdio-paranoia
      php: => 5.4.12 (stable), 5.3.22 (previous), 5.5.0alpha5 (alpha)
      mtr: => 0.83
      siege: => 2.75
      ncdc: => 1.15
      poppler: this was a security update
      pygments: => 1.6
      openssl: added recast on x.y -> x.z upgrades
      tinc: => 1.0.20
      openldap: => 2.4.34
      burp: => 1.3.26 (devel)
      proftpd: => 1.3.4c
      lxml: => 3.1.0
      mksh: => R44
      audiofile: => 0.3.6
      siege: => 2.77
      tcc: => 0.9.26
      minicom: => 2.6.2
      sudo: => 1.8.6p7 (security)
      mupdf: => 1.2
      redis: => 2.6.10
      pv: => 1.4.6
      rxvt-unicode: => 9.17
      mtr: => 0.84
      geany: => 1.23
      geany-plugins: => 1.23
      privoxy: => 3.0.21 (security)
      xfdesktop: => 4.10.2
      siege: => 2.78
      libdbi: => 0.9.0
      libdbi-drivers: => 0.9.0
      sqlite: => 3.7.16
      man-pages: => 3.50
      ncdc: => 1.16
      znc: => 1.0
      gajim: => 0.15.3
      added missing 'ratbox' account for ircd-ratbox spell
      roundup: added suggest dependency on native SQLite extension for Python
      distribute: => 0.6.35
      urwid: => 1.1.1
      pudb: => 2013.1
      php: => 5.3.23 (previous), 5.4.13 (stable) [security]
      php: updated backports+security patches for legacy branch to 20130320
      php: removed icu dependency for branches older than 5.3
      php: added conflicts with fileinfo for PHP >=5.3
      fileinfo: added conflicts with PHP >=5.3
      egenix-mx-base: => 3.2.5
      psutil: new spell, process and system utilities module for Python
      burp: => 1.3.28 (devel)
      mozcache: new spell, viewer and manager for cache files stored by Gecko-based browsers
      openldap: => 2.4.35
      isc.gpg: added 189CDBC5 public key (Internet Systems Consortium, Inc. (Signing key, 2013) <codesign@isc.org>)
      dhcp: => 4.2.5-P1 (security)
      postgresql: => 9.2.4 (security)
      ncdc: => 1.16.1
      python: => 2.7.4 (security)
      psycopg2: => 2.5
      lxml: => 3.1.2
      imagick: => 3.0.1
      imagemagick: => 6.8.4-10, reenabled ghostscript support
      mpd: => 0.17.4
      python-mpd: => 0.5.1
      cherrypy: => 3.2.4
      tinc: => 1.0.21 (security)
      loop-aes: => 3.6h
      burp: => 1.3.30 (devel)
      fox: => 1.6.49
      vifm: => 0.7.5
      mksh: corrected description for new release
      gajim: fixed compat. with new GTalk API
      geany: => 1.23.1
      weechat: => 0.4.1
      sqlite: => 3.7.17
      ppp: added mppe.h header into build; added missing dependencies
      pppd-chldap: new spell, pppd LDAP plugin
      accel-ppp: new spell, high performance PPTP/L2TP/PPPoE server for Linux
      xl2tpd: new spell, Layer 2 Tunnelling Protocol Daemon (RFC 2661)
      accel-ppp: fixed HISTORY entry
      openl2tp: new spell, complete implementation of RFC2661
      fping: => 3.5
      Revert "disk/udev: install udevadm to /sbin"
      Revert "disk/udev: version 182"
      seamonkey: updated required versions for nss and sqlite
      gajim: => 0.15.4
      socat: => 1.7.2.2 (security)
      wireshark: removed obsolete options and dependencies
      openjpeg: fixed 1.5.0 -> 1.5.1 upgrade procedure
      xine-lib: => 1.2.3
      flac: post-updated dependencies and flags
      flac: included static libs flags (on by default like in previous version)
      dosfstools: => 3.0.17
      acpid2: => 2.0.19
      memcached: added security update info for 1.4.15 release
      ruby-1.9: => 1.9.3-p429 (security)
      libxslt: added security info for 1.1.28 release
      libxml2: => 2.9.1 (security)
      mongodb: => 2.0.9 (security)
      py-bcrypt: => 0.3 (security)
      policykit: => 0.111
      alsa-lib: => 1.0.27.1
      alsa-utils: => 1.0.27.1
      cups: fixed source url
      burp: => 1.3.32 (devel)
      qpdf: fixed migration on major/minor spell updates
      cups-filters: disable installation of distro-specific init stuff
      cairo: added binutils optional dependency
      binutils: fixed migration for spells that require libbfd
      mercurial: => 2.6.2
      fbreader: fixed multijob build, source urls
      xdebug: => 2.2.3
      wireshark: fixed build (doc generation)
      gtk+3: => 3.8.2
      evince: => 3.8.2
      proftpd: => 1.3.4d
      ncdc: => 1.17
      softflowd: => 0.9.9
      xfce4-mixer: added missing required dependencies
      redis: => 2.6.13
      samba: => 3.6.16
      xcache: => 3.0.3
      linux: => 3.0.82 (lts)
      linux: => 3.7.10 (eol)
      linux: => 3.8.13 (eol)
      linux: => 3.2.47 (lts)
      linux: => 3.4.49 (lts)
      sudo: => 1.8.7
      whois: => 5.0.25
      dialog: => 1.2-20130523
      krb5: => 1.11.3 (security)
      xen: => 4.1.5 (security)
      curl: => 7.31.0 (security)
      linux: => 3.4.50 (lts)     (cherry picked from commit ffccaa7de604cfe286ad5f4f3d200337834be860)
      linux: => 3.0.83 (lts)     (cherry picked from commit 4373e294029fc81d666ba3e432f19e99f881bcf6)
      mongodb: fixed build with boost 1.50+
      greylist: fixed collecting triplets (init mode support)
      burp: => 1.3.34 (devel)
      ruby-1.8: => 1.8.7-p374 (security)
      ruby-1.9: => 1.9.3-p448 (security)
      linux: => 3.0.84 (lts)
      linux: => 3.2.48 (lts)
      linux: => 3.4.51 (lts)
      id3v2: => 0.1.12
      loop-aes: => 3.6i
      alsa-lib: => 1.0.27.2
      ferm: => 2.2
      gdisk: => 0.8.7
      apache22: => 2.2.25
      apache.gpg: added 9088F565 public key; cleaned and minimized keyring
      gnu.gpg: cleaned and minimized keyring
      transmission: => 2.81
      php: => 5.3.27 (previous), 5.4.17 (stable), 20130717 (legacy: backports+security)
      code-browser: => 4.7 (4)
      postfix: => 2.9.7
      mksh: => R47
      sendmail: moved signing keyring to mail section
      mail/sendmail.gpg: added public key 5207CAD3 (Sendmail Signing Key/2013 <sendmail@Sendmail.ORG>)
      libmilter: new spell, mail filter support library for sendmail
      tinc: => 1.0.22
      burp: => 1.3.36 (devel)
      transmission: => 2.82
      hatta: => 1.6.2
      cronie: => 1.4.11
      taskwarrior: => 2.2.0
      libbsd: => 0.6.0
      dejavu-ttf: => 2.34
      opendkim: new spell, open source DKIM library, MTA filter implementation and associated tools
      loop-aes: => 3.7a
      mpd: => 0.17.5
      knockd: => 0.6
      fwknop: => 2.5.1
      postfix: => 2.9.8
      mksh: => R48b
      xfe: => 1.35
      xlockmore: => 5.43
      pv: => 1.4.12
      psmisc: => 22.20
      geoip: => 1.5.1
      libqrencode: => 3.4.3
      lxml: => 3.2.3
      klavaro: => 1.9.9
      nsd: => 3.2.16
      python-ldap: => 2.4.13
      msmtp: => 1.4.31
      libogg: => 1.3.1
      smem: => 1.3
      tnftp: => 20130505
      kexec-tools: => 2.0.4
      dialog: => 1.2-20130902
      aumix: => 2.9.1
      added missing 'opendkim' account for opendkim spell
      ChangeLog: corrected date record
      added 'dk-milter' account for dk-milter spell
      dk-milter: new spell, DomainKeys milter for Sendmail
      acpid2: => 2.0.20
      xfce4-dict: added missing libxfcegui4 dependency
      ffmpeg: => 0.7.15 (legacy); fixed branch detection
      deadbeef: dependency fixes
      monit: => 5.6
      pmount: => 0.9.23
      spacefm: => 0.8.7
      easytag: removed extra harfbuzz dependency
      inkscape: fixed boost dependency and multijob build
      vlc: fixed permissions for PRE_BUILD
      ffmpeg: => 1.2.3 (stable)
      libass: => 0.10.1
      ffmpeg: rewritten the spell
      ffmpeg: added build for qt-faststart tool
      mpv: new spell, free and open-source general-purpose video player
      lighttpd: => 1.4.33
      fwknop: added missing handle of config options
      added AD00BE50 public key (Toni Gundogdu <legatvs@gmail.com>)
      libquvi-scripts: new spell, support scripts for libquvi calls
      libquvi: new spell, library with the C API for parsing the media stream properties
      quvi: => 0.4.2
      mpv: added libquvi support
      monit: moved init script to Unix System-V runlevel 2
      ncdc: => 1.18
      xlockmore: added missing dependencies
      slim: => 1.3.6
      xen: => 4.1.6.1 (security)
      ffmpeg: => 1.2.4 (stable)
      openswan: => 2.6.39 (security)
      hatta: => 1.6.3
      burp: => 1.3.38 (devel)
      psmouse-elantech: new spell, psmouse kernel module with support for elantech with multitouch
      dosfstools: => 3.0.23
      tinc: => 1.0.23
      php: fixed building regular mysql module for legacy branch
      openldap: => 2.4.37
      burp: => 1.3.40 (devel)
      castfs: removed extra doc collection
      spacefm: => 0.9.0
      libass: => 0.10.2
      mpv: => 0.2.2
      ipsec-tools: => 0.8.1
      fping: => 3.7
      mpv: => 0.2.3
      spacefm: => 0.9.1
      fping: => 3.8
      xautolock: added option to read X resources file
      vifm: => 0.7.6
      libquvi-scripts: => 0.4.20
      openldap: => 2.4.38
      loop-AES.gpg: added 8132F189 public key (Jari Ruusu (2013) <jariruusu@users.sourceforge.net>)
      util-linux: => 2.24 (aes); removed conflicts with simpleinit-msb/shadow
      nginx: security update
      xfe: => 1.37
      php-clamav: new spell, ClamAV Interface for PHP5 scripts
      burp: => 1.3.42
      slowhttptest: => 1.6
      rdesktop: added missing dependencies
      mpv: => 0.2.4
      spacefm: => 0.9.2
      deadbeef: => 0.6.0
      lua: => 5.2.3
      nss-pam-ldapd: => 0.7.19
      trac: added flup suggest dependency
      lxml: => 3.2.4
      imagemagick: => 6.8.7-10
      imagemagick: removed deprecated flag
      ruby-1.9: => 1.9.3-p484 (security)
      php: => 5.4.23 (stable) [security]
      geoip: => 1.6.0
      xcache: => 3.1.0
      lighttpd: added patches to use custom ldap port in authentication module
      libmnl: => 1.0.3
      ipset: => 6.20.1 (2.6 branch)
      ipset: => 6.20.1
      ipset: added HISTORY entry
      burp: => 1.3.46 (devel)
      minicom: => 2.7
      mhwaveedit: => 1.4.23
      php: => 5.3.28 (previous) [security]
      php: => 5.4.24 (stable)
      mdp: new spell, simplified password manager
      lighttpd: => 1.4.34 (security)
      gettext: added glib2 optional dependency
      Revert "gettext: added glib2 optional dependency"
      tilda: => 1.1.11
      tilda: fixed cursor customization patch to save cursor color on changing palette
      klavaro: => 3.00
      liblo: => 0.27
      ardour3: => 3.5.308
      socat: => 1.7.2.3 [security]
      openldap: => 2.4.39
      burp: => 1.3.48 (devel)
      mtr: => 0.85
      spacefm: => 0.9.3
      bluefish: => 2.2.5
      ardour3: jack -> JACK-DRIVER
      jack2: post-update fixes
      waf_build(): include missing configdir option
      fluidsynth: switched to cmake build (officially preferred) -- fixes long options parsing
      njconnect: new spell, curses JACK connection manager
      jack: added missing header (jslist.h)
      seq24: => 0.9.2
      mercurial: => 2.9
      rsa: => 3.1.2
      stunnel: => 4.56
      sqlite: => 3.8.3
      accounts, groups: added account data for gnarwl spell
      gnarwl: new spell, LDAP based email autoresponder
      stunnel: added forgotten HISTORY changes (thanks to lace@)
      pycrypto: => 2.6.1 [security]
      rsa: updated dependencies
      rsa: added missing &&
      mdp: => 0.7.0
      mdp: => 0.7.2
      apache22: => 2.2.26
      php: => 5.4.25
      ncdc: => 1.19
      mdp: => 0.7.3
      cherrypy: => 3.2.5
      monit: => 5.7
      iotop: => 0.6
      rsa: => 3.1.4
      lxml: => 3.3.2
      py-bcrypt: => 0.4
      fwknop: => 2.6.0
      burp: => 1.3.48 (stable); => 1.4.10 (devel)
      fabric: => 3.8.3.1
      postgresql: => 9.3.3 (security)
      python-ecdsa: new spell, ECDSA cryptographic signature library
      paramiko: => 1.12.2
      fabric: => 1.8.2
      sylpheed: => 3.3.1
      fping: => 3.9
      elvis: added missing libxt dependency
      php: => 5.4.26 (stable) [security]
      bitlbee: => 3.2.1
      socat: => 1.7.2.4
      lighttpd: => 1.4.35 [security]
      postgresql: => 9.3.4
      smtpc: new spell, test smtp client
      gigolo: => 0.4.2
      optipng: => 0.7.5
      monit: => 5.8
      sqlite: => 3.8.4.2
      lxml: => 3.3.3
      znc: => 1.2 [security]
      gstpw: new spell, simple GTK+2 stopwatch program
      spacefm: => 0.9.4
      apache22: => 2.2.27 [security]
      loop-aes: => 3.7b
      sylpheed: => 3.4.0
      sqlite: => 3.8.4.3
      sylpheed: => 3.4.1
      deadbeef: => 0.6.1
      ristretto: renewed dependencies
      libunwind: fixed syntax errors in spell files; don't do useless doc-ing
      google-perftools: => 2.1
      redis: => 2.6.17
      copper: added copper-elf-1.6 symlink
      code-browser: => 4.9
      mongodb: => 2.4.10
      postfix: => 2.9.9
      mariadb: added branch 5.5
      mariadb: update triggers for switching between branches
      tdb: => 1.2.13
      samba: => 3.6.23 [security]
      virtualenv: => 1.11.4
      pip: new spell, Python easy_install replacement
      geany: => 1.24
      geany-plugins: => 1.24
      fwknop: => 2.6.1
      polipo: new spell, caching web proxy
      ChangeLog: corrected double-spaces for history entries
      slim: fixed build with recent freetype2/cmake
      freetype2: => 2.5.3 [security]
      fontconfig: => 2.11.1
      geany: => 1.24.1
      isomaster: => 1.3.11
      polipo: implemented reload function to prevent exiting when HUP signal is sent
      nginx: fixed logic bug in init script
      cherrypy: => 3.3.0 (branch 3)
      gettext: made libxml2 optional
      bluefish: => 2.2.6
      ncdc: => 1.19.1
      php: => 5.4.27 [security]
      lilo: added patch for Xen XVD disks recognition
      smem: => 1.4
      pngquant: => 2.2.0
      mpv: => 0.3.8
      optipng: fixed man directory
      ipsec-tools: => 0.8.2
      uget: => 1.10.4
      exim: fixed priority for gdbm
      neon: re-added spaces patch
      davfs: => 1.5.0
      fwknop: => 2.6.2
      django: => 1.4.11 [security]
      proxychains-ng: new spell, TCP and DNS through proxy server
      proxychains-ng: fixed config path
      php: => 5.4.28 [security]
      pv: => 1.5.3
      fping: => 3.10
      moe: => 1.5
      mercurial: => 3.0
      libreswan: new spell, IPsec implementation for Linux - Openswan fork
      openswan: conflicts with new libreswan spell
      mcabber: => 0.10.3
      ldns: => 1.6.17
      ldns: added openssl warn and perl opt dep
      terminus-font: => 4.39
      masqmail: fixed logging
      tinc: => 1.0.24
      opensp: don't duplicate docs and added gettext opt dep
      libofx: renewed dependencies
      homebank: => 4.5.6
      dhcp: => 4.2.6
      psycopg2: => 2.5.2
      monit: => 5.8.1
      mariadb: => 5.5.37 (5.5 branch)
      getmail: post-update fixes
      znc: => 1.4
      polipo: => 1.1.1
      proftpd: => 1.3.5
      iozone: => 3_424
      vifm: => 0.7.7
      transmission: => 2.83
      greenlet: new spell, lightweight in-process concurrent programming
      curtsies: new spell, curses-like terminal wrapper, with colored strings
      bpython: => 0.13
      rdesktop: => 1.8.2
      mpv: => 0.3.10
      taskwarrior: post-update fixes
      mariadb: corrected HISTORY entry
      psycopg2: => 2.5.3
      mod_wsgi: => 3.5 [security]
      php: => 5.4.29 [security]
      openssl: => 1.0.1h (1.0), 0.9.8za (0.9) [security]
      tilda: => 1.1.12
      sqlite: => 3.8.5
      mercurial: => 3.0.1
      lxml: => 3.3.5
      irssi: => 0.8.16
      sylpheed: => 3.4.2
      knock: => 0.7
      easytag: => 2.2.2
      libquvi-scripts: corrected HISTORY entry
      mariadb: => 5.5.38 (5.5)
      gstopwatch: new spell, simple stopwatch, written in GTK3
      liblo: added gcc pre-4.8 support
      ardour3: => 3.5.380
      homebank: => 4.6
      simpleinit-msb: fixed critical segfault on invoking from Xen (as a guest HVM DomU)
      pptp-linux: => 1.8.0
      easytag: => 2.2.3
      homebank: => 4.6.1
      php: => 5.4.30 [security]
      burp: => 1.4.16 (devel)
      lighttpd: added libev optional dependency
      transmission: => 2.84
      cherrypy: => 3.5.0
      php: fixed 5.2 branch build
      Revert "php: fixed 5.2 branch build"
      mercurial: => 3.0.2
      galculator: => 2.1.3
      gnarwl: added optional patch to allow usage of $time variable that returns current time in days since 1 Jan 1970
      jpeg: => 9a
      libfm: => 1.2.1
      pcmanfm: => 1.2.1
      bitlbee: => 3.2.2
      freeradius: => 2.2.5
      bpython: => 0.13.1
      mksh: => R50
      chrony: => 1.30
      libreswan: => 3.9
      exim: => 4.83 (security)
      rsync: => 3.1.1
      burp: => 1.4.18 (devel)
      php: => 5.4.31 (stable)
      gnarwl: fixed blacklist functioning
      fwknop: => 2.6.3
      homebank: => 4.6.2
      hatta: fixed exception on +wanted page
      lighttpd: added Lua 5.2 support
      hatta: added pygments suggest dep
      proxychains-ng: => 4.8.1
      openssl: => 1.0.1i (1.0), 0.9.8zb (0.9) [security]
      exim: => 4.84
      homebank: => 4.6.3
      accel-ppp: => 1.8.0
      greylist: added ability to show configured timeout value in defer message
      trac-ldapplugin: => 0.7.0
      python-ldap: => 2.4.15
      php: => 5.3.29 (previous) [security]
      roundup: => 1.5.0
      sqlite: => 3.8.6
      wavegain: new spell, wav files loudness normalizer
      php: => 5.4.32 (stable) [security]
      acpid2: => 2.0.23
      davfs2: => 1.5.2
      lxml: => 3.3.6
      psycopg2: => 2.5.4
      mpd: => 0.18.13
      memcache: => 3.0.8
      libreswan: => 3.10
      postgresql: => 9.3.5
      dia: => 0.97.3
      mksh: => R50b
      mpd: => 0.18.14
      cherrypy: => 3.6.0
      lxml: => 3.4.0
      chrony: => 1.31
      openvpn: => 2.3.4
      hexchat: => 2.10.1
      monit: => 5.9
      tilda: => 1.1.13
      mpd: => 0.18.16
      mariadb: => 5.5.39 (5.5)
      easytag: => 2.2.4
      mongodb: => 2.4.11
      Revert "distcc 3.2rc1"
      megatools: new spell, command line client for mega.co.nz
      megatools: added missing glib-networking dependency
      nodejs: => 0.10.32
      phantomjs: new spell, headless WebKit scriptable with a JavaScript API
      php: => 5.4.33
      bash: => 4.3.28 [security]
      jack2: added primary mirror
      ulimits: new spell, user limits utility
      ulimits: added missing release note for patch
      ulimits: added yet another missing release note for patch
      bash: => 4.3.29 [security]
      mercurial: => 3.1.2
      ipmitool: => 1.8.14
      mksh: => R50c [security]
      ardour3: => 3.5.403
      cracklib: => 2.9.2
      mksh: => R50d
      mupdf: => 1.6
      klavaro: => 3.01
      at: => 3.1.16
      Revert "gajim: depends SSL"
      pyasn1-modules: => 0.0.5
      pyasn1: => 0.1.7
      nbxmpp: new spell, non-blocking Jabber/XMPP module
      gajim: => 0.16
      postfix: => 2.9.10
      php: => 5.4.34 (stable) [security]
      at: fixed docdir
      mxml: => 2.9
      sqlite: => 3.8.7
      asunder: => 2.5
      postfix: => 2.9.11
      libbsd: => 0.7.0
      postfix: post-update fixes
      postfix: removed obsolete options + more post-update fixes
      postfix: ignore running queue files
      at: fixed permissions on atjobs dir
      nspr: => 4.10.7
      nss: => 3.17.2
      seamonkey: => 2.30 [security]
      Revert "ldns: depends SSL"
      ldns: corrected openssl's subdependency behaviour
      Revert "burp: fix bad with-SSL usage"
      Revert "burp: depends SSL"
      burp: => 1.4.24 (devel)
      php: corrected ssl flags
      Revert "lighttpd: fix bad with-SSL usage"
      Revert "lighttpd: depends SSL"
      lighttpd: use SSL provider
      Revert "libesmtp: fix bad with-SSL usage"
      Revert "libesmtp: depends SSL"
      libesmtp: use SSL provider
      Revert "nmap: fix bad with-SSL usage"
      Revert "nmap: depends SSL"
      nmap: use SSL provider
      Revert "cyrus-sasl: fix bad with-SSL usage"
      Revert "cyrus-sasl: depends SSL"
      cyrus-sasl: use SSL provider
      Revert "flow-tools: fix bad with-SSL usage"
      Revert "flow-tools: depends SSL"
      flow-tools: use SSL provider
      Revert "bind-tools: fix bad with-SSL usage"
      Revert "bind-tools: depends SSL"
      bind-tools: => 9.9.6 [security]
      Revert "bind: fix bad with-SSL usage"
      Revert "bind: depends SSL"
      bind: use SSL provider
      Revert "php4: fix bad with-SSL usage"
      Revert "php4: depends SSL"
      php4: use SSL provider
      nss: => 3.16.6 (3.16); re-enabled PEM support in the last versions; rewritten SUB_DEPENDS
      libreswan: => 3.11
      cpuminer: => 2.4
      Revert "cherrypy: depends SSL"
      Revert "roundup: depends SSL"
      Revert "webcleaner: depends SSL"
      Revert "attic: depends SSL"
      Revert "papyon: depends SSL"
      Revert "pyicqt: depends SSL"
      Revert "pymsn: depends SSL"
      Revert "pymsnt: depends SSL"
      Revert "scrapely: depends SSL"
      Revert "scrapy: depends SSL"
      Revert "twisted: depends SSL"
      Revert "xen: depends SSL"
      xen: added 4.2 branch
      trac: => 0.12.6
      tinyproxy: security update
      vifm: => 0.7.8
      sqlite: => 3.8.7.1
      openvpn: => 2.3.5
      monit: => 5.10
      Revert "neon: depends SSL"
      neon: => 0.30.1
      wget: more properly migrate from openssl to SSL provider
      python-ldap: => 2.4.18
      stunnel: => 5.06; added cert installation target (missed by previous update)
      libev: => 4.19
      Revert "libssh - fix build with libressl"
      libssh: use SSL provider
      Revert "openldap: depends SSL"
      openldap: => 2.4.40; use SSL provider
      openldap: handle obsolete '--disable-slurpd' flag
      mariadb: => 5.5.40 (5.5) [security]
      dash: => 0.5.8
      ca-certificates: => 20141019
      tnftp: => 20141031
      tnftp: => 20141104
      mercurial: => 3.2
      dave_robillard.gpg: updated keyring, added 7364C240 and 9BF368F3 keys
      ganv: new spell, interactive Gtkmm canvas widget for graph-based interfaces
      patchage: => 1.0.0
      vile: new spell, vi-like Emacs
      apache22: => 2.2.29 [security]
      rdesktop: => 1.8.3
      dovecot: backported official patch from branch 2.1 to support ssl_protocols option (allows turning off SSLv3 to mitigate POODLE attack - CVE-2014-3566)
      php: => 5.4.35 (stable) [security]
      mercurial: => 3.2.1
      amsynth: => 1.5.1
      stunnel: => 5.07
      fwknop: => 2.6.4
      sqlite: => 3.8.7.2
      maim: new spell, desktop screenshot utility
      xlockmore: => 5.44
      libreswan: => 3.12
      speedtest-cli: new spell, Internet bandwidth measurement tool
      glibc: added ability to build valgrind-friendly version
      lxml: => 3.4.1
      Revert "unbound: depends SSL"
      unbound: => 1.5.0
      unbound: fixed build with nss support
      ldns: made GOST support optional for openssl 1.0; added missing options
      nsd: => 4.1.0
      Revert "gftp: depends SSL"
      gftp: fixed several crashes by third-party patches
      gftp: use SSL provider
      gftp: fixed FTPS connections
      hexchat: => 2.10.2
      easytag: => 2.2.5
      cronie: => 1.4.12
      ipmitool: => 1.8.15
      maim: => 2.3.37
      mysql-python: => 1.2.5
      ruby-1.9: => 1.9.3-p551 [security]
      pv: => 1.5.7
      pygments: => 2.0.1
      Revert "exim: depends SSL"
      libspf2: new spell, fully thread safe SPF implementation
      exim: added ability to build with experimental SPF support
      maim: => 2.3.38
      libfcgi: fixed build
      openvpn: => 2.3.6
      openvpn: incremented forgotten security patch for CVE-2014-8104
      xlockmore: => 5.45 [potential security]
      maim: => 3.3.41
      seamonkey: => 2.31 [security]
      sqlite: => 3.8.7.3
      unbound: => 1.5.1 [security]
      sqlite: => 3.8.7.4
      python: => 2.7.9 [security]
      nginx: fixed ulimits tuning on PAM-less systems
      recaptcha-client: new spell, plugin for reCAPTCHA and reCAPTCHA Mailhide
      hatta: added recaptcha-client suggest dep
      php: => 5.4.36 [security]
      mercurial: => 3.2.3 [security]
      argh: => 0.26.1
      args: new spell, argument parsing for humans
      clint: => 0.4.1
      feedgenerator: => 1.7
      httplib2: => 0.9
      markupsafe: => 0.23
      jinja2: markupsafe becomes required from 2.7
      pyyaml: => 3.11
      python-dateutil: => 2.3
      python-markdown: => 2.5.2
      python-markdown2: new spell, fast and complete Python implementation of Markdown
      regex: new spell, alternative regular expression module, to replace re
      unidecode: => 0.04.17
      python-textile: new spell, Textile processing for Python
      pathtools: new spell, file system general utilities
      watchdog: new spell, filesystem events monitoring
      py: new spell, library with cross-python path, ini-parsing, io, code, log facilities
      pytest: new spell, simple powerful testing with Python
      awesome-slugify: new spell, Python flexible slugify function
      clint: added missing args req dep
      avfs: => 1.0.2
      simplejson: => 3.6.5
      watchdog -> python-watchdog: renamed spell
      pelican: => 3.5.0
      hatta: => 1.6.5
      wok: new spell, static site generator
      tinc: => 1.0.25
      mercurial: => 3.2.4
      freeradius: => 2.2.6
      mtr: => 0.86
      monit: => 5.11
      fluxbox: => 1.3.6
      monit: post-update fixes
      Revert "msmtp 1.6.0rc3"
      Revert "msmtp 1.6.0rc2"
      msmtp: => 1.6.1
      openntpd: => 5.7p1
      seamonkey: => 2.32 [security]
      fbnews: new spell, RSS/RDF newsfetcher for Fluxbox
      pgpdump: => 0.29
      pygments: => 2.0.2
      fwknop: => 2.6.5
      monit: cleaned up the spell
      monit: corrected typo
      wsgigzip: new spell, decorator for flup's gzip compression WSGI middleware
      breach_buster: new spell, BREACH-resistant gzip middleware for Django
      unidecode: use SPELLX in SOURCE
      php: => 5.4.37 [security]
      bpython: => 0.13.2
      mariadb: => 5.5.41 (5.5) [security]
      readline: corrected a typo in HISTORY
      readline: resurrect-compliance++
      lilo: => 24.1
      sqlite: => 3.8.8.2
      wsgigzip: => 0.1.3
      hatta: added missing dependency
      socat: => 1.7.3.0 [security]
      privoxy: => 3.0.23 [security]
      stunnel: => 5.10
      mercurial: => 3.3
      dialog: => 1.2-20150125
      nsd: => 4.1.1
      openntpd: => 5.7p3
      burp: => 1.4.32 (devel)
      libtirpc: made libgssglue optional
      rpcbind: => 0.2.2
      accounts, groups: added account data for rpcbind spell
      postgresql: => 9.3.6 [security]
      easytag: => 2.2.6
      fluxbox: => 1.3.7
      mpd: => 0.19.9
      samba: security+feature update
      seamonkey: => 2.32.1
      lxml: => 3.4.2
      bluefish: => 2.2.7
      p7zip: => 9.38
      eudev: renamed provider UDEV -> DEVICE-MANAGER
      udev: renamed provider UDEV -> DEVICE-MANAGER
      pulseaudio: depends on UDEV -> DEVICE-MANAGER
      libgpod: depends on UDEV -> DEVICE-MANAGER
      media-player-info: depends on UDEV -> DEVICE-MANAGER
      drbd: depends on UDEV -> DEVICE-MANAGER
      pcsc-lite: depends on UDEV -> DEVICE-MANAGER
      gparted: depends on UDEV -> DEVICE-MANAGER
      libatasmart: depends on UDEV -> DEVICE-MANAGER
      udisks: depends on UDEV -> DEVICE-MANAGER
      udisks2: depends on UDEV -> DEVICE-MANAGER
      e17: depends on UDEV -> DEVICE-MANAGER
      eeze: depends on UDEV -> DEVICE-MANAGER
      devicekit: depends on UDEV -> DEVICE-MANAGER
      gvfs: depends on UDEV -> DEVICE-MANAGER
      libgphoto2: depends on UDEV -> DEVICE-MANAGER
      drm: depends on UDEV -> DEVICE-MANAGER
      libdrm: depends on UDEV -> DEVICE-MANAGER
      libusb: depends on UDEV -> DEVICE-MANAGER
      libvirt: depends on UDEV -> DEVICE-MANAGER
      sdl2: depends on UDEV -> DEVICE-MANAGER
      upower: depends on UDEV -> DEVICE-MANAGER
      connman: depends on UDEV -> DEVICE-MANAGER
      dhcpcd: depends on UDEV -> DEVICE-MANAGER
      system-config-printer: depends on UDEV -> DEVICE-MANAGER
      qtbase: depends on UDEV -> DEVICE-MANAGER
      qtserialport: depends on UDEV -> DEVICE-MANAGER
      qtimageformats: changed mode to 755 for CONFLICTS
      spacefm: depends on UDEV -> DEVICE-MANAGER
      init.d: depends on UDEV -> DEVICE-MANAGER
      systemd: depends on UDEV -> DEVICE-MANAGER
      bluez5: depends on UDEV -> DEVICE-MANAGER
      cdemu-daemon: depends on UDEV -> DEVICE-MANAGER
      hal: depends on UDEV -> DEVICE-MANAGER
      pcmciautils: depends on UDEV -> DEVICE-MANAGER
      xen: depends on UDEV -> DEVICE-MANAGER
      guvcview: depends on UDEV -> DEVICE-MANAGER
      kino: depends on UDEV -> DEVICE-MANAGER
      vlc: depends on UDEV -> DEVICE-MANAGER
      razor-qt: depends on UDEV -> DEVICE-MANAGER
      xf86-input-wacom: depends on UDEV -> DEVICE-MANAGER
      xf86-video-intel: depends on UDEV -> DEVICE-MANAGER
      xorg-server: depends on UDEV -> DEVICE-MANAGER
      basesystem: fix force depends bug for wget on 'sorcery rebuild'
      php: => 5.4.38 [security]     (cherry picked from commit e6fb738df3fd36cdb87caf3d2ac19af5e5d3a63c)
      Revert "FUNCTIONS - fix typo"
      Revert "FUNCTIONS - fix python2 usage"
      Revert "libxml2 - tweak build for python3"
      Revert "fix builds involving python3.3"
      reiser4progs: fixed build with readline 6.3     (cherry picked from commit 6bf31e0a2bdd4652e0b2def1e23ef8f1e57942b2)     (cherry picked from commit 7b12c2b26642fcaa843ffe0204b415c3a977dab9)
      jfsutils: fixed build with recent glibc     (cherry picked from commit 31f4ce62933ac218b9598b8107eeaab7afe24874)
      shadow: use sha512-based crypt passwords by default     (cherry picked from commit 3f51925fe11d90911d51ae319d092cca9a5a5c5b)
      sysstat: fixed syntax errors in INSTALL     (cherry picked from commit bbe844e826c638ef47e2bb270f722810ef80f32c)
      Revert "gtk-led-askpass 0.11"
      btrfs-progs: => 3.18.2     (cherry picked from commit 629339bdb357c243182fb580b436c1909b0df063)
      samba: => 3.6.25 [security]     (cherry picked from commit f7e3a04ecfe80cf7c53d0e0a5809ea468d60afa4)
      gnupg: => 1.4.19 [security]
      libgcrypt: => 1.6.3 [security]
      VERSION: 0.62-0

root (1):
      mesalib: development: 7.11.2
```

[0] Generated with: `git shortlog --no-merges stable-0.61..stable-0.62`
