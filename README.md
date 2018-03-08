[![Github All Releases](https://img.shields.io/github/downloads/atom/atom/total.svg)](https://github.com/OfflineIMAP/offlineimap/graphs/traffic)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![GitHub contributors](https://img.shields.io/github/contributors/OfflineIMAP/offlineimap.svg)](https://github.com/OfflineIMAP/offlineimap/graphs/contributors)
[![Snap status](https://build.snapcraft.io/badge/snapcrafters/offlineimap.svg)](https://build.snapcraft.io/user/snapcrafters/offlineimap)

[![Python versions supported](https://img.shields.io/pypi/pyversions/offlineimap.svg)](https://pypi.python.org/pypi/offlineimap)
[![Package stability](https://img.shields.io/pypi/status/offlineimap.svg)](https://pypi.python.org/pypi/offlineimap)
[![PyPI status](https://badge.fury.io/py/offlineimap.svg)](https://pypi.python.org/pypi/offlineimap)
[![Kit format](https://img.shields.io/pypi/format/offlineimap.svg)](https://pypi.python.org/pypi/offlineimap)
[![Implementation](https://img.shields.io/pypi/implementation/offlineimap.svg)](https://pypi.python.org/pypi/offlineimap)

[![GitHub last commit](https://img.shields.io/github/last-commit/OfflineIMAP/offlineimap.svg)](https://github.com/OfflineIMAP/offlineimap/commits/master)
[![GitHub Release Date](https://img.shields.io/github/release-date/OfflineIMAP/offlineimap.svg)](https://github.com/OfflineIMAP/offlineimap/releases)
[![Follow on twitter](https://img.shields.io/twitter/follow/OfflineIMAP.svg?style=social&logo=twitter)](https://twitter.com/intent/follow?screen_name=OfflineIMAP)

Master: [![OfflineIMAP build status on Travis-CI.org](https://travis-ci.org/OfflineIMAP/offlineimap.svg)](https://travis-ci.org/OfflineIMAP/offlineimap)
[![Code coverage](https://codecov.io/gh/OfflineIMAP/offlineimap/branch/master/graph/badge.svg)](https://codecov.io/gh/OfflineIMAP/offlineimap)
[![Gitter chat](https://badges.gitter.im/OfflineIMAP/offlineimap.png)](https://gitter.im/OfflineIMAP/offlineimap)
[![Say thanks to OfflineIMAP](https://img.shields.io/badge/Say%20Thanks-!-______.svg)](https://saythanks.io/to/OfflineIMAP)

Next:
[![OfflineIMAP build status on Travis-CI.org](https://travis-ci.org/OfflineIMAP/offlineimap.svg?branch=next)](https://travis-ci.org/OfflineIMAP/offlineimap)
[![Code coverage](https://codecov.io/gh/OfflineIMAP/offlineimap/branch/next/graph/badge.svg)](https://codecov.io/gh/OfflineIMAP/offlineimap)

Fork status:
[![OfflineIMAP build status on Travis-CI.org](https://travis-ci.org/EspaceNetworks/offlineimap.svg?branch=master)](https://travis-ci.org/EspaceNetworks/offlineimap)
[![OfflineIMAP code coverage on Codecov.io](https://codecov.io/gh/EspaceNetworks/offlineimap/branch/master/graph/badge.svg)](https://codecov.io/gh/EspaceNetworks/offlineimap)
[![Gitter chat](https://badges.gitter.im/EspaceNetworks/offlineimap.png)](https://gitter.im/EspaceNetworks/offlineimap)
[![Say thanks to ESPACE Networks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/chris001)
[![Follow on twitter](https://img.shields.io/twitter/follow/ESPACENetworks.svg?style=social&logo=twitter)](https://twitter.com/intent/follow?screen_name=ESPACENetworks)

[offlineimap]: https://github.com/OfflineIMAP/offlineimap
[website]: http://www.offlineimap.org
[wiki]: https://github.com/OfflineIMAP/offlineimap/wiki
[blog]: http://www.offlineimap.org/posts.html
[docs]: https://offlineimap.readthedocs.io/
[mailing_list]: http://lists.alioth.debian.org/mailman/listinfo/offlineimap-project

<p align="center>
[![OfflineIMAP](https://upload.wikimedia.org/wikipedia/commons/1/13/OfflineIMAP_logo.png)]
# OfflineIMAP
***"Get the emails where you need them."***

## Read/sync your IMAP mailboxes. Works on Linux and MacOSX.

Links:
* [Official (upstream) github code repository][offlineimap]
* [Website][website]
* [Wiki][wiki]
* [Blog][blog]
* [![Documentation](https://readthedocs.org/projects/offlineimap/badge/?version=latest&style=flat)](https://offlineimap.readthedocs.io/)
* [Mailing list][mailing_list]


## Description

OfflineIMAP is software that downloads your email mailbox(es) as **local
Maildirs**. OfflineIMAP will synchronize both sides via *IMAP*.

## Why should I use OfflineIMAP?

IMAP's main downside is that you have to **trust** your email provider to
not lose your email. While certainly unlikely, it's not impossible.
With OfflineIMAP, you can download your Mailboxes and make you own backups of
your [Maildir](https://en.wikipedia.org/wiki/Maildir).

This allows reading your email offline without the need for your mail
reader (MUA) to support IMAP operations. Need an attachment from a
message without internet connection? No problem, the message is still there.


## Project status and future

> As one of the maintainer of OfflineIMAP, I'd like to put my efforts into
> [imapfw](http://github.com/OfflineIMAP/imapfw). **imapfw** is software in
> development that I intend to replace OfflineIMAP with in the long term.
>
> That's why I'm not going to continue OfflineIMAP development. I'll continue
> to maintain OfflineIMAP (fixing small bugs, reviewing patches and merging,
> and rolling out new releases), but that's all.
>
> While I keep tracking issues for OfflineIMAP, you should not expect future support.
>
> You won't be left at the side. OfflineIMAP's community is large enough so that
> you'll find people for most of your issues.
>
> Get news from the [blog][blog].
>
>                                  Nicolas Sebrecht. ,-)


## License

GNU General Public License v2.


## Downloads

* You should first check if your distribution already packages OfflineIMAP for you.
* Downloads releases as [tarball or zipball](https://github.com/OfflineIMAP/offlineimap/tags).
* You can easily [Install as a Snap](https://snapcraft.io/offlineimap)
`sudo snap install offlineimap`
The configuration file for offlineimap should be placed in ```$HOME/snap/offlineimap/current/.offlineimaprc```
([Don't have snapd installed?](https://snapcraft.io/docs/core/install))


## Feedbacks and contributions

**The user discussions, development, announcements and all the exciting stuff take
place on the mailing list.** While not mandatory to send emails, you can
[subscribe here](http://lists.alioth.debian.org/mailman/listinfo/offlineimap-project).

Bugs, issues and contributions can be requested to both the mailing list or the
[official Github project][offlineimap].  Provide the following information:
- system/distribution (with version)
- offlineimap version (`offlineimap -V`)
- Python version
- server name or domain
- CLI options
- Configuration file (`~/.offlineimaprc`)
- pythonfile (if any)
- Logs, error
- Steps to reproduce the error


## The community

* OfflineIMAP's main site is the [project page at Github][offlineimap].
* There is the [OfflineIMAP community's website][website].
* And finally, [the wiki][wiki].


## Requirements & dependencies

* Python v2.7+
* Python v3.4+ ***[STALLED](experimental: [see known issues](https://github.com/OfflineIMAP/offlineimap/issues?q=is%3Aissue+is%3Aopen+label%3APy3))***
* six (required)
* imaplib2 >= 2.57 (optional)


## Documentation

All current and updated documentation is on the [community's website][website].


### Read documentation locally

You might want to read the documentation locally. Get the sources of the website.
For the other documentation, run the appropriate make target:

```sh
$ ./scripts/get-repository.sh website
$ cd docs
$ make html  # Requires rst2html
$ make man   # Requires a2x (http://asciidoc.org)
$ make api   # Requires sphinx
```

# Contributors

OfflineIMAP exists thanks to [all the people who contribute](https://github.com/OfflineIMAP/offlineimap/graphs/contributors).

[How To Contribute](CONTRIBUTING.rst).

<a href="https://github.com/OfflineIMAP/offlineimap/graphs/contributors"><img src="https://opencollective.com/offlineimap/contributors.svg?width=890" /></a>


# Backers

Thank you to all our backers! 🙏 [Become a backer](https://opencollective.com/offlineimap#backer)

<a href="https://opencollective.com/offlineimap#backers" target="_blank"><img src="https://opencollective.com/offlineimap/backers.svg?width=890"></a>


# Sponsors

Support OfflineIMAP by becoming a sponsor. Your logo will show up here with a link to your website. 

[Become A Sponsor of OfflineIMAP.](https://opencollective.com/offlineimap#sponsor)

<a href="https://opencollective.com/offlineimap/sponsor/0/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/1/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/2/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/3/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/4/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/5/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/6/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/7/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/8/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/offlineimap/sponsor/9/website" target="_blank"><img src="https://opencollective.com/offlineimap/sponsor/9/avatar.svg"></a>

