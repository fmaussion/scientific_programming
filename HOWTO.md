HOWTO use this repository
-------------------------

- install [nbstripout](https://github.com/kynan/nbstripout) and apply it to this git repository (``nbstripout --install --attributes .gitattributes``)
- install [this branch](https://github.com/fmaussion/bookbook/tree/add-toc) of [bookbook](https://github.com/takluyver/bookbook) (for context: see this [PR](https://github.com/takluyver/bookbook/pull/13))
- install the laster repository version of [jupyter_contrib_nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) (or a version later than [this PR](https://github.com/ipython-contrib/jupyter_contrib_nbextensions/pull/1252)). Activate the spell-checking and Table of Contents extensions
- to modify the notebooks, start a normal jupyter-notebook server from the repository's root (this is necessary to display the images correctly).
- to create the html output, run ``python -m bookbook.html notebooks/`` from the repository's root.

This should be it!

