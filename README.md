# <font color="Green">Wind Turbines 2nd✋ - Inventory tool</font>  
The following project consists of a **quick tool for tracking wind turbines in inventory** for small business enterprises. This case recreated a fictiony company orientated to repowering wind turnines.  

### Objectives
* Develop a friendly checking inventory tool to control wind turbine in the warehouse. The information can be printed out in TXT and PDF files. 

### User Stories - UX

- ### As an employee of an inventory department, I would like the following:
  - ### Friendly tool to add wind turbines to the company's inventory.
  - ### Friendly tool to remove wind turbines from the company's inventory.
  - ### Friendly tool to see a quick breakdown of the company's inventory. 
  - ### Friendly tool to update/modify details of the wind turbines in inventory. 
  - ### Friendly tool to print out wind turbines from the company's inventory.
  - ### Friendly option to exit the software.

### Feature Planning - Snapshot.

- ### Smooth user navigation process when the tool is used.
- ### Display current date.
- ### Smooth Add, Remove, Visuallitation, and Update of data for the user. 
- ### Export options of txt & pdf files with a basic breakdown of the data entered by the user(s).
- ### Straight forward option to exit.

### Design
The present software version is a raw tool, i.e., no images. However, it has been included some **symbol emoji** and colours also. The colors used are as follow: **Green, Blue, Cyan, Yellow, and Red**.

The current version offers to the user(s) the following options: ADD items, LIST items, REMOVE items, UPDATE items, PRINT REPORT IN TXT & PDF files.

  ### Implementation
  This tool support structure is as follows:
  - #### Main Menu: ADD, DELETE, LIST,  UDPATE, EXPORT FILES  [PDF & TXT], & EXIT options. See image 1 below.

![./images/Main_Menu.JPG](./images/Main_Menu.JPG)
<center>image 1</center>

  - #### ADD option: Agent Name, Manufacturer, Model, Country, Year, Nominal Power [kW]. See image 2 below.
![./images/Main_Menu.JPG](./images/adding%20wind%20turbine.JPG)
<center>image 2</center>

  - #### DELETE option: Select the item to remove and message confirmation. See images 3 & 4 below.
![./images/Main_Menu.JPG](./images/delete%20wind%20turbine%20option%202.JPG)
<center>image 3</center>

![./images/Main_Menu.JPG](./images/display%20inventory%20after%20deleting%20wind%20turbine.JPG)
<center>image 4</center>

  - #### LIST option: Display Item(s) in Inventory. See image 5 below.

![./images/Main_Menu.JPG](./images/display%20windturbines.JPG)
<center>image 5. This image prior to be deleted item 2.</center>


  - #### Update option: Same fields as ADD option to be updated. See image 6 below.

![./images/Main_Menu.JPG](./images/windturbine%20updated.JPG)
<center>image 6</center>

  - #### Export option 5 & 6: TXT & PDF Files produced. See image 7 below.
![./images/Main_Menu.JPG](./images/txt%20pdf%20files%20exported.JPG)<center>image 7</center>


  - #### EXIT option - 7 -: Leave the tool. See image 8 below.
![./images/Main_Menu.JPG](./images/exit%20option.JPG)<center>image 8</center>

### Data Model

- #### OOP & class use
The coding includes class level(s) to create different instances depending on user choice and navigation.

- #### Error Handling / Validation
The draft or initial version didn't include any statement or code clause to capture and inform if the user's input were valid or invalid, the print statement was used only. However, there have been included functions and statements to improve the current software version regarding errors detection.

If and try/except statements were implemented all over the coding to handle errors. However, this demands more time testing to detect as many user errors as possible to improve more the code and mitigate issues. See main comments below.

  #### a. The user(s) must type the correct option's number from the main menu, otherwise, an alert message will pop up unit the user select the correct option.
 ##### b. In the sub-menu level, user must input the correct info, otherwise, they will be alert to repeat the operation in red colour and returning to the main menu in all the cases.
 ##### c. if user(s) request any option without a prior data input, the software will alert to the user(s) with an alert in red colour.
  ##### d. The fields of Manufacturer & Model are free of character restrictions due to their input nature. Other input fields have been validated.

- #### Validator Testing
The coding includes class level(s) to create different instances depending on user choice and navigation. See images (9-20) of testing completed below.

  - #### Main Menu: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%201%20main%20menu.JPG)<center>image 9</center>

  - #### Main Menu: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%202%20main%20menu.JPG)<center>image 10</center>

  - #### Main Menu: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%203%20main%20menu.JPG)<center>image 11</center>

  - #### Main Menu: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%204%20main%20menu.JPG)<center>image 12</center>

  - #### Main Menu: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%205%20main%20menu.JPG)<center>image 13</center>

  - #### Main Menu: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%206%20main%20year.JPG)<center>image 14</center>

  - #### Add: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%201%20add.JPG)<center>image 15</center>

  - #### Add: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%201%20add%20country.JPG)<center>image 16</center>

  - #### Add: Wrong input.
![./images/Main_Menu.JPG](./images/validation/validation%201%20add%20power.JPG)<center>image 17</center>

  - #### Delete: Wrong input and correct input.
![./images/Main_Menu.JPG](./images/validation/validation_1_delete.JPG)<center>image 18</center>

  - #### List: Wrong input and correct input.
![./images/Main_Menu.JPG](./images/validation/validation%20lis%20turbines.JPG)<center>image 19</center>

  - #### List: Wrong input and correct input.
![./images/Main_Menu.JPG](./images/validation/validation%20update%20item.JPG)<center>image 20</center>

 - #### Accessibility & Performance, see results below:

![./images/Main_Menu.JPG](./images/validation/accessability%20and%20perforance%20test.JPG)<center>image 21</center>

- #### Browser Testing, see results below:
![./images/Main_Menu.JPG](./images/validation/coding%20performance.JPG)<center>image 22</center>


The template provided by Code Institute as provided to all students is assumed to be tested for the above.

Using the file template [code institute], no ajor errors remain in current coding version. As a relevant comment, there have been fixed over 100 errors. 
























 
   
  ### Flowhart
  - #### See the link below:
  https://app.code2flow.com/ylb4Oj9KgP9t.pdf
<center>o</center>




 ### Design
 





