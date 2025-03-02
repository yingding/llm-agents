# cd to the directory
cd $env:USERPROFILE\Documents\VCS\llm-agents;

# activate python env
$VERSION="3.12";
$ENV_NAME="agents";
$ENV_SURFIX="pip";
$ENV_FULL_NAME = "$ENV_NAME$VERSION$ENV_SURFIX";
& "$env:USERPROFILE\Documents\VENV\$ENV_FULL_NAME\Scripts\Activate.ps1";

# test python version
Invoke-Expression "(Get-Command python).Source";