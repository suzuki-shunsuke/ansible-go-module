# ansible-go-module

[![Build Status](https://travis-ci.org/suzuki-shunsuke/ansible-go-module.svg?branch=master)](https://travis-ci.org/suzuki-shunsuke/ansible-go-module)

Manage go packages with go command.

## Notice

* This module supports only the "go get" command.
* This module doesn't support the check mode.
* If this module succeeds, the result's changed attribute is always true.

## Requirements

* Go

## Install

In the following example this module is installed in ~/ansible/modules directory.

```
$ mkdir -p ~/ansible/modules
$ export ANSIBLE_LIBRARY=~/ansible/modules
$ git clone suzuki-shunsuke/ansible-go-module ~/ansible/modules/ansible-go-module
```

## Options

parameter | required | default | choices | comments
--- | --- | --- | --- | ---
name | yes | | | The name of go package to install
executable | no | | | The executable path of go command
gopath | no | | | The environment variable GOPATH
install | no | yes | bool | If no, the -d option is added to "go get" command
update | no | no | bool | If yes, the -u option is added to "go get" command
command | no | get | get | The subcommand of "go" command. Now support only "get"

## Example

```yaml
# Install hub
go:
  name: github.com/github/hub

# Specify GOPATH and the path of go command
go:
  name: github.com/github/hub
  executable: /usr/local/go/bin/go
  gopath: /home/vagrant/.go

# Not install
go:
  name: github.com/github/hub
  install: no

# Update
go:
  name: github.com/github/hub
  update: yes
```

## Licence

MIT
