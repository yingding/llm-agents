## Creat VENV
use the `create_env.sh` script to create a venv on macosx

```powershell
$env:VERSION = "3.11"
$env:ENV_NAME = "agents$env:VERSION"
#TODO

# source ./envtools/create_env.sh -p ~/VENV/${ENV_NAME} -v $VERSION
```

## Install packages 
```powershell
$env:VERSION = "3.11";
$env:ENV_NAME = "agents$env:VERSION";
& "$HOME\Documents\VENV\$env:ENV_NAME\Scripts\Activate.ps1";
python -m pip install --upgrade pip;
python -m pip install -r requirements_win.txt --no-cache-dir;
```

Note:
* Use `python` instead of `python3` on windows os

## Add a jupyter notebook kernel to VENV
```powershell
$env:VERSION = "3.11"
$env:ENV_NAME = "agents$env:VERSION"
& "$HOME\Documents\VENV\$env:ENV_NAME\Scripts\Activate.ps1"
python -m pip install --upgrade pip
python -m pip install ipykernel
deactivate
```

We need to reactivate the venv so that the ipython kernel is available after installation.
```powershell
# ipython kernel install --user --name=$env:ENV_NAME
python -m ipykernel install --user --name=$env:ENV_NAME --display-name $env:ENV_NAME
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
$env:VERSION = "3.11"
$env:ENV_NAME = "agents$env:VERSION"
jupyter kernelspec uninstall -y $env:ENV_NAME
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