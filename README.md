# Sandbox project for Azure CLI extensions

## Instructions
    cd C:\...\azure-cli-extension-sandbox\sandbox
    python setup.py bdist_wheel
    az extension remove --name sandbox
    az extension add --source C:\...\azure-cli-extension-sandbox\sandbox\dist\sandbox-0.0.1-py2.py3-none-any.whl
    az do stuff