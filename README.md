# unity-starter
Stater code for playing with Unity

### Unity
If you haven't done so, download Unity (https://unity.com/download)


### Python dependencies
Create conda virtual environment by running in command line. Note that Python version higher than 3.9 doesn't work right now.

```conda env create -f environment.yml python=3.9```

Activate the virtual environment `unitystarter` by running

```conda activate unitystarter```

### Build Unity project
Create a new 3D project in Unity. You can name it `UnityStarter` and place it under the `unity` folder here.

#### Import packages
Open your project, in the `Project` window, 
right click the `Assets` folder and 
choose `Import Package --> Custom Package`. Select `unity/unitystarter.unitypackage`. You will probably need to go up one level in the file hierarchy to find this.

Now go to `Window --> Package Manager`, 
change `Packages: In Project` to `Packages: Unity Registry`, then search and install the `ml-agents` package.

Now go to `Scenes` folder in the `Assets` window in the bottom, and double click `WaterballScene`.

Now you can build your package by going to `File --> Build and Run`. Save the built binary at 
`unity/UnityStarter/unitystarter.app`.

### Run the game in Python
Run the sample game by running ``python main.py``
