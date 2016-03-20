title: Sorcery module for Ansible
author: stealth
category: news
date: 2015-09-22
tags: [misc, sorcery]
---

We're pleased to announce that as per ([ee25bb0](https://github.com/vaygr/ansible-modules-extras/commit/ee25bb0fc3c96d504190927c39eccae0b01f49d7)), alpha version of [Ansible](http://www.ansible.com/) module for [Sorcery](/Sorcery) has been released!

We will also make a request for its inclusion into official [ansible-modules-extras](https://github.com/ansible/ansible-modules-extras) repository, once it's tested enough and production-ready.

This version introduces just the basic functionality for system operations:

- install a spell (with required dependencies)
- rebuild/update a spell (or the entire system)
- dispel a spell
- update codex
- update sorcery

To test it, you can put the module itself (`sorcery.py`) into your library directory specified by `library =` under `[defaults]` in `ansible.cfg`.  
Then invoke it by running[^0], i.e.:

```
ansible -b --ask-become-pass -m sorcery -a 'name=tcpdump depends=openssl(SSL) state=present' inventory-server
```

Check mode is supported, so you can use `-C` switch as well.

The module uses simple [gaze](/Sorcery/Commands/Gaze) commands to check for spells' existence as well as manipulates with `depends` file directly to simplify switching on/off of desired dependencies.

It also uses some hacks with environment variables to bypass queries and choose default answers: Sorcery hackers are free to inspect them.  
And, as always -- patches, notes and remarks are welcome!

Here's an example usage taken from the EXAMPLES section of the module:

```
# Make sure spell 'foo' is installed
- sorcery: spell=foo state=present

# Make sure spells 'foo', 'bar' and 'baz' are removed
- sorcery: spell=foo,bar,baz state=absent

# Make sure spell 'foo' with dependencies 'bar' and 'baz' is installed
- sorcery: spell=foo depends=bar,baz state=present

# Make sure spell 'foo' with 'bar' and without 'baz' dependencies is installed
- sorcery: spell=foo depends=+bar,-baz state=present

# Make sure spell 'foo' with libressl (providing SSL) dependency is installed
- sorcery: spell=foo depends=libressl(SSL) state=present

# Install the latest version of spell 'foo' using regular glossary
- sorcery: name=foo state=latest

# Rebuild spell 'foo'
- sorcery: spell=foo state=rebuild

# Rebuild the whole system, but update Sorcery and Codex first
- sorcery: spell=* state=rebuild update=yes update_cache=yes

# Refresh the grimoire collection if it's 1 day old using native sorcerous alias
- sorcery: update_codex=yes cache_valid_time=86400

# Update only Sorcery itself
- sorcery: update=yes
```

[^0]: Note that you have to use `-b` (`--become`) or `-s` (`--sudo`) to run commands under superuser (root), otherwise Sorcery would switch to interactive mode to ask for a password making Ansible hang while waiting for input.
