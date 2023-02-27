# unity-starter
Stater code for playing with Unity

### Unity
If you haven't done so, download Unity (https://unity.com/download)


### Python dependencies
Create conda virtual environment by running in command line

```conda env create -f environment.yml```

Activate the virtual environment `unitystarter` by running

```conda activate unitystarter```

### Build Unity project
Create a new 3D project in Unity. You can name it `UnityStarter` and place it under the `unity` folder here.

#### Import packages
Open your project, in the `Project` window, 
right click the `Assets` folder and 
choose `Import Package --> Custom Package`. Select `unity/unitystarter.unitypackage`.

Now go to `Window --> Package Manager`, then search and install the `ml-agents` package.

Now you can build your package by going to `File --> Build and Run`. Save the built binary at 
`unity/UnityStarter/unitystarter.app`.

### Run the game in Python
Run the sample game by running ``python main.py``