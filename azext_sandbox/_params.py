# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import os.path
from argcomplete.completers import FilesCompleter
from azure.cli.core.commands.parameters import get_location_type, get_enum_type, file_type, tags_type, get_three_state_flag
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from knack.arguments import (CLIArgumentType, CaseInsensitiveList)

def load_arguments(self, _):
    with self.argument_context('gimme tips') as c:
        c.argument('foo', help='Optional foo.')