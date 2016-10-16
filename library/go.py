#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: go
short_description: Install go package.
options:
  name:
    description:
    - A package name, like (github.com/github/hub)
    required: true
  executable:
    description:
      - The executable location for go.
    required: false
  command:
    description:
      - subcommand
    required: false
    default: "get"
  install:
    description:
      - When this option is false, it instructs get not to install the package.
    required: false
    default: true
  update:
    description:
      - When this option is true, it instructs get to use the network to update the named packages and their dependencies.
    required: false
    default: false
requirements:
- go
author: "Suzuki Shunsuke"
'''

EXAMPLES = '''
# Install hub
go:
  name: github.com/github/hub

# Specify the path of go command
go:
  name: github.com/github/hub
  executable: /usr/local/go/bin/go

# Not install
go:
  name: github.com/github/hub
  install: no

# Update
go:
  name: github.com/github/hub
  update: yes
'''

RETURN = '''
'''

import json

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(argument_spec={
        "name": {"required": True, "type": "str"},
        "executable": {"required": False, "default": "go", "type": "str"},
        "install": {"required": False, "default": True, "type": "bool"},
        "update": {"required": False, "default": False, "type": "bool"},
        "command": {
            "required": False, "default": "get",
            "choices": ["get"]
        },
    })
    # module.run_command_environ_update = APT_ENV_VARS
    params = module.params
    go = params["executable"]
    command = params["command"]
    package = params["name"]
    install = params["install"]
    update = params["update"]

    cmd = [go, command]
    if not install:
        cmd.append("-d")
    if update:
        cmd.append("-u")
    cmd.append(package)

    rc, out, err = module.run_command(cmd)
    if rc:
        module.fail_json(msg=err, stdout=out)
    else:
        module.exit_json(changed=True, stdout=out, stderr=err)


if __name__ == '__main__':
    main()
