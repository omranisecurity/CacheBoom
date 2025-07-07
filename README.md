<h1 align="center">
CacheBoom!
</h1>

<h4 align="center">A tool for discovering Web Cache Deception and Web Cache Poisoning vulnerabilities</h4>

<p align="center">
<a href="https://github.com/omranisecurity/cacheboom/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/omranisecurity/cacheBoom/releases"><img src="https://img.shields.io/badge/release-v0.8.0-blue"></a>
<a href="https://twitter.com/omranisecurity"><img src="https://img.shields.io/twitter/follow/omranisecurity?logo=twitter"></a>
</p>

<p align="center">
    <a href="#features">Features</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#examples">Examples</a>
</p>

---

## Features

- Scan and identify Web Cache Deception and Web Cache Poisoning vulnerabilities
- Simple and user-friendly command-line interface
- Readable result reporting

## Quick Start

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.x must be installed.
- Internet access to install dependencies.

### Installation

1. Clone the repository:
     ```sh
     git clone https://github.com/omranisecurity/cacheboom.git
     cd cacheboom
     ```
2. Install required packages:
     ```sh
     pip install -r requirements.txt
     ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

After installation, you can run CacheBoom from the command line. For example:

```sh
python cacheboom.py --url https://target.com --mode cp
```

Replace `https://target.com` with the target URL you want to test.

_For more examples, please refer to the [Documentation](https://github.com/omranisecurity/cacheboom/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
## Roadmap

- [x] Added a simple test case for cache poisoning
- [ ] Advanced test cases for cache poisoning will be collected from various research papers and added soon
- [ ] Web Cache Deception vulnerability detection will be added soon

## Contributing