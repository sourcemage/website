title: castfs 0.6.2 released
author: stealth
category: news
date: 2015-03-27
tags: [misc]
---

[castfs](/castfs) 0.6.2 has been released!

This release fixes various bugs related to multijob install (broken filenames, crashes) mostly. It also adds several configure flags and refreshes the overall build system.
castfs spell has been updated too, and will be backported to the current [stable 0.62 grimoire](/Grimoire/stable/0.62) (as a part of upcoming 0.62-2 update).

Release notes include the following (copied from the NEWS file in the distribution tarball):

- disabled multi-threaded mode for fuse to fix rare race condition cases
- made xattr support configurable (WARNING: xattr support is still broken)
- removed fgetattr call
- corrected compilation warnings
- display proper arguments in a process tree
- display actual version information
- updated configure/build toolchain
- updated manual page

A detailed changelog of updates which have been integrated[^0] since the last tagged (0.6.0) release:

```
Eric Sandall (5):
      autom4te.cache: Remove autoconf cache files
      configure.in: Look for architecture-dependent files under exec_prefix
      configure: configure: Regenerate with latest configure.in
      debian/changelog: Bump to 0.6.1
      debian/changelog: Fix old bump to 0.6.0 to really be 0.6.0

Vlad Glagolev (27):
      fixed segfault, when running without any arguments
      fixed warnings after compilation with -Wall flag
      added ability to use '-o debug' option
      fixed the warning: implicit declaration of function
      fixed possible race condition by removing of fgetattr call
      do not modify command-line arguments directly in memory
      use dynamic version info; updated configure template
      updated authors
      force single-threaded mode to fix multijob installs in rare cases
      do not cut off the last value from a new argv array
      added forgotten bracket in the changelog entry
      use generated config.h and VERSION
      remastered configure/build scheme
      move config.h to upper level
      made xattr support optional
      added note about broken xattr support
      updated news
      fixed static build
      moved outdated doc files/mails to 'old'
      removed outdated manual and info pages
      removed hand-made Makefile
      added makefile generation template for doc
      added castfs manual page in POD format
      made building of documentation optional
      docs-related cosmetic changes
      suppress output from the doc makefile
      release 0.6.2
```

[^0]: Generated with: `git shortlog --no-merges stable-0.6.0..stable-0.6.2`
