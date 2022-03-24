# Contributing to Raudio

Thank you for wanting to and taking the time to contribute!

What follows includes some basic suggestions and details on how and what you can contribute to **Raudio**.
___
### Table Of Contents

* [Code of Conduct](#code-of-conduct)

* [Resources](#resources)

* [Areas to Contribute To](#areas-to-contribute-to)
  * [Testing](#testing)
  * [Error Checking](#error-checking)
  * [Code Organization and Optimization](#code-organization-and-optimization)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggestions](#suggestions)

* [Pull Requests](#pull-requests)
___

## Code of Conduct

This project and all contributors must follow the [Raudio Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to follow these guidelines. 
Please report unacceptable behavior to an appropriate maintainer on our [Discord server](https://discord.gg/EBvyTrneGj).

## Resources
To get a familiarity with this platform, we recommend looking through our [GitHub wiki](https://github.com/raudio-project/raudio-server/wiki). If there are
any clarifications you need or additions you feel would improve our wiki, feel free to add to it.

Secondly, we have a [Discord server](https://discord.gg/EBvyTrneGj) as our main method of communication for this project, so feel free to join it.

If you are unfamiliar with the packages used in this project or are new to Python itself, here are some links you may find useful. Remember to adhere to the
[_Hands-on Imperative of the Hacker Ethic_](https://en.wikipedia.org/wiki/Hacker_ethic#:~:text=Employing%20the%20Hands%2DOn%20Imperative,that%20improvements%20can%20be%20made.). 
But also, don't hesitate to ask any questions! Discussion is welcomed as it can benefit everyone involved. Remember to join our [Discord server](https://discord.gg/EBvyTrneGj)
where you can find and chat with Raudio contributors.
  * [GStreamer](https://gstreamer.freedesktop.org/)
  * [gst-python](https://gitlab.freedesktop.org/gstreamer/gst-python)
  * [rtpbin](https://gstreamer.freedesktop.org/documentation/rtpmanager/rtpbin.html?gi-language=c)
  * [ffmpeg](https://ffmpeg.org/)
  * [Python](https://www.python.org/about/gettingstarted/)

## Areas to Contribute to

### Testing
**Raudio** currently has no automated testing. Unit tests would make the entire process of changing pieces of the program a lot more efficient because it would 
eliminate the need for manual testing. Thus far, manual testing has consisted of running a server having some audio files and using client commands, 
observing if the server responds and executes an appropriate response.

### Code Organization and Optimization
**Raudio**, as of its initial release, is satisfactorily organized. As the project expands and new features are added, problems of code duplication, dead code, and/or
poor organization in general may arise. Therefore, any contributions that can mitigate these problems, if prevalent, would be greatly appreciated. 

### Reporting Bugs
To report a bug that you may have encountered with **Raudio**, [open an issue](https://github.com/raudio-project/raudio-server/issues) with a _bug_ label. 
Please include steps to replicate said error and any information about your system that may be relevant to the issue. Before creating an issue, please check the
current issues, and/or start a discussion in the issues channel of our Discord server. If the bug found already appears to be a known issue, add your input
to the existing issue instead of creating a new one. If you are unsure whether you are experiencing a bug or a _feature_, feel free to consult with the community
the Discord server.

### Suggestions
We are open to any suggestions for **Raudio** that were not already listed above! Please [open an issue](https://github.com/raudio-project/raudio-server/issues) 
with an _enchancement_ label and elaborate, to a reasonable extent, what your suggestion is. Alternatively, suggestions could be brought up with maintainers directly
through the Discord server. Finally, this is a reminder that the project is _open source_, and that anyone is free to contribute and make a suggestion come to life,
under reasonable assumption.

## Pull Requests

To submit a bug fix or new feature, [create a pull request](https://github.com/raudio-project/raudio-server/pulls) to a new branch of this repository.
When you create a new pull request, please fill out the contents of the request will as much info as you can, to the best of your ability. Remember to apply
any appropriate labels and prepend the title of your pull request with a categorization (i.e. [Bug Fix], [New Feature], [Refactorization]).
1. Fork this repository
3. Make changes to your fork of the repository
4. Ensure your changes are working properly (through manual or automated testing)
5. [Create a pull request](https://github.com/raudio-project/raudio-server/pulls)
