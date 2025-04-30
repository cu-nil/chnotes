# Working with GitHub

## Storage

* GitHub will [complain about any file committed over 50MB](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

* The hard quota is 100MB. Everything larger has to go to LFS.

* LFS has a hard cap at [4GB for teams](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage), but we are also metered.

* That is, using LFS has an inherent cost in terms of storage (how much you upload) and bandwidth (how much you download). In short, we should **avoid using LFS**. It solves nearly nothing.
