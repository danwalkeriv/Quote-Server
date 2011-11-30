Quote Server
============

This is a quick and dirty application for serving up random quotes from a
simple database of quotes.  The quote database is a simple text format where
each quote consists of contiguous non-empty lines of text separated by one or
more empty lines.  Included in the repo is a file of Christmas quotes.

The program starts a server on port 8080.  A get request on the document root
of this server returns a quote chosen at random from the set of quotes.

In order to work, the bottle library must either be installed on the system or
the `bottle.py` file must be copied to the project directory.

The server currently only takes one optional parameter, the path to a quote
file.  In the future this may be augmented with an option to choose the
port that the server will listen on.
