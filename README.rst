Pelican_ based web site for PyCon LT conferences.

For how to use Pelican, read this:

http://docs.getpelican.com/en/3.5.0/publish.html#make

For contributors
================

If you would like to improve or update content of this web site, here is the
list of things you should know:

- All articles are reserved for conference events, because top menu is
  automatically generated from articles. It means, that all other pages have to
  be pages, not articles.

- Each new conference event is new article in this form
  ``content/{year}.rst``, time line for each conference goes to
  ``content/pages/{year}/programa.rst``.

- ``content/partials/`` folder is reserved for reStructuredText files, that can
  be included in other pages.

- Title page is specified in ``theme/templates/index.html``.


.. _Pelican: http://getpelican.com/
