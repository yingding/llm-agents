## Creat VENV
use the `create_env.sh` script to create a venv on windows, the `create_env.sh` file located current in a different project

```powershell
cd $env:USERPROFILE\Documents\VCS\llm-train;

$VERSION="3.12";
$ENV_NAME="agents";
$ENV_SURFIX="pip";
$PM="pip";
.\envtools\create_env.ps1 -VERSION $VERSION -ENV_NAME $ENV_NAME -ENV_SURFIX $ENV_SURFIX -PM $PM;
```

Install the packages in the curent project
```powershell
cd $env:USERPROFILE\Documents\VCS\llm-agents;
$PackageFile="requirements_win.txt";
Invoke-Expression "(Get-Command python).Source";
& "python" -m pip install -r $PackageFile --no-cache-dir;
```

## Install packages (general)
```powershell
$VERSION="3.12";
$ENV_NAME="agents";
$ENV_SURFIX="pip";
$ENV_FULL_NAME = "$ENV_NAME$VERSION$ENV_SURFIX";
$PackageFile="requirements_win.txt";
& "$env:USERPROFILE\Documents\VENV\$ENV_FULL_NAME\Scripts\Activate.ps1";
Invoke-Expression "(Get-Command python).Source";

& "python" -m pip install --upgrade pip;
& "python" -m pip install -r $PackageFile --no-cache-dir;

deactivate
```

Note:
* Use `python` instead of `python3` on windows os

## Add a jupyter notebook kernel to VENV
```powershell
$VERSION="3.12";
$ENV_NAME="agents";
$ENV_SURFIX="pip";
$ENV_FULL_NAME = "$ENV_NAME$VERSION$ENV_SURFIX";

& "$env:USERPROFILE\Documents\VENV\$ENV_FULL_NAME\Scripts\Activate.ps1";
Invoke-Expression "(Get-Command python).Source";

& "python" -m pip install --upgrade pip
& "python" -m pip install ipykernel

deactivate
```

We need to reactivate the venv so that the ipython kernel is available after installation.
```powershell
# ipython kernel install --user --name=$env:ENV_NAME
python -m ipykernel install --user --name=$ENV_FULL_NAME --display-name $ENV_FULL_NAME
```
Note: 
* restart the vs code, to select the venv as jupyter notebook kernel 
* name is `$env:ENV_NAME`, which is the venv name.

Reference:
* https://ipython.readthedocs.io/en/stable/install/kernel_install.html
* https://anbasile.github.io/posts/2017-06-25-jupyter-venv/

## (Optional) Remove ipykernel
```powershell
# jupyter kernelspec uninstall -y <VENV_NAME>
$VERSION="3.12";
$ENV_NAME="agents";
$ENV_SURFIX="pip";
$ENV_FULL_NAME = "$ENV_NAME$VERSION$ENV_SURFIX";

jupyter kernelspec uninstall -y $ENV_FULL_NAME
```

## (Optional) Remove all package from venv
For the venv python
```powershell
which python
python -m pip freeze | %{$_.split('==')} | %{python -m pip uninstall -y $_}
python -m pip list
```

Note: `which` cmd can be installed from powershell with `winget install which`

For the system python3
```powershell
which python3
python3 -m pip freeze | %{$_.split('==')} | %{python3 -m pip uninstall -y $_}
python3 -m pip list
```