from knack.help_files import helps

from azure.cli.core import AzCommandsLoader

helps['gimme tips'] = """
    type: command
    short-summary: Points you to a world of Azure Tips and Tricks.
"""

class TipsAndTricksCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_sandbox.custom#{}')
        super(TipsAndTricksCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=custom_type)

    def load_command_table(self, args):
        from azext_sandbox.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_sandbox._params import load_arguments
        load_arguments(self, command)

COMMAND_LOADER_CLS = TipsAndTricksCommandsLoader