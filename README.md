# Object-oriented scientific programming with C++

This repository contains the slides of the course _Object-oriented scientific programming with C++_ given at TU Delft under the two course codes TW3720TW (bachelor programme) and WI4771TU (master programme). The slides are offered in three different variants: 
-  `notebooks` are jupyterlab notebooks meant for studying the material before or after the lecture
-  `interactive slides` will be used during the lecture with the option to adjust the content interactively
-  `static slides` are static versions of the lecture slides

We strongly recomment using the notebooks and slides in the provided binder environment. Slides and notebooks **will not run** on a local JupyterLab installation because they require the [Jupyter kernel for C++](https://github.com/jupyter-xeus/xeus-cling) to be installed and configured properly. Note that **no support will be given** to make the slides and notebooks run on a local JupyterLab installation.

# Lecture 1 - November 11, 2026

This lecture introduces some of the basic C++ concepts: variables and constants, loops, namespaces and scopes, structuring programs into functions, passing arguments by value and reference, error handling with exceptions, fixed-size arrays and pointers.

| notebook | interactive slides | static slides | reader |primer | prompts |
| :------: | :----------------: | :-----------: | :----: | :----: | :-----: |
| [![Lecture 1][badge-binder-lecture]][binder-jupyterlab-lecture1] | [![Lecture 1][badge-binder-lecture]][binder-jupyternb-lecture1] | [![Lecture 1][badge-pages-lecture]][pages-lecture1] | [![Reader 1][badge-reader]][reader1] | [![Primer 1][badge-primer]][primer1] | [![Prompts 1][badge-prompts]][prompts1] |

[Download all printable PDFs (Releases)](https://github.com/mmoelle1/OospCpp/releases)

[badge-binder-lecture]: https://img.shields.io/badge/interactive-lecture-579ACA.svg?logo=data:image/png;base64,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&style=flat-square

[badge-pages-lecture]: https://img.shields.io/badge/static-lecture-579ACA.svg?style=flat-square
[badge-pdf-lecture]: https://img.shields.io/badge/pdf-lecture-579ACA.svg?style=flat-square
[badge-reader]: https://img.shields.io/badge/pdf-reader-579ACA.svg?style=flat-square
[badge-primer]: https://img.shields.io/badge/md-primer-579ACA.svg?style=flat-square
[badge-prompts]: https://img.shields.io/badge/md-prompts-579ACA.svg?style=flat-square

[binder-jupyterlab-lecture1]: https://mybinder.org/v2/gh/mmoelle1/OospCpp/binder?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fmmoelle1%252FOospCpp%26urlpath%3Dlab%252Ftree%252FOospCpp%252Fnotebooks%252Flecture1.ipynb%26branch%3D2026

[binder-jupyternb-lecture1]:
https://mybinder.org/v2/gh/mmoelle1/OospCpp/binder?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fmmoelle1%252FOospCpp%26urlpath%3Dtree%252FOospCpp%252Fnotebooks%252Flecture1.ipynb%26branch%3D2026

[pages-lecture1]: https://mmoelle1.github.io/OospCpp/_static/lecture1.slides.html

[pdf-lecture1]: https://mmoelle1.github.io/OospCpp/_static/lecture1.slides.html?print-pdf

[reader1]: https://github.com/mmoelle1/OospCpp/readers/Reader_week1.pdf

[primer1]: https://github.com/mmoelle1/OospCpp/primers/Primer_week1.md

[prompts1]: https://github.com/mmoelle1/OospCpp/prompts/Prompts_week1.md

&copy; Copyright 2026, Matthias Möller.
