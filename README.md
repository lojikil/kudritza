# Overview:

In 2014, a colleague and I ran a CTF at the company I was working at. In order to safely (e.g. without impacting
our ability to run the game) have Remote Code Execution (RCE), I decided to write a _very_ simple programming language.
This language was meant to be:

- Simple to implemented: I didn't want to spend more than 8 hours on it.
- Simple to understand: I didn't want anyone spending more than 20 minutes trying to figure it out.
- Terrible: it's no fun to implement for a CTF that works perfectly.

All told, I've spent *maybe* 12 hours on this (including some cleanup this year for release). The repository has the
following files:

1. `README.md`: this file.
2. `LICENSE`: ISC license.
3. `kudritza.py`: the actual REPL/script runner.
4. `test.py`: a simple test system (and not at all complete).
5. `test_procedure.curl`: a simple test of the procedure system.
6. `web.py`: the original web harness

# Language background:

The language is meant to be a heady mix of [Curl](https://en.wikipedia.org/wiki/Curl_\(programming_language\)) and 
[Logo](https://en.wikipedia.org/wiki/Logo_(programming_language\)), with a bit of Scheme here & there. Some Examples:

1. `{define x 10}` defines a variable.
2. `{+ :x 10}` adds 10 to the value (`:`) of `x`.
3. `{define foo {fn {y} {+ :y 10}}}` defines a procedure.
4. `{:foo 10}` returns 20.

The language is lexically scoped (and terribly, implemented by dict copying), but Mostly Works™ as expected.
