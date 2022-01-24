# dotbot-ifarch

Conditional execution of dotbot directives based on the local architecture with thanks to [dotbot-ifplatform](https://github.com/ssbanerje/dotbot-ifplatform).

## Prerequisites
This plugin requires [`dotbot`](https://github.com/anishathalye/dotbot) to be installed.

## Installation
1. Run `git submodule add https://github.com/ryansch/dotbot-ifarch.git`
2. Run `git submodule update --init --recursive`
3. Pass in the CLI argument `--plugin-dir dotbot-ifarch` when executing the `dotbot` executable.

## Usage

Add the `if<arch>` directive to the `dotbot` YAML file to conditionally execute the directives.
For example:

```yaml
- ifaarch64:
    - shell:
        - echo Raspberry pi?

- ifarm64:
    - shell:
        - echo Apple Silicon?

- ifx86_64:
    - shell:
        - echo Intel/AMD
```

### Details

The plugin queries the local architecture using the `platform` module which uses `uname -m`.
Acceptable values of `<arch>` in the `if<arch>` directive are shown below:

- `aarch64`
- `arm64`
- `armv7l`
- `x86_64`

NOTE: Issues/PRs will be accepted to help fill out this list.
