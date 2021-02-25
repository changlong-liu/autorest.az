# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['vm virtual-machine'] = """
    type: group
    short-summary: Manage virtual machine with vm
"""

helps['vm virtual-machine assess-patch'] = """
    type: command
    short-summary: "Assess patches on the VM."
    examples:
      - name: Assess patch state of a virtual machine.
        text: |-
               az vm virtual-machine assess-patch --resource-group "myResourceGroupName" --name "myVMName"
"""

helps['vm virtual-machine wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm virtual-machine is met.
    examples:
      - name: Pause executing next line of CLI script until the vm virtual-machine is successfully created.
"""

helps['vm virtual-machine-scale-set-vm-extension'] = """
    type: group
    short-summary: Manage virtual machine scale set vm extension with vm
"""

helps['vm virtual-machine-scale-set-vm-extension list'] = """
    type: command
    short-summary: "The operation to get all extensions of an instance in Virtual Machine Scaleset."
    examples:
      - name: List extensions in Vmss instance.
        text: |-
               az vm virtual-machine-scale-set-vm-extension list --instance-id "0" --resource-group "myResourceGroup" \
--vm-scale-set-name "myvmScaleSet"
"""

helps['vm virtual-machine-scale-set-vm-extension show'] = """
    type: command
    short-summary: "The operation to get the VMSS VM extension."
    examples:
      - name: Get VirtualMachineScaleSet VM extension.
        text: |-
               az vm virtual-machine-scale-set-vm-extension show --instance-id "0" --resource-group "myResourceGroup" \
--vm-extension-name "myVMExtension" --vm-scale-set-name "myvmScaleSet"
"""

helps['vm virtual-machine-scale-set-vm-extension create'] = """
    type: command
    short-summary: "The operation to Create the VMSS VM extension."
    parameters:
      - name: --substatuses
        short-summary: "The resource status information."
        long-summary: |
            Usage: --substatuses code=XX level=XX display-status=XX message=XX time=XX

            code: The status code.
            level: The level code.
            display-status: The short localizable label for the status.
            message: The detailed status message, including for alerts and error messages.
            time: The time of the status.

            Multiple actions can be specified by using more than one --substatuses argument.
      - name: --statuses
        short-summary: "The resource status information."
        long-summary: |
            Usage: --statuses code=XX level=XX display-status=XX message=XX time=XX

            code: The status code.
            level: The level code.
            display-status: The short localizable label for the status.
            message: The detailed status message, including for alerts and error messages.
            time: The time of the status.

            Multiple actions can be specified by using more than one --statuses argument.
    examples:
      - name: Create VirtualMachineScaleSet VM extension.
        text: |-
               az vm virtual-machine-scale-set-vm-extension create --location "westus" --type-properties-type \
"extType" --auto-upgrade-minor-version true --publisher "extPublisher" --settings "{\\"UserName\\":\\"xyz@microsoft.com\
\\"}" --type-handler-version "1.2" --instance-id "0" --resource-group "myResourceGroup" --vm-extension-name \
"myVMExtension" --vm-scale-set-name "myvmScaleSet"
"""

helps['vm virtual-machine-scale-set-vm-extension wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the vm virtual-machine-scale-set-vm-extension \
is met.
    examples:
      - name: Pause executing next line of CLI script until the vm virtual-machine-scale-set-vm-extension is \
successfully created.
        text: |-
               az vm virtual-machine-scale-set-vm-extension wait --instance-id "0" --resource-group "myResourceGroup" \
--vm-extension-name "myVMExtension" --vm-scale-set-name "myvmScaleSet" --created
"""
