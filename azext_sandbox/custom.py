from azure.cli.core._profile import Profile
import requests
import platform
import os
import uuid


DISABLE_VERIFY_VARIABLE_NAME = "AZURE_CLI_DISABLE_CONNECTION_VERIFICATION"

def should_disable_connection_verify():
    return bool(os.environ.get(DISABLE_VERIFY_VARIABLE_NAME))

def get_az_user_agent():
    # Dynamically load the core version
    from azure.cli.core import __version__ as core_version

    agents = ["AZURECLI/{}".format(core_version)]

    from azure.cli.core._environment import _ENV_AZ_INSTALLER
    if _ENV_AZ_INSTALLER in os.environ:
        agents.append('({})'.format(os.environ[_ENV_AZ_INSTALLER]))

    # msrest already has this
    # https://github.com/Azure/msrest-for-python/blob/4cc8bc84e96036f03b34716466230fb257e27b36/msrest/pipeline/universal.py#L70
    # if ENV_ADDITIONAL_USER_AGENT in os.environ:
    #     agents.append(os.environ[ENV_ADDITIONAL_USER_AGENT])

    return ' '.join(agents)

def get_az_rest_user_agent():
    """Get User-Agent for az rest calls"""

    agents = ['python/{}'.format(platform.python_version()),
              '({})'.format(platform.platform()),
              get_az_user_agent()
              ]

    return ' '.join(agents)

def do_stuff(cmd, foo="default foo", object_id="123"):
    print('Azure CLI sandbox extension!')
    """
    print(cmd.cli_ctx.cloud.name)
    print(vars(cmd.cli_ctx.cloud.endpoints))
    print(vars(cmd.cli_ctx.cloud.suffixes))
    print(cmd.cli_ctx.cloud.endpoints.active_directory)
    print(foo)
    """
    endpoint = cmd.cli_ctx.cloud.endpoints.microsoft_graph_resource_id
    profile = Profile(cli_ctx=cmd.cli_ctx)
    raw_token, _, _ = profile.get_raw_token(endpoint)
    token_type, token, _ = raw_token
    headers = {}
    headers['Authorization'] = '{} {}'.format(token_type, token)
    agents = [get_az_rest_user_agent()]
    headers['User-Agent'] = ' '.join(agents)
    headers["x-ms-client-request-id"] = str(uuid.uuid4())
    s = requests.Session()
    url = f"{endpoint}/v1.0/servicePrincipals/{object_id}" 
    req = requests.Request(method="GET", url=url, headers=headers)
    prepped = s.prepare_request(req)
    settings = s.merge_environment_settings(prepped.url, {}, None, not should_disable_connection_verify(), None)
    r = s.send(prepped, **settings)
    print(r.content)

    """
    #metadata = {"dataplaneEndpoints" : {"arcConfigEndpoint" : "testArcConfigEndpoint"}}
    metadata = {"asd" : {"arcConfigEndpoint" : "testArcConfigEndpoint"}}
    if cmd.cli_ctx.cloud.endpoints.resource_manager == "dogfoodEndpointTest":
        azure_cloud = "dogfood"
        config_dp_endpoint = "dogfoodConfigDpEndpoint"
    # Get the values or endpoints required for retreiving the Helm registry URL.
    if "dataplaneEndpoints" in metadata:
        config_dp_endpoint = metadata["dataplaneEndpoints"]["arcConfigEndpoint"]
    # Get the default config dataplane endpoint.
    if config_dp_endpoint is None:
        config_dp_endpoint = "defaultConfigDpEndpoint"
    """