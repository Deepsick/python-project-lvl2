### Hexlet tests and linter status:
[![Actions Status](https://github.com/Deepsick/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Deepsick/python-project-lvl2/actions)
[![Github Actions Status](https://github.com/Deepsick/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/Deepsick/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/7a3afc14de0e0db48dec/maintainability)](https://codeclimate.com/github/Deepsick/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7a3afc14de0e0db48dec/test_coverage)](https://codeclimate.com/github/Deepsick/python-project-lvl2/test_coverage)

# Gendiff

Read files and return diff according to picked format


## Installation

Python packaging and dependency management tool ```Poetry``` should be preinstalled.

```bash
make build
make package-install
```


## Usage

```bash
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help                 show this help message and exit
  -f FORMAT, --format FORMAT set format of output
```

### JSON

[![asciicast](https://asciinema.org/a/408QmrwUiO6MSOUZGsVOVn5bk.svg)](https://asciinema.org/a/408QmrwUiO6MSOUZGsVOVn5bk)

### Stylish

[![asciicast](https://asciinema.org/a/ee5nFt1S6cYC6q8HVbsMNTy5X.svg)](https://asciinema.org/a/ee5nFt1S6cYC6q8HVbsMNTy5X)

### Plain

[![asciicast](https://asciinema.org/a/UXJboxF2MVMSeAl3qwAZKQ5xS.svg)](https://asciinema.org/a/UXJboxF2MVMSeAl3qwAZKQ5xS)

## Testing

```bash
make install
make lint
make test
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

[MIT](https://choosealicense.com/licenses/mit/)