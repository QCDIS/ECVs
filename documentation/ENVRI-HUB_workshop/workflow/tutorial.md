# How to run workflow

This is the instruction on how to run the workflow.

To run the workflow, you need to open the virtual lab in NaaVRE. If you are not in NaaVRE, click the link to the virtual lab (https://beta.naavre.net/vreapp/vl/ecvs) and press the `Launch my instance` button.

## Run the workflow using **parameter** input

To execute the workflow do the following:

<div style="display: inline-block">

|      | Step | Action |
| ---- | ---- | ------ |
| 1    | Open the workflow file | open [workflow](./workflows.naavrewf) |
| 2    | Start workflow         | ![img_tutorial_01](images/tutorial_01-Run_workflow.png "Start workflow") |
| 3    | Set parameter values   | ![img_tutorial_02](images/tutorial_02-Set_default_parameters.png "Set parameter values") | 
| 3.1  | Fill in default values | ![img_tutorial_03](images/tutorial_03-Use_default_parameters.png "Default parameter values")
| 3.2  | Change values          | argo_catalogue (DOXY, CHLA, ocean temperature)</br>longitude min and max, decimal degrees</br>latitude min and max, decimal degrees</br>date, yyyy-mm-dd</br>workflow name</br>|
| 4    | Execute workflow       | ![img_tutorial_04](images/tutorial_04-Exec_workflow.png "Execute workflow") |
| 5    | Check the progress     | ![img_tutorial_05](images/tutorial_05-Progress.png "Check the progress") |

> Option: the details of the progress can be found by pressing `Show in workflow engine` or https://staging.demo.naavre.net/argowf/workflows, login required.

</div>

## Retrieve the output data

In the `data` folder, you should see the result files from you workflow.
* jpg file: Plot of the data
* csv file: Qureied data table

You can download the file by doing right click, then pressing `download`.

| 1  | 2  | 3  | 4  |
| -- | -- | -- | -- |
| ![img_tutorial_06a-Result.png](images/tutorial_06a-Result.png "Result in data folder") | ![img_tutorial_06b-Result.png](images/tutorial_06b-Result.png "Result in data folder") | ![img_tutorial_06c-Result.png](images/tutorial_06c-Result.png "Result in data folder") | ![img_tutorial_06d-Result.png](images/tutorial_06d-Result.png "Result in data folder") |
