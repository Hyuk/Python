# Installation

### Python Installation
https://www.python.org/

* Download python install file from the website.

* Double click the install file and setup.

* Check the checkbox option for the Path

### Jupyter Notebook Installation

* Open CMD window
* Install Jupyter Notebook
```bash
$ pip install jupyter 
```
* Open Jupyter Notebook
```bash
$ jupyter notebook 
```

### How to run python.py file on CMD
```bash
$ C:/python/python37-32/python.exe D:/playground/python/python.py
```

### Python Virtual Environment Setup
* python_basic 이라는 python 가상환경을 만든다.
* python_basic 가상환경이 만들어 지면, Script 폴더로 들어가서 activate.bat을 실행한다.
* bash에서 잘 안되면, CMD 환경에서 진행한다.
```bash
$ python -m venv python_basic
$ cd Scripts
$ activate.bat
```
* How to check the list of the installed python packages
```bash
$ pip list
```
* How to install python packages
```bash
$ pip install simplejson
```
* main.py에서 설치한 python package를 불렀는데 오류가 난다면, 
* Visual Studio Code 좌측 하단에 interpreter 정보를 클릭 후, Enter interpreter path... > find... > Scripts > python.exe 를 선택한다.




* Open Command Palette (Ctrl + Shift + p)
```
>build
```
* Select "Tasks: Configure Default Build Task"
* Select "Create tasks.json file from template"
* Select "MSBuild"

* 여기까지 진행하면 .vscode 폴더가 생성되고 setting.json 파일과 tasks.json 파일이 생성된다.

tasks.json
```json
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build",
      "type": "shell",
      "command": "msbuild",
      "args": [
        // Ask msbuild to generate full paths for file names.
        "/property:GenerateFullPaths=true",
        "/t:build",
        // Do not generate summary otherwise it leads to duplicate errors in Problems panel
        "/consoleloggerparameters:NoSummary"
      ],
      "group": "build",
      "presentation": {
        // Reveal the output only if unrecognized errors occur.
        "reveal": "silent"
      },
      // Use the standard MS compiler pattern to detect errors, warnings and infos
      "problemMatcher": "$msCompile"
    }
  ]
}
```

* tasks.json 파일을 아래와 같이 변경해준다.
```json
{
  // See https://go.microsoft.com/fwlink/?Linkid=733558
  // for the documentation about the tasks json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Project Label",
      "type": "shell",
      "command": "python",
      "args": [
        "${file}"
      ],
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "options": {
        "env": {
          "PYTHONIOENCODING": "UTF-8"
        }
      },
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

* 그리고 Settings.json 파일에서 값을 복사해서 tasks.json 파일의 command 값에 대체해서 붙여넣기 해준다.
```json
{
  "python.pythonPath": "Scripts\\python.exe"
}
```
* tasks.json
```json
{
  // See https://go.microsoft.com/fwlink/?Linkid=733558
  // for the documentation about the tasks json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Project Label",
      "type": "shell",
      "command": "Scripts\\python.exe",
      "args": [
        "${file}"
      ],
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "options": {
        "env": {
          "PYTHONIOENCODING": "UTF-8"
        }
      },
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

* 그리고 json 파일들을 닫고,
* main.py파일에서 Crtl + Shift + b 키를 눌러 빌드를 실행하면, 
* hello world가 정상적으로 표시되는 것을 확인할 수 있습니다.

* Visual Studio Code > Setting 에서 다음 항목을 선택해제해 준다.
```
Python > Terminal: Activate Environment
Activate Python Environment in Terminal created using the Extension
```
* 해당 항목이 선택되어 있다면, 사용자 입력시 activation.bat이 출력되기 때문이다.