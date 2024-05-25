# TypstDiff tool
## Introduction
TypstDiff is a tool to compare two documents with Typst extention.
Our tool takes two documents and marks changes made in both documents.
Styling of those changes can be set by user (more info in user guide).
TypstDiff marks:

* **insertions** - underlining inserted elements and putting on extra styling if specified by user
* **deletions** - striking out deleted elements and putting on extra styling if specified by user
* **updates** - adding old version of element to output file with strikeout and extra formating and new version of element to output file with underlining and extra formating from user.

Due to Typst tool being relatively new our project does not support some
particular features and elements of Typst documents. List of unnsupported
elements can be found on this page.

## TypstDiff processing
In the process of checking files for changes TypstDiff uses three main tools:

* **Pandoc** - for converting files from Typst to JSON format and back
    - Pandoc started supporting Typst extention only recently so a lot of features and typst elements are not converted properly - this is the reason for most of restriction in our tool. With newer versions of Pandoc, TypstDiff will probably also support more and more Typst features.
* **jsondiff** - for finding changes in both files
    - in some cases jsondiff marks changes in hard to predict way. For example adding element to the first element of a list will be marked as updating all elements till the last one, and last one will be marked as inserted. You must take this into consideration while using TypstDiff.
