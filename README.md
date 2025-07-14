<h1 align="center">
CacheBoom!
</h1>

<h4 align="center">A tool for discovering Web Cache Deception and Web Cache Poisoning vulnerabilities</h4>

<p align="center">
<a href="https://github.com/omranisecurity/cacheboom/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/omranisecurity/cacheBoom/releases"><img src="https://img.shields.io/badge/release-v0.8.2-blue"></a>
<a href="https://twitter.com/omranisecurity"><img src="https://img.shields.io/twitter/follow/omranisecurity?logo=twitter"></a>
</p>

<p align="center">
    <a href="#features">Features</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#Contributing">Contributing</a>
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

## Usage

After installation, you can run CacheBoom from the command line to scan for Web Cache Deception (WCD) and Web Cache Poisoning (WCP) vulnerabilities.

### Basic Usage

To scan a single URL for cache poisoning:

```sh
python3 cacheboom.py --url https://target.com --mode cp
```

To scan for cache deception:

```sh
python cacheboom.py --url https://target.com --mode cd
```

### Advanced Options

- **Scan multiple URLs from a file:**
  ```sh
  python cacheboom.py --list urls.txt --mode cp
  ```
  `urls.txt` should contain one URL per line.

- **Use a raw HTTP request file:**
  ```sh
  python cacheboom.py --raw_request raw_request.txt --mode cp
  ```

- **Add cookies to your requests:**
  ```sh
  python cacheboom.py --url https://target.com --mode cp --cookie "name=value; name2=value2"
  ```

- **Set the number of threads (default is 10):**
  ```sh
  python cacheboom.py --url https://target.com --mode cp --thread 20
  ```

- **Silent mode (show only results):**
  ```sh
  python cacheboom.py --url https://target.com --mode cp --silent
  ```

### Help

To see all available options, run:
```sh
python cacheboom.py --help
```

Replace `https://target.com` with the target URL you want to test.

_For more examples, please refer to the [Documentation](https://github.com/omranisecurity/cacheboom/wiki)_

## Roadmap

- [x] Basic cache poisoning test implemented
- [x] Web Cache Deception detection coming soon
- [ ] Implement `--output` flag for saving results
- [ ] Add advanced cache poisoning tests from research literature


## Contributing
Contributions are welcome!
If you have ideas, bug reports, or feature requests, please open an issue in the [GitHub Issues](https://github.com/omranisecurity/cacheboom/issues) section before submitting a pull request. This helps us discuss and track changes
