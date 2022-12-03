def showtipsurl(cmd, foo="default foo"):
    print('Azure CLI sandbox extension!')
    print(vars(cmd.cli_ctx.cloud))
    print(vars(cmd.cli_ctx.cloud.endpoints))
    print(vars(cmd.cli_ctx.cloud.suffixes))
    print(foo)