<div class="inner">

<div id="toplinks">

[Skip to main text](#content) <span class="gnun-split"></span> [Set language
<span class="gnun-split"></span>](/server/select-language.html?callback=/software/make/)

</div>

<div id="searcher">

<div>

</div>

</div>

<div id="translations">

<span class="original" dir="ltr">[English](/software/make/) \[en\]</span>

</div>

<div style="clear: both">

</div>

<div id="header">

<div id="fsf-frame">

[JOIN THE FSF](https://www.fsf.org/associate/support_freedom?referrer=4052)

<div id="fssbox">

[Free Software Supporter](//www.fsf.org/fss)

<div>

</div>

</div>

</div>

<div id="gnu-banner">

[![\[A GNU head\]](/graphics/heckert_gnu.transp.small.png)**GNU** Operating System](/)

Sponsored by the [Free Software Foundation](#mission-statement)

</div>

<div style="clear:both">

</div>

</div>

<div id="navigation">

  - <span id="tabAboutGNU">[ABOUT GNU](/gnu/gnu.html)</span>
  - <span id="tabPhilosophy">[PHILOSOPHY](/philosophy/philosophy.html)</span>
  - <span id="tabLicenses">[LICENSES](/licenses/licenses.html)</span>
  - <span id="tabEducation">[EDUCATION](/education/education.html)</span>
  - <span id="tabSoftware"><span class="no-display">=</span> [SOFTWARE](/software/software.html)
    <span class="gnun-split"></span> <span class="no-display">=</span></span>
  - <span id="tabDoc">[DOCS](/doc/doc.html)</span>
  - <span id="tabHelp">[HELP GNU](/help/help.html)</span>
  - <span id="more-links">[More ▼](#fsf-links)</span>

<div style="clear:both">

</div>

</div>

<div id="content">

## GNU Make

GNU Make is a tool which controls the generation of executables and other non-source files of a
program from the program's source files.

Make gets its knowledge of how to build your program from a file called the *makefile*, which lists
each of the non-source files and how to compute it from other files. When you write a program, you
should write a makefile for it, so that it is possible to use Make to build and install the program.

#### Capabilities of Make

  - Make enables the end user to build and install your package without knowing the details of how
    that is done -- because these details are recorded in the makefile that you supply.

  - Make figures out automatically which files it needs to update, based on which source files have
    changed. It also automatically determines the proper order for updating files, in case one
    non-source file depends on another non-source file.
    
    As a result, if you change a few source files and then run Make, it does not need to recompile
    all of your program. It updates only those non-source files that depend directly or indirectly
    on the source files that you changed.

  - Make is not limited to any particular language. For each non-source file in the program, the
    makefile specifies the shell commands to compute it. These shell commands can run a compiler to
    produce an object file, the linker to produce an executable, `ar` to update a library, or TeX or
    Makeinfo to format documentation.

  - Make is not limited to building a package. You can also use Make to control installing or
    deinstalling a package, generate tags tables for it, or anything else you want to do often
    enough to make it worth while writing down how to do it.

#### Make Rules and Targets

A *rule* in the makefile tells Make how to execute a series of commands in order to build a *target*
file from source files. It also specifies a list of *dependencies* of the target file. This list
should include all files (whether source files or other targets) which are used as inputs to the
commands in the rule.

Here is what a simple rule looks like:

    target:   dependencies ...
              commands
              ...

When you run Make, you can specify particular targets to update; otherwise, Make updates the first
target listed in the makefile. Of course, any other target files needed as input for generating
these targets must be updated first.

Make uses the makefile to figure out which target files ought to be brought up to date, and then
determines which of them actually need to be updated. If a target file is newer than all of its
dependencies, then it is already up to date, and it does not need to be regenerated. The other
target files do need to be updated, but in the right order: each target file must be regenerated
before it is used in regenerating other targets.

#### Advantages of GNU Make

GNU Make has many powerful features for use in makefiles, beyond what other Make versions have. It
can also regenerate, use, and then delete intermediate files which need not be saved.

GNU Make also has a few simple features that are very convenient. For example, the `-o file` option
which says \`\`pretend that source file *file* has not changed, even though it has changed.'' This
is extremely useful when you add a new macro to a header file. Most versions of Make will assume
they must therefore recompile all the source files that use the header file; but GNU Make gives you
a way to avoid the recompilation, in the case where you know your change to the header file does not
require it.

However, the most important difference between GNU Make and most versions of Make is that GNU Make
is free software.

#### Makefiles And Conventions

We have developed conventions for how to write Makefiles, which all GNU packages ought to follow. It
is a good idea to follow these conventions in your program even if you don't intend it to be GNU
software, so that users will be able to build your package just like many other packages, and will
not need to learn anything special before doing so.

These conventions are found in the chapter [\`\`Makefile conventions'' (147 k
characters)](/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions) of the [GNU
Coding Standards (147 k characters)](/prep/standards.html).

### Downloading Make

Make can be found on the main GNU ftp server: <http://ftp.gnu.org/gnu/make/> (via HTTP) and
<ftp://ftp.gnu.org/gnu/make/> (via FTP). It can also be found on the [GNU mirrors](/prep/ftp.html);
please [use a mirror](http://ftpmirror.gnu.org/make/) if possible.

### Documentation

[Documentation for Make](manual/) is available online, as is [documentation for most GNU
software](/manual/). You may also find more information about Make by running *info make* or
*man make*, or by looking at */usr/share/doc/make/*, */usr/local/doc/make/*, or similar directories
on your system. A brief summary is available by running *make --help*.

### Mailing lists

Make has the following mailing lists:

  - [bug-make](https://lists.gnu.org/mailman/listinfo/bug-make) is used to discuss most aspects of
    Make, including development and enhancement requests, as well as bug reports.
  - [help-make](https://lists.gnu.org/mailman/listinfo/help-make) is for general user help and
    discussion.

Announcements about Make and most other GNU software are made on
[info-gnu](http://lists.gnu.org/mailman/listinfo/info-gnu)
([archive](http://lists.gnu.org/archive/html/info-gnu/)).

Security reports that should not be made immediately public can be sent directly to the maintainer.
If there is no response to an urgent issue, you can escalate to the general
[security](http://lists.gnu.org/mailman/listinfo/security) mailing list for advice.

### Getting involved

Development of Make, and GNU in general, is a volunteer effort, and you can contribute. For
information, please read [How to help GNU](/help/). If you'd like to get involved, it's a good idea
to join the discussion mailing list (see above).

  - Test releases  
    Trying the latest test release (when available) is always appreciated. Test releases of Make can
    be found at <http://alpha.gnu.org/gnu/make/> (via HTTP) and <ftp://alpha.gnu.org/gnu/make/> (via
    FTP).
  - Development  
    For development sources, issue trackers, and other information, please see the [Make project
    page](http://savannah.gnu.org/projects/make/) at [savannah.gnu.org](http://savannah.gnu.org).
  - Translating Make  
    To translate Make's messages into other languages, please see the [Translation Project page for
    Make](http://translationproject.org/domain/make.html). If you have a new translation of the
    message strings, or updates to the existing strings, please have the changes made in this
    repository. Only translations from this site will be incorporated into Make. For more
    information, see the [Translation Project](http://translationproject.org/html/welcome.html).
  - Maintainer  
    Make is currently being maintained by Paul Smith. Please use the mailing lists for contact.

### Licensing

Make is free software; you can redistribute it and/or modify it under the terms of the [GNU General
Public License](http://www.gnu.org/licenses/gpl.html) as published by the Free Software Foundation;
either version 3 of the License, or (at your option) any later version.

</div>

<div style="clear:both">

</div>

<div id="back-to-top">

[TOP ▲](#navigation)

</div>

-----

<div id="fsf-links">

  - [MALWARE](/proprietary/proprietary.html)
  - [GNU ART](/graphics/graphics.html)
  - [GNU'S WHO?](/people/people.html)
  - [SITEMAP](/server/sitemap.html)
  - [SOFTWARE DIRECTORY](//directory.fsf.org)
  - [HARDWARE](https://h-node.org/)

</div>

<div id="mission-statement">

> [![\[FSF logo\]](/graphics/fsf-logo-notext-small.png)](//www.fsf.org) **“The Free Software
> Foundation (FSF) is a nonprofit with a worldwide mission to promote computer user freedom. We
> defend the rights of all software users.”**

[JOIN](//www.fsf.org/associate/support_freedom?referrer=4052) [DONATE](//donate.fsf.org/)
[SHOP](//shop.fsf.org/)

</div>

<div id="footer">

<div class="unprintable">

Please send general FSF & GNU inquiries to [\<gnu@gnu.org\>](mailto:gnu@gnu.org). There are also
[other ways to contact](/contact/) the FSF. Broken links and other corrections or suggestions can be
sent to [\<bug-make@gnu.org\>](mailto:bug-make@gnu.org).

Please see the [Translations README](/server/standards/README.translations.html) for information on
coordinating and submitting translations of this article.

</div>

Copyright © 2019 Free Software Foundation, Inc.

This page is licensed under a [Creative Commons Attribution-NoDerivatives 4.0 International
License](http://creativecommons.org/licenses/by-nd/4.0/).

<div id="bottom-notes" class="unprintable">

[Copyright Infringement Notification](//www.fsf.org/about/dmca-notice)

<div id="generic">

</div>

</div>

Updated: $Date: 2020/01/19 22:30:06 $

</div>

</div>
